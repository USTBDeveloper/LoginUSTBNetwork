#!/bin/bash
# Your StuNo. & Password
# Using Parameters
# Use: ./login.sh username password
username=$1
password=$2
curl --retry 3 --data  "DDDDD=${username}&upass=${password}&0MKKey=123456789" http://202.204.48.66 --silent -o LOGIN_STATUS.out
if [[ "grep UID='${username}' LOGIN_STATUS.out" != "" ]]
then
echo "Login Success"
else
echo "Login Fail"
fi
