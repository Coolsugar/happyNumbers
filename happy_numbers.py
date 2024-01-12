print('Happy Number Generator')
r = 1 + int(input("Enter range: 0 - "))
s = 0 
i = 0 
happyNumbers = []
if r > 1000:
	d = 0.000000000001
else:
	d = 0.1
import time as t
def log(num):
	str_happyNumbers = [str(_) for _ in happyNumbers]
	number_of_elements = len(happyNumbers)
	fl = open("/Users/esraaj/Documents/Code/Maths/happyNumLog.txt" , 'a') 
	fl.write('\n')
	fl.write("[!] Updated: ")
	fl.write(str(num))
	fl.write(": \n")
	fl.write('\n'.join(str_happyNumbers))
	fl.write("\n Ratio: ")
	fl.write(str(number_of_elements))
	fl.write('/')
	fl.write(str(num))
	fl.write("\n =============")
	print("List file updated.")
	print("Ratio: " , number_of_elements , "/" , num )
def split(word):
	List = list(word)
	fixList = [int(x) for x in List]
	return fixList
def succ(num):
	t.sleep(d)
	print('-> ',num)
	happyNumbers.append(num)
	if num + 1 == r:
		print(happyNumbers)
		log(num)
def fail(num):
	if num + 1 == r:
		print(happyNumbers)
		log(num)
for num in range(r):		
	l = split(str(num))			
	while 0 == 0:
		for elm in l:
			s += (elm**2)
		if s == 1:
			succ(num)
			l = split(str(s))
			s = 0
			break
		elif s == 0:
			fail(num)
			l = split(str(s))
			s = 0
			break
		elif s == 4:
			fail(num)
			l = split(str(s))
			s = 0
			break
		elif s == 16:
			fail(num)
			l = split(str(s))
			s = 0
			break
		elif s == 20:
			fail(num)
			l = split(str(s))
			s = 0
			break
		elif s == 37:
			fail(num)
			l = split(str(s))
			s = 0
			break
		elif s == 42:
			fail(num)
			l = split(str(s))
			s = 0
			break
		elif s == 58:
			fail(num)
			l = split(str(s))
			s = 0
			break
		elif s == 89:
			fail(num)
			l = split(str(s))
			s = 0
			break
		elif s == 145:
			fail(num)
			l = split(str(s))
			s = 0
			break
		else:
			l = split(str(s))
			s = 0 
# end