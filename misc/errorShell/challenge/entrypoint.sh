#!/bin/sh

exec socat -v tcp-listen:1337,reuseaddr,fork,keepalive, EXEC:"./login.sh",stderr
