#!/bin/bash

start() {
  stop
  CMD='ssh -fN -L 9983:localhost:8983 -L 9306:localhost:3306 backend.liang.center'
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
