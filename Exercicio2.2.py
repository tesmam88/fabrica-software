# DESENVOLVA  O  DIAGRAMA  DE  CLASSES  EIMPLEMENTA EM PYTHON, O SEGUINTE CASO:UMA CLASSE TERÁ UM ATRIBUTO "RAIO" E DOISMÉTODOS:  UM  PARA  CALCULAR  A  ÁREA  DOCÍRCULO  E  OUTRO  
# PARA  CALCULAR  OPERÍMETRO ( CRIAR NO MÍNIMO DOIS OBJETOS).


class calculando():
    def __init__(self):
        self.raio=float(input("Digite o raio: "))
        self.pi=3.14

    def calculoarea(self):
        area=self.pi*self.raio*self.raio
        print("O valor da area é: ",area)

    def calculoperimetro(self):
        perimetro=2*self.pi*self.raio
        print("O valor do perimetro é: ",perimetro)

calculo=calculando()

calculo.calculoarea()
calculo.calculoperimetro()

