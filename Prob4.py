import psutil
import sys
from datetime import datetime

def main():
	
	if len(sys.argv) == 1:
		print "Enter some arguments"
		exit()
		
	myargv=sys.argv
	numberOfArguments=len(sys.argv)
	
	temp = numberOfArguments
	counter =1
	
	while(counter <  temp):
		try:
			num = int(myargv[counter])
			p = psutil.Process(num)
			print "Process Name: %s" % p.name()
			print "Process Status: %s" % p.status()
			print "Parent ID: %s" % p.ppid()
			print "Process Status: %s" % p.create_time()
			print "Process Status: %s" % p.parent()
			print "----------------------------------"
			
		except :
			print "Error, %s must be an valid and existing integer PID" % myargv[counter]	
				
		counter = counter + 1


if __name__ == "__main__":
	main()
