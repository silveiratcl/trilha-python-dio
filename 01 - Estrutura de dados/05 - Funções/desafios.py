# Desafio 1

C = int(input())


for i in range(C):

    N = int(input())


    if N <= 8000:
        print('Inseto!')
    else:
        print('Mais de 8000!')



# desafio 2

T = int(input())

for i in range(T):
    linha: str = input() # faz a string do input
    linha_split: list = linha.split(' ') # cria a lista fazendo o split separando por espaço
    garrafas_compradas: int = int(linha_split[0]) # cria a variável selecionando pelo indice
    garrafas_vazias: int = int(linha_split[1]) # idem
    diference: int = int(garrafas_compradas % garrafas_vazias) # divisão inteira  relação de compradas e ganhadas na troca
    result: int = int((garrafas_compradas / garrafas_vazias) + diference)



 print(result)


 a = input()
b = input()
c = input()


if a == 'vertebrado':
    if b == 'ave':
        if c == 'carnivoro':
            print('aguia')
        elif c == 'onivoro':
            print('pomba')
    elif b== 'mamifero':
        if c == 'onivoro':
            print('homem')
        elif c == 'herbivoro':
            print('vaca')

elif a == 'invertebrado':
    if b == 'inseto':
        if c == 'hematofago':
            print('pulga')
        elif c == 'herbivoro':
            print('lagarta')

    elif b == 'anelideo':
        if c == 'hematofago':
            print('sanguessuga')
        elif c == 'onivoro':
            print('minhoca')


