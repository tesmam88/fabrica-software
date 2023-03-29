# CRIE UMA FUNÇÃO QUE RECEBA UMA LISTA E NUMEROS COMO PARAMETRO E RETORNE O NUMERO DE OCORRENCIA DE UM DETERMINADO NUMERO DA LISTA.

def contagem_ocorrencia(lista, num):
    contador=0
    for n in lista:
        if n == num:
            contador +=1
    return print(f"O numero {num} apareceu {contador} vezes na lista")

contagem_ocorrencia([3,2,3,6,4,5,6,8,8,6,2,3,5,9,5,4,2,1,5,6],2)



