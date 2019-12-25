#!/bin/sh

# https://leetcode.com/problems/tenth-line/
# https://www.cyberciti.biz/faq/unix-howto-read-line-by-line-from-file/
# https://stackoverflow.com/questions/18488651/how-to-break-out-of-a-loop-in-bash

# runtime; 0ms, 100.00%
# memory; 3.8MB, 28.57%
_cnt=0
input="./file.txt"
while IFS= read -r line
do
	: $((_cnt = $_cnt + 1))
  if [ $_cnt -eq 10 ]; then
    echo "$line"
    break
  fi
done < "$input"
