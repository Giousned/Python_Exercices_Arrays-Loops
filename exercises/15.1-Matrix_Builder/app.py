#Import random

#Create the function below:

def matrixBuilder(number):

    matriz_final = []

    for i in range(number):
        matriz = []        
        for j in range(number):
            matriz.append(1)
        matriz_final.append(matriz)
    
    return matriz_final


print(matrixBuilder(3))
