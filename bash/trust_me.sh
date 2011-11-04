#!/bin/bash

USER_AT_REMOTE_HOST=$1
echo Establishing trust for ${USER_AT_REMOTE_HOST} ...
if [ ! -e ~/.ssh/id_dsa.pub ];
# create a new public key
then ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa;
fi
# copy the public key remotely to id_dsa_temp.pub
# !does not check for overwrite
scp ~/.ssh/id_dsa.pub ${USER_AT_REMOTE_HOST}:~/id_dsa_temp.pub
ssh ${USER_AT_REMOTE_HOST} "mkdir ~/.ssh"
ssh ${USER_AT_REMOTE_HOST} "touch ~/.ssh/authorized_keys"
# add to the authorized key set
ssh ${USER_AT_REMOTE_HOST} "cat id_dsa_temp.pub >> ~/.ssh/authorized_keys"
# clean up; test should not require password
ssh ${USER_AT_REMOTE_HOST} "rm id_dsa_temp.pub"
