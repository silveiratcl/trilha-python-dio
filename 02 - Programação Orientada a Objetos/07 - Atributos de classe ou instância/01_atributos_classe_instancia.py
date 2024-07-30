class Estudante:
    escola = "DIO"

    def __init__(self, nome, matricula): #self é instância
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 13234)
aluno_2 = Estudante("Giovanna", 22323)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_3 = Estudante("Chappie", 346545)
aluno_4 = Estudante("Roberta",454545)
mostrar_valores(aluno_1, aluno_2, aluno_3, aluno_4)

