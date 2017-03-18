import RPi.GPIO as GPIO
import time
import time as time_

# get millis current
def millis():
    return int(round(time_.time() * 1000))

#====declare button and led ======
button = 3
led = 7

# use ping number
GPIO.setmode(GPIO.BOARD)

GPIO.setup(led,GPIO.OUT)
GPIO.setup(button,GPIO.IN,GPIO.PUD_UP)

sleep = 0.5
mode = 0
flag = False

while True:
	bt_state = GPIO.input(button)

	#check button press
	if bt_state == GPIO.LOW:
		time_start = millis();

		# wait untill button release 
		while (bt_state == GPIO.LOW):
			bt_state = GPIO.input(button)
			pass
		# press < 1s
		if (millis() - time_start) < 1000 :
			mode = 1
		# press > 1s vs press < 2s
		elif ((millis() - time_start) < 2000) & ((millis() - time_start) > 1000):
			mode = 2
		# press > 3s
		elif (millis() - time_start) > 3000:
			mode = 3

	if(mode == 1):
		sleep = 0.2
		flag = True
	elif(mode == 2):
		sleep = 0.5
		flag = not flag
	elif(mode == 3):
		sleep = 1
		flag = not flag

	# set output led	
	GPIO.output(led,flag)
	time.sleep(sleep)		

