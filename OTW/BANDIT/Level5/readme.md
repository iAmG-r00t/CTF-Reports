# OTW - Over The Wire (Bandit) :neckbeard:

## Level 5 ➡ Level 6
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal for this challenge was to learn how to use the `find` command and identify the file with the flag that is within a directory with sooo many files.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- We were informed that the flag was in a file somewhere under the `inhere` directory and had the following properties;
  - human-readable
  - 1033 bytes in size
  - not executable

- That being said, I went straight to the point using the `find` command that I used on solving [Level4](../Level4/readme.md).
- For this one it has the option of adding not executable.

```sh
find ./inhere/ -type f -size 1033c ! -executable -exec file {} + | grep ASCII
```


- The flag is at the home directory in the file you will locate inside `inhere` directory.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 
