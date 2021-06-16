# External module imports 
import RPi.GPIO as GPIO 
import time 

print("Hello Knight-Rider") 

ledPins = [x,x,9,x,x] #AUFGABE 

# Pin Setup: 

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme 
GPIO.setup(ledPins, GPIO.OUT) # Definiere die ledPins als output pins 

print("Druecke STRG+C um das Programm zu beenden!") 

GPIO.output(x,GPIO.LOW) #AUFGABE 

try: # Weiss nicht ob Try-Catch nicht den Rahmen bissl sprengt 
    while 1:     
        for x in ledPins: 
            
            print("AUFGABE")  

except KeyboardInterrupt: # Wenn STRG+C gedrueckt wird beende Programm 
    GPIO.cleanup() # cleanup all GPIO