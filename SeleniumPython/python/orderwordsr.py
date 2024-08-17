s=input('enter the string')
k=s.split()
l1=[]
i=len(k)-1
while i>=0:
    l1.append(k[i])
    i=i-1
output=' '.join(l1)
print(output)