print('*'*50)
n = int(input('Enter a with multiplycation table:'))
a = int(input('Enter a any number:'))
print('*'*50)
print('Multiplycation Table',n)
for i in range(1,a+1):
	print('\t{0} * {1} = {2}'.format(n,i,n*i))
print('*'*50)