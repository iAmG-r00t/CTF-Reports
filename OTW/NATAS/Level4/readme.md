# OTW - Over The Wire (NATAS) :neckbeard:

## Level 4 ➡ Level 5
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- Level Goal: Get the password for the next challenge.

### How I did it

- We see a web page informing us that **Access disallowed**, that we are visiting from the wrong URL while authorized users should come only from another URL.
- Once I saw that I knew what I was to do, I knew it had to do with http headers, after some reading on Mozilla MDN Web Docs on HTTP headers there was a section on Request context headers.
- After reading I came to know that the referer header is the one we should change to match the URL authorized users should come from.
- The `Referer` request content header contains an absolute or partial address of the page making the request, the header allows servers to identify where people are visiting them from.
- So editing is the major problem, from a terminal one can use curl to do this fairly easy but when using the web browser you will be forced to install an extension that will allow you to do so.
- After doing so, **!! BOOM !!** we found the password for the next challenge.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 
