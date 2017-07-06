#!/usr/bin/env python
# encoding: utf-8

import os
import urllib
import eyed3
import time
import linecache
file_mp3 = '/home/jele/mp3/'
file_image = '/home/jele/image/'
file_flv = '/home/jele/flv/'
for i in range(1, 20+1):
    filename = file_mp3 + str(i) + '.mp3'
    filename_cout = file_mp3 + 'log.cout'
    cout = linecache.getline(filename_cout, i)
    if cout[len(cout)-3:len(cout)-1] == 'no':
        if os.path.exists(filename):
            xx = eyed3.load(filename)
            seconds = xx.info.time_secs
            if(seconds < 600):
                os.system('ffmpeg -loop 1 -r 1 -t '+ str(seconds) + ' -f image2 -i ' + file_image + str(i) + '.jpg -vcodec libx264 -pix_fmt yuv420p -crf 24 -y tmp.mp4')
                os.system('ffmpeg -i tmp.mp4 -i ' + file_mp3  + str(i) + '.mp3  -c:v copy -c:a aac -y ' + file_flv + str(i) + '.flv')
                os.remove('tmp.mp4')
                os.remove(file_mp3 + str(i) + '.mp3')
                openfile = open(filename_cout, 'r+')
                flist = openfile.readlines()
                tmp = flist[i+1]
                tmp1 = tmp[0:len(tmp)-3]
                tmp1 = tmp1+'yes\n'
                flist[i+1] = tmp1
                openfile.close()
                openfile = open(filename_cout, 'w+')
                openfile.writelines(flist)
                openfile.close()
                print(file_flv +str(i)+ 'flv渲染成功!10秒后开始下一个')
                time.sleep(10)
            else:
                os.remove(file_mp3 + str(i) + '.mp3')
                time.sleep(10)
    else:
        os.remove(file_mp3 + str(i) + '.mp3')
