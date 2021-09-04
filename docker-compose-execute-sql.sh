#!/usr/bin/env bash

declare database="database"
declare password="password"
declare user="username"
declare charset="${2:-utf8mb4}"
if [[ -n "$1" ]];then
    docker-compose exec mariadb mysql\
        --user="$user"\
        --password="$password"\
        --database="$database"\
        --default-character-set="$charset"\
        --execute="$1"
else
    echo --execute="usage: sql 'query' [charset]"
fi

