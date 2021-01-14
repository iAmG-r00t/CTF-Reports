# OTW - Over The Wire (Bandit) :neckbeard:

## Level 19 ➡ Level 20
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge was to learn about **setuid** binaries and how to escalate privilege with it.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- Just did as I was requested at the level goal.

- **setuid binary** + `cat` == **GOD MODE**

- The flag is at the home directory in the `readme.md` file.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 

- The Unix access rights flags setuid and setgid (short for "set user ID" and "set group ID")[1] allow users to run an executable with the file system permissions of the executable's owner or group respectively and to change behaviour in directories. They are often used to allow users on a computer system to run programs with temporarily elevated privileges in order to perform a specific task. While the assumed user id or group id privileges provided are not always elevated, at a minimum they are specific.
