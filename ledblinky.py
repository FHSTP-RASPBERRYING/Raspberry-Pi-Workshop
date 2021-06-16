# External module imports 

import RPi.GPIO as GPIO 

import time 

 

print("Hello LED") 

ledPin = #AUFGABE 

# Pin Setup: 

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme 

 

GPIO.setup(ledPin, GPIO.OUT) # Definiere ledPin (PIN 9) als Output Pin! 

 

print("Druecke STRG+C um das Programm zu beenden!") 

try: # Weiss nicht ob Try-Catch nicht den Rahmen bissl sprengt 

    while 1: 

            #AUFGABE 

except KeyboardInterrupt: # Wenn STRG+C gedrueckt wird beende programm 

    GPIO.cleanup() # GPIO Pins freigeben 