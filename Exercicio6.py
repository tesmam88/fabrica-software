#CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE STRING COMO PARAMETRO E RETORNA A STRING MAIS LONGA

def nomes(lista):
    maior=lista[0]
    for i in lista:
       if len(i) > len(maior):
          maior=i


    return print( maior)

nomes(['jacare', 'casa', 'automovel', 'pao'])



    