#!/usr/bin/env bash

declare -r SCRIPT_NAME
SCRIPT_NAME="$(basename "$0")"

usage() {
    echo "$SCRIPT_NAME <ext> <input> <output>"
}

main() {
    local ext="$1"
    local input="$2"
    local output="$3"
    local new
    if [[ -z "$ext" || -z "$input" || -z "$output"]];then
        usage
        return 1
    fi
    find "$input" -name "*.$ext" -print0 | while IFS= read -r -d '' old;do
        hash="$(sha1sum "$old")"
        hash="${hash// */}"
        mkdir --parents "$output"
        new="$output/$hash.$ext"
        echo "$old -> $new"
        mv --no-clobber "$old" "$new"
    done
}

main "$@"
