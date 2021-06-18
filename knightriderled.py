# External module imports 
import RPi.GPIO as GPIO 
import time 

print("Hello Knight-Rider") 

#AUFGABE
ledPins = [7,8,9,10,11] # AUFGABE: lass LED 9 bis 13 blinken

# Pin Setup: 

GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme 
GPIO.setup(ledPins, GPIO.OUT) # Definiere die ledPins als output pins 

print("Willkommen zu Knight-Rider LED")
print("Druecke STRG+C um das Programm zu beenden!") 

#AUFGABE: schalte LEDs 9 bis 13 ab
# GPIO.output( )

try: # Weiss nicht ob Try-Catch nicht den Rahmen bissl sprengt 
    
    while 1:     
        for x in ledPins:
            # AUFGABE: bringe LEDs 9 bis 13 wie bei Knight-Rider zum leuchten
            time.sleep(0.50)
            

except KeyboardInterrupt: # Wenn STRG+C gedrueckt wird beende Programm 
    GPIO.cleanup() # cleanup all GPIO