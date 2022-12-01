numeroconta = int(input("digite o numero da conta"))
saldo= float(input("digite o saldo da conta"))
debito= float(input("digite o debito da conta"))
credito= float(input("digite o credito da conta"))


saldoatual =(saldo-debito+credito)
if (saldoatual >=0 ):
    print("saldoatual é positivo")
if (saldoatual <=0):
    print("saldoatual é negativo")
