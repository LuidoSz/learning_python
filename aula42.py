
def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

numeros = soma(1, 2, 3, 4, 5)

soma_1_2_3 = soma(1, 2, 3)
# print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
# print(soma_4_5_6)

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
# print(*numeros)
print(type(None))