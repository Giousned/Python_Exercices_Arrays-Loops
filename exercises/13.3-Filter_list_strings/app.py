
names = ['Liam','Emma','Noah','Olivia','William','Ava','James','Isabella','Logan','Sophia',
'Benjamin','Mia','Mason','Charlotte','Elijah','Amelia','Oliver','Evelyn','Jacob','Abigail',
'Lucas','Harper','Michael','Emily','Alexander','Elizabeth','Ethan','Avery','Daniel','Sofia',
'Matthew','Ella','Aiden','Madison','Henry','Scarlett','Joseph','Victoria','Jackson','Aria',
'Samuel','Grace','Sebastian','Chloe','David','Camila','Carter','Penelope','Wyatt','Riley']


#Your code go here:

def find_string(name):
    return name.lower().find("am") != -1

new_list = list(filter(find_string, names))

print(new_list)


# OTRA SOLUCION, QUE VA BIEN PERO NO PASA EL TEST
# def find_string(name):
#     return "am" in name

# new_list = list(filter(find_string, names))

# print(new_list)