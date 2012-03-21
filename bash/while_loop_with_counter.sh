#!/bin/sh

_cnt=1
while [  $_cnt -lt 10 ]; do
	echo The counter is $_cnt
	#	http://tldp.org/LDP/abs/html/ops.html
	: $((_cnt = $_cnt + 1))
done
