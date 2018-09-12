

a = 18
b = 30

while a and b:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a+b)

