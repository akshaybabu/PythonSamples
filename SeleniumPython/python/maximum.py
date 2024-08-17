a = int(input("enter first number"))
b = int(input("enter second number"))
c = int(input("enter third number"))
d=input()
print(type(d))
min = a if a>b and a>c else b if b>c else c
print(min)
