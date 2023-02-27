#include <stdio.h>
#include <stdlib.h>

#define FLAG_SIZE 64

void win(int val1 ,int val2){
    FILE* f = fopen("flag.txt","r");
    char flag[FLAG_SIZE];
    if (f==NULL){
        perror("Flag file not found");
        exit(1);
    }
    fgets(flag,FLAG_SIZE,f);

    if ((val1==0xdeadbeef)&&(val2==0x1337))
        printf("gg, here is your flag: %s\n",flag);
    else
        printf("You were close; try again");
}

void disable_buffering(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void vuln(){
    char buf[32];
    int a = 400 ; 
    int b = 500 ;
    printf("Enter data: ");
    gets(buf);
    if ((a!=400)||(b!=500)){
        printf("Stack Smashing detected\nThe program will automatically exit");
        exit(-1);
    }
    printf("You entered: %s\n",buf);
}

int main(){
    disable_buffering();
    vuln();
    return 0 ;
}