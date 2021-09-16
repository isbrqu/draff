#!/usr/bin/env bash

declare fullname="$1"
declare directory="${fullname%/*}"
declare filename="${fullname##*/}" 

# si ya existe o no existe el directorio lo abre
if [[ -f "$fullname" || -z "$directory" ]]; then
 vim "$fullname"
vim "$1"

check_directory() {
 local fullname="$1"
 local left="${fullname%%/*}"
 local right="${fullname#*/}"
 if [[ ! -e "$left" ]];then
  echo "$left -> $right"
  return 0
 else
  _check_directory "$left" "$right"
  (( $? == 0 )) && return 0 || return 1
 fi
}

_check_directory() {
 local left="$1"
 local right="$2"
 sleep 1
 if [[ -e "$left" ]];then
  # es un directorio si no queda nada que analizar
  # o es un archivo si el resultado es el mismo al sacar lo izquierdo
  if [[ -z "$right" || "$right" == "${right#*/}" ]];then
   echo "$left -> $right"
   return 0
  elif [[ -d "$left" ]];then
   echo "$left -> $right"
   _check_directory "$left/${right%%/*}" "${right#*/}"
   (( $? == 0 )) && return 0 || return 1
  else
   echo "no es un directorio"
   return 1
  fi
 else
  return 0
 fi
}
