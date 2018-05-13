import random
from random import randint


def main():
	
	MainMatrix = []
	counter = 0
	counter2 = 0
	
	#randomly generating a 8x8 matrix
	while( counter !=8):
		
		mylist = [x for x in range(8)]
		random.shuffle(mylist)
		MainMatrix.append(mylist)
		counter = counter + 1
	
	
	# printing the 8x8 matrix
	print "\t8 x 8 matrix"
	print "-----------------"
	for list in MainMatrix:
		for num in list:
			print "%s ," % num ,
		print " "


	# printing the 2x2 matrix
	print "\n\t2 x 2 matrix"
	print "-----------------"
	randIndex= randint(0,6)
		
	indexes = [randIndex, randIndex+1]	
	for list in MainMatrix:
		if counter2 ==2:
			break
		else:
				counter2 = counter2 + 1
				
		print "%s" % [list[x] for x in indexes]



# calling main
if __name__ == "__main__":
	main()
