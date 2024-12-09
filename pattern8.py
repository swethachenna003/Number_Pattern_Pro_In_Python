'''
5
45
345
2345
12345
'''

num = 5
for line in range(num,0,-1):
    for val in range(line,num+1):
        print(val, end = ' ')
    print()
        
