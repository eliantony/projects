print("Hello World")

s = input("Please Enter Number To Sigma:\t")

def Sigma(n):
	s = 0	
	print("\n\nI\t|\t"+ '\u03a3' +"\t|")
	print("-------------------------")
	for i in range(1, n+1):
		s = s+i			
		print(str(i) + " \t|\t" + str(s) + "\t|")
		
Sigma(int(s))

