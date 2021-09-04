#!/usr/bin/env bash

# -- join content in a file --
for item in *;do
    if [[ -f "$item" ]];then
        echo "# $item" >> b
        cat "$item" >> b
    fi
done

