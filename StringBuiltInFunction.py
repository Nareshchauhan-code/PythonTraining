# string operations

# concatenation
str1 = "Vinoth"
str2 = "Vinoth"
print(str1 + str2)
# print(str1,str2)

# comparison
print("Selenium" == "selenium")
print("Selenium" == "Selenium")
print(str1.__eq__(str2))

print("***********************************")
# membership operator ( in and not in)
str3 = "Welcome to python class"
# in
print('python' in str3)
print('Python' in str3)
print('Java' in str3)
print('s' in str3)

# not in
print('Java' not in str3)
print('python' not in str3)

print("***********************************")

str4 = "Telus International"
# for
for val in str4:
    print(val)

str5 = "Telus"
print(str5 * 5)

print("***************Built In Functions********************")

# 1. strip()
str6 = " Hello Team "
print(str6)
print(str6.strip())

# 2. len()
print(len(str5))

# 3. islower
str7 = "telus"
print(str7.islower())

# 4.  lower()
print(str6.lower())

# 5. isupper()
str8 = "HELLO"
print(str8.isupper())

# 5. upper
print(str7.upper())

print("***********************************")

str9 = "Selenium"
str10 = "selenium123"
str11 = "123487"
str12 = "vinoth121@gmail"

print(str9.isalpha())
print(str10.isalpha())
print(str11.isalpha())
print(str12.isalpha())
print("***********************************")

print(str9.isdigit())
print(str10.isdigit())
print(str11.isdigit())
print(str12.isdigit())

print("***********************************")

print(str9.isalnum())
print(str10.isalnum())
print(str11.isalnum())
print(str12.isalnum())

print("***********************************")

# join

str12 = "Messi"
str13 = '$'
print(str13.join(str12))

# split
credit_card = '1345-6635-7775-8533'
print(credit_card.split('-'))

# count
str14 = "Welcome to python class. python is easier to learn. I like python. python is best"
print(str14.count('python'))
print(str14.count('to'))

# find
print(str14.find('python'))
print(str14.find('java'))

# replace
updated_value = str14.replace("python","java")
print(updated_value)

# sorted
str15 = "gfsdhdsknwkenrwlskdvkshsrjtnvnslsdfutnbvkdl"
print(sorted(str15))

# startswith
print(str14.startswith('Welcome'))
print(str14.startswith('welcome'))

# ends with
print(str14.endswith('best'))




