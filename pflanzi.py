#!/usr/bin/python 

import sht2x 
 

if __name__ == "__main__": 
    try: 
        with sht2x.SHT21(1) as sht21:		 
            
            minTemp = 12.0
            maxTemp = 35.0

            #AUFGABE

            temp = sht21.read_temperature()  

            #AUFGABE 

            if temp < minTemp:	 
                print "Temperatur ist bei %s und ist zu niedrig" % temp
            elif temp > maxTemp:
                print "Temperatur ist bei %s und ist zu hoch" % temp
            else: 				 
                print "Temperatur ist %s" % temp

            #AUFGABE 

    except IOError, e:
        print e 
        print "Error creating connection to i2c. This must be run as root"