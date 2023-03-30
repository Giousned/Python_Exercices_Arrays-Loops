myNumbers = [23,234,345,4356234,243,43,56,2]

#Your code go here:

#incrementByThree
def increment_by_one(number):
    return number * 3

new_list = list(map(increment_by_one, myNumbers))

print(new_list)   #returns [69, 702, 1035, 13068702, 729, 129, 168, 6]