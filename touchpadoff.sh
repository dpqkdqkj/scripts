#!/bin/sh
if [ `synclient -l | grep TouchpadOff | awk '{ print $3 }'` = 0 ]; then
  synclient touchpadoff=1
else
  synclient touchpadoff=0
fi
exit 0
