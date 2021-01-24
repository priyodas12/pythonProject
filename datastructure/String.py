s1 = "Priyobrato";
# indexing

print(s1[3]);
print(s1[-3]);

# slicing

print(s1[:4])
print(s1[3:6])
print(s1[3:6])
print(s1[::])
print(s1[::2])
print(s1[::-1])

# Immutability in String

# TypeError: 'str' object does not support item assignment
# s1[0]='S'
letter="a"
print(letter*10)
print('2'+'3')
# print('2'+3)

# String function

print(letter.join("abc"))
print(letter.upper())
type(letter.upper())
print(s1.split("o"))

# Print formatting

print("here is count of b= {}".format("abc".count("b")))
print("{2}{1}{0}".format("a","z","s"))
print("{c}{a}{b}".format(a="abc" ,b="xyz" ,c="mno"))

# precision calculation

result=1000/777
print("the result is={r:1.6f}".format(r=result))

# formatted string
print(f"this is result={result}")