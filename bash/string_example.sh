#/bin/sh

#	http://softroom.springnote.com/pages/2088108

#	string length
#	http://wiki.kldp.org/HOWTO/html/Adv-Bash-Scr-HOWTO/string-manipulation.html
STRING=$1
echo $STRING
if [ -z "$STRING" ];then
	echo "STRING is NULL"
	exit
else
	echo ${#STRING}
fi

#	string cut
list="CREATE_DATABASE_LOG.sql"
echo ${list%.sql}
echo -n "[ENTER]" ; read
echo "OK"
exit

