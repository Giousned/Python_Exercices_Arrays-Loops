my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

#Your code go from here:

def maxInteger(list_number):

    bigger = 0
    
    for item in list_number:
        if item > bigger:
            bigger = item

    return bigger

print(maxInteger(my_list))

# SOLUCION DADA
# def maxInteger(arr):
#     maxInt=0
#     for i in range(len(arr)):
#         if arr[i] > maxInt:
#             maxInt = arr[i]
#     return maxInt

# print(maxInteger(my_list))