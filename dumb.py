import sys
import time
num = sys.argv[1]
velocity = int(sys.argv[2])
delay = float(sys.argv[3])
counter = 1
while 1:
	print " "*(int((int(num)-counter)/2)+20),'|', "*"*counter,'|',"\n"
	if counter >= int(num) or counter <= 0:
		velocity = -velocity
	counter += velocity
	time.sleep(delay)
