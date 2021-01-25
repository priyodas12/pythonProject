def tax_calc(*args):
    return sum(args) * 0.10


print(tax_calc(100, 223, 1233, 334, 545, 1000))


def find_choice(**kwargs):
    if 'car' in kwargs:
        print(f"got my car from {kwargs['car']}")
    else:
        print("no hope here!")


find_choice(fruits='apple',car='tata')