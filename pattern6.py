'''
12345
1234
123
12
1
'''

num = 5
for line in range(num+1,1,-1):
    for val in range(1,line):
        print(val, end = ' ')
    print()
        
