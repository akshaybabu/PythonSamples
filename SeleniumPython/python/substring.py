s=input("enter the main string")
subs=input("enter the subs string")
flag=False
pos=-1
n=len(s)
while True:
    pos=s.find(subs,pos+1,n)
    if pos==-1:
        break
    print("found at ",pos)
    flag=True
if flag==False:
    print("not found")