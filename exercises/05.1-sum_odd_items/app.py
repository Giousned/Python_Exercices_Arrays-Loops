arr = [4,5,734,43,45,100,4,56,23,67,23,58,45]

#Your code go here:

def sum_odds(array):

    total = 0

    for item in array:
        if item % 2 != 0:
            total += item
    return total

print(sum_odds(arr))
