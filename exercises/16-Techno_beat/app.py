
def lyrics_generator(lista):

    string_final = ""

    contador = 0

    for item in lista:
        if item == 0:
            string_final += "Boom "
        elif item == 1:
            string_final += "Drop the base "
            contador += 1
            if contador == 3:
                string_final += "!!!Break the base!!! "

    return string_final


# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))


# OTRA SOLUCION, AUNQUE NO PASA EL TEST, SE VE QUE LLEVA ESPACIO AL FINAL
# def lyrics_generator(lista):

#     string_final = ""

#     contador = 0

#     for item in lista:
#         if item == 0:
#             string_final += "Boom "
#         elif item == 1:
#             string_final += "Drop the base "
#             contador += 1
#             if contador == 3:
#                 string_final += "!!!Break the base!!! "

#     return string_final.strip()