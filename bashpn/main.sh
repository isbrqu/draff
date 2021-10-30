#!/usr/bin/env bash

# load USERNAME and PASSWORD
source .env
declare scheme="https"
declare domain="hb.redlink.com.ar"
declare directory="bpn"
declare cookie=""
declare tmpdir
tmpdir="$(mktemp --directory)"
declare cookiefile="$tmpdir/cookie.txt"
declare headerdir="header"
declare -A html
html=(
    ["login"]="$(mktemp --suffix=".login.html" --tmpdir="$tmpdir")"
    ["home"]="$(mktemp --suffix=".home.html" --tmpdir="$tmpdir")"
    ["position"]="$(mktemp --suffix=".position.html" --tmpdir="$tmpdir")"
)

source request.sh
source extract_state.sh

get_number_and_tandem() {
    jq --raw-output '.response.data[] | "\(.numero) \(.tipoTandem)"'
}

get_first_match() {
    local regex="$1"
    local file="$2"
    grep --perl-regexp --only-matching --max-count=1 --regexp="$REGEX" "$file"
}


main() {
    local -A states
    local state
    local items
    # login
    request_username > "${html[login]}"
    get_states_form states "${html[login]}"
    # states=$(get_states "${html[login]}"))
    request_login "${states[form_dologin]}" &> /dev/null
    # home
    request_home "${states[form_home]}" > "${html[home]}"
    # accounts and position
    state="$(get_state_realhref "posicionConsolidada.htm" "${html[home]}")"
    request_position "$state" > "${html[position]}"
    state="$(get_state_js "getCuentasForPC.htm" "${html[position]}")"
    items="$(request_accounts "$state" | get_number_and_tandem)"
    state="$(get_state_js "getSaldoPosCons.htm" "${html[position]}")"
    # list balance for account
    while IFS=' ' read -r number tandem;do
        json="$(request_balance "$state" "$number" "$tandem")"
        echo "$json"
    done <<< "$items"
    request_logout &> /dev/null
    rm --recursive --force "$tmpdir"
}

main "$@"

