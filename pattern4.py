'''
   1
  22
 333
4444

'''

var = 4
num = 1
space = var-1
for line in range(1,var+1):
    for sp in range(space):
        print(' ', end = ' ')
    for n in range(num):
        print(num, end = ' ')
    space -= 1
    num +=1 
    print()
