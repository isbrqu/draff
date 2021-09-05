#!/usr/bin/env bash

sleep 5
echo 'go!'
for item in {1..10};do
    echo "item: $item"
    xdotool key --delay 200 2 ctrl+w ctrl+c 1 ctrl+l
done

