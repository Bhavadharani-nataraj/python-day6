li=[12,24,35,70,88,120,155]
for i in li:
    if i%7==0 and i%5==0:
        li.remove(i)
print(li)
