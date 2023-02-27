#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdint.h>

char* message[2];

void setup(){
    setbuf(stdin, 0LL);
    setbuf(stdout, 0LL);
    setbuf(stderr, 0LL);
    message[0] = strdup("Go on write something somewhere\n");
    message[1] = strdup("How nice!! but be careful that's your last chance.\n");
}

int main(void){
    char input[0x20];
    char report[0x20];
    uint64_t* where;
    setup();

    for(int i = 0; i < 2; i++){
        printf("%s", message[i]);
        puts("[*] where: ");
        fgets(input, 20, stdin);
        input[strcspn(input, "\n")] = 0;
        where = (uint64_t *)atoll(input);
        puts("[*] what: ");
        fgets(input, 20, stdin);
        input[strcspn(input, "\n")] = 0;
        *where = atoll(input);
    }

  puts("Okey tell me what you've done and i will assess your skills later");
  fgets(report, 112, stdin);

}
