#!/bin/sh

_dir_name="some directory name"

_cnt=1
while [  $_cnt -lt 20 ]; do
	[ $_cnt -lt 10 ] && _name="$_dir_name 0$_cnt" || _name="$_dir_name $_cnt"
	zip -9 -r "$_name.zip" "$_name"
	#echo The counter is $_name
	#ls "$_name"
	: $((_cnt=$_cnt+1))
done
