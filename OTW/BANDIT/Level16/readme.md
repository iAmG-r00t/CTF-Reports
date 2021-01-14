# OTW - Over The Wire (Bandit) :neckbeard:

## Level 16 ➡ Level 17
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge was scan for open ports in a given range, `31000 - 32000` find ports that have a server listening on them and the one that speaks SSL and the one that doesn't.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- I took this opportunity to use a method that I learnt that can do port scanning which was netcat also known as `nc`.
- There are alot of ways to scan for open ports without the use of `nmap` and even `nc` itself. Check the conclusion section for other links.

```sh
# nc: a unix utility used for just about anything under the sun involving TCP, UDP, or UNIX-domain sockets.

# scan for tcp ports
nc -z -v localhost port - range
```

- The flag is the `key` that will be outputed to you if you submit the right password to one of those listening server ports.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.

- [How to Check (Scan) for Open Ports in Linux](https://linuxize.com/post/check-open-ports-linux/)
- [Scanning ports with netcat “nc” command on Linux](https://pc-freak.net/blog/scanning-ports-netcat-nc-command-linux-unix/)
- [Port scanning with Bash (without sudo, nmap or nc)](https://coderwall.com/p/udnrjq/port-scanning-with-bash-without-sudo-nmap-or-nc)
- [TCP Port Scanner in Bash](https://catonmat.net/tcp-port-scanner-in-bash)
- [Creating A TCP Port Scanner With Bash](https://pentestlab.blog/2012/11/12/creating-a-tcp-port-scanner-in-bash/)
