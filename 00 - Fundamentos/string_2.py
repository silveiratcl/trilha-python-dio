nome = "Guilherme"
idade = 28
profissao = "Programador"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Guilherme", "idade": 28}

# old style
print("Nome: %s Idade: %d" % (nome, idade))

# old style 2
print("Nome: {} Idade: {}".format(nome, idade))

print("Nome: {1} Idade: {0}".format(idade, nome))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(idade, nome))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

# modern mode
print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}") # .2 duas casas de precisão
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.1f}") # 10 - 10 espaços em branco e .1 de precisão
