from time import sleep
from gpiozero import LED, Button
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN)


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
test = LED (16)

while GPIO.input(20)==True:
        rød1.on()
        print("rød")
        print("grøn")

 
        