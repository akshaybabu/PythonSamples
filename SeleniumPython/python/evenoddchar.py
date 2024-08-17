s=input("string:")
print("even",s[0::2])
print("odd",s[1::2])
i=0
print("even")
while i<len(s):
    print(s[i],end=',')
    i=i+2
print()
i=1
print("odd")
while i < len(s):
    print(s[i],end=',')
    i=i+2