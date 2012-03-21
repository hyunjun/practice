#!/bin/sh
#	http://www.cyberciti.biz/tips/handling-filenames-with-spaces-in-bash.html
SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
for f in *
do
#	echo "$f"
	[ -d "$f" ] && zip -9 -r "$f.zip" "$f"
done
IFS=$SAVEIFS
