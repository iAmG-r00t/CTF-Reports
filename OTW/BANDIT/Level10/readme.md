# OTW - Over The Wire (Bandit) :neckbeard:

## Level 10
## Author: [@th3-gr00t](https://th33-gr00t.tk/) -  [:bird:](https://twitter.com/th3_gr00t/)

> For more resources you can check our my [blog](https://th33gr00t.blogspot.com/)

### Challenge

- The main goal of this challenge was to learn about base64 encoding scheme/format.
- We were provided the `target host` to connect to, `port` to use, `username` and `password` for authentication.

### How I did it

- So for me this challenge was actually easy for me, I even hadn't read the level goal from the website.
- We were provided with a `data.txt` file that contained base64 encoded data.
- The momement I outputed the file data using `cat`, I knew the encoding scheme that was used and I proceeded to decoding it.

```sh
# so I will avoid showing the flag ...
# ... because that's how I do it

# output the file contents
cat data.txt

# pipe the file contents to `base64` command t decode it
cat data.txt | base64 --decode 
```

- The flag is at the home directory in the `data.txt` file, once you decode the encoded data.
- **Note:** The *flag* is the `password` for the next level.

### Conclusion / To Note

> If any please note them down here, if not leave it blank.

- You can research on other ways to decode `base64` with either python or online tools.
- Also read about base64 learn it by heart. 👨‍🏫
