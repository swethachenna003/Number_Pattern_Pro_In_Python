'''
    1
   12
  123
 1234
12345

'''

num = 5
space = num-1
for line in range(2,num+2):
    for sp in range(space):
        print(' ', end = ' ')
    for val in range(1,line):
        print(val, end = ' ')
    space -= 1
    print()
        
