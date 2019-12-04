from gpiozero import LED
from time import sleep

rød1 = LED(13)
rød2 = LED(22)
gul1 = LED(19)
gul2 = LED(27)
grøn1 = LED(26)
grøn2 = LED (17)

tid = 1
tid2 = 2
while True:
        rød1.on()
        sleep(tid2)
        gul1.on()
        sleep(tid)
        rød1.off(), gul1.off()
        grøn1.on()
        sleep(tid2)
        grøn1.off()
        gul1.on()
        sleep(tid)
        gul1.off()
    
    

    
    
    
    
    