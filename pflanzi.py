#!/usr/bin/python

import sht2x

if __name__ == "__main__":
    
    try:
        with sht2x.SHT21(1) as sht21:
            minTemp = 12.0
            maxTemp = 35.0
            
            minHumi = 49.0
            maxHumi = 98.0
            
            temp = sht21.read_temperature() 
            humi = sht21.read_humidity() 

            if temp < minTemp:  
                print "Temperatur liegt bei %s und ist zu niedrig" % temp  
            elif temp > maxTemp:  
                print "Temperatur liegt bei %s und ist zu hoch" % temp  
            else:  
                print "Temperatur ist %s" % temp
            if humi < minHumi: 
                print "Luftfeuchtigkeit bei %s und somit zu niedrig" % humi 
            elif humi > maxHumi: 
                print "Luftfeuchtigkeit bei %s und somit zu hoch" % humi 
            else: 
                print "Luftfeuchtigkeit ist %s" % humi
                
    except IOError, e:
        print e
        print "Error creating connection to i2c.  This must be run as root"