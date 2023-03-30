people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

#Your code go here:
def deletePerson(person_name):
    new_list = []
    #Your code go here:
    for item in people:
        if item != person_name:
            new_list.append(item)
    return new_list
    
print(deletePerson("daniella"))
print(deletePerson("juan"))
print(deletePerson("emilio"))