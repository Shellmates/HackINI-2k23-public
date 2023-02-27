# Fibonatcp

## Write-up

```bash
tshark -r fibonatcp.pcapng -Y "tcp.len==1" -T fields -e data.data > data.txt
```
```python
data = open("data.txt","r").read().splitlines()
# Look up fibonnaci's 
fibo=[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040]

flag =""
ps = 1
while "}" not in flag:
	if ps in fibo:
		flag+=bytes.fromhex(data[ps-1]).decode()
		print(flag)
	ps+=1

```
## Flag

`shellmates{F!b0Oo0}`
