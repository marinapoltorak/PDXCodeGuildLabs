
lst = []

while True:
    user_input = input("Enter a number, or enter 'done' ")
    if user_input == 'done':
        break
    lst.append(float(user_input))
    print(lst)

total = 0
for num in lst:
    total += num / len(lst)
print(total)
