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
        gul1.on()
        sleep(tid1)
        rød1.off(), gul1.off()
        return lysgrøn(x)


lys = lysgrøn(x="gå grøn")

while lys: lys = lys(x="gå grøn")
