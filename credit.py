# Convert the input string into a list of ints
# Slice off the last digit. That is the check digit.
# Reverse the digits.
# Double every other element in the reversed list.
# Subtract nine from numbers over nine.
# Sum all values.
# Take the second digit of that sum.
# If that matches the check digit, the whole card number is validself.

user_string = input('enter 5 numbers: ')
my_list = []
def problem(str):
    for i in range(len(user_string)):
        my_list.append(int(user_string[i]))
    print(user_string)
    print(my_list)
check_digit = my_list.pop(4)
print(my_list)
my_list.reverse()
print(my_list)

my_list[1::2] = [x*2 for x in my_list[1::2]]
print(my_list)

total = 0
for i in range(len(my_list)):
    if my_list[i] > 9:
        my_list[i] -= 9
print(my_list)
total += my_list[i]

print(total)

second_digit = total % 10

if check_digit == second_digit:
        return True
    else:
        return False



problem(user_string)
