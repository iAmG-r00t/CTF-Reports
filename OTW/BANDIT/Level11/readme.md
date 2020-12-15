# OTW - Over The Wire (Bandit) :neckbeard:

## Level 11

## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge was to learn about `rot13` encoding scheme/format.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- There are various ways of solving this challenge.
- For me I learnt something new from this challenge, I learnt how to decode `rot13` using a linux command known as `tr` and by hand. I don't know why it took me this long to learn this.

```sh
# linux command tr
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
```

- **Explanation**
- `tr` is a linux command that can translate, squeez and/or delete characters from standard input, writing to standard output.
	- `A-Za-z` : searches for characters `A to Z` and `a to z`.
	- `N-ZA-Mn-za-m` : replaces any character in `N to Z` with characters `A to M` and `n to z` with `a to m`. 

- The flag is at the home directory in the `data.txt` file after you decode the encoded data.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 

- Get to learn how to do it online, and maybe with any programming language you have in mind.
