# CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE PALAVRAS COMO PARAMETRO E RETORNE UMA LISTA COM PALAVRAS QUE COMEÇAM COM A LETRA "A"

def palavras(lista):
    vogal_a=[]
    for a in lista:
        if a[0] == 'A' or a[0] == 'a':
            vogal_a.append(a)

    return print(vogal_a)
palavras(['anta', 'Arara', 'cobra', 'carro', 'bike', 'Amora', 'Bento', 'Antonio'])