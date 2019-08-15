l=str(input("enter the string"))
a=''
for i in range(len(l)):
    if i%2==0:
        a+=l[i]
print(a)
