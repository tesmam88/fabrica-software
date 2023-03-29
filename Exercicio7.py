# CRIE UMA FUNÇÃO QUE RECEBA UMA LISTA DE NUMEROS COMO PARAMETRO E RETORNE UMA LISTA COM APENAS NUMEROS IMPARES.

def numeros(lista):
    impar=[]
    for num in lista:
        if num %2:
            impar.append(num)

    return print(impar)
numeros([1,2,3,4,5,6,7,8,9,10])
