contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)

carro = {"marca": "Fiat", "modelo": "palio", "placa": "ABD-9826"}
carro.get("motor")


contatos = {"idioma": "pt_br", "pais": "Brasil" }
contatos.get("pais")
contatos["pais"]