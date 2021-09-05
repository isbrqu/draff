#!/usr/bin/env bash

# -- rename all *.txt to *.text --
for item in *.txt; do 
    mv -- "$item" "${item%.txt}.text"
done

