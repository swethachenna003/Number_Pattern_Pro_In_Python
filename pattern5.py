'''
4444
 333
  22
   1

'''

var = 4
num = var
space = 0
for line in range(1,var+1):
    for sp in range(space):
        print(' ', end = ' ')
    for n in range(num):
        print(num, end = ' ')
    space += 1
    num -=1 
    print()
