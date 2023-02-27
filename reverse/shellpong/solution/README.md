# shellpong

## Write-up

In this challenge you are given a game binary. It's mentioned in the description that the first one to attend 100 points win. 
When trying to play you will find out that it's impossible to win against the AI at least ones, so it's clearly not the intended way.
When the game lunches it says that it was made using godot. We search for a godot decompiler and we can easily find [this one](https://github.com/bruvzg/gdsdecomp).

There is multiple ways to solve the challenge, we will explain 2 of them:

1. You can modify different game parameters like the AI speed and the ball speed to make it easy for you to win and recompile the game.
2. Reverse the function that sends your score to the server and exploit it.

## Flag

`shellmates{G4m35_h4ck1ng_15_fun}`
