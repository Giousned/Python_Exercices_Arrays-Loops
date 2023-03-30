incoming_ajax_data = [
    { "name": 'Mario', "last_name": 'Montes' },
    { "name": 'Joe', "last_name": 'Biden' },
    { "name": 'Bill', "last_name": 'Clon' },
    { "name": 'Hilary', "last_name": 'Mccafee' },
    { "name": 'Bobby', "last_name": 'Mc birth' }
]


#Your code go here:

def data_transformer(lista):
    new_list = list(map(lambda item:  item["name"] + " " + item["last_name"] , lista))
    return new_list

print(data_transformer(incoming_ajax_data))
        

# SOLUCION DADA
#Your code go here:
# def data_transformer(data_list):
#     return list(map(lambda element: f"{element['name']} {element['last_name']}", data_list))

# print(data_transformer(incoming_ajax_data))