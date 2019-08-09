l=[12,24,35,24,88,120,155,88,120,155]
dup_items=set()
unique_item=[]
for i in l:
    if i not in dup_items:
        unique_item.append(i)
        dup_items.add(i)
print(unique_item)
