# OTW - Over The Wire (Bandit) :neckbeard:

## Level 18 ➡ Level 19
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge was to execute a command remotely through ssh.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- Basically we can't login because we are being disconnected at every instance we try to login so we execute a command to read the flag in the home directory.

- The flag is at the home directory in the `readme.md` file.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 

- [Run / Execute Command Using SSH](https://www.cyberciti.biz/faq/unix-linux-execute-command-using-ssh/)
