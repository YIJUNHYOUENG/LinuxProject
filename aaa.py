import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led1 = 24
led2 = 23
led3 = 20
led4 = 21

btn1 =16
btn2 =18

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)
GPIO.setup(btn1, GPIO.IN)
GPIO.setup(btn2, GPIO.IN)

count = 0
on = False
click1 = False
click2 = False

try:
    while True:
        bI1 = GPIO.input(btn1)
        bI2 = GPIO.input(btn2)
    
        if bI1 and not click1:
            GPIO.output(led1,0)
            GPIO.output(led2,0)
            GPIO.output(led3,0)
            GPIO.output(led4,0)
            count += 1
            if count == 16: count = 15
        elif bI2 and not click2:
            count -= 1
            if count == -1: count = 0
            GPIO.output(led1,0)
            GPIO.output(led2,0)
            GPIO.output(led3,0)
            GPIO.output(led4,0)

        a = count
        if a >= 8:
            a -= 8
            GPIO.output(led4,1)
        if a >= 4:
            a -= 4
            GPIO.output(led3,1)
        if a >= 2:
            a -= 2
            GPIO.output(led2,1)
        if a%2 == 1:
            a -= 1
            GPIO.output(led1,1)
       

        click1 = bI1
        click2 = bI2
except KeyboardInterrupt:
    pass

GPIO.cleanup()
