#!/bin/bash
while true
do
  ffmpeg -re -f concat -safe 0 -i playlist.txt -vcodec copy -acodec aac -b:a 192k -f flv "rtmp://txy.live-send.acg.tv/live-txy/?streamname=live_10282743_8404146&key=e182b0cf9d2ea4f93e132c5dac5d5a35"
done
