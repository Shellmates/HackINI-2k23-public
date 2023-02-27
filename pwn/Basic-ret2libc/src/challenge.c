#include <stdio.h>
#include <stdlib.h>

void disable_buffering(){
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

void vuln(){
    char buf[32] ;
    printf("Enter data: ");
    gets(buf);
}

int main(){
    disable_buffering();
    printf("Some help: %p\n",printf);
    vuln() ;
    return 0 ;
}