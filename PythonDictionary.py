# key : value pair {K:V}
my_dictionary = {}
print(my_dictionary)
print(type(my_dictionary))

# Integer Key and String values
name = {1:'Vinoth',2:'Anand',3:'Pranav'}
print(name)

# duplicate keys
name3 = {1:'Vinoth',2:'Anand',3:'Pranav',2:'Vishal'}
print(name3)

# Mixed key and value pairs
name2 = {1:'Vinoth','address':'Chennai','experience':['tcs','cts','telus']}
print(name2)

# access the values ONLY using key
print(name2[1])
print(name2['address'])
print(name2['experience'])
# print(name2['email'])
print(name2.get('address'))
print((name2.get('email')))

# adding the values
print(name2)
name2['emailId'] = 'vinothrwins@gmail.com'
print(name2)

# update the value
name2['emailId'] = 'vinoth.r@telusinternational.com'
print(name2)

# delete
name2.pop('emailId')
print(name2)

del name2['address']
print(name2)

# clear
name2.clear()
print(name2)

print("**************************************************")
employee = {1:'Vinoth',2:'Anand',3:'Pranav',4:'Vishal',5:'Kamran',6:'Rahul'}
print(employee)

for val in employee:
    print(val,employee[val])

# Methods
# lenname3 = {1:'Vinoth',2:'Anand',3:'Pranav',2:'Vishal'}
print(len(employee))

# membership
print(1 in employee)
print(7 not in employee)
print('Vinoth' in employee)

# sorted
employee2 = {5:'Kamran',1:'Vinoth',3:'Pranav',4:'Vishal',6:'Rahul',2:'Anand'}
print(sorted(employee2))

#keys
print(employee.keys())

# values
print(employee.values())

# items
print(employee.items())

#  copy
newlist = employee.copy()
print(newlist)

# update
newlist.update({2:'Soba'})
print(newlist)