# OTW - Over The Wire (NATAS) :neckbeard:

## Level 7 ➡ Level 8
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- Level Goal: Get the password for the next Level.

### How I did it

- We are presented with a web page that has two links, when we click either of them they take us to a web page.
- When you take a closer look at the URL of the new web pages you will notice that the site is vulnerable to a [File inclusion vulnerability](https://en.wikipedia.org/wiki/File_inclusion_vulnerability).
- I tried afew things but seems like the password isn't stored at the same directory. After going back to the original web page and viewed the source code I saw a comment with a hint and after following the hint ... **!! BOOM !!** we found the password for the next Level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.

- Read this link on how to test for [Local File Inclusion](https://wiki.owasp.org/index.php/Testing_for_Local_File_Inclusion)
