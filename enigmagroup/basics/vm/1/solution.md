# Variable Manipulation 1

If you append `?page=../admin/.htpasswd` to the URL it will output the contents of the Apache file `.htpasswd`. This is as follows:

```
admin:dXWxIS6i6irN6
```

I didn't find `dXWxIS6i6irN6` in any rainbow table. I found out it was to be decoded by [crypt(3)](https://en.wikipedia.org/wiki/Crypt_(C)), and that this particular password was encrypted with DES.

John The Ripper could probably crack this nicely, but I wrote my own python programme, `crypt_crack.py`, that works for this case.

I could log in with username `admin`, password `dog`.
