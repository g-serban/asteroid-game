list = [1,2,3]
print(list, 'list1')

b = list[:]
print(b, 'list2')

list.reverse()
print(list)
b.clear()
print(b)