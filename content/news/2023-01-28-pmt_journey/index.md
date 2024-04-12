---
title: "PMTs are dead...Long live PMTs"
author: "John Sallay"
date: "2023-01-28"
categories: ["pmt", "gr4"]
aliases: ["blog/gr4-modernization"]
---

A few years back I was working on a pair of gnuradio blocks.  The first one would produce a
"report" that we stored in a `pmt` dictionary.  The second block would read in the "report" and do 
some processing based on the contents.

I'm a big fan of data validation, so I wanted to ensure that the received `pmt` had the exact
structure that we were expecting.  I started to write a function to check that the `pmt` was a
dictionary, had all of the correct keys, and all of the values had the correct types.  This
proved to be extremely difficult.  The `pmt` interface can be inconsistent and non-intuitive.  As
I was banging my head against the wall in frustration, I turned to a co-worker and said something
like "This isn't that hard - I could do something better."  A few minutes later, it dawned on me -
GNURadio is an open source project - I really could do something better.

I sent a message on the GNURadio message boards and found out that a new version of pmts was
already in the works using `flatbuffers`.  One of my biggest complaints about the original `pmt`s 
was the user interface.  I wanted to introduce modern c++ concepts into the design to make them
easier and safer to use.  An an example:
```
// Old pmt list creation (non uniform)
pmt_t p1 = pmt_integer(1);
pmt_t p2 = pmt_integer(2);
pmt_t p3 = pmt_integer(3);

pmt_t p_list = pmt_list3(p1, p2, p3);

// New pmt list creation using initializer lists
pmt p_list_new{std::vector<pmt>{1,2,3}};
```
For maps, it is also much easier
```
// Old pmt map iteration (assume dict var defined earlier)
// Items is a list of pairs
auto items = pmt::dict_items(dict);
auto length = pmt::length(items);
for (size_t i = 0; i < length; i++) {
    // Get the key and value
    auto ref = pmt::vector_ref(items, i);
    auto key = pmt::car(ref);
    auto value = pmt::cdr(ref);
    std::cout << key << ": " << value << std::endl;
}

// New pmt map
// Interpret the pmt as a map and iterate over the keys/values
for (auto& [k, v]: std::get<pmt::map_t>(dict)) {
    std::cout << key << ": " << value << std::endl;
}
```

### If it's worth writing, it's worth rewriting
When I took on the pmt redeisng, a proposed new pmt interface using `flatbuffers` was largely written.  I went about creating
a more friendly developer interface.  In order to not mess with the existing code, I wrote wrapper
classes that contained all of the modern c++ features.  When all was said and done we ended up with
some code that resembled Frankenstein.  To achieve dynamic types we were using flatbuffers, 
polymorphic types, templates, and `std::variants`.  To make matters worse, we did some benchmarking
and found that although the new pmts were faster in some important cases, they were significantly
slower in the case of serializing vectors of contiguous data - which is a really important case.  I
did some digging and found that throughout our many wrappers and dynamic types we copied the data
twice when serializing vectors.  This was a fundamental design flaw that was not easily fixable.

I went about redesigning the `pmt` classes to remove layers of wrappers which greatly simplied the
design.  It took a lot of effort, but we were able to get rid of the extra vector `memcpy` without
changing the user interface at all.  I ran all of the old benchmarks and we were better on every
one.  

Then I made the mistake of creating new benchmarks, starting out with one that measured object
construction time.  It turns out that in most cases, the new `pmt` class was significantly slower
than the old `pmt` class.  Digging into it, I discovered that the "problem" was the `flatbuffers`.
`flatbuffers` allow us to store arbitrary structures of data efficiently.  However, the way we were
using it involved storing a very small amount of data in many `flatbuffers` instead of a larger
amount of data in a single `flatbuffer`...back to the drawing board.

The c++17 standard introduced `std::variant` which is typesafe union of types.  This looked like
the best way to solve the construction problem.  `flatbuffers` have a few tables with pointers that
need to be instantiated every time in addition to the data.  An `std::variant` only requires the 
data and an index that specifies which type is being stored.  Switching to the `std::variant` also
simplified the code greatly.  For the `flatbuffers`, I had to write my own wrapper classes that
acted like `std::vector` and `std::map` but also allows us to manipulate the underlying
`flatbuffer`.  Using the `std::variant`, those wrappers were no longer needed.

I think it's time to write more benchmarks, but from what I have seen so far, it looks like we have
succeeded at creating a more user friendly interface that is at least as fast (and in some cases
significantly faster) than the previous `pmt` implementation.

### Are we there yet?
I believe that the primary functionality of the `pmt` is there, so I'm not planning on having to 
rewrite it again (hopefully).  There are a few key improvements that will add more value to the
library.

#### Custom memory allocators 
The `std::map` and `std::vector` classes allow for the user to set a custom memory allocator.  We
could for example use a memory pool or allocate the vector in CUDA unified memory.

#### Struct Conversion
A common task is to convert to and from a struct and a `pmt`.  For example, in a spectrum survey
application, I may have a structure defined that defines information about a detected signal such
as center frequency and bandwidth.  Once a signal is detected, we want to send the information to
another block as a `pmt`.  It is annoying and error prone to write the code on the send and receive
side for pulling the data in and out of a struct.

There is a new c++ library called `refl-cpp` that allows us to query information about structures 
at compile-time.  The goal is to allow to the developer to use functions like:
```
auto struct_pmt = struct_to_pmt(my_struct);
auto struct_out = pmt_to_struct<struct_type>(struct_pmt);
```

#### Data Validation
This whole journey started because I wanted to validate incoming data.  Although, I think the task
is much simpler now, I still think it could be easier and I think that `refl-cpp` can again help
us out here.  We can write a validation function that works like:
```
bool valid = validate_struct<struct_type>(struct_pmt);
// if valid -> then we know we can call pmt_to_struct without issue
```