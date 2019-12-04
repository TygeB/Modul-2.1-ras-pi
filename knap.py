from time import sleep
from gpiozero import LED, Button 
from signal import pause

button1=Button(3)
button=Button(2)
rød1 = LED(13)
rød2 = LED(22)
gul1 = LED(19)
gul2 = LED(27)
grøn1 = LED(26)
grøn2 = LED (17)

while True:
    button.when_pressed = rød1.on
    button.when_released = rød1.off
    
    
    button1.when_pressed = grøn1.on
    button1.when_released = grøn1.off

    
    
