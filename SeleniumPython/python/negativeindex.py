s=input("enter a string:")
i=0
for x in s:
    print("the character at positive index {} and at nEgative index {} is {}".format(i,i-len(s),x))
    i=i+1