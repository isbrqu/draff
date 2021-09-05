declare -a list=(...)
declare url="https://casilla.com/index.php"
declare action="$url?accion=descarga&mbox=INBOX&msgid="
for id in "${list[@]}";do
    _open "$url?accion=descarga&mbox=INBOX&msgid=$id&atchid=0"
    sleep 2
done

