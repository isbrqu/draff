make_url() {
    local file="$1"
    local parameters="$2"
    local url="$scheme://$domain/$directory/$file?$parameters"
    echo "$url"
}

request_username() {
    local file="doLoginFirstStep.htm"
    local form_data="isInclu=false&username=$USERNAME&pin=" 
    local url
    url="$(make_url "$file")"
    curl "$url"\
        --header "@$headerdir/username.hd"\
        --cookie-jar "$cookiefile"\
        --data-raw "$form_data"\
        --progress-bar\
        --compressed
}

request_login() {
    local state="$1"
    local file="doLogin.htm"
    local url
    url="$(make_url "$file")"
    local data_username="username=$USERNAME"
    local data_password="password=$PASSWORD"
    local form_data="jsonRequest=true&$data_username&$data_password&sfaInfo=&pcCompartida=true&inclu=false&recordarUsuario=false&_STATE_=$state"
    curl "$url"\
        --header "@$headerdir/dologin.hd"\
        --cookie "$cookiefile"\
        --cookie-jar "$cookiefile"\
        --data-raw "$form_data"\
        --progress-bar\
        --compressed
}

request_home() {
    local state="$1"
    local file="home.htm"
    local url
    url="$(make_url "$file")"
    curl "$url"\
        --header "@$headerdir/home.hd"\
        --cookie "$cookiefile"\
        --cookie-jar "$cookiefile"\
        --form "_STATE_=$state"\
        --progress-bar\
        --compressed
}

request_position() {
    local file="posicionConsolidada.htm"
    local state="$1"
    local url
    url="$(make_url "$file" "_STATE_=$state")"
    curl "$url"\
        --header "@$headerdir/posicion_consolidada.hd"\
        --cookie "$cookiefile"\
        --cookie-jar "$cookiefile"\
        --progress-bar\
        --compressed
}

request_accounts() {
    local file="getCuentasForPC.htm"
    local state="$1"
    local url
    url="$(make_url "$file" "_STATE_=$state")"
    curl "$url"\
        --header "@$headerdir/getCuentasForPC.hd"\
        --cookie "$cookiefile"\
        --cookie-jar "$cookiefile"\
        --progress-bar\
        --compressed
}

request_balance() {
    local file="getSaldoPosCons.htm"
    local state="$1"
    local number="$2"
    local tandem="$3"
    local url
    url="$(make_url "$file" "_STATE_=$state")"
    curl "$url"\
        --header "@$headerdir/saldo_pos_cons.hd"\
        --cookie "$cookiefile"\
        --cookie-jar "$cookiefile"\
        --data-raw "numero=$number&tipoTandem=$tandem"\
        --progress-bar\
        --compressed
}

request_logout() {
    local file="logout.htm"
    local state="$1"
    local url
    url="$(make_url "$file")"
    curl "$url" \
        --header "@$headerdir/logout.hd"\
        --cookie "$cookiefile"\
        --cookie-jar "$cookiefile"\
        --progress-bar\
        --compressed
}

