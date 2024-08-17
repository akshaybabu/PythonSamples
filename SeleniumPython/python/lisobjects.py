
l =list(range(0,10,2))
print(l)
print(type(l))
a="achu"
m=list(a)
print(m)
b="achu is a good boy"
n=b.split()
print(n)
print(type(n))
print(n[-1])
print(n[0])

v=[10,20,307,8,8,6,5,3,90]
print(v)
i=0
while i<len(v):
    print(v[i])
    i=i+1
for v1 in v:
    print(v1)

for v2 in v:
    if v2%2==0:
        print(v2)

print(len(v))

count()