#!/usr/bin/env python
# encoding: utf-8

import os
import urllib
import eyed3
import time
for i in range(1, 20+1):
    filename = r'/home/pi/mp3/' + str(i) + '.mp3'
    if os.path.exists(filename):
        xx = eyed3.load(filename)
        seconds = xx.info.time_secs
        if(seconds < 600):
            os.system('ffmpeg -loop 1 -r 1 -t '+ str(seconds) + ' -f image2 -i /home/pi/image/' + str(i) + '.jpg -vcodec libx264 -pix_fmt yuv420p -crf 24 -y tmp.mp4')
            os.system('ffmpeg -i tmp.mp4 -i /home/pi/mp3/' + str(i) + '.mp3  -c:v copy -c:a aac -y /home/pi/songs/' + str(i) + '.flv')
            os.remove('tmp.mp4')
            os.remove('/home/pi/mp3/' + str(i) + '.mp3')
            print('/home/pw/songs/'+str(i)+'flv渲染成功!10秒后开始下一个')
            time.sleep(10)
        else:
            os.remove('/home/pi/mp3/' + str(i) + '.mp3')
            time.sleep(10)
