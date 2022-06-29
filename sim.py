import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led1 = 23
led2 = 24
led3 = 25
led4 = 8

btn1 = 14
btn2 = 15

GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(led4, GPIO.OUT)

GPIO.setup(btn1, GPIO.IN)
GPIO.setup(btn2, GPIO.IN)

prev1 = False
prev2 = False
prev1_1 = False
prev2_1 = False

GPIO.output(led1, 0)
GPIO.output(led2, 0)
GPIO.output(led3, 0)
GPIO.output(led4, 0)
v = False
m = False

try:
    while True:
        input_btn1 = GPIO.input(btn1)
        input_btn2 = GPIO.input(btn2)

        if input_btn1 and not prev1 and not v:
            m = False
            GPIO.output(led1, 0)
            GPIO.output(led2, 0)
            GPIO.output(led3, 0)
            GPIO.output(led4, 0)
            a = int(input("첫번째 정수를 입력하세요: "))
            k = True
            cnt = 0
            f = 0
            while k:
                input1 = GPIO.input(btn1)
                input2 = GPIO.input(btn2)
            
                if input1 and not prev1_1:
                    cnt += 1
                    p = cnt%2+1
                    if p == 1:
                        f = 0
                        print("+")
                    elif p == 2:
                        f = 1
                        print("-")

                    v = True
                elif input2 and not prev2_1 and v:
                    b = int(input("두번째 정수를 입력하세요: "))
                    if f == 0:
                        total = a+b
                    elif f == 1:
                        total = a-b
                    print("결과를 확인하고 싶으면 두번째 버튼을 눌러주세요!")
                    k = False

                prev1_1 = input1
                prev2_1 = input2
            m = True
        elif input_btn2 and not prev2 and m:
            if total >= 0 and total <= 16:
                if total >= 8:
                    total -= 8
                    GPIO.output(led1,1)
                if total >= 4:
                    total -= 4
                    GPIO.output(led2,1)
                if total >= 2:
                    total -= 2
                    GPIO.output(led3,1)
                if total%2==1:
                    total -= 0
                    GPIO.output(led4,1)
            else:
                print("16진수에 없는 숫자입니다")
                         
            v = False                
        prve1 = input_btn1
        prev2 = input_btn2
        
except KeyboardInterrupt:
    pass

GPIO.cleanup()
