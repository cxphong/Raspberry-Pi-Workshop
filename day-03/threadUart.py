import serial
import thread
import time

def receiveData(ser):
	while True:
		length = ser.inWaiting()
		if (length > 0):
			inStr = ser.read(length)
			print inStr

if __name__ == '__main__':
	ser = serial.Serial(port='/dev/ttyAMA0',115200)
	print(ser.isOpen())

	try:
		thread.start_new_thread( receiveData, (ser,))
	except:
   		print "Error: unable to start thread"
   
   	while True:
   		nb = raw_input('Enter name: ')
   		ser.write(nb)