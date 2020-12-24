# OTW - Over The Wire (Bandit) :neckbeard:

## Level 8 ➡ Level 9
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge was to learn how to use two commands, `sort` and `uniq`.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- We were informed that there is a file called `data.txt` with data where the flag was there and it was the only line that occurs once.

```sh
# sort + uniq
# -u option only prints uniq lines.
sort data.txt | uniq -u

```

- We first sort the data so that the lines that are the same to be grouped together then the get the uniq line that doesn't occur more than once.

- The flag is at the home directory in the `data.txt` file.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 

- **Note:** this challenges can be solved in very different ways.
