# Imagem usada apenas para gerar o `fs.bin` (LittleFS) com os fontes
# em `src/`. O Wokwi monta esse arquivo no offset 0x200000, conforme
# `flasher_args.json`. A imagem do MicroPython em si vem pre-compilada
# em `binaries/micropython.bin`.

FROM espressif/idf:v5.2.2

ENV IDF_PATH="/opt/esp/idf/"

WORKDIR "/"

COPY src/ /src/

RUN git clone https://github.com/earlephilhower/mklittlefs.git && \
    cd mklittlefs && \
    git submodule update --init && \
    make dist && \
    ./mklittlefs --version

RUN cd mklittlefs && \
    mkdir -p ~/fs && \
    cp -r /src/. ~/fs/ && \
    ./mklittlefs -c ~/fs -b 4096 -p 256 -s 0x200000 /fs.bin

CMD ["/bin/bash"]
