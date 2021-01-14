# OTW - Over The Wire (Bandit) :neckbeard:

## Level 20 ➡ Level 21
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge was to just challenge you to think outside the box, that how best I can describe it.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- I started a listener that is sending the password of the current level to a specific port, then continued with the following.

- The flag will be sent back to the listener.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 

- [Netcat Listener](https://www.sciencedirect.com/topics/computer-science/netcat-listener)
