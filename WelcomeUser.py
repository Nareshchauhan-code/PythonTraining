print("Welcome To Python Automation")

# Declare the variable
# snake case
# variable_name = value
age = 20
print(age)
print(id(age))

first_name = "vinoth"
print(first_name)
print((id(first_name)))

# Rules 1
EMPLOYEE = ''
Employee = ''
employee = ''
employee_name = ''
employee07 = ''

# Rule 2
# employee@ = '';
# employee$ = '';
# employee% = '' ;

# rule 3 - case sensitive
name = "Anand"
Name = "anand"
lastname = "Anandhi"
print(id(name))
print(id(Name))
print(id(lastname))

# rule 4
# if = "Hello"
# else = "Python"

# rule 5
# 456employee = ''

# keywords
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))

# multiple assignments
num1,num2,num3,num4,num5 = 10,20,30,40,50
print("Output values", num1,num2,num3,num4,num5)

emp_name,emp_id,emp_salary = "Anand",12345,4545.56
print(emp_name,emp_id,emp_salary)

# single value to multiple variables
maths_marks = science_marks = english_marks = 60
print(maths_marks)
print(science_marks)
print(english_marks)
print(id(maths_marks))
print(id(science_marks))
print(id(english_marks))

science_marks =  70
print(id(science_marks))


# Numbers - Data type
emp_id = 12345 # integer
emp_salary = 12345.624 # float
compl_num = 2 + 4j; # complex

print(type(emp_id))
print(type(emp_salary))
print(type(compl_num))






