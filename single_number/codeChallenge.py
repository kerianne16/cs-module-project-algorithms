
'''
Print out all of the numbers in the following array that are divisible by 3:
'''

number_list = [85, 46, 27, 81, 94, 9, 27, 38, 43, 99, 37, 63, 31, 42, 14]


# need to loop and check if divisble by 3
# print
# in a func

def number(number_list):
    for i in number_list:
        if i % 3 == 0:
            print(i)


number(number_list)
