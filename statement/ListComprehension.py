myString1="hello"
mylist1=[]
for letter in myString1:
    mylist1.append(letter)
print(mylist1)

myString2="helloWorld"
mylist2=[letter for letter in myString2]
print(mylist2)

# first num is for appending that number ,2nd is for iteration
mylist3=[num**2 for num in range(0,10)]
print(mylist3)

# adding condition
mylist4=[num**2 for num in range(0,10) if num%2==0]
print(mylist4)

celcious=[37,45,-31,67,98]
farenheit=[(9/5*temp+32) for temp in celcious]
print(farenheit)