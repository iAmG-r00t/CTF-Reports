# OTW - Over The Wire (Bandit) :neckbeard:

## Level 0 ➡ Level 1
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- Using SSH.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- So I have been using **SSH** for a while, but I learnt about it from these challenges.
- Generally it is easy for us here, but if you may not know you can use the `man` command or `google.com` to solve this.

```sh
ssh username@target -p port
```

- The flag is at the home directory in the `readme.md` file.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.

- So SSH is good, I have learnt alot about it and there is more to learn on SSHD configs and also config for SSH itself on the client side.
- The biggest complaint/ISSUE I have with SSH is the termination of session when one is having a bad internet and maybe inactivity after along time.
- But we are in 2020 so I would recommend for someone facing some issue have a look at [MOSH: the Mobile Shell](https://mosh.org/) :boom:. Just have a look at it use it and you will thank me later one day one time. 
