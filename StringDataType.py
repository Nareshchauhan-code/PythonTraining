# String data type
welcome_msg = "Welcome to Python Class"
print(welcome_msg)
print(type(welcome_msg))

# index -> ZERO(0) - ACCESS
print(welcome_msg[0])
print(welcome_msg[5])

# slicing
print(welcome_msg[0:7]) # end index -1
print(welcome_msg[:])
print(welcome_msg[11:])
print(welcome_msg[:17])

# negative indexing
transaction = "Registration Form is Successfully Submitted. The Transaction ID : NXTGEN96107"
print(transaction[-1])
print(transaction[11:-11])
# print(transaction[100])


# update the string - IMMUTABLE
name = "Pranav"
print(name[5])
# name[5] = "i"
print(name)

# deleting the string
del name
# print(name)





