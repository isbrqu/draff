#!/usr/bin/env bash


main() {
    local ext="$1"
    local input="$2"
    local output="$3"
    if [[ -z "$ext" ]];then
        echo "ext is empty"
        return 1
    fi
    if [[ -z "$input" ]];then
        echo "input is empty"
        return 1
    fi
    if [[ -z "$output" ]];then
        echo "output is empty"
        return 1
    fi
    find "$input" -name "*.$ext" -print0 | while IFS= read -r -d '' name;do
        hash="$(sha1sum "$name")"
        hash="${hash// */}"
        echo "$hash"
        mkdir --parents "$output"
        mv --no-clobber "$name" "$output/$hash.$ext"
    done
}

main "$@"
