# OTW - Over The Wire (NATAS) :neckbeard:

## Level 6 ➡ Level 7
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- Level Goal: Get the Secret Flag which will enable us to get the password for the next Level.

### How I did it

- We are welcomed with a web page that has a form requesting us to input secret then submit it.
- There is also a View sourcecode link which when you click it you are directed to the html file.
- From the html file there is a section of code just above the form which is a PHP script that includes a file called `secret.inc` from`include` folder, then checks if input has been posted and if it has been posted it checks if secret variable is equeal to the posted secret value and if it is equal it would print; `Access granted. ...` with the password for the next Level.
- The script section doesn't have the `$secret` variable that is holding the secret key but when you check the file that is included, **!! BOOM !!** you will find the secret key hence gaining the password for the next Level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 
