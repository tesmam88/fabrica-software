salario =float(input("digite o salario"))


if salario <=280:
    salario_atual = salario+(salario*0.2)
    print(f"o aumento do salario é de 20% , seu novo salario é de{salario_atual}")

elif salario > 280 and salario <= 700:
        salario_atual = salario+(salario * 0.15)
        print(f"o aumento do salario é de 15%, seu novo salario é de {salario_atual}")

elif salario > 700 and salario<= 1500:
        salario_atual = salario +(salario*0.1)
        print (f"o aumento do salario é de 10%, seu novo salario é de {salario_atual}")
elif salario > 1500 :
    salario_atual = salario + (salario*0.1)
    print(f"o aumento do salario é de 5%, seu novo salario é de {salario_atual}")



