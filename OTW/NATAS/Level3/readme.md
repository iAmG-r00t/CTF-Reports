# OTW - Over The Wire (NATAS) :neckbeard:

## Level 3 ➡ Level 4
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- Level Goal: Get the password for the next Level.

### How I did it

- We are introduced with the same message as before; `There is nothing on this page.`
- When I checked the page source there was a comment saying; `No more information leaks!! Not even Google will find it this time....`
- Well being Level3 I thought of the simplicity of the challenge.
- Bing!! Bing!! Bing!! ... I then remembered about the `robots.txt` file, which according to the mozilla MDN Web Docs states it is a file which is usually placed in the root of any website. It decides whether crawlers are permitted or forbidden access to the web site.
- **!! BOOM !!** we find our data leak.

### Conclusion / To Note

> If any please note them down here, if not leave it blank. 
