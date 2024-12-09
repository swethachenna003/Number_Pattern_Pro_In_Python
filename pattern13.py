'''
    5
   54
  543
 5432
54321

'''

num = 5
space = num-1
for line in range(num-1,-1,-1):
    for sp in range(space):
        print(' ', end = ' ')
    for val in range(num,line,-1):
        print(val, end = ' ')
    space -= 1
    print()
        
