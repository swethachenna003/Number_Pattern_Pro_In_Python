'''
    1
   21
  321
 4321
54321

'''

num = 5
space = num-1
for line in range(1,num+1):
    for sp in range(space):
        print(' ', end = ' ')
    for val in range(line,0,-1):
        print(val, end = ' ')
    space -= 1
    print()
        
