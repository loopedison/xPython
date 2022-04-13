import RPi.GPIO as GPIO
import time
import remoLed
 
 
ip = '192.168.2.12'
port = 8888
def blink(times, delay):
 
    R=11
    Y=12
    W=15
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(R, GPIO.OUT)
    GPIO.setup(Y, GPIO.OUT)
    GPIO.setup(W, GPIO.OUT)
 
    remoLed.init(ip, port)
    remoLed.send('Now, you can input 1,2 or 3 to turnon  the right led:')
    #in order to initial a communication protocol, add code here
    #....
    command = ''
    while 1:
        command = remoLed.read()
        if command=='1\n':
            GPIO.output(R, GPIO.LOW)
            time.sleep(2)
            GPIO.output(R, GPIO.HIGH)
            remoLed.send('ok for 1\t')
        elif command=='2\n':
            GPIO.output(Y, GPIO.LOW)
            time.sleep(2)
            GPIO.output(Y, GPIO.HIGH)
            remoLed.send('ok for 2\t')
        elif command=='3\n':
            GPIO.output(W, GPIO.LOW)
            time.sleep(2)
            GPIO.output(W, GPIO.HIGH)
            remoLed.send('ok or 3\t')
        elif command=='quit\n':
            remoLed.send('end remote control!\r\n')
            remoLed.end()
            break
        else:
            remoLed.send('eroor input!\r\n')
 
    while times>0:
        if 0==times%2:
            GPIO.output(R, GPIO.HIGH) #or output(R, GPIO.True)
        else:
            GPIO.output(R, GPIO.LOW)
        time.sleep(delay)
        times-=1
    return
 
 
if __name__ == '__main__':
    blink(10, 0.5)