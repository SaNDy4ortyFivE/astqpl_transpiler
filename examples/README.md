#### Quorum to Arduino Examples
1. quorum_if.txt  
```Demonstration of if condition block in quorum```
2. quorum_if_else.txt  
```Demonstration of if else condition block in quorum```
3. quorum_infrared.txt  
```
Demonstration of how to use infrared sensor in quorum
Library Name:
IRED
Functions:
Attach pin: instance_name:pinIRED(pin_number)
Read Value: instance_name:READVAL()...returns 1 if object is detected, else 0
```
4. quorum_led.txt  
```
Demonstration of how to use an LED in quorum
Library Name:
LED
Functions:
Attach pin: instance_name:pinLED(pin_number)
Turn on Led: instance_name:ON()
Turn off Led: instance_name:OFF()
```

5. quorum_lmtemp.txt  
```
Demonstration of how to use an LM35 Temperature sensor in quorum
Library Name:
LMTEMP
Functions:
Attach pin: instance_name:pinLMTP(pin_number)
Read Temperature: instane_name:READTEMP()...returns temperature in celsius(float valaue)
```
__Note: float is called as number in quorum__

6. quorum_ultrasonic.txt  
```
Demonstration of how to use an Ultrasonic sensor(HCSR-04) in quorum
Library Name:
USONIC
Functions:
Attach trigger pin: instance_name:trigpin(pin_number)
Attach echo pin: instance_name:echopin(pin_number)
Read Distance: instane_name:GETDISTANCE()...returns distance in cms(int value)
```
__Note: int is called as integer in quorum__  

7. quorum_button.txt  
```
Demonstration of how to use a simple push button in quorum
Library Name:
BUTTON
Functions:
Attach pin: instance_name:pinBTN(pin_number)
Read button state: instane_name:STATE()... returns 1 if button is pressed, else 0

8. quorum_1.txt  
- Reads distance from ultrasonic sensor  
- If value is less than 10, turns on red led and turns off blue led  
- Else turns off red led and turns on blue led  

9. quorum_2.txt  
- Reads state of the button  
- If button is pressed, turns on led
- Else turns off led

10. quorum_3.txt  
- Reads state of the button  
- If button is pressed, gets temperature from sensor and turns on led if temperature is greater than 5 
