#!/bin/bash

while true; do
    update_blastdb.pl nr
    if [ $? -eq 0 ]; then
        break
    fi
    sleep 5
done

