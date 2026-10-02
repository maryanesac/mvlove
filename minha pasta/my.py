number1 = float(input("Digite o primeiro número: "))
number2 = int(input("Digite o segundo número: "))
pergunta = input("sao iguais?")
# Escolha o número maior
if number1 > number2:
    larger_number = number1
elif number1 < number2:
    larger_number = number2
else:
    number1 = number2
    larger_number = ("não tem, são iguais")
 
# Imprimir o resultado
print("O maior número é:", larger_number)
 