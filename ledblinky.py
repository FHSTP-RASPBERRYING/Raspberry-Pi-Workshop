# External module imports 

import RPi.GPIO as GPIO 

import time 

 

print("Hallo zu LED Blinky!")

#AUFGABE 
ledPin = 11 # Definiere ledPin (PIN 9) als Output Pin!

# Pin Setup: 

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme 

 

GPIO.setup(ledPin, GPIO.OUT) # Definiere ledPin (PIN 9) als Output Pin! 

 

print("Druecke STRG+C um das Programm zu beenden!") 

try:
    
    while 1: 
        #AUFGABE
        time.sleep(2)
        
except KeyboardInterrupt: # Wenn STRG+C gedrueckt wird beende programm 

    GPIO.cleanup() # GPIO Pins freigeben