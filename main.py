import random

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
          'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
          'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
          'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+'] 


print("Bem-Vindo ao Gerador de Senhas!")
nr_letras = int(input("Quantas letras você gostaria de ter na sua senha?\n"))
nr_numeros = int(input("Quantos números você gostaria de ter na sua senha?\n"))
nr_simbolos = int(input("Quantos símbolos você gostaria de ter na sua senha?\n")) 

letra_str = ''  
numero_str = ''  
simbolo_str = ''

for letra in range(1, nr_letras + 1):
  letra = random.choice(letras)
  letra_str = letra 
for numero in range(1, nr_numeros + 1): 
  numero = random.choice(numeros)
  numero_str = numero
for simbolo in range(1, nr_simbolos + 1):
  simbolo = random.choice(simbolos) 
  simbolo_str = simbolo
  
print(f"\nSua senha é: {letra_str}{numero_str}{simbolo_str}")