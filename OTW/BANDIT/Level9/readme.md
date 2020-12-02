# OTW - Over The Wire (Bandit) :neckbeard:

## Level 9
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge was to learn how to use `grep`.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- We are informed that the **flag** is stored in the file known as **`data.txt`** in one of the few human readable strings, preceded by several '**=**' characters.
- To be honest at first my thoughts went too deep that I forgot to try the basic things.
- I ended up googling to see other peoples solution and well it was too basic which is as below.

```sh
# Using strings and grep
strings data.txt | grep '='

# Maybe better results
strings data.txt | grep -E "==+"
```

- First and foremost for those wondering why one is using the `strings` command, its because the file data type is just data, meaning the file contains both non-human readable and human readable strings.
- Second I wasn't satisfied with this two solutions, so I proceeded to look for a more precise solution that I would love and maybe learn something from it.
- So the solution that I came up with were two using the strings command and grep, and using the grep command only.

```sh
# First solution: using the strings and grep command.
strings data.txt | grep -E '==+.*\ [[:alnum:]]{13,}'

# Second solution: using the grep command only.
grep -aE '==+.*\ [[:alnum:]]{13,}' data.txt 
```

- The first solution is searching for two patters, where it looks for the multiple special character and (which is equal to **`.*`** ) alphanumeric character after a space that are more than 13 characters.
- Breaking it down;
  - `strings` :  Linux command that displays printable strings in a file.
  - `data.txt` : file
    - `grep` : Linux command that searches for patterns in a file.
    - `-E` : grep command argument option where PATTERNS are extended regular expressions.
    - `==+` : First pattern where it describes the special character is more/countless. (=========== ....)
    - `.*` : Works as an AND Operator in grep expression command.
    - `\ ` : Begin of the second pattern where it escapes a character, which is the space. You can use [[:space:]] other than the actual space character.
    - `[[:alnum:]]` : continuation of the second pattern where it means alphanumeric characters.
    - `{13,}` : end of the second pattern which means character count should be more than 13.

- The second solution now avoid using the string command and just uses grep to find the flag using the `grep` command.
- The only difference to this grep command is how we use the argument `-a` which allows grep command to search for patterns in binary files/ files with both human readable and non-human readable characters. 

- The flag is at the home directory in the `data.txt` file.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.

- Read on the below resource on grep and patterns.
  - [Regular Expressions.](https://www.princeton.edu/~mlovett/reference/Regular-Expressions.pdf)
  - [Linux Grep Operators with Examples.](https://www.thegeekstuff.com/2011/10/grep-or-and-not-operators/)
  - [Grep for multiple Strings,Patterns Or Words.](https://phoenixnap.com/kb/grep-multiple-strings)
  - [Regular expressions in grep (regex) with examples.](https://www.cyberciti.biz/faq/grep-regular-expressions/)

- You learn by being curious, and all I can say is keep questioning the impossible. **!! THAT'S HOW YOU WILL LEARN BEST !!**
