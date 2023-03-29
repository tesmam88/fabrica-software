class pessoa():
    def __init__(self):
        self.nome=input("Digite o nome: ")
        self.idade=int(input("Digite a idade: "))
        self.altura=float(input("Digite a altura: "))

    def exibir(self):
        print(self.nome, self.idade, self.altura)

    


    
    
pessoa1 = pessoa()

pessoa1.exibir()
     