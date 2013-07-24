#!/bin/bash

#	http://danielcorin.github.io/blog/2013/07/23/qc/
#	https://github.com/danielcorin/qc/blob/master/qc/qc.sh
#	qc.sh 7-8
#	qc.sh 9.8-1
#	qc.sh 2**4
#	qc.sh "factorial(10)"
#	qc.sh "hex(255)"
#	qc.sh "sin(pi/7)"

python -c "from math import *; print $1" | pbcopy
pbpaste
