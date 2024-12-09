'''
12345
 1234
  123
   12
    1

'''

num = 5
space = 0
for line in range(num+1,1,-1):
    for sp in range(space):
        print(' ', end = ' ')
    for val in range(1,line):
        print(val, end = ' ')
    space += 1
    print()
        
