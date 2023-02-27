# Sharing is caring

## Write-up

First decompile the binary with ghidra.

We can see the key to the shared memory, use it to read the flag.
```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <unistd.h>


#define N 30
#define MAXCHAINE 50


typedef char String[MAXCHAINE];

int adr,idf_sem;

int main(){
	
	

	
	key_t key =ftok("/etc/passwd" ,1);

	
	adr = shmget(key, N, IPC_CREAT | 0666);
	if(adr==-1){ printf(" \n Error"); exit(0);}

	String* backet =  shmat(adr, 0, 0); 
	if( backet == (String *)-1){ printf("\nError"); exit(0);}


	printf("%s", backet);
	
	
	
	shmdt(backet);
	shmctl(adr, IPC_RMID, 0);
}

```

## Flag

`shellmates{PL41N_1N_M3M0Ry}`