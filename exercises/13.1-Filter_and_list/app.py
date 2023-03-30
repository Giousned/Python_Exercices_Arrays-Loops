
all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

#Your code go here:

def start_names(name):
    return name.startswith("R")

resulting_names = list(filter(start_names, all_names))

print(resulting_names)



# OTRA SOLUCION
# def start_names(name):
#     return name[0] == "R"

# resulting_names = list(filter(start_names, all_names))

# print(resulting_names)
