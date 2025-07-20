#!/bin/sh
# I originally used this script in the httpd source code directory to configure the stuff...
export PREFIX=/home/oof/apache-afl/install_dir/
PREFIX=/home/oof/apache-afl/install_dir/ \
CC=afl-clang-fast \
CXX=afl-clang-fast++ \
CFLAGS="-Wno-error=declaration-after-statement -g -fsanitize=address,undefined -fno-sanitize-recover=all" \
CXXFLAGS="-Wno-error=declaration-after-statement -g -fsanitize=address,undefined -fno-sanitize-recover=all" \
LDFLAGS="-fsanitize=address,undefined -fno-sanitize-recover=all -lm" \
./configure --with-apr="$PREFIX/apr/" \
            --with-apr-util="$PREFIX/apr-util/" \
            --with-expat="$PREFIX/expat/" \
            --with-pcre="$PREFIX/pcre/" \
            --disable-pie \
            --disable-so \
            --disable-example-ipc \
            --disable-example-hooks \
            --disable-optional-hook-export \
            --disable-optional-hook-import \
            --disable-optional-fn-export \
            --disable-optional-fn-import \
            --with-mpm=prefork \
            --enable-static-support \
            --enable-mods-static=reallyall \
            --enable-debugger-mode \
            --with-crypto --with-openssl \
            --prefix=$PREFIX \
            --disable-shared
