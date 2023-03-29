#CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NUMEROS COMO PARAMETRO E RETORNE O MAIOR NUMERO DA LISTA.

def maior_numero(lista):
    maior=lista[0]
    for num in lista:
        if num>maior:
            maior=num

    return print(maior)
maior_numero([1,3,8,9,4,6])