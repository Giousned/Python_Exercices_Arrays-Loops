par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}
#your code go here:

def count_letter(string_done):

    global counts

    string_lower = string_done.lower()


    for i in range(len(string_lower)):

        if string_lower[i] == " ":
            continue

        contador = string_lower.count(string_lower[i])

        counts[string_lower[i]] = contador

    return counts
            
count_letter(par)

print(counts)


# OTRA SOLUCION

# string_lower = string_done.lower().replace(" ", "")
# for i in range(len(string_lower)):

#     if {string_lower[i]}:
#         contador = string_lower.count(string_lower[i])

#     counts[string_lower[i]] = contador

# return counts
