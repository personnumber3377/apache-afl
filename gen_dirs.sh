#!/bin/bash

INPUT_FILE="fuzzer-dir/conf/default.conf"  # replace with your file
ROOT_DIR="install_dir/htdocs"          # where to put the generated dirs

mkdir -p "$ROOT_DIR"

# extract lines like <Location "/xyz"> and get the "/xyz" part
grep -oP '(?<=<Location ")[^"]+' "$INPUT_FILE" | while read -r path; do
    dir="$ROOT_DIR$path"
    mkdir -p "$dir"

    # create 'a' and 'a.html' with basic HTML content
    echo -e "<html><body><h1>File a in $path</h1></body></html>" > "$dir/a"
    echo -e "<html><body><h1>File a.html in $path</h1></body></html>" > "$dir/a.html"
done

