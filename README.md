## It's a Python script that takes a subdomain file and generates a wordlist with some archive extensions.

## How to Use
It takes an input and output file name. An input file is required; otherwise, it throws an error.

```
# python3 main.py input.txt output.txt
```

#### Extenstions
```
zip
tar
gz
bz2
xz
7z
rar
tar.gz
tgz
tar.bz2
tbz2
tar.xz
config
sql
txt
```


##### Example 
Subdomain file
```
xfinity.com
www.xfinity.com
amdocs-omni.gslb2.xfinity.com
si-x1-nightly.xfinity.com
urlredirector.xfinity.com
```

The script will be generating the 255 possible file names.
```
xfinity_com.gz
xfinity.com.7z
xfinity.com.tar.xz
xfinity_com.tar
xfinity_com.xz
xfinity.com.tgz
xfinity_com.bz2
xfinity-com.7z
xfinity_com.tar.gz
xfinity.com.tar.bz2
....
....
```
