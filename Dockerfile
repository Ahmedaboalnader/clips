FROM ubuntu:20.04

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    wget unzip build-essential gcc g++ && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://sourceforge.net/projects/clipsrules/files/CLIPS/6.30/clips_core_source_630.zip/download -O clips_core_source_630.zip && \
    unzip clips_core_source_630.zip -d clips_core && \
    cd clips_core/clips_core_source_630/core && \
    make -f ../makefiles/makefile.gcc && \
    mv clips /usr/local/bin/

WORKDIR /engine

COPY clips_engine/ /engine

ENTRYPOINT ["clips"]
