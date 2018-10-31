# Integers = Whole Number
# Floats = Decimal

integer = 3
decimal = 3.14

#Prints data type of object
print(type(integer))
print(type(decimal))

#-------------------------------------------------------------------------------------------------------------------------------------------------

# Arithmetic Operators:
# Addition:         3 + 2
# Subtraction:      3 - 2
# Multiplication:   3 * 2
# Division:         3 / 2
# Floor Division:   3 // 2
# Exponent:         3 ** 2
# Modulus:          3 % 2

print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)
print(3 ** 2)
print(3 % 2)

print(3 * 2 + 1)
print(3 * (2 + 1))

num = 1

#Prints variable with operator used epual to number used
num += 10

print(num)

#Prints absolute value of object
print(abs(-3))

#Rounds to the neartest integer value
print(round(3.75))
#Rounds to the first digit after the Decimal
print(round(3.75, 1))

#-------------------------------------------------------------------------------------------------------------------------------------------------

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

num_1 = 3
num_2 = 2

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)
print(num_1 >= num_2)
print(num_1 <= num_2)

#-------------------------------------------------------------------------------------------------------------------------------------------------

#Turn strings into actual numbers
num_3 = '100'
num_4 = '200'

num_3 = int(num_3)
num_4 = int(num_4)

print(num_3 + num_4)
