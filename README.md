## It's a Python script that takes a subdomain file and generates a wordlist with some archive extensions.

## How to Use
It takes an input and output file name. An input file is required; otherwise, it throws an error.

```
# python3 main.py input.txt output.txt
```

#### Extenstions
```
.zip
.tar
.gz
.bz2
.xz
.7z
.rar
.cab
.tar.gz
.tgz
.tar.bz2
.tbz2
.tar.xz
.txz
.zipx
.ace
.arj
.lzh
.sit
.z
.cbr
.cbz
.jar
.txt
.config
.sql
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

The script will be generating the 1300 possible file names.
```
xfinity.com.tgz
xfinity-com.tar
xfinity-com.7z
xfinity.com.cbr
xfinity-com.sql
XFINITY.COM.config
xfinity-com.rar
COM.z
COM.gz
XFINITY.zipx
xfinity-com.config
xfinity.com.txt
xfinity.cbr
COM.arj
....
....
```
