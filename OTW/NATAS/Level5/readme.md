# OTW - Over The Wire (NATAS) :neckbeard:

## Level 5 ➡ Level 6
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- Level Goal: Get the password for the next Level.

### How I did it

- We are presented with a web page informing us `Access disallowed.` That we are not logged in.
- After some review I checked around and noticed that from our local stored Cookies there was a Cookie under the URL named `loggedin` with the value `0`.
  - I changed the value from `0` to `1`, refreshed the web page and we got our password for the next challenge.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 
