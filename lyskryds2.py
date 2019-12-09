from time import sleep
from gpiozero import LED

tid1 = 2
tid2 = 4

rød1 = LED(13)
rød2 = LED(22)
gul1 = LED(19)
gul2 = LED(27)
grøn1 = LED(26)
grøn2 = LED (17)

def rr(x):
    global tid1
    global tid2
    
    if x=="rød":
        x="bliv ns"
        rød1.on()
        rød2.on()
        sleep(tid1)
        return ns(x)
    elif x=="røød":
        x="bliv øv"
        rød1.on()
        rød2.on()
        sleep(tid1)
        return øv(x)
    
def ns(x):
    if x=="bliv ns":
        x="røød"
        gul1.on()
        sleep(tid1)
        rød1.off()
        gul1.off()
        grøn1.on()
        sleep(tid2)
        grøn1.off()
        gul1.on()
        sleep(tid1)
        gul1.off()
        return rr(x)
    
    
def øv(x):
    if x=="bliv øv":
        x="rød"
        gul2.on()
        sleep(tid1)
        rød2.off()
        gul2.off()
        grøn2.on()
        sleep(tid2)
        grøn2.off()
        gul2.on()
        sleep(tid1)
        gul2.off()
        return rr(x)   
    
    
state=rr(x="rød")
while state: state=rr(x="rød")


