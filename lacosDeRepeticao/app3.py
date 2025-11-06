'''Você está recebendo uma lista de valores representando os produtos 
de sua loja virtual e gostaria de calcular a soma total desses 
produtos para entender o desempenho financeiro semanal.

valores = [10, 20, 30, 40, 50]

Crie um programa para implementar a soma.'''

numeros = [10, 20, 30, 40, 50]

soma = 0
for numero in numeros:
    soma += numero

print(f"A soma total das receitas é: {soma}")