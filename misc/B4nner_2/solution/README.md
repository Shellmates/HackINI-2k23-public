# B4nner_2

---

## Write-up

When we SSH into the machine we notice that it outputs the whole file and than exits, it means that either one of the commands `more` or `less` is excuted with `-e` , `-E` respectively. 

```
more :
-e, --exit-on-eof
           Exit on End-Of-File, enabled by default if not executed on terminal.
-------------------------
less :
-E or --QUIT-AT-EOF 
              Causes less to automatically exit the first time it reaches end-of-file.
```

![Untitled](B4nner_2%20d26d4fb37d8d42d2bac874f0f18d38cd/Untitled.png)

It means we have to force the command to read the file in interactive mode, and to do so we only need to resize our terminal ( the size of the window less than the size of the text ) like this :

![Untitled](B4nner_2%20d26d4fb37d8d42d2bac874f0f18d38cd/Untitled%201.png)

Now we’re in interactive mode and it’s the `more` command.

Our goal now is to gain a shell , inside the interactive mode of the more command we can do the following according to the help of the more command ( click `h` to display it ):

```
!<cmd> or :!<cmd>       Execute <cmd> in a subshell
v                       Start up '/usr/bin/vi' at current line
```

1. The first way by executing commands through `!{command}` , this approach won’t work because the default login shell has been changed to a script which outputs the banner , which means we won’t get any result 
2. The second way by doing a VI or VIM escape , clicking `v` will start up the text editor like this :

![Untitled](B4nner_2%20d26d4fb37d8d42d2bac874f0f18d38cd/Untitled%202.png)

And since our default login shell has been changed it means we have to reset the shell variable inside the VI or VIM editor by typing the following `:set shell:/bin/bash`

![Untitled](B4nner_2%20d26d4fb37d8d42d2bac874f0f18d38cd/Untitled%203.png)

and to open up the shell we simply execute it by `:shell`

Now we’re truely in :

![Screenshot from 2023-02-16 19-55-41.png](B4nner_2%20d26d4fb37d8d42d2bac874f0f18d38cd/Screenshot_from_2023-02-16_19-55-41.png)

Now we have to look around how to get the flag and it seems it’s not that quite easy, there are two mainly users `ctf` which is a simple user and `ctf-cracked` which have more permissions and he can read the flag, one special thing here is that the use `ctf` is part of the `ctf-cracked` group

Checking what we can execute using the `sudo -l` command :

1. Can’t modify `hash.py` but we can execute it using the command `sudo -u ctf-cracked python3 /home/ctf/hash.py`

![Untitled](B4nner_2%20d26d4fb37d8d42d2bac874f0f18d38cd/Untitled%204.png)

And the script simply prints the hash of the file flag.txt as shown below : 

![Screenshot from 2023-02-16 20-03-14.png](B4nner_2%20d26d4fb37d8d42d2bac874f0f18d38cd/Screenshot_from_2023-02-16_20-03-14.png)

The script of `[hash.py](http://hash.py)` is the following :

```python
from flaglib import * 

try:
    with open("/home/ctf-cracked/flag.txt","rb") as flag:
        flaghash = filehash(flag)
        print(flaghash)
except:
    print("Permession denied")
    exit(2)
```

Since the challenge is tagged with `Python` and `Linux` it means we don’t need to think outside of this scope we only need to figure out what’s wrong with this script.
the `flaglib` doesn’t seem to be a native python library we need to find out where it’s located and what does it contains and what kind of permession it has

![Untitled](B4nner_2%20d26d4fb37d8d42d2bac874f0f18d38cd/Untitled%205.png)

The imported library is owned by `root` and belongs to the group `ctf-cracked` and since our user is part of the group `ctf-cracked`, the library has write permession on the group, it means we can hijack the library easly by putting our code inside it 

Opening the imported library : `vim /opt/pylib/flaglib.py`

![Untitled](B4nner_2%20d26d4fb37d8d42d2bac874f0f18d38cd/Untitled%206.png)

We can just a piece of code where it prints the flag for us we can do it simply by :

![Untitled](B4nner_2%20d26d4fb37d8d42d2bac874f0f18d38cd/Untitled%207.png)

Let’s try to execute the script once again

![Untitled](B4nner_2%20d26d4fb37d8d42d2bac874f0f18d38cd/Untitled%208.png)

## The flag

`shellmates{vIm_3$c4pE_&_pyth0N_lIb_hIj4cKING_cOMbO}`

GGs for @Fa2y and @Cynex for finding an unintended way solution which is creating a `flaglib.py` in the current directory with the malicious code
so when we execute the `hash.py`script, python will find their library before my library.
