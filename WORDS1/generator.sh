#!/bin/bash

TESTS=5
WORDS=100000
WORD_LENGTH=4

random-string () {
    s=abcdefghijklmnopqrstuvwxyz
    i=1
    while [[ i -le $WORD_LENGTH ]]
    do
        p=$((RANDOM % ${#s}))
        echo -n ${s:$p:1}
        ((i = i + 1))
    done
    echo
}

echo $TESTS
TEST=1
while [[ $TEST -le $TESTS ]]
do

    echo $WORDS
    WORD=1
    while [[ $WORD -le $WORDS ]]
    do
        random-string
        ((WORD = WORD + 1))
    done

    ((TEST = TEST + 1))

done

