#encoding: utf-8
import os.path
import re

def str2num(t):
	# t=float(eval(t))
	if t.find('/')==-1:
		ret=int(t)
	else:
		(a,b)=t.split('/')
		if b!='0':
			ret=float(a)/float(b)
		else:
			ret=int(a)

	# return round(ret,3)
	return ret

def num2srt(num):
	num='%.3f' % num
	seconds,decimal=num.split('.')

	hour=minute=second=0
	seconds=int(seconds)
	if seconds<60:
		second=seconds
	else:
		minute=seconds/60
		second=seconds-minute*60
		if minute>=60:
			hour=minute/60
			minute=minute-hour*60

	hour='%02.f' % hour
	minute='%02.f' % minute
	second='%02.f' % second
	return hour+':'+minute+':'+second+','+str(decimal)

# fcpxmlPath=unicode(r'C:\Users\jeffl\Desktop\0415 2130 外挂字幕.fcpxml','utf8').encode('gbk')
fcpxmlPath=unicode(r'C:\Users\jeffl\Desktop\活力社区最新（右上角）字幕0708.fcpxml','utf8').encode('gbk')
xml=open(fcpxmlPath).read()
# subs=re.findall(r'<title name="中: (.*)" lane="\d+" offset="(.*)s" ref="r\d+" duration="(.*)s" start',xml)
# subs=re.findall(r'<title .* offset="(.*)s" .* duration="(.*)s" start[\s\S]*?<text>[\s\S]*?<text-style ref=".*">(.*)</text-style>',xml)
subs=re.findall(r'<title name="渐变.* offset="(.*)s" .* duration="(.*)s" start[\s\S]*?<text>[\s\S]*?<text-style ref=".*">(.*)</text-style>',xml)
count=0
srt=open('srt output.srt','wb')

for sub in subs:
	count+=1

	startTime,duration,text=sub
	startTime=str2num(startTime)
	duration=str2num(duration)
	endTime=round(startTime+duration,3)

	srt.write(str(count)+'\n'+num2srt(startTime)+' --> '+num2srt(endTime)+'\n'+text+'\n\n')

srt.close()
