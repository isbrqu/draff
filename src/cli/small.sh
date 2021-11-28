#!/usr/bin/env bash

while getopts ":a" option;do
    case "${option}" in
        a)
            echo "-${OPTARG} was triggered!"
        ;;
        \?)
            echo "Invalid option: -${OPTARG}"
        ;;
    esac
done

