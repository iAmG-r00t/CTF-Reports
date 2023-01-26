# Level6 -> Level7

lvl6 pass; `YZ55XPVk2l`

strace ./leviathan6 shows you that the binary is setting the password as 4 digits
so create a bruteforcer of 4 possible digits in `/tmp/brTTu`.

Pass: `7123`

```sh
#!/bin/bash

for a in {0000..9999}
do
	echo "pass: $a"
	~/leviathan6 $a
done
```

After a few seconds you get a shell and you can get the password; `cat /etc/leviathan_pass/leviathan7`

Password for leviathan7; `8GpZ5f8Hze`
