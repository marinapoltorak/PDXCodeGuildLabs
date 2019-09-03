operation = input("What is the operation you would like to perform? ")
first_number_input = input("What is the first number? ")
second_number_input = input("What is the second number? ")
add = ['add', 'addition', '+']
subtract = ['subtract', 'subtraction', 'minus', '-']
multiply = ['multiply', 'multiplication', '*']
divide = ['divide', 'division', '/']

first_number = float(first_number_input)
second_number = float(second_number_input)

print(operation)
print(first_number)
print(second_number)

if operation in add:
    answer = first_number + second_number
    print(answer)
elif operation in subtract:
    answer = first_number - second_number
    print(answer)
elif operation in multiply:
    answer = first_number * second_number
    print(answer)
elif operation in subtract:
    answer = first_number - second_number
    print(answer)
