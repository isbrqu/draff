#!/usr/bin/env bash

pdftotext -nopgbrk -eol unix -table ~/Downloads/input.pdf example.txt
echo "" > students.txt
echo "" > draff.txt
while IFS=' ' read -r dni line;do
    if [[ "$dni" == [[:digit:]]* ]];then
        dni="${dni//./}"
        draff="${line#* [MF] }"
        IFS=' '
        read -r course division tourn date _ <<< "$draff"
        unset IFS
        draff="${line%%     [12345][ABCDE][TM]*}"
        if [[ "$draff" != *[MF] ]];then
            echo "$draff"
        fi
        echo "$draff" >> draff.txt
        echo "$dni,$course,$division,$tourn,$date" >> students.txt
    fi
done < example.txt
