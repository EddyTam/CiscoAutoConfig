#!/usr/bin/python
import serial
import time
from builtins import str
from re import search
search = ".68/123.#."
search2 = ".0/1.#"
replace =""
replace2=""
temp=""
a=[]
com = input("please input the serial interface\n")
dialerac = input("please input the dialer account\n")
dialerpw = input("please input the dialer password\n")
storenumber = int(input("Please input the storenumber\n"))
if storenumber<=250:
    replace = ".68."+str(storenumber)+"."
    replace2 = ".0."+str(storenumber)
else:
    replace = ".123."+str(storenumber-250)+"."
    replace2 = ".1."+str(storenumber-250) 
fo = open("S000.txt","r+")
result = fo.read()
fo.close
filename="S"+str(storenumber)+".txt"
result = result.replace(search,replace)
result = result.replace(search2,replace2)
result = result.replace("STORE-#","STORE-"+str(storenumber))
result = result.replace("ppp pap sent-username XXXX password","ppp pap sent-username "+dialerac+" password "+dialerpw)
output = open(filename,"w")
output.write(result)
output.close

ser =serial.Serial()
ser.baudrate = 9600
ser.port=com
ser.open()
ser.write("en\n".encode())
ser.write("config t\n".encode())
with open("S"+str(storenumber)+".txt")as my_file:
    for line in my_file:
        a.append(line)
    for index,item in enumerate(a):
        ser.write(item.encode())
        time.sleep(0.5)
        print(item)
ser.close()
print("FINISH")



