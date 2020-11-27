# OTW - Over The Wire (Bandit) :neckbeard:

## Level 4
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge is to identify a file with ASCII data in a directory filed with files with random data.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- At first I played along with `ls` command to list all the files properties.
- Then proceeded with `du` command to list the file sizes.
- I wanted to know what kind of files I was dealing with, if they were executables ones also known as `binaries` or just normal files.
- I also wanted to know if they were of different sizes, but they weren't. They were all the same size.

```sh
ls -l * 		# List content present in the home directory

ls -l inhere/*		# List content present in the `inhere` directory

# Best solution, the hard way, but give you the file itself.
# will explain the command below
find ./inhere/ -type f ! -executable -exec file {} + | grep ASCII

	# OR

# Hmmm solution, the easy way

file ./inhere/*
```

**Explanation** of below command:
- `find /directory/path/ -type f ! -executable -exec file {} + | grep ASCII`
   	- `find`: linux command for locating files/directories.
	- `-type f`: this is an argument/option for the `find` command, which tells it to only output objects that are **files**.
	- `! -executable`: this is an argument/option for the `find` command, that also tells it to **exclude** [executable](https://en.wikipedia.org/wiki/Executable) files.
	- `-exec`: this is an argument/option for `find` command that allows the `find` command to execute another series of command.
- `file`: linux command to determine type of FILEs.
- `{} +`: input of the `find` command result contents.
- `|`: [pipe](https://en.wikipedia.org/wiki/Pipeline_(Unix)) outputs of file command to the next command.
- `grep`: linux command that searches for PATTERNS from the output of the previous command.
- `ASCII`: data type.


- The flag is at the home directory in the file that you will locate inside the `inhere` directory.
**Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 

- To learn more of what you haven't understood please visit [here](https://google.com) or [here](https://duckduckgo.com) for more information.
