#!/bin/bash

start() {
  stop
  CMD='ssh -fN -L 9983:solr.aws:8983 ec2-user@aws.liangzhang.io'
  echo ${CMD}
  ${CMD}
}

stop() {
  PID=$(lsof -t -i @localhost:9983 -sTCP:listen)

  if [ ! -z ${PID} ]
  then
    kill ${PID}
  fi
}

ACTION='start'
if [ ! -z $1 ]
then
  ACTION="$1"
fi

eval ${ACTION}
