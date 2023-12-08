nome = "gUIlherME"

print(nome.upper())
print(nome.lower())
print(nome.title())

texto = "  Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".") # tira espaço
print(texto.rstrip() + ".") # tira espaço direito
print(texto.lstrip() + ".") # tira espaço esquerdo

menu = "Python"

print("####" + menu + "####") # adiciona caracteres
print(menu.center(14)) # centraliza
print(menu.center(14, "#")) # centraliza e prenche com o character
print("-".join(menu)) # une separando por um character
