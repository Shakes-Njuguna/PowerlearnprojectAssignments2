#declare and initialize

num1 = 6

num2 = 9

print('This is output')

#Implicit type conversion- automatically converts

integer_number = 123

float_number = 1.23

new_number = integer_number + float_number
#display new value resulting data type 

print("Value:",new_number)

print("Data Type:",type(new_number))

#Explicit Type Conversion- users convert them 

num_string = '12'

num_integer = 23

print("Data type of num_string before Type Casting:", type(num_string))

#Explicit Type conversion 

num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("sum:",num_sum)

print("Data type of num_sum:",type(num_sum))