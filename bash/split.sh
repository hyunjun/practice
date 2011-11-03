#!/bin/sh

#	split.sh
#		split text file line by line
#		Usage:	split.sh [file to split] [number of split]

_file=$1
_split_cnt=$2
echo "file: split $_file into $_split_cnt files"
_total_line=`wc -l $_file | awk '{print $1}'`
echo "total line = $_total_line"
_make_split_num=$(($_total_line/$_split_cnt))
echo "need to make split every $_make_split_num lines"

#	1.	read line by line from file and write line by line using echo
#exec<$_file	#	read from file
#_line_num=0
#_split_num=0
#while read line
#do
#	_line_num=`expr $_line_num + 1`
#	echo $line >> $_file.$_split_num
#	if [ `expr $_line_num % $_make_split_num` = 0 ]; then
#		_split_num=`expr $_split_num + 1`
#	fi
#done
#
#if [ -e $file.$_split_num ]; then
#	_split_num=`expr $_split_num + 1`
#fi

#	2.	read using head & tail
#_cur_idx=0
#while [ $_cur_idx -lt $_split_cnt ]
#do
#	_cur_idx=`expr $_cur_idx  + 1`
#	_head_line=$(($_make_split_num*$_cur_idx))
#	head $_file -n $_head_line | tail -n $_make_split_num >> $_file.$_cur_idx
#done
#
#_printed_line=$(($_make_split_num*$_cur_idx))
#if [ $_printed_line -lt $_total_line ]; then
#	_rest_line=$(($_total_line-$_printed_line))
#	tail $_file -n $_rest_line >> $_file.$_cur_idx
#fi

#	3.	read n lines using sed
_cur_idx=0
while [ $_cur_idx -lt $_split_cnt ]
do
	_start_line=$(($_make_split_num*$_cur_idx + 1))
	_end_line=`expr $_start_line + $_make_split_num - 1`

	_padding=''
	_padding_num=`expr ${#_split_cnt} - ${#_cur_idx}`
	while [ $_padding_num -gt 0 ]
	do
		_padding=0$_padding
		_padding_num=`expr $_padding_num - 1`
	done

	sed -n "${_start_line},${_end_line}w ${_file}.${_padding}${_cur_idx}" $_file
	_cur_idx=`expr $_cur_idx  + 1`
done

_start_line=`expr $_end_line + 1`
if [ $_start_line -le $_total_line ]; then
	#	http://unix-school.blogspot.com/2011/04/sed-read-from-file-or-write-into-file.html
	sed -n "${_start_line},${_total_line}w ${_file}.${_cur_idx}" $_file
fi

_splitted_files=`ls -al | awk '{print $8}' | grep -e $_file."[[:digit:]]\+$" | sort -n`
#tar cfz $_file.$_split_cnt.tar.gz $_splitted_files
tar cfz $_file.$_split_cnt.tar.gz `ls -al | awk '{print $8}' | grep -e $_file."[[:digit:]]\+$" | sort -n`
#rm $_file.[[:digit:]]		#	only deletes $_file.?
#rm $_file."[[:digit:]]\+$"	#	it doesn't work properly
rm $_splitted_files

