#!/usr/bin/env bash

shopt -s nocasematch

export PATH="$PATH:./script"

declare course
declare users
declare user
declare users_cohort

action() {
    local action="$1"
    local course="$2"
    local dni="$3"
    local email="$4"
    local user
    cohort "$action" "$course" "${dni:-@@}"\
    || cohort "$action" "$course" "${email:-@@}"
}

add() {
    local course="$1"
    local filename="$2"
    local cohort
    cohort="$(cohort self "$course")"
    echo "dni,email,nombre,apellido" >&2
    {
        read
        while IFS=, read -r dni email name lastname; do
            echo "search: $dni, $email, $name, $lastname"
            if [[ ("$cohort" == *"$dni"* && -n "$dni") || ("$cohort" == *"$email"* && -n "$email") ]];then
                echo 'ok!'
            elif [[ -n "$dni" || -n "$email" ]];then
                user="$(action add "$course" "$dni" "$email" 2> /dev/null)"
                if [[ -n "$user" ]];then
                    cohort="$cohort $user"
                    echo "enroll: $user"
                else
                    echo "bad: $dni, $email, $name, $lastname"
                    echo "$dni,$email,$name,$lastname" >&2
                fi
            fi
            echo ""
        done
    } < $filename
}

del() {
    local course="$1"
    local filename="$2"
    local csv
    local cohort
    csv="$(cat "$filename")"
    cohort="$(cohort self "$course")"
    while IFS='@' read -r dni_or_email id;do
        dni_or_email="${dni_or_email##* }"
        id="${id##* }"
        if [[ "$csv" != *"$dni_or_email"* ]];then
            echo "$dni_or_email $id"
            cohort del-by-id "$course" "$id"
        fi
    done <<< "$cohort"
}

declare action="$1"
declare course="$2"
declare filename="$3"
case "$action" in
    del)
        del "$course" "$filename"
    ;;
    add)
        add "$course" "$filename"
    ;;
esac
