'''
5
54
543
5432
54321
'''

num = 5
for line in range(num-1,-1,-1):
    for val in range(num,line,-1):
        print(val, end = ' ')
    print()
        
