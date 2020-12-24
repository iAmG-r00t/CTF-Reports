# OTW - Over The Wire (Bandit) :neckbeard:

## Level 7 ➡ Level 8
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge was to learn how to use the `grep` command.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- We were given a file called `data.txt` where it contained a large amount of data and the flag was stored in that file next to the word `millionth`.
- First and foremost, I checked the file line count, then proceeded to grep the line with the word `millionth`.

```sh
# Line count
wc -l data.txt

# Grep the line with the word millionth
grep millionth data.txt
```


- The flag is at the home directory in the `data.txt` file.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 
