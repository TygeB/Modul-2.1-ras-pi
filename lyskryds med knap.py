from time import sleep
from gpiozero import LED, Button
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(16,GPIO.IN)
tid1 = 2
tid2 = 4
button1=Button(3)
button=Button(2)
rød1 = LED(13)
rød2 = LED(22)
gul1 = LED(19)
gul2 = LED(27)
grøn1 = LED(26)
grøn2 = LED (17)


def lysgrøn(x):
    global tid1
    global tid2

    if x=="gå grøn":
        x="gå gul"
        print("grøn")
        grøn1.on()
        print("2rød")
        rød2.on()
        sleep(tid2)
        if GPIO.input(16) == True:
            return fodgænger(x)
        else:
            return lysgul(x)

def lysgul(x):
    global tid1
    global tid2

    if x=="gå gul":
        x="gå rød"
        print("gul")
        grøn1.off()
        gul1.on()
        sleep(tid1)
        if GPIO.input(16) == True:
            return fodgænger(x)
        else:
            return lysrød(x)


def lysrød(x):
    global tid1
    global tid2

    if x=="gå rød":
        x="gå grøn"
        gul1.off()
        print("rød")
        rød1.on()
        print("2rød og gul")
        rød2.on()
        sleep(tid1)
        gul2.on()
        sleep(tid1)
        print("2grøn")
        rød2.off(), gul2.off()
        grøn2.on()
        sleep(tid2)
        grøn2.off()
        print("2gul")
        gul2.on()
        sleep(tid1)
        gul2.off()
        print("2rød")
        rød2.on()
        print("rød og gul")
        rød1.on()
        sleep(tid1)
        
        
        if GPIO.input(16) == True:
            return fodgænger(x)
        else:
            gul1.on()
            sleep(tid1)
            rød1.off(), gul1.off()
            return lysgrøn(x)
    
def fodgænger(x):
        rød1.on() , rød2.on()
        gul1.off(), gul2.off(), grøn1.off(), grøn2.off()
        print("fodgænger")
        sleep(tid1)
        rød1.off() , rød2.off()
        sleep(1)
        rød1.on() , rød2.on()
        sleep(2)
        gul1.on()
        sleep(1)
        rød1.off()
        gul1.off()
        
        return lysgrøn(x)
        
    



lys = lysgrøn(x="gå grøn")

while lys: lys = lys(x="gå grøn")