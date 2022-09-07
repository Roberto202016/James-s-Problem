from ast import parse
from calendar import week
from datetime import datetime
from lib2to3.pytree import convert
from msilib import type_key
import re
from time import time
from xmlrpc.client import DateTime
import datetime

#horario = "Mon 01:00-22:00\nTue 04:00-18:00\nWed 01:00-23:00\nThu 08:00-20:00\nFri 10:00-22:00\nSat 02:00-22:00\nSun 08:00-22:00"
horario = "Sun 10:00-20:00\nFri 05:00-10:00\nFri 16:30-23:50\nSat 10:00-24:00\nSun 01:00-04:00\nSat 02:00-06:00\nTue 03:30-18:15\nTue 19:00-20:00\nWed 04:25-15:14\nWed 15:14-22:40\nThu 00:00-23:59\nMon 05:00-13:00\nMon 15:00-21:00"
lista_horario = re.split(r'\n',horario)

sun = []
mon = []
tue = []
wed = []
thu = []
fri = []
sat = []

for meeting in lista_horario:
    if(meeting[0]+meeting[1]=='Mo'):
        mon.append(meeting)
    if(meeting[0]+meeting[1]=='Su'):
        sun.append(meeting)
    if(meeting[0]+meeting[1]=='Sa'):
        sat.append(meeting)
    if(meeting[0]+meeting[1]=='Fr'):
        fri.append(meeting)
    if(meeting[0]+meeting[1] == 'Tu'):
        tue.append(meeting)
    if(meeting[0]+meeting[1] == 'We'):
        wed.append(meeting)
    if(meeting[0]+meeting[1] == 'Th'):
        thu.append(meeting)

sat.sort()
mon.sort()
sun.sort()
tue.sort()
wed.sort()
thu.sort()
fri.sort()

week = sun+mon+tue+wed+thu+fri+sat

timeListStart=[]
timeListEnd=[]

for d in week:
    resty=datetime.timedelta(hours=(int(d[4]+d[5])),minutes=int(d[7]+d[8]))
    timeListStart.append(resty)

for d in week:
    resty = datetime.timedelta(hours=(int(d[10]+d[11])), minutes=int(d[13]+d[14]))
    timeListEnd.append(resty)

rest=[]
counter=0
times=0

for e in week:
    times+=1

while(counter<len(week)-1):
    rest.append((timeListStart[counter+1]-timeListEnd[counter]))
    counter+=1

print("////////////////////////")
print(rest)
print(max(rest))