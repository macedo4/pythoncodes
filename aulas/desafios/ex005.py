print("Antecessor e Sucessor")
try:
    numero = int(input("Digite um número: "))
    antecessor = numero - 1
    sucessor = numero + 1
    print(f"O antecessor de {numero} é {antecessor} e o sucessor de {numero} é {sucessor}")
except ValueError:
    print(("DIgite um número válido"))
