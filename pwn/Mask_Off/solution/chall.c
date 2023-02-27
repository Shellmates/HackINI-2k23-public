#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define KEY_LENGTH 9
#define RANDOM_BYTES_LENGTH 8

bool generateRandomBytes(unsigned char *bytes, int length) {
    int i;

    srand(time(NULL));   // seed the random number generator with current time

    for (i = 0; i < length; i++) {
        bytes[i] = rand() % 256;   // generate a random byte between 0 and 255
    }

    return true;
}

int main() {

    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);

    //# Define the chunck of bytes in the heap

    int length;  // length of random bytes array
    unsigned char *bytes;   // pointers to dynamic arrays of unsigned chars
    int i;

    srand(time(NULL));   // seed the random number generator with current time

    length = rand() % 800 + 600;   // generate a random length between 1 and 10

    bytes = (unsigned char *) malloc(length * sizeof(unsigned char));   // allocate memory for bytes1 array

    if (bytes == NULL) {
        printf("Memory allocation failed.\n");
        return 1;
    }

    if (!generateRandomBytes(bytes, length)) {
        printf("Error generating random bytes.\n");
        free(bytes);
        return 1;
    }


    //# Read Key From a file

    char *filename = "./flag.txt";
    char key[KEY_LENGTH];
    FILE *file = fopen(filename, "r");

    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Read the first line of the file into the 'key' variable
    if (fgets(key, KEY_LENGTH, file) != NULL) {
        // Remove the newline character from the end of the line
        if (key[strlen(key) - 1] == '\n') {
            key[strlen(key) - 1] = '\0';
        }
    }

    //# Define and copy key and offsets inside the chunck
    unsigned char random_bytes1[RANDOM_BYTES_LENGTH];
    unsigned char random_bytes2[RANDOM_BYTES_LENGTH];
    char *string_value = "MaskingU";
    int offset = rand() % 500 + 300;

    // Copy the file value into the big buffer at the specified offset
    memcpy(bytes + offset, key, strlen(key));

    // Generate two random bytes arrays and copy them into the big buffer at the specified offset
    generateRandomBytes(random_bytes1, RANDOM_BYTES_LENGTH);
    memcpy(bytes + offset + strlen(key), random_bytes1, RANDOM_BYTES_LENGTH);

    generateRandomBytes(random_bytes2, RANDOM_BYTES_LENGTH);
    memcpy(bytes + offset + strlen(key) + RANDOM_BYTES_LENGTH, random_bytes2, RANDOM_BYTES_LENGTH);

    // Copy the string value into the big buffer at the specified offset
    memcpy(bytes + offset + strlen(key) + RANDOM_BYTES_LENGTH * 2, string_value, strlen(string_value));




    //# Print the heap 
    unsigned char *heap = sbrk(0) - 0x20d60;   // get current program break
    printf("Here you go: ");
    for (i = 0; i < length; i++) {
        printf("%c", heap[i]);   // print each byte in hexadecimal format
    }
    printf("\n");


    fclose(file);
    free(bytes);   // free the dynamically allocated memory

    return 0;
}