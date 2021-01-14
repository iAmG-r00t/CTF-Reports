# OTW - Over The Wire (Bandit) :neckbeard:

## Level 25 ➡ Level 26
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The goal of this challenge was to learn how to exploit a bug in `more` command and how to get a shell from a texteditor.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- So the first way of how I approached this challenge was wrong, I never thought through of what was required but here I am teaching you the proper way of how to approach this challenge.
- So the level goal informs us that Logging in to bandit26 from bandit25 should be fairly easy, and that's true because there is an ssh key at the home directory.
- But there is a catch, the shell for user `bandit26` is not `\bin\bash`, but something else, we are to find out what it is, how it works and how to break out of it.
- So first our main goal is to get to know what user shell bandit26 is using. The straight and quick method to do this is to check the `/etc/passwd` file and grep for user `bandit26` and see what shell he has been assinged.
- If you have done the above step, I think you know what you should do next. View the contexts of that file in that directory.
- So from here on I wouldn't want to show you the whole solution and make it les fun, so here is a clue before you try to login to user `bandit26` please reduce the size of your terminal to be really small, then login.
- You will see something interesting, so read the following [blog](https://www.sans.org/blog/escaping-restricted-linux-shells/), It will assist in helping you solve this solution. A very interesting one indeed.
- Also do research on how to escalate `more` command preview to a text editor.
- Google should be your best friend, also once you are done you will have access to a shell for bandit26.

- This level does not require a flag, the flag is the shell for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.

- [Escaping Restricted Shell rbash](https://www.metahackers.pro/breakout-of-restricted-shell/)
- [Upgrade Shell to fully interactive tty](https://www.metahackers.pro/upgrade-shell-to-fully-interactive-tty-shell/).
- [Spawing real TTY shells](https://www.metahackers.pro/spawing-tty-shells/)
- [Escape Restricted Shell Environments on Linux](https://null-byte.wonderhowto.com/how-to/escape-restricted-shell-environments-linux-0341685/)
