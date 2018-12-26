# gnuradio/hugo:latest
FROM alpine:3.8
MAINTAINER Andrej Rode <mail@andrejro.de>

ENV security_updates_as_of 2018-12-26
RUN apk update && apk add py-pygments && apk add git && apk add bash && apk add openssh-client && apk add libstdc++ && rm -rf /var/cache/apk/*
ENV HUGO_VERSION 0.53
ENV HUGO_BINARY hugo_extended_${HUGO_VERSION}_linux-64bit
ENV HUGO_ARCHIVE https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
ADD ${HUGO_ARCHIVE} /usr/local/
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/bin/ \
	&& rm /usr/local/${HUGO_BINARY}.tar.gz

ENV GLIBC_VERSION 2.27-r0
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC_VERSION/sgerrand.rsa.pub" \
&&  wget "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC_VERSION/glibc-$GLIBC_VERSION.apk" \
&&  apk --no-cache add "glibc-$GLIBC_VERSION.apk" \
&&  rm "glibc-$GLIBC_VERSION.apk" \
&&  wget "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC_VERSION/glibc-bin-$GLIBC_VERSION.apk" \
&&  apk --no-cache add "glibc-bin-$GLIBC_VERSION.apk" \
&&  rm "glibc-bin-$GLIBC_VERSION.apk" \
&&  wget "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/$GLIBC_VERSION/glibc-i18n-$GLIBC_VERSION.apk" \
&&  apk --no-cache add "glibc-i18n-$GLIBC_VERSION.apk" \
&&  rm "glibc-i18n-$GLIBC_VERSION.apk"
