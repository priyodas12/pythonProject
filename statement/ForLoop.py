my_list=[3,4,5,6,7,9]
for number in my_list:
    if(number%2==0):
        print("even mumber {} ".format(number))
    else:
        print("odd number {}".format(number))

sum=0;
for num in my_list:
    sum+=num;
print(sum)

sample_str="aasakmsmalma"

for letter in "aasak ms mal ma":
    print(letter)


for _ in "ak ms mal ma":
    print(100)

new_list=[(0,1),(2,3),(4,5),(6,7)]

for num in new_list:
    print(num)

for a,b in new_list:
    print(a)
    print(b)

new_dict={"k1":8,"k2":2,"k3":3,"k4":4}

for key,value in new_dict.items():
    print("KEY="+key+",VALUE={}".format(value))

