s=input("enter some string")
i=[]
for x in s:
    if x not in i:
        i.append(x)
output=''.join(i)
print(output)