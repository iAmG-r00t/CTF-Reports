# OTW - Over The Wire (Bandit) :neckbeard:

## Level 1
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- I really can't explain the goal, when looking at it but the commands noted that I may need to solve this level were `ls` ,`cd`, `cat`, `file`, `du` and `find`.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- So there is a file named with a special character: `-`.
- Wasn't sure if it was a file or a directory so I played with `ls` command.

```sh
# ls - List
# This will basically help you to know if its a file or directory.
# If it's a directory at the beginning of the permission you will see it has a letter `d`.
# If it's not a directory it will lack the letter `d`.

ls -l	# Will basically list everything plus its permissions user owner and group owner.
ls -f	# List files
ls -d	# List directories 

# cat - read files and output its contents
cat ./-
```

- The flag is at the home directory in the `-` file.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.

- I thought too much about solving this challenge in a special way, while it was easy as pie.
- Don't think too much. 
