for i in range(4):
    for j in range(4):
        print("i=",i,"j=",j)
n = int(input("enter the value"))
for l in range(1,n+1):
    for k in range(1,l+1):
        print("*",end=" ")
    print()

for m in range(1,n+1):
    print(' ' * n, end='')
    print('* ' * (m))
    n-=1
for i in range(1, 11):
    print(' '*(n-i) + '* '*(i))
# pass statement
for i in range(100):
    if i%9==0:
        print(i)
    else:pass
