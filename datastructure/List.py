my_list=[1,2,3,4,5,6]
print(type(my_list))
# indexing of list
print(my_list[1])
# slicing of list
print(my_list[1:4])
print(my_list[1:])

# list operations
another_list=[7,8,9]
print(my_list+another_list)

# mutable

my_list[4]=22
print(my_list)
my_list.append(21)
print(my_list)

# heterogeneous
next_list=['2',3,'asd',1.2,True]
print(next_list)

# alter list
next_list.pop()
print(next_list)
next_list.pop(0)
print(next_list)
next_list.insert(2,29)
print(next_list)

# sorting of list
new_list=[4,3,0,8,-2,19]
# does not return anything
new_list.sort()
print(new_list)
new_list.reverse()
print(new_list)