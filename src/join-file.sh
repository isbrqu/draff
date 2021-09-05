#!/usr/bin/env bash

# usage: ./joinfile to/path namefile ext

declare path="$1"
declare namefile="$2"
declare ext="$3"
declare title

if [[ -z "$path" && -z "$namefile" && -z "$ext" ]];then
    return 1
fi

for item in "$path"/*;do
    if [[ -f "$item" ]];then
        title="${item%.$ext}"
        title="${title##*/}"
        echo -e "\n// -- $title --" >> "$path"/out
        cat "$item" >> "$path"/out
    fi
done
sed "s/\r//g" "$path"/out > "$path"/"$namefile"."$ext"
rm "$path"/out

