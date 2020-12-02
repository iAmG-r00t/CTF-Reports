# OTW - Over The Wire (Bandit) :neckbeard:

## Level 2
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The goal was to read a file that was named with spaces inbetween. `this is an example` <= such as that.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- So bash has improved and has this fellah `autocompletion` who will make people lazy.
- But when you are is a situation where you don't have autocompletion use the below options.

```sh
cat 'spaces in this filename'
	# or
cat spaces\ in\ this\ filename
```

- The flag is at the home directory in the `spaces in this filename` file.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 
