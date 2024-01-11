def depositar(saldo, extrato):
    """
    Realiza um depósito na conta.

    Parameters:
    - saldo (float): O saldo atual da conta.
    - extrato (str): O extrato da conta.

    Returns:
    Tuple[float, str]: Uma tupla contendo o novo saldo e o extrato atualizado.

    Raises:
    ValueError: Se o valor do depósito for negativo.

    """

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n================ Depósito realizado com sucesso! ================")
        print("\n========================= Extrato ============================")
        print(extrato)
        print(f"Seu saldo é: R$ {saldo:.2f} ")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(saldo, extrato, numero_saques, limite_saques, limite):
    """
    Realiza saque em conta

    Args:
        saldo (float): saldo
        extrato (str): operacoes realizadas
        numero_saques (int): acumula o numero de saques
        limite_saques (int): limite de saques diário
        limite (float): limite a ser sacado

    Returns:
        str: retorna o output da operacao considerando
        os limite de saque e limite de saldo
        saldo, extrato e numero de saques restantes

    """

    valor = float(input("Informe o valor do saque: "))

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n================ Saque realizado com sucesso! ================")
        print(f"Valor sacado: {valor} ")
        print("\n========================= Extrato ============================")
        print(extrato)
        print(f"Seu saldo é: {saldo} ")
        print(f"numero saques: {numero_saques}")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    """ imprime o extrato

    Args:
        saldo (float): saldo
        extrato (str): extrato
    """

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cria_usuario(lista_clientes):
    """ cria usuario

    Args:
        nome (str): nome
        data_nascimento (str): DD-MM-AAAA
        cpf (str): cpf
        logradouro:
        lista_clientes (_type_):

    Returns:
        usuário (str)
        lista de clientes (list)
    """

    nome = str(input("Informe o nome: "))
    data_nascimento = str(input("Data de nascimento (DD-MM-AAAA): "))
    cpf = str(input("Insira o CPF (somente números): "))

    # Validando cpf se duplicado
    if any(cliente['cpf'] == cpf for cliente in lista_clientes):
        print("CPF já cadastrado")
        cpf = str(input("Insira um CPF diferente (somente números): "))
    else:
        print("CPF válido")

    logradouro = str(input("Logradouro: "))
    bairro = str(input("Bairro: "))
    cidade = str(input("Cidade: "))
    estado = str(input("Estado: "))

    endereco = [logradouro, bairro, cidade, estado]
    cliente = {'nome': nome, 'data_nascimento': data_nascimento, 'cpf': cpf, 'endereco': endereco}
    lista_clientes.append(cliente)

    # chamando cria_conta_corrente
    if any(cliente['cpf'] != cpf for cliente in lista_clientes):
        cria_conta_corrente(AGENCIA, lista_clientes, lista_contas)
    else:
        pass


    print(f"============== Cliente '{nome}' cadastrado com sucesso! =================")

    return cliente, lista_clientes


def exibe_clientes(lista_clientes):
    """ exibe a lista de clientes cadastrados

    Args:
        lista_clientes (list): lista de clientes
    """

    print("\n================ Clientes Cadastrados ================")
    for cliente in lista_clientes:
        print(cliente)
    print("========================================================")


def cria_conta_corrente(agencia, lista_clientes, lista_contas):
    AGENCIA = "0001"

    for index, cliente_conta in enumerate(lista_clientes, start=1):

        nova_conta_corrente = index
        agencia_conta_cpf = {
            "AGENCIA": AGENCIA,
            "conta_corrente": nova_conta_corrente,
            "cpf": cliente_conta["cpf"],
            "nome": cliente_conta["nome"],
        }
        lista_contas.append([agencia_conta_cpf])

    return AGENCIA, nova_conta_corrente, agencia_conta_cpf, lista_contas

def exibe_clientes_conta(lista_contas):
    """
    exibe clientes com a conta corrente

     Args:
        cliente_conta (list): lista de clientes cadastrados
        lista_contas (list): lista de clientes com conta

    """

    print("\n================ Clientes Cadastrados ================")
    for cliente_conta in lista_contas:
        for key, value in cliente_conta[0].items():
            print(f"{key}: {value}")
        print("--------------------------------------------------------")


    print("========================================================")

    return lista_contas, cliente_conta



menu = """

*** CLIENTE MENU ***

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

*** ADMIN MENU ***

[c] Cadastrar Cliente
[l] Listar Clientes
[lc] Listar Contas


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
nome = None
data_nascimento = None
cpf = None
endereco = None
cliente = None
conta_corrente = None
agencia_conta_cpf = None
lista_clientes = []
lista_contas = []
AGENCIA = str("0001")

while True:
    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques, LIMITE_SAQUES, limite)
    elif opcao == "e":
        exibir_extrato(saldo, extrato)
    elif opcao == "c":
        cliente, lista_clientes = cria_usuario(lista_clientes)
    elif opcao == "l":
        cliente = exibe_clientes(lista_clientes)
    elif opcao == "lc":
        cliente, lista_contas = exibe_clientes_conta(lista_contas)
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
