# CRIE UMA FUNÇÃO QUE RECEBE UMA LISTA DE NUMEROS COMO PARAMETRO E RETORNE O SEGUNDO MENOR NUMERO DA LISTA



def numeros(lista):
  menor = lista[1]
  for num in lista:
    if num != menor:
      if menor == min(lista):
        menor = num
      elif num < menor:
        menor = num
  return print(menor)

numeros([4,6,1,5,3,7])


