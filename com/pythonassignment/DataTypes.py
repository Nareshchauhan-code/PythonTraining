# Numbers - Data type
print("***************Numbers Data type**********")
emp_id = 12345  # integer
emp_salary = 12345.624  # float
complex_num = 2 + 4j;  # complex

print(type(emp_id))
print(type(emp_salary))
print(type(complex_num))

# String data type
print("************String Data type********************")
welcome_msg = "Welcome to Python"
print(welcome_msg)
print(type(welcome_msg))

print("************Index*************")
print(welcome_msg[0])
print(welcome_msg[5])

# slicing
print("**********Slicing***************")
print(welcome_msg[0:7])  # end index -1
print(welcome_msg[:])
print(welcome_msg[11:])
print(welcome_msg[:17])

# negative indexing
print("**********Negative Indexing***************")
login_password = "Your Login and Password is naresh:12345"
print(login_password[-1])
print(login_password[0:-12])
print('Your Login and Password is:', login_password[26:])

# update the string - IMMUTABLE
print("**********Update the String***************")
name = "naresh"
print(name[5])
# name[5] = "i"
print(name)

# deleting the string
print("**********Deleting the String***************")
del name
# print(name)

print("**********List Data type***************")
list = [10, 20, 30, 40, 50, 60, 70, 80]

print(list[2:4])
print(list[4])
print(list[2:])
print(list[2:-3])
print(list[:-3])
print("********************For Loop*********************** ")
for val in list:
    print(val, end=" ")

names = ['Kapil', 'Sonu', 'Monu']

positions = ['Manager', 'HR', 'QA']

positions.extend(names)

print(positions)

print("**********Tuple Data type***************")

# create an empty tuple
my_tuple = ()
print(my_tuple)
print(type(my_tuple))

# tuple of integers
num_tuple = (10, 20, 30, 40, 50)
print(num_tuple)

# tuple of string
name_tuple = ("Kapil", "Anand", "Pranav", "Soba")
print(name_tuple)

# tuple of tuple
tuple1 = ((10, 20, 30), ("Python", "Java"))
print(tuple1)

# all the data types
tuple2 = (10, 50, "Telus", True, 774.54)
print(tuple2)

print("*****************Indexing and Slicing *************************")

tuple3 = (10, 20, 30, 40, 50, 60, 70, 80)
# [starting index:end index-1]
print(tuple3[4])
print(tuple3[:])
print(tuple3[2:])
print(tuple3[:6])  # end index - 1
print(tuple3[2:5])

# negative index
print(tuple3[-3])
print(tuple3[2:-3])

# updating the tuple - Immutable
name_tuple1 = ("Kapil", "Anand", "Pranav", "Soba")
print(name_tuple1)

del name_tuple1
# print(name_tuple1)

tuple4 = (10, 20, 30, 40, 50, 60, 70, 80)
for num in tuple4:
    print(num)

print("************tuple Methods********************")

# concatenation
tuple5 = (10, 20, 50)
tuple6 = (57, 46, 36, 88)
final_tuple = tuple5 + tuple6
print(final_tuple)

# length
print(len(final_tuple))

# Repetition
tuplerep = ("Telus")
print(tuplerep * 10)

# Membership - in || not in
print(final_tuple)  # [10, 20, 50, 57, 46, 36, 88]
print(50 in final_tuple)
print(40 in final_tuple)
print(33 not in final_tuple)
print(88 not in final_tuple)

# min
print(min(final_tuple))

# max
print(max(final_tuple))

# sum
print(sum(final_tuple))

# sorted
print(sorted(final_tuple))

# sort in reverse order
print(sorted(final_tuple, reverse=True))

# count
tuple_count = (10, 20, 10, 4, 0, 10, 50, 10)
print(tuple_count.count(10))

# index
print(tuple_count.index(50))

print("**********Dictionary Data type***************")

# key : value pair {K:V}
my_dictionary = {}
print(my_dictionary)
print(type(my_dictionary))

# Integer Key and String values
name = {1: 'Kapil', 2: 'Anand', 3: 'Pranav'}
print(name)

# duplicate keys
print("*********************duplicate keys************")
name3 = {1: 'Kapil', 2: 'Anand', 3: 'Pranav', 2: 'Vishal'}
print(name3)

# Mixed key and value pairs
name2 = {1: 'Kapil', 'address': 'Chennai', 'experience': ['tcs', 'cts', 'telus']}
print(name2)

# access the values ONLY using key
print(name2[1])
print(name2['address'])
print(name2['experience'])
# print(name2['email'])
print(name2.get('address'))
print((name2.get('email')))

# adding the values
print("************************Adding the values***************************")
print(name2)
name2['emailId'] = 'Kapil@gmail.com'
print(name2)

# update the value
name2['emailId'] = 'naresh@telusinternational.com'
print(name2)

# delete
print("************************Delete the values***************************")
name2.pop('emailId')
print(name2)

del name2['address']
print(name2)

# clear
name2.clear()
print(name2)

print("********************All Values******************************")
employee = {1: 'Kapil', 2: 'Anand', 3: 'Pranav', 4: 'Vishal', 5: 'Kamran', 6: 'Rahul'}
print(employee)

for val in employee:
    print(val, employee[val])

# Methods
print(len(employee))

# membership
print(1 in employee)
print(7 not in employee)
print('Kapil' in employee)

# sorted
employee2 = {5: 'Kamran', 1: 'Kapil', 3: 'Pranav', 4: 'Vishal', 6: 'Rahul', 2: 'Anand'}
print(sorted(employee2))

# keys
print(employee.keys())

# values
print(employee.values())

# items
print(employee.items())

#  copy
new_disc = employee.copy()
print(new_disc)

# update
new_disc.update({2: 'Soba'})
print(new_disc)
