#!/usr/bin/env bash

declare folder
declare path="$1"
if [[ -d "$path" ]];then
    cd "$path"
    for mbz in *.mbz;do
        folder="${mbz%.mbz}"
        mkdir "$folder"
        tar -xvzf "$mbz" -C "$folder" > /dev/null
    done
    rm *.mbz
fi

