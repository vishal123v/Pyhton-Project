a=0
b=1
n=int(raw_input("enter number"))
print a,
print b,
for i in range(n-2):
	s=a+b
	a=b
	b=s
	print s,
