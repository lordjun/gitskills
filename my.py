import random
secret = random.randint(1,10)
num = 0
temp = input("please input an number:\n")
guess = int(temp)
num = num+1
while (guess != secret) and (num < 3):
	if (guess > secret):
		temp = input("Too big, please input again:\n")
		guess = int(temp)
		num = num+1
	else:
		temp = input("Too small, please input again:\n")
		guess = int(temp)
		num = num+1
if (num==3) and (guess != secret):
	print ("Reach the limit, game over!")	
else:
	print ("You're right, game over!")
