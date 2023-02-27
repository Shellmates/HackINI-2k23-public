#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/wait.h>
#include <unistd.h>


#define N 30

typedef char String[N];

int adr,idf_sem;

int main(){
	
	

	
	key_t key =ftok("/etc/passwd" ,1);

	
	adr = shmget(key, N, IPC_CREAT | 0666);
	if(adr==-1){ printf(" \n Error"); exit(0);}

	String* backet =  shmat(adr, 0, 0); 
	if( backet == (String *)-1){ printf("\nError"); exit(0);}


	strcpy(backet, "shellmates{fake_flag}\0");
	
}
