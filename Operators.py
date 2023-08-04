# Arithmetic Operator

num1 = 60;
num2 = 40;
print(num1 + num2)
print("Sum of two numbers ", num1 + num2)

# Addition
print("Sum of {1} and {0} = ".format(num1, num2), num1 + num2)

# subtraction
print("Subtraction of {} and {} = ".format(num1, num2), num1 - num2)

# multiplication
print("Multiplication of {} and {} = ".format(num1, num2), num1 * num2)

# float division
print(10 / 3)

# integer division
print(10 // 3)

# modules
print(10 % 3)

# exponential
print(2 ** 4)

## Relational Operators
num3 = 35
num4 = 25

print(num3 > num4)
print(num3 < num4)
print(num3 == num4)
print(num3 >= num4)
print(num3 <= num4)
print(num3 != num4)

# logical operator
print("*******************")
x = 50
y = 100

# and operator 'and'
print(x < y and num3 > num4)
print(x > y and num3 > num4)

# or operator
print(x < y or num3 > num4)
print(x > y or num3 > num4)
print(x > y or num3 < num4)

# not operator
print(not (x < y))

# Augmented Operator
i = 1
i = i + 1
print(i)

j = 1
j += 1  # j = j + 1
print(j)

k = 10
k -= 2
print(k)

# Identity Operator

num5 = 100
num6 = 100
num7 = 200
print(num5 is num6)
print(num6 is not num5)
