#!/usr/bin/env bash

declare file
declare folder_input="input"
declare folder_output="output"
declare TITLE="Comprobante de Transferencia"
declare value
declare row

for item in "$folder_input"/*.pdf;do
    file="${item##*/}"
    file="${file%.*}.txt"
    pdftotext -nopgbrk -layout "$item" "$folder_output/$file"
done
python3 generate-summary.py

