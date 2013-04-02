import subprocess
import sys

#cmd = "awk -F\\\"\\t\\\" '{ print \\$1\\\"\\t\\\"\\$3\\\"\\t\\\"\\$5 }' " + sys.argv[1] + " > " + sys.argv[1] + ".out"	#	for executing awk command via ssh
name = sys.argv[1]
cmd = "awk -F\"\\t\" '{ print $1\"\\t\"$3\"\\t\"$5 }' " + name + " > " + name[:name.rindex('.')] + ".out"
subprocess.call(cmd, shell=True)

