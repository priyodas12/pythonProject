my_nums = [1, 2, 3, 4, 5]


def square(num):
    return num ** 2


print(list(map(square, my_nums)))


def check_even(num):
    return num % 2 == 0


print(list(filter(check_even, my_nums)))

print(list(map(lambda num:num**2,my_nums)))

print(list(filter(lambda num:num%2==0,my_nums)))