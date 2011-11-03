#!/bin/sh

#	arithmetic.sh
#		show calculation
#		Usage:	arithmetic.sh [num1] [num2]

_left=$1
_right=$2
echo "$_left + $_right = "`expr $_left + $_right`
echo "$_left - $_right = "`expr $_left - $_right`
echo "$_left * $_right = $(($_left*$_right))"
echo "$_left / $_right = $(($_left/$_right))"
echo "$_left % $_right = "`expr $_left % $_right`
