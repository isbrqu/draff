#!/usr/bin/env bash

# donwload-docker.sh
if [[ ! -d docker ]];then
    mkdir docker
fi
declare URL="https://download.docker.com"
declare URL="$URL/linux/debian/dists/bullseye/pool/stable/amd64"
# containerd.io_1.4.9-1_amd64.deb
# docker-ce-cli                    _ 20.10.8 ~3-0~ debian-bullseye _ amd64.deb
# docker-ce-rootless-extras        _ 20.10.8 ~3-0~ debian-bullseye _ amd64.deb
# docker-ce                        _ 20.10.8 ~3-0~ debian-bullseye _ amd64.deb
declare ce="docker-ce"
declare cli="docker-ce-cli"
declare rootless="docker-ce-rootless-extras"
declare n1="20.10.8"
declare n2="3-0"
declare os="debian-bullseye"
declare arch="amd64"
declare version="${n1}~${n2}~${os}_${arch}"
declare -a items=(
    "${ce}_${version}"
    "${cli}_${version}"
    "${rootless}_${version}"
    "containerd.io_1.4.9-1_${arch}"
)
cd docker
for item in "${items[@]}";do
    wget --continue "$URL/$item.deb"
done
cd ..

