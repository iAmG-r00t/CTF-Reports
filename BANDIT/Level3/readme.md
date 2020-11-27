# OTW - Over The Wire (Bandit) :neckbeard:

## Level 3
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- Main goal of the challenge was to locate a hidden file.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- Honestly I live within hidden files, so this challenge was a breeze for me.
- At the home directory there was a directory named `inhere` where there was a hidden file called `.hidden`.

```sh
ls -l * 		# List all of the files present

ls -l inhere/* 		# List all of the files present in `inhere` directory

ls -l -a inhere/* 	# List all files and don't ignore entries starting with

cat inhere/.hidden	# parse and output contents of .hidden file
```


- The flag is at the home directory in the `.hidden` file.
**Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.

- So for those people who don't know about **hidden** files and directories, please read below resources to get more conversant with them and it's history.

1. Source @ Wikipedia - [Hidden file and hidden directory](https://en.wikipedia.org/wiki/Hidden_file_and_hidden_directory)
2. Source @ Stack Exchange - [Why are filenames that start with a dot hidden? Can I hide files without using a dot as their first character](https://unix.stackexchange.com/questions/88875/why-are-filenames-that-start-with-a-dot-hidden-can-i-hide-files-without-using-a)
3. Source @ Waybackmachine - [A lesson in shortcuts by Rob Pike](https://web.archive.org/web/20140803082229if_/https://plus.google.com/+RobPikeTheHuman/posts/R58WgWwN9jp) who worked on UNIX at Bell Labs.

**Interesting Snippets**

```sh
: <<'COMMENT1'
The notion that filenames preceded by a . should be hidden is the result of a software bug in the early days of Unix. When the special . and .. directory entries were added to the filesystem, it was decided that the ls command should not display them. However, the program was mistakenly written to exclude any file whose name started with a . character, rather than the exact names . or ...
COMMENT1

: <<'COMMENT2'
I'm pretty sure the concept of a hidden file was an unintended consequence. It was certainly a mistake.
COMMENT2
``` 

- So it started off as a bug, and then it was embraced as a feature (for the record, . is a link to the current directory and .. is a link to the directory above it.
- They are commonly used for storing user preferences or preserving the state of a utility, and are frequently created implicitly by using various utilities.
- They are **not a security mechanism** because **access is not restricted**.
- Usually the intent is simply to not "clutter" the display of the contents of a directory listing with files the user did not directly create.
