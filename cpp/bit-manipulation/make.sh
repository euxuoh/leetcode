#!/bin/bash

set -x

fullname=$1

if [[ $fullname == "clean" ]]; then
    rm -f *.out
    exit 0
else 
    if [[ ! -f $fullname ]]; then
        echo "$fullname is not exist"
        exit -1
    fi
fi

filename=$(echo $fullname | cut -d . -f1)

g++ -o "${filename}.out" ${fullname} -I../include/ -L../lib/ -lgtest -lpthread -std=c++11

./"${filename}.out"
