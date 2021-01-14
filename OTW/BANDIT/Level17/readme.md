# OTW - Over The Wire (Bandit) :neckbeard:

## Level 17 ➡ Level 18
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of the challenge was to find the difference between two files.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- This is basically an easy task, no need to write the way I did it because it's really straight forward, `diff` the difference.
- But before you login remember ssh keys usually has `400` permissions, it should be readable by the logged in user.

- Also do note that `<` - denotes lines in **file1** and `>` - denotes lines in **file2**.

- The flag is the difference file.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.
