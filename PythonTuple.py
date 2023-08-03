# create an empty tuple
my_tuple = ()
print(my_tuple)
print(type(my_tuple))

# tuple of integers
num_tuple = (10,20,30,40,50)
print(num_tuple)

# tuple of string
name_tuple = ("Vinoth","Anand","Pranav","Soba")
print(name_tuple)

# tuple of tuple
tuple1 = ((10,20,30),("Python","Java"))
print(tuple1)

# all the data types
tuple2 = (10,50,"Telus",True,774.54)
print(tuple2)

print("*****************Indexing and Slicing *************************")

tuple3 = (10,20,30,40,50,60,70,80)
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
name_tuple1 = ("Vinoth","Anand","Pranav","Soba")
print(name_tuple1)
# name_tuple1[3] = 'Vimal'
# print(name_tuple1)

# delete the tuple
# del name_tuple1[1]
# print((name_tuple1))

del name_tuple1
# print(name_tuple1)


tuple4 = (10,20,30,40,50,60,70,80)
for num in tuple4:
    print(num)

print("************tuple Methods********************")

# concatenarion
tuple5 = (10,20,50)
tuple6 = (57,46,36,88)
finaltuple = tuple5 + tuple6
print(finaltuple)

# length
print(len(finaltuple))

# Repetition
tuplerep = ("Telus")
print(tuplerep * 10)

# Membership - in || not in
print(finaltuple) # [10, 20, 50, 57, 46, 36, 88]
print(50 in finaltuple)
print(40 in finaltuple)
print(33 not in finaltuple)
print(88 not in finaltuple)

# min
print(min(finaltuple))

# max
print(max(finaltuple))

# sum
print(sum(finaltuple))

# sorted
print(sorted(finaltuple))

# sort in reverse order
print(sorted(finaltuple,reverse=True))

# count
tuple_count = (10,20,10,4,0,10,50,10)
print(tuple_count.count(10))

# index
print(tuple_count.index(50))

