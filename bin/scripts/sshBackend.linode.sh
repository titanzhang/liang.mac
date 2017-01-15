PID=$(lsof -t -i @localhost:9983 -sTCP:listen)
CMD='ssh -fN -L 9983:localhost:8983 -L 9306:localhost:3306 backend.liang.center'

if [ ! -z ${PID} ]
then
  kill ${PID}
fi

echo ${CMD}
${CMD}
