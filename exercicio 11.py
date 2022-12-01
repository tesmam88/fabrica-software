nome = input("digite seu nome")
idade = int(input("digite a sua idade"))

if (idade > 0) and (idade < 2):
    print(f'{nome} esta com {idade} e pela tabela é considerado bebe')
elif idade < 0:
    print(f'{nome}esta com {idade} essa idade não existe')
    

elif (idade >= 3) and (idade <= 11):
    print(f'{nome} esta com {idade} e pela tabela é considerado criança')

elif (idade >= 12) and (idade <= 21):
    print(f'{nome} esta com {idade} e pela tabela é considerado jovem')
elif (idade >=22) and (idade <= 64):
    print(f'{nome} esta com {idade} e pela tabela é comsiderado adulto')
elif (idade >= 65) and (idade<=100):
    print(f'{nome}esta com {idade} e pela tabela é considerado idoso')
else :
    print (f'{nome} esta com {idade} e pela tabela é considerado cracudo!!!')
