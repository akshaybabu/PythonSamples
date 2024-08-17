s=input("enter some string")
output=''
previous=''
for x in s:
    if x.isalpha():
        output=output+x
        previous=x
    else:
        output=output+chr(ord(previous)+int(x))
print(output)