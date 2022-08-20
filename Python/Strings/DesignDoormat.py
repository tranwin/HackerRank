a = '-'
b = '.|.'

height, width = map(int, input().split())

# Top part
for i in range(1, height):
    j = (width - 3*i)//2
    if i %2 !=0:
        print(a*j + b*i + a*j)

# Middle part
print ('WELCOME'.center(width,'-'))

# Bottom part
for i in range(1, width//6 + 1):           
    print(a*3*i + b*((width-height)//2 - 2*i) + a*3*i)

# More elegant
# for i in range(1, y):
#     if i % 2 != 0:
#         print (('.|.' * i).center(x, '-'))
# print('WELCOME'.center(x, '-'))
# for i in reversed(range(1, y)):
#     if i % 2 != 0:
#         print (('.|.' * i).center(x, '-'))










