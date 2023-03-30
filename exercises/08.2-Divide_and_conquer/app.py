list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


#Your code here:

def merge_two_list(list_number):
    odd = []
    even = []

    mergeTwoList = []

    for item in list_number:
        if item % 2 == 0:
            even.append(item)
        else:
            odd.append(item)
    
    mergeTwoList.append(odd)
    mergeTwoList.append(even)
    
    return mergeTwoList


print(merge_two_list(list_of_numbers))

