'''
1
11
111
1111
11111

'''

num = 5
for line in range(0,num+1):
    for col in range(line):
        print('1', end = ' ')
    print()
