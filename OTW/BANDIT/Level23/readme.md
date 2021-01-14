# OTW - Over The Wire (Bandit) :neckbeard:

## Level 23 ➡ Level 24
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge was to extend the teaching lessons on `cron`; the time-based job scheduler.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- Ohhhh this is an interesting level, it will require us to create our own firt shell-script.
- You can keep a copy of it, because it will be removed once it has been executed.

- So I started as the level goal guided us to do, checked in the `/etc/cron.d/` directory for the configuration to see what command was being executed.
- If you see the below code, then it means you are on the right track, if not please do read the level goal carefully.


```sh
#!/bin/bash

myname=$(whoami)

cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done
```

- This is the code that is being executed when the `cron job` is being executed.
- Basically what the script does it check the current user and stores it in a variable named `$myname` where this will be `bandit24` because the cron job is being executed by user `bandit24` if you check the cron job configuration.
- Then enters the directory `bandit24` inside `/var/spool/`, then runs an echo command saying, `Executing and deleting all scripts in `var/spool/bandit24:`
- After the echo command there is a for loop that checks if `$i` is not equal to `.` and is not equal to `..` then echo which file you are handling and find who is the owner which should be the current user, `bandit23`.
- Afterwards it checks if the owner is equal to `bandit23` and they are equal it will execute the file with a timeout of 60 seconds where it will send a SIGKILL to terminate the process after 60 seconds.
- Then it deletes the script.

- So we are required to create a script that will retrieve the flag which is the password for the next level in the directory `/etc/bandit_pass/`.
- Our script will be stored in the directory `/var/spool/bandit24` where it will be executed with the above script.
- So after explaining all that, I know you know what you are expected to do, but I will just make your work more simpler by giving you a oneliner I created to retrieve the password but with a twist. I will leave out a section the most important one for you.

```sh
# Oneliner
echo -e '#!/bin/bash \n\nyour-command-to-retrieve-the-flag' > /var/spool/bandit24/script.sh; chmod +x /var/spool/bandit24/script.sh
```

- Place the command to retrieve the flag, remember `/tmp/` directory is always your best friend.

- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.

- [Signal (IPC)](https://en.wikipedia.org/wiki/Signal_(IPC)#List_of_signals)
- [How to Use Logical OR & AND in Shell Script with Examples](https://tecadmin.net/use-logical-or-and-in-shell-script/)
- [Bash-Scripting: Other Comparison Operators](https://tldp.org/LDP/abs/html/comparison-ops.html)
- [Bash Reference Manual](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html#Bash-Conditional-Expressions)
- How to force crontab to run for debugging and testing purposes: `run-parts /etc/cron-directory-with-your-cron-configs`
