#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// gcc chall.c -O1 -fno-stack-protector -o chall

void disable_buffering() {
  setbuf(stdin, NULL);
  setbuf(stdout, NULL);
  setbuf(stderr, NULL);
}

int is_numerical(char * );
int degits_sum(int);
int check_part1(char * );
int check_part2(char * );
int check_part3(char * );
int check_part4(char * );
int check_part5(char * );

int check_key(char * key) {
  if (strlen(key) == 24) {zz
    if (check_part1(key) || check_part2(key) || check_part3(key) || check_part4(key) || check_part5(key)) {
      printf("Wrong Key.\n");
      exit(EXIT_FAILURE);
    } else {
      int c;
      FILE * file;
      file = fopen("flag.txt", "r");
      if (file) {
        while ((c = getc(file)) != EOF)
          putchar(c);
        fclose(file);
      }

    }
  } else {
    printf("Wrong Key.\n");
    exit(EXIT_FAILURE);
  }

}

int main() {
  disable_buffering();
  char key[32];
  printf("Enter your serial key: ");
  fgets(key, 25, stdin);
  check_key(key);

  return 0;
}

int is_numerical(char * str) {
  for (int i = 0; i < strlen(str); i++)
    if (!isdigit(str[i])) {
      return 1;
    }
  return 0;
}

int degits_sum(int n) {
  int sum = 0;
  while (n != 0) {
    sum = sum + n % 10;
    n = n / 10;
  }
  return sum;
}

int check_part1(char * key) {
  char part1[4];
  part1[3] = '\0';
  strncpy(part1, key, 3);
  if (is_numerical(part1) || atoi(part1) > 365 || atoi(part1) < 1) return -1;
  else return 0;
}

int check_part2(char * key) {
  char part2[3];
  part2[2] = '\0';
  strncpy(part2, key + 3, 2);
  if (is_numerical(part2) || (atoi(part2) < 95 && atoi(part2) > 3)) return -1;
  else return 0;
}

int check_part3(char * key) {
  char part3[6];
  strncpy(part3, key + 5, 5);
  if (strncmp(part3, "-MUH-", 5)) return -1;
  else return 0;
}

int check_part4(char * key) {
  char part4[8];
  part4[7] = '\0';
  strncpy(part4, key + 10, 7);
  if (is_numerical(part4) || (degits_sum(atoi(part4)) % 7)) return -1;
  else return 0;
}

int check_part5(char * key) {
  char part5[6];
  part5[5] = '\0';
  strncpy(part5, key + 18, 5);
  if (key[17] != '-' || is_numerical(part5)) return -1;
  else return 0;
}
