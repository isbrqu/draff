#!/usr/bin/env bash

declare filename="/media/windows/Users/isbrq/desktop/personal/isaac/w/books/politic/libro/biblioteca/conceptos/Politica y Estado/A. Toynbee-A Study of History [One-Volume edn]-Oxford (1972).pdf"

time (
    echo "with sha1sum and md5sum"
    for i in {1..7};do
        sha1sum "$filename" &> /dev/null
        md5sum "$filename" &> /dev/null
    done
)

echo "-------------------------------"
time (
    echo "with sha256sum";
    for i in {1..7};do
        sha256sum "$filename" &> /dev/null;
    done;
)
