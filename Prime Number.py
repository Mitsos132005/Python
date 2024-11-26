num = int(input("Give me a Number"))
def number_prime(num):	
	num2 = int(num/2)
	if num > 1:
		for i in range(2, num2):
			if (num % i) == 0:
				print(num, "is not a prime number")
				break
			else:
				print(num, "is a prime number")
				break
number_prime(num)


	


				
    
    
        






	

