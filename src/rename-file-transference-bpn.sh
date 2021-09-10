#!/usr/bin/env bash

declare -r TITLE="Comprobante de Transferencia"

get_value() {
    local file="$1"
    local regex="$1"
    local value
    value="$(grep --perl-regexp --only-matching --regexp="$REGEX" "$file")"
    echo "$value"
}
get_datetime() {
    local file="$1"
    local value
    local -r REGEX="Fecha y Hora:\s+\K.+"
    value="$(get_value "$file" "$regex")"
    value="${value//\//-}"
    value="${value//:/-}"
    value="${value// /-}"
    echo "$value"
}

get_number() {
    local file="$1"
    local value
    local -r REGEX="Número de Transacción:\s+\K.+"
    value="$(get_value "$file" "$regex")"
    value="${value//:/-}"
    value="${value// /-}"
    echo "$value"
}

main() {
    local folder="$1"
    local title
    local datetime
    local number
    local new
    local bytes
    local -a files=($(\
        find "$folder" -type f -name "*.pdf" -size +3000c -a -size -7000c\
    ))
    for old in "${files[@]}";do
        txt="$(mktemp --suffix=.txt)"
        echo "try with $old ($bytes)"
        pdftotext -nopgbrk -layout "$old" "$txt"
        title="$(head --lines=1 "$txt")"
        if [[ "$title" == *"$TITLE"* ]];then
            datetime="$(get_datetime "$txt")"
            number="$(get_number "$txt")"
            new="$folder/transference-$datetime-$number.pdf"
            mv --no-clobber "$old" "$new"
            echo "successful! $old"
        fi
        rm "$txt"
    done
}

main "$@"
