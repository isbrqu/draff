#!/usr/bin/env bash

# -- execute command with array --
declare -a tables=(
    "category"
    "course"
    "user"
    "board_url"
    "book"
    "page"
    "forum"
    "discussion"
)

for table in "${tables[@]}";do
    orator make:model $table
done

