# DESENVOLVA  O  DIAGRAMA  DE  CLASSES  E IMPLEMENTA EM PYTHON, O SEGUINTE CASO:UMA   CLASSE   PARA   REPRESENTAR   UMA CALCULADORA  QUE  REALIZA  AS  OPERAÇÕES BÁSICAS 
# (ADIÇÃO, SUBTRAÇÃO, MULTIPLICAÇÃO E DIVISÃO), CRIAR NO MÍNIMO DOIS OBJETOS.


class calculadora():
    def __init__(self):
        self.numero1=int(input("digite um numero: "))
        self.numero2=int(input("digite um numero: "))
        self.operacao=int(input("Informe a operação (1-ADIÇÃO, 2-SUBTRAÇÃO, 3-MULTIPLICAÇÃO, 4-DIVISÃO): "))
                 
       
    def verificar_operacao(self):   
        
        if self.operacao==1:
            print(f"Valor do operação: {self.numero1+self.numero2} ")
        if self.operacao==2:
            print(f"Valor do operação: {self.numero1-self.numero2} ")
        if self.operacao==3:
            print(f"Valor do operação: {self.numero1*self.numero2} ")
        if self.operacao==4:
            if self.numero1!=0 and self.numero2!=0:
                print(f"Valor do operação: {self.numero1/self.numero2} ")
            else:
                print("Operação Invalida!!!")

                   

calculo=calculadora()
calculo.verificar_operacao()








