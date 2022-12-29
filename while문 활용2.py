flo=int(input())

i=1
while i<=flo:
	for j in range(flo-i):
		print(' ', end='')
	for k in range(2*i-1):
		print('*', end='')
	i=i+1
	print()
