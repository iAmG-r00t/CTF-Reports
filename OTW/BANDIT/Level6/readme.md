# OTW - Over The Wire (Bandit) :neckbeard:

## Level 6
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal for this challenge was to learn how to use the `find` command and identify a file with the flag that was somewhere within the server. 
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- We were informed that the flag was in a file somewhere withing the server with the following properties;
  - owned by user bandit7
  - owned by group bandit6
  - 33 bytes in size

- That being said, I went straight to the point using `find` command. I proceeded checking how to find a file with the following first two properties; **user** and **group**.
- Below was my solution;

```sh
# Find command
# $USER variable was the host user which was bandit6

find / -type f -size 33c -user bandit7 -group $USER

# This printed the file but also had some 'Permission denied' errors that filled the screen soo much
# After some googling I found a solution of using print that will redirect `stderr` to `/dev/null` device.

find / -type f -size 33c -user bandit7 -group $USER -print 2>/dev/null

# The below command will confirm the file properties, where it will check the size, list file properties ...
# ... that have the file user and group and then cat to see the flag

find / -type f -size 33c -user bandit7 -group $USER -print 2>/dev/null -exec wc -c {} + -exec ls -l {} + -exec cat {} +
```


- The flag is at the home directory in the file you will find.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.

- Below we take note and talk about `riderects`, `stdout` and `stderr` redirects plus `/dev/null` device.
  - `> file` : redirects **stdout** to file.
  - `1> file` : redirects **stdout** to file.
  - `2> file` : redirects **stderr** to file.
  - `&> file` :  redirects **stdout** and **stderr** to file.
  - `> file 2>&1` : redirects **stdout** and **stderr** to file.
  - `/dev/null` is the null device it takes any input you want and throws it away. **It can be used to suppress any output.**

- **Note:** that `> file 2>&1` is an **older syntax** which still works, `&> file` is **neater**, but would not have worked on older systems.
