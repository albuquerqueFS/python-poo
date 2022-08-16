myvar = "NEW"
mylist = [100,200,300,400,500]
mylist.append(myvar)
print(mylist)

mylist.insert(2, myvar)
print(mylist)

item_removed = mylist.pop(2)
print(f"Item removed: {item_removed}")
print(mylist)

print("Reverse")
mylist.reverse()
print(mylist)

list_to_sort = [42,142,521,612,213,74,41]
print(list_to_sort)
list_to_sort.sort(reverse=True)
print(list_to_sort)