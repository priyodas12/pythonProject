# range function
for num in range(1,10,2):
    print(num)

# enumerate function
for letter in enumerate("abcdged"):
    print(letter)

for index,letter in enumerate("abcdged"):
    print(letter)

# zip function
list1=[1,2,3,4]
list2=["a","b","c"]
list3=[True,False]

for item in zip(list1,list2,list3):
    print(item)

print(list(zip(list1,list2)))

# in operator

print("s" in [1,2,3])
print(2 in [1,2,3])
print("a" in "abca")
print("s" in {"a":2,"s":3})

