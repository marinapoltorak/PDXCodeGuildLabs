# def powers_of_two(a):
#     powers = [2 ** num for num in range (10)]
#     return powers
#
# print(powers_of_two(2))

# def ten_evens(num_even):
#     evens = [num for num in range (num_even) if num % 2 == 0]
#     return evens
#
# print(ten_evens(20))

# def swap_keys_values(a_dict):
#     return {v: k for k, v in  old_dict.items()}
#
# old_dict = {'a': 1, 'b': 2}
#
# print(swap_keys_values(old_dict))

# def combine(list1, list2):
#     combined = {}
#     for i in range (len(list1)):
#         combined.update({list1[i]: list2[i]})
#         return (combined)
# print(combine(fruits, prices))

# problem 1
# def p1():
#     lis = ['a', 'b', 'c']
#     elis = [1, 2, 3]
#     return {lis[i]:elis[i] for i in range(len(lis))}
# print(p1())

# fruits = ['apple', 'banana', 'pear']
# prices = [1.2, 3.3, 2.1]
#
# def combine_lists(list_1, list_2):
#     return dict(zip(fruits, prices))
#
# fruit_prices = combine_lists(fruits, prices)
#
# def average(d):
#     price_list = list(d.values())
#     print(price_list)
#     total = 0
#     for price in price_list:
#         total += price
#     return total / len(price_list)
# print(average(fruit_prices))
# import string
# to have the alphabet
# d = {'a1':5, 'a2':2, 'a3':3, 'b1':10, 'b2':1, 'b3':1, 'c1':4, 'c2':5, 'c3':6}
# # dict to work
# def unify(a_dict):
#     results = {}
#     # dictionary to update
#     for letter in string.ascii_lowercase:
#         # for each letter in the alhabet
#         count = 0
#         # how many times the letter occurs
#         total = 0
#         # total of values added for each letter
#         for key in a_dict:
#             # itirating through the keys in the dictionary
#             if not key.startswith(letter):
#                 continue
#                 # if key does not match the letter, continue
#             count += 1
#             # if match, add one to count
#             total += a_dict[key]
#             # and add the values to total
#             results.update({letter: round(total / count)})
#             # create an average and add key and average to results dictionary
#     return results
#
# print(unify(d))

# import string
