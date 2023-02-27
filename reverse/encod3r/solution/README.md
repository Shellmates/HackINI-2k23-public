# GOpher KEY

## Write-up

We can start by opening the file using `Ghidra`

We can notice at the beginning of the main function that two files are opened

```C
  local_9 = 'N';
  local_10 = 0;
  printf("%s","Filename: ");
  __isoc99_scanf(&DAT_0010200f,local_78); // reading the file name
  strcpy((char *)local_c8,local_78);
  sVar3 = strlen((char *)local_c8);
  *(undefined8 *)((long)local_c8 + sVar3) = 0x7972616e69625f; // generating the 2nd filename
  strcpy((char *)&local_118,local_78);
  sVar3 = strlen((char *)&local_118);
  *(undefined8 *)((long)&local_118 + sVar3) = 0x6465646f636e655f; // generating another filename
  auStack272[sVar3] = 0;
  local_18 = fopen(local_78,"rb+"); // opening the first file
  local_20 = fopen((char *)local_c8,"w"); // opening the second file
  if ((local_20 == (FILE *)0x0) || (local_18 == (FILE *)0x0)) {
    printf("%s","Error while opening file");
    uVar4 = 0xffffffff;
  }
  while( true ) {
      iVar2 = feof(local_18);
      if (iVar2 != 0) break;
      fread(&local_139,1,1,local_18); // reading the char
      uVar1 = convert_to_binary((uint)local_139);
      sprintf(local_138,"%d",(ulong)uVar1); // converting the result into string
      add_zeros(local_138);
      fputs(local_138,local_20);
}
```

Now the file is beeing read char by char and passed into a function `convert_to_binary` which seems that it coneverts an integer to a binary

```C
int convert_to_binary(int param_1)
{
  int local_1c;
  int local_10;
  int local_c;
  
  local_c = 1;
  local_10 = 0;
  for (local_1c = param_1; local_1c != 0; local_1c = local_1c / 2) {
    local_10 = local_10 + ((local_1c - (local_1c >> 0x1f) & 1U) + (local_1c >> 0x1f)) * local_c;
    local_c = local_c * 10;
  }
  return local_10;
}
```
The result is converted to string and passed to another function `add_zeros` which seems that it adds zeros from the left to make the entered string with a length of `8`

```C
void add_zeros(char *param_1)
{
  size_t sVar1;
  undefined2 local_15 [4];
  int local_c;
  
  sVar1 = strlen(param_1);
  local_15[0]._0_1_ = '\0';
  for (local_c = 8 - (int)sVar1; 0 < local_c; local_c = local_c + -1) { // while the difference between the length of the string and 8 is not 0
    sVar1 = strlen((char *)local_15);
    *(undefined2 *)((long)local_15 + sVar1) = 0x30; // adding "0"
  }
  strcat((char *)local_15,param_1);
  strcpy(param_1,(char *)local_15);
  return;
}
```

Now let's return to the main function, we can conclude that this loop reads every char from the 1st file

Then the char is converted to a binary a string and to make them with the same length zeros are added from the left

Finally the binary string is written the 2nd file

```C
while( true ) {
      iVar2 = feof(local_18);
      if (iVar2 != 0) break;
      fread(&local_139,1,1,local_18); // reading the char
      uVar1 = convert_to_binary((uint)local_139); // converting the char to binary string
      sprintf(local_138,"%d",(ulong)uVar1); // converting the result into string
      add_zeros(local_138); // adding zeros from the left
      fputs(local_138,local_20); // writing the binary string in the 2nd file
}
```

The 1st and 2nd files are closed

The 2nd file is reopned in read mode and a third file is opened in write mode using the 3rd generated filename

```C
    fclose(local_18);
    fclose(local_20);
    local_28 = fopen((char *)local_c8,"r");
    local_30 = fopen((char *)&local_118,"w");
    if ((local_28 == (FILE *)0x0) || (local_30 == (FILE *)0x0)) {
      printf("%s","Error while opening file");
      uVar4 = 0xffffffff;
    }
```

`local_9` was initialized to `N`

in case `local_9` equals to `N` its value is changed to the first readen char from the file that contains the binary strings so it can be `1` or `0`

in case the readen char and `local_9` are equal and `local_10` is inferior to `8` a`1` is added to `local_10`

We can conclude that `local_10` is used a counter to caluclate the succesive occurence of a `0` or `1`

The counter is used as an index to two arrays to get an element and write in the third file

By searching we can find that the values of the two arrays are: `zero_table.1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']` and `one_table.0 = ['I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q']`

So at the end we can say that each number of successive occurence of `0` or `1` est replaced with a specific char

At the end the file that contains binary strings is deleted

```C
      while( true ) {
        iVar2 = fgetc(local_28);
        local_31 = (char)iVar2;
        if (local_31 == -1) break;
        if ((local_31 == local_9) && (local_10 != 8)) {
          local_10 = local_10 + 1;
        }
        else if (local_9 == 'N') {
          local_10 = local_10 + 1;
          local_9 = local_31;
        }
        else {
          if (local_9 == '0') {
            fputc((int)*(char *)((long)&zero_table.1 + (long)(local_10 + -1)),local_30);
          }
          if (local_9 == '1') {
            fputc((int)*(char *)((long)&one_table.0 + (long)(local_10 + -1)),local_30);
          }
          local_10 = 1;
          local_9 = local_31;
        }
      }
      fclose(local_28);
      fclose(local_30);
      remove((char *)local_c8);
    }
```

Now, we understood how it works we can make a python program the reverse the process
Let's start by regenrating the file that contains the binary strings

```Python
encoded_file = open("flag_encoded", "r")
binary_file = open("binary_file", "w")

zero_table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
one_table = ['I', 'J', 'K', 'L', 'M', 'N', 'P', 'Q']

encoded = encoded_file.read()

for c in encoded:
    if c in zero_table:
        binary_file.write((zero_table.index(c) + 1) * "0")
    if c in one_table:
        binary_file.write((one_table.index(c) + 1) * "1")
        
encoded_file.close()
binary_file.close()
```

The 2nd step is to regnerate the original file

```Python
binary_file = open("binary_file", "r")
flag = open("flag2", "wb")

while True:
    c = binary_file.read(8)
    if not c:
        break
    flag.write(int(c, 2).to_bytes(1, 'big'))
    
binary_file.close()
flag.close()
```

Now we look for the file type

`GIF image data, version 89a, 498 x 272`

It's a GIF image that contains the flag

## Flag

`shellmates{h0w_d1D_Y0u_br34K_mY_3nc0d1nG?}`