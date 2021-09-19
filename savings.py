import time
f = open('savings.txt', 'r+')
a = f.read()
f.seek(0)
a = str(a)
message = 'There is currently $' + a + ' in your savings account. Would you like to change the amount inside?[Y/n]'
c = input(message)
a = int(a)
if c == ('y'):
	b = input('How many dollars would you like to add to your account?(please enter value WITHOUT dollar sign)')
	b = int(b)
	a = a + b
	a = str(a)
	f.write(a)
	f.truncate()
	d = input('The value in your savings account is now $' + a + '. Would you like to undo the changes made?[Y/n]')
	if d == ('y'):
		b = int(b)
		a = int(a)
		a = a - b
		a = str(a)
		print('The value in your savings account is now $' + a)
		time.sleep(1)
		f.seek(0)
		f.write(a)
		print('Thanks, and bye!')
	elif d == ('n'):
		print('OK, well then,')
		time.sleep(1)
		print('Bye!')
	f.truncate()
	f.close()
	
	
	
elif c == ('n'):
	print('OK, well then,')
	time.sleep(1)
	print('Bye!')



