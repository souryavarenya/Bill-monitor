from serial import Serial
import time
from mechanize import Browser

rate = 4.5
#Sample Unit Rate

def fill_formon(ind):
        br = Browser()
        page = br.open('http://trickster.site88.net/Billmon/formonr1.php')
        br.select_form(nr=0)
        br.form["7"] = str(ind)
        br.submit()

def fill_formoff(ind,units,cost,durn):

        br = Browser()
        page = br.open('http://trickster.site88.net/Billmon/formoffr1.php')
        br.select_form(nr=0)
        br.form["7"] = ind
        br.form["5"] = str(durn)
        br.form["6"] = str(units)
        br.form["8"] = str(cost)
        br.submit()

def fill_formupdate(ind,units,cost,durn):

        br = Browser()
        page = br.open('http://trickster.site88.net/Billmon/formupd.php')
        br.select_form(nr=0)
        br.form["7"] = ind
        br.form["5"] = str(durn)
        br.form["6"] = str(units)
        br.form["8"] = str(cost)
        br.submit()

def on():
	text = open('index.txt',"r")
	index = text.read()
	text.close()
	fill_formon(index)
	Ippd2 = serialrecord()

def off():
	duration = t2 - t1
	power = Get_power(Ippd2)
	units = power * float(duration) / 3600000
	#wattsec to kWh
	cost = units * rate
	
	text = open('index.txt',"r")
	index = text.read()
	text.close()
	
	fill_formoff(index, units, cost, duration )
	
	text = open('index.txt',"w")
	text.write(str(int(index)+1))
	text.close()

def update():
	duration = t2 - t1
	power = Get_power(Ippd2)
	units = power * float(duration) / 3600000
	#wattsec to kWh
	cost = units * rate
	
	text = open('index.txt',"r")
	index = text.read()
	text.close()
	
	fill_formupdate(index, units, cost, duration)
	


def Get_power(I):
	power =  230 * I / (2 ** 0.5)
	#watts
	return power

def serialrecord():
        readingArray = []
        initialTime = time.clock()

        while ((time.clock() - initialTime)<20):
                reading = float(ser.readline())
                readingArray.append(reading)

        delI = (max(readingArray) - min(readingArray))/2
        return delI

ser = Serial('/dev/ttyAMA0',115200,timeout=0.005)
ser.close()
ser.open()
t1 = 0
t2 = 0
prevst = 0
Ippd2 = 0
while 1:
	if abs(float(serial.read())) > 0.1 and prevst == 0:
		t1 = time.clock()
		on()
		prevst = 1
	elif abs(float(serial.read())) < 0.1 and prevst == 1:
		t2 = time.clock()
		off()
		prevst = 0
        elif abs(float(serial.read())) > 0.1 and prevst == 1:
                t2 = time.clock()
                update()
