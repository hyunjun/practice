#!/bin/sh

echo `date -d "-5 days" +%Y%m%d`	#	5 days ago
echo `date +%Y%m%d`
echo `date -d "5 days" +%Y%m%d`	#	5 days after
