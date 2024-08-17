s="achu is a good boy"
n=len(s)
i=0
print("forward")
while i<n:
    print(s[i],end='')
    i+=1
print("\nbackward")
i=-1
while i>=-n:
    print(s[i],end='')
    i=i-1