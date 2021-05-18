# OTW - Over The Wire (NATAS) :neckbeard:

## Level 9 ➡ Level 10
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- Level Goal: Find the password for the next challenge.

### How I did it

- I will have to be honest with this, I went to read a writeup and after that I really felt as if I was stupid.
- Let me explain, so we are presented with a web page that allows us ti search for any word/words.
- we are also provided the source code. When reviewing the source code we have a section where there is a PHP script that contains a variable called `$key` that is empty and then there are two if condintions where the first one checks for a variable in the request named `$neddle` and applies that value to the `$key` variable.
- The second if statement performs an action if the `$key` is not an empty string.
- As I said I read a [writeup](https://hackmethod.com/overthewire-natas-9/?v=518f4a738816) just after reading it I realized that it was vulnerable to [command injection](https://owasp.org/www-community/attacks/Command_Injection).
- You will have to dig check around to get the password for the next Level. 

### Conclusion / To Note

> If any please note them down here, if not leave it blank.o

- Code Injection; [Shell Injection](https://en.wikipedia.org/wiki/Code_injection#Shell_injection). 
