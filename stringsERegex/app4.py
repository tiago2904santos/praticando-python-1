'''João é atendente em uma farmácia e precisa verificar se um cliente 
forneceu um número de receita válido em uma descrição. O número da 
receita é sempre o único número presente no texto fornecido pelo cliente. 
Ele quer um programa que extraia esse número diretamente e confirme se o 
texto está correto, sem a necessidade de trabalhar com listas ou loops.

Com base nesse cenário, crie um programa que receba um texto com uma 
descrição e exiba uma mensagem com o número encontrado.

Exemplo de Entrada:

Digite a descrição da receita: A receita 1087568 foi enviada pelo cliente.

Saída esperada:

O número da receita é: 1087568'''

import re

# receita = input("Digite a descrição da receita: ")
# numero_da_receita = re.search(r"\d+",receita)

# if numero_da_receita:
#     print(f"O número da receita é: {numero_da_receita.group()}")
# else: 
#     print("Nenhum número encontrado na receita.")

receita = input("Digite a descrição da receita: ")
numero_da_receita = re.findall(r"\d+",receita) [0]

print(f"O número da receita é: {numero_da_receita}")