a=0
b=1
n=int(raw_input("enter number"))

def fibbo(n):
	global a,b
	print a,
	print b,
	for i in range(n-2):
		s=a+b
		a=b
		b=s
		print s,


if __name__ == '__main__':
    fibbo(n)		
