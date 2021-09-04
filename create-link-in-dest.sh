#!/usr/bin/env bash

# create links in <dest>
for file in origin/*;do
    link="${file##*-}"
    ln --symbolic --relative "$file" dest/$link
done

