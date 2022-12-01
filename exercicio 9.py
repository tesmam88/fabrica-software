nome=input("digite o nome do aluno")
disciplina= input("digite o nome da disciplina")
nota=float(input("digite a primeira nota"))
nota2=float(input("digite a segunda nota"))
nota3=float(input("digite a terceira nota"))

media=(nota+nota2+nota3)/3
if(media>6):
    print(f"as notas foram: {nota},{nota2} e {nota3} media do f aluno{nome} foi{media:.1f},foi o suficiente para passar")

else:
    print(f"as notas foram: {nota},{nota2},{nota3} media do " f"aluno {nome} foi {media:.1f}, NAO foi suficiente para passar")
