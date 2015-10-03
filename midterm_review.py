#discussion 1
def  wears_jacket(temp,raining):
	return temp<60 or raining

def handle_overflow(s1,s2):
	if s1<=30 and s2<=30:
		print('no overflow')
	elif s1>=30 and s2>=30:
		print('No space left in either section')
	elif s2<30:
		print(30-s2,' spot left in Section 2')
	else:
		print(30-s1,' spot left in Section 1')

def keep_ints(n):
	def inner(f):
		i=1
		while i<=n:
			if f(i):
				print(i)
			i+=1
	return inner
	
def haha():
	print('hehe')
