# GOpher KEY

## Write-up

At the beginning we can notice a syscall to receive an input

```Assembly
<main+37>:	call   0x555555555030 <__isoc99_scanf@plt>
```

After that, there's a block which is repeated but with different values

```Assembly
<main+42>:	movzx  eax,BYTE PTR [rbp-0x19]
<main+46>:	cmp    al,0x4e
<main+48>:	je     0x555555555175 <main+60>
<main+50>:	mov    eax,0xffffffff
<main+55>:	jmp    0x5555555553d5 <main+668>
```

We can see that there's a jump to the same destination at the end of each block which jumps to the end of the program.

We can conclude that it's comparing the input byte by byte to a direct value in each block.

By putting the bytes following the order of the index of the compared byte in `RBP` we can find the flag.

## Flag

`shellmates{Y0u_r34aly_kN0w_4ss3MBlY}`