#!/bin/bash

error(){
	echo \>
	read cmd
	eval $cmd  2>&1 1>/dev/null
}

while : ;do
	error 
done
