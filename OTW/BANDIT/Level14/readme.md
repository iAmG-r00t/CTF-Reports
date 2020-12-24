# OTW - Over The Wire (Bandit) :neckbeard:

## Level 14 ➡ Level 15
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge was to pass the password of the current level to port `30000` on localhost.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- I basically echoed out the password and used netcat - (often abbreviated to `nc`) a computer networking utility for reading from and writing to network connections using TCP or UDP - to pass the password to that port at localhost.

```sh
echo password | nc localhost 30000
```


- The flag will be outputed back to the user.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.

- Learn networking, its really important and will come in handy when learning how to hack. 
