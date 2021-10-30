get_states_form() {
    local -n states_="$1"
    local file="$2"
    local RE='(?<=input type="hidden" name="_STATE_" value=").+(?=")'
    local -a tmp=($(grep --perl-regexp --only-matching --regexp="$RE" "$file"))
    states_=(
        ["form_dologin"]="${tmp[0]}"
        ["form_home"]="${tmp[1]}"
        ["form_aceptartyc"]="${tmp[2]}"
    )
}

get_state_realhref() {
    local expresion="$1"
    local file="$2"
    local REGEX="(?<=/bpn/$expresion\?_STATE_=).+(?=\" href)"
    local state
    state="$(get_first_match "$expresion" "$file")"
    echo "$state"
}

get_state_js() {
    local expresion="$1"
    local file="$2"
    local REGEX="(?<=$expresion\?_STATE_=).+(?=')"
    local state
    state="$(get_first_match "$expresion" "$file")"
    echo "$state"
}

