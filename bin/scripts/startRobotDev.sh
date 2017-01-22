#!/bin/bash

STATUS=$(docker ps -a|grep robotdev);
if [ -n "$STATUS" ]; then
  docker start robotdev
else
  docker run -d -p 5000:22 -h robotdev -v ~/dev:/home/dev --name "robotdev" titanzhang/robotdev
fi
