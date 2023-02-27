# MW95

## Write-up

In this cahllenge you're given a binary. When you try to run it it asks you for a serial key.

You decompile the binary using a decompiler like Ghidra/Cutter, you will notice that the binary isn't stripped and that the serial key is validated through 5 functions named check_part[1-5].

After analysing each function we can figure out this algorithm (Which is the actual algorithm used for validating windows95 serial number).

1. The first three digits represent the day of the year, ranging from 001 to 366.
2. The next two digits represent the year, ranging from 95 to 03.
3. The next 5 characters must be '-MUH-' ('-OEM-' in the actual windows 95 algorithm)
4. The next seven digits must be divisible by 7 and start with 0.
5. The last five digits do not matter.

So basically you can use any window95 serial key and replace `OEM` with `MUH` to validate the challenge and get the flag.

## Flag

`shellmates{s3R14l_K3YS_4R3_N07_4_G00d_s3cuR17Y_M3ch4N1sm}`
