# CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NUMEROS COMO PARAMETRO E RETORNE UMA LISTA COM APENAS NUMEROS MENORES QUE 10.

def numeros(lista):
    menores=[]
    for num in lista:
        if num <10:
            menores.append(num)

    return print(menores)

numeros([1,2,3,4,5,6,7,8,9,10])