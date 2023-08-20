# create an empty list
name_list = []
print(name_list)
print(type(name_list))

# list of integers
num_list = [10, 20, 30, 40, 50]
print(num_list)

# list of string
name_list = ["Vinoth", "Anand", "Pranav", "Soba"]
print(name_list)

# list of list
list1 = [[10, 20, 30], ["Python", "Java"]]
print(list1)

# all the data types
list2 = [10, 50, "Telus", True, 774.54]
print(list2)

print("*****************Indexing and Slicing *************************")

list3 = [10, 20, 30, 40, 50, 60, 70, 80]
# [starting index:end index-1]
print(list3[4])
print(list3[:])
print(list3[2:])
print(list3[:6])  # end index - 1
print(list3[2:5])

# negative index
print(list3[-3])
print(list3[2:-3])

# updating the list
name_list1 = ["Vinoth", "Anand", "Pranav", "Soba"]
print(name_list1)
name_list1[3] = 'Vimal'
print(name_list1)

# delete the list
del name_list1[0]
print(name_list1)

# delete entire list - deleting the variable and its values
del name_list1
# print(name_list1)


list4 = [10, 20, 30, 40, 50, 60, 70, 80]
for num in list4:
    print(num)

print("************List Methods********************")

# concatenarion
list5 = [10, 20, 50]
list6 = [57, 46, 36, 88]
finallist = list5 + list6
print(finallist)

# length
print(len(finallist))

# Repetition
listrep = ["Telus"]
print(listrep * 10)

# Membership - in || not in
print(finallist)  # [10, 20, 50, 57, 46, 36, 88]
print(50 in finallist)
print(40 in finallist)
print(33 not in finallist)
print(88 not in finallist)

# min
print(min(finallist))

# max
print(max(finallist))

# sum
print(sum(finallist))

# sort
finallist.sort()
print(finallist)

# sort in reverse order
finallist.sort(reverse=True)
print(finallist)

# append - use when you want to add single element to the existing list
list_telus = ['Hasan', 'Dhanraj', 'Kamran', 'Shafeeq', 'Naresh', 'Tanvi']
print(list_telus)

# adding single value
list_telus.append('Rahul')
print(list_telus)

# adding the list
list_new = ['Rajat']
list_telus.append(list_new)
print(list_telus)

# extend - iterate
program_lang = ['Python', 'Java', 'C#', 'Ruby', 'VB Script']
print(program_lang)

# adding single character will be added using iteration mode
program_lang.extend('Telus')
print(program_lang)

# adding the list
program_lang.extend(['C++', 'Cobal'])
print(program_lang)

print("*******************************************************")
# insert
list_prog = ['Python', 'Java', 'C#', 'Ruby', 'VB Script']
list_prog.insert(2, 'Kotlin')
print(list_prog)

# remove
list_prog.remove('C#')
print(list_prog)

# pop - to know the value which we removed
val = list_prog.pop(3)
print(val)
print(list_prog)

# count
list_count = [10, 20, 10, 4, 0, 10, 50, 10]
print(list_count.count(10))

# reverse
list_count.reverse()
print(list_count)
list_count.clear()
print(list_count)
