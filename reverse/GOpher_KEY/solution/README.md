# GOpher KEY

## Write-up

It's a GO binary, we can use `delve` which is a GO debugger

The binary isn't stripped so we can easily retrieve the source code

After extracting the source code using `delve` we can notice there's an input

The input format is check to verify if it's the same as `shellmates{content}` which is the flag format

Then the content is encrypted using `AES` encryption and the key obtained from an http request

After encrypting the content it's compared to a string which we can suppose it's the content of the correct flag

after decrypting the content we can put in the flag format and find the flag


## Flag

`shellmates{1n_G0l4nG_w0rLDD}`