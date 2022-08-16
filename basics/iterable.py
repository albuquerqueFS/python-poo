my_iterable = [1,2,3]

for x in my_iterable:
    print(x)

employees = {'ceo':'cindy', 'cfo':'james'}
employeesList = [('ceo','cindy'), ('cfo','james')]

for position in employees:
    print(position)
    print(employees[position])

for (position, name) in employeesList:
    print(position)
    print(name)


my_list1 = [1, 2, 3, 4, 5, 10]
my_list2 = []

for index, value in enumerate(my_list1):
    my_list2.append(my_list1[index] + 42)

print(my_list2)