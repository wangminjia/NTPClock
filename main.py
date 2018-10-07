import sntp
import wifi
from tm1639 import TM1639 
from machine import Timer
import utime

DIO=13
CLK=14
STB=15

tm=TM1639(DIO,CLK,STB)
buf1=bytearray(16)
buf2=bytearray(16)
def secondCallback(t):
    (year,month,day,hour,min,sec,wday,ss)=utime.localtime()
    tmp='%02d%02d' %(hour,min)
    buf1[0]=tm.FONT[tmp[3]]
    buf1[1]=tm.FONT[tmp[2]]
    buf1[3]=tm.FONT[tmp[1]]
    buf1[8]=tm.FONT[tmp[0]]
    buf1[2]^=0x60
    tm.convert(buf1,buf2,16)
    for i in range(16):
        tm.send_data(i,buf2[i])
    

def hourCallback(t):
    sntp.settime()


if __name__ == '__main__':
    wifi.do_connect()
    sntp.settime()
    tm.enable()
    t_sec=Timer(1)
    t_sec.init(period=1000,mode=Timer.PERIODIC,callback=secondCallback)
    t_hour=Timer(2)
    t_hour.init(period=3600000,mode=Timer.PERIODIC,callback=hourCallback)
    