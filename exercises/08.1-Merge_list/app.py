chunk_one = [ 'Lebron', 'Aaliyah', 'Diamond', 'Dominique', 'Aliyah', 'Jazmin', 'Darnell' ]
chunk_two = [ 'Lucas' , 'Jake','Scott','Amy', 'Molly','Hannah','Lucas']


def merge_list(list1, list2):
    #Your code go here:
    two_list = []

    for item in chunk_one:
        two_list.append(item)

    for item in chunk_two:
        two_list.append(item)

    return two_list

    
print(merge_list(chunk_one, chunk_two))
