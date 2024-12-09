'''
1
22
333
4444
55555

'''

num = 5
for line in range(0,num+1):
    for col in range(line):
        print(line, end = ' ')
    print()
