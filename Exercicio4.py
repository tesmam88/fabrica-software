#CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NUMEROS COMO PARAMETRO E RETORNE UMA LISTA COM APENAS NUMEROS PARES

def numeros(lista):
    pares=[]
    for num in lista:
        if num %2 == 0:
            pares.append(num)

    return print (pares)
numeros([1,2,3,4,5,6,7,8,9,10])