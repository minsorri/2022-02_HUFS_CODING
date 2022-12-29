'''
for i in range(1,6):
	for j in range(i):
		print('*', end='')
	print()
'''

i=1
while i<6:
	for j in range(i):
		print('*', end='')
	i=i+1
	print()
