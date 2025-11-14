'''O clube de atletismo Alura Runners organizou uma corrida e 
divulgou a lista com a classificação final dos participantes. 
Mas, um erro foi identificado: um dos nomes está incorreto. 
O organizador precisa de um programa que permita localizar o 
nome errado e substituí-lo pelo correto.

Como você escreveria um programa que solicite o nome errado, 
o nome correto e atualize a lista exibindo a nova 
classificação ao final?

Exemplo de Entrada:

Digite o nome incorreto: Carlos
Digite o nome correto: João

Saída esperada:

O nome Carlos foi substituído por João.

Lista atualizada: ['Ana', 'João', 'Pedro']'''

lista = ['Ana', 'Carlos', 'Pedro']

nome_errado = input("Digite o nome incorreto: ").title()

if nome_errado in lista:
    nome_certo = input("Digite o nome correto: ").title()
    posicao = lista.index(nome_errado)
    lista.remove(nome_errado)
    lista.insert(posicao, nome_certo)
    print(f"Lista atualizada: {lista}")
else:
    print("Nome nao encontrado!")