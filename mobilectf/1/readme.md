# App CTF Challenge 1

## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

### Challenge

- The goal behind this challenge is to figure out the username and password that would let the challenger login successfully.

### How I solved it

- Started by installing the application with adb. The app is quite simple it is called `admin Login Application` with a `username` and `password`.
- When trying to input a random username and password it fails and shows a sad smilling face. 
- **Next Stop**: `Source Code Analysis`;
  - Fired up `jadx`; knowing we are looking for the username and password, I started by looking for hardcorded data at location; `resources.arsc/res/values/strings.xml`
  - After checking the source code, I found a MD5 hash in the MainActivity.
  - Decrypting it using an online site gave us the username and password, inputing them gave us a smile.

![image](https://user-images.githubusercontent.com/29776892/116350172-220ef400-a7fa-11eb-8f8b-c3889b8f2f76.png)


### Conclusion / To Note

- A smile is what we want, so the important thing here we have learnt is source code analysis is where the bugs are at.
- Anything hardcoded can be found.
