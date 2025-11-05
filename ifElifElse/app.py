'''

Bruno gerencia um pequeno comércio e quer saber qual 
produto teve o melhor desempenho de vendas no mês passado.
Ele registrou a quantidade vendida de dois produtos: 
maçãs e bananas. Agora, ele precisa escrever um programa 
que identifique e exiba qual deles teve maior venda.

Crie um programa que receba o número de vendas dos dois
produtos e exiba uma mensagem indicando qual deles vendeu 
mais. Se as quantidades forem iguais, exiba uma mensagem 
dizendo que houve empate.



numero_de_maças = int(input("Digite a quantidade de maçãs vendidas: "))
numero_de_bananas = int(input("Digite a quantidade de bananas vendidas: "))

if numero_de_maças > numero_de_bananas:
    print("As maçãs tiveram mais vendas.")

elif numero_de_bananas == numero_de_maças:
    print("as vendas foram iguais.")
    
else:
    print("As bananas tiveram mais vendas.")

'''


'''

Camila está organizando um projeto e precisa calcular o 
tempo total necessário para concluir três atividades: A, B e C. 
No entanto, se alguma atividade tiver um número de dias negativo, 
o código deve avisar que os valores inseridos são inválidos 
e não calcular o total.

Escreva um programa que receba o número de dias de três atividades 
e exiba o tempo total do projeto. Se algum valor for negativo, 
mostre uma mensagem informando o erro.



atividade_a = int(input("Informe os dias para a atividade A: "))
atividade_b = int(input("Informe os dias para a atividade B: "))
atividade_c = int(input("Informe os dias para a atividade C: "))
soma = atividade_a + atividade_b + atividade_c

if atividade_a < 0 or atividade_b or 0 or atividade_c < 0:
    print("Por favor insira apenas valores positivos.")
else:
    print(f"O tempo total do projeto é de {soma} dias.")

'''


'''

Lucas trabalha em TI e precisa garantir que a temperatura 
de uma sala de servidores não ultrapasse 25°C. Ele quer um 
programa que receba a temperatura atual como entrada e, 
se necessário, exiba uma mensagem de alerta.

temperatura = float(input("Digite a temperatura atual: "))

if temperatura > 25:
    print("Alerta! Temperatura acima do limite permitido.")
else:
    print("Temperatura dentro do limite seguro.")

'''


'''

Anna Júlia está criando um sistema para calcular o Índice 
de Massa Corporal (IMC) e fornecer recomendações básicas. 
O programa deve receber o peso e a altura de uma pessoa e 
exibir o valor do IMC, além de indicar se está abaixo do peso, 
com peso normal ou acima do peso. Crie um programa que receba 
o peso (em kg) e a altura (em metros) e calcule o IMC usando a 
fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC 
e uma mensagem indicando se está abaixo do peso (IMC < 18.5), 
peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).


peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite seu peso em metros: "))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}.\nVocê está abaixo do peso.")

elif 18.5 <= imc < 25:
    print(f"Seu IMC é {imc:.2f}.\nVocê está com peso normal.")

else:
    print(f"Seu IMC é {imc:.2f}.\nVocê está acima do peso.")

'''

'''
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. 
Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de 
um programa que ajude a controlar suas despesas. O programa deve receber o 
total de despesas realizadas e informar se ele ultrapassou o limite 
ou ainda está dentro do orçamento.

limite = 3000.0
despesas = float(input("Digite o total de despesas do mês (R$): "))

if despesas > limite:
    print("Atenção! Você ultrapassou o limite do orçamento.")
else:
    print("Você está dentro do orçamento.")

'''

'''

Mariana é responsável por liberar o acesso ao escritório e precisa 
de um programa que verifique se os funcionários podem entrar. Para isso, 
ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. 
Crie um programa que receba a hora atual como entrada (em formato de 24 horas) 
e exiba uma mensagem informando se o acesso é permitido ou negado.

hora_atual = int(input("Digite a hora atual (formato 24 horas): "))

if 8 <= hora_atual < 18:
    print("Acesso permitido.")
else:
    print("Acesso negado.")

'''


'''

Uma professora precisa de um programa que ajude a calcular a 
média final dos alunos e informe se foram aprovados, ficaram de 
recuperação ou reprovados. As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado

Escreva um programa que receba três notas como entrada e calcule a média final. 
Com base na média, exiba a situação do aluno.


nota_1 = float(input("digite o valor da primeira nota: "))
nota_2 = float(input("digite o valor da segunda nota: "))
nota_3 = float(input("digite o valor da terceira nota: "))

media = (nota_1 + nota_2 + nota_3) / 3

if media >= 7:
    print(f"Média final: {media:.1f}\nAluno aprovado.")

elif 5 <= media < 7:
    print(f"Média final: {media:.1f}\nAluno em recuperação.")

else:
    print(f"Média final: {media:.1f}\nAluno reprovado.")

'''


'''

Fernanda está planejando uma viagem e quer calcular quanto pagará 
de pedágio. O valor do pedágio depende da distância percorrida:

Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00

Crie um programa que receba a distância percorrida e 
informe o valor do pedágio correspondente.

distancia = float(input("Digite a distância percorrida (em km): "))

if distancia <= 100:
    print("Valor do pedágio: R$ 10,00")
elif 100 < distancia <= 200:
    print("Valor do pedágio: R$ 20,00")
else:
    print("Valor do pedágio: R$ 30,00")

'''


'''

Lucas está desenvolvendo um jogo e precisa de uma funcionalidade 
que verifique se um número é par ou ímpar. Essa verificação será 
usada para definir ações diferentes dentro do jogo. Escreva um 
programa que receba um número inteiro e exiba uma mensagem 
informando se ele é par ou ímpar.


numero = int(input("Digite um número inteiro: "))

verificacao = numero % 2

if verificacao == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

'''


''' 

Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

O valor da renda mensal precisa ser maior que R$ 2.000,00.
O valor da parcela não pode ultrapassar 30% da renda.

Crie um programa que receba como entrada a renda mensal de Pedro e o 
valor da parcela desejada. O programa deve informar se o empréstimo 
foi aprovado ou negado com base nas condições acima.

'''

renda_mensal = float(input("Digite sua renda mensal (R$): "))
valor_parcela = float(input("Digite o valor da parcela desejada (R$): "))

if renda_mensal > 2000 and valor_parcela < ((30 * renda_mensal) / 100):
    print("Empréstimo aprovado.")

else:
    if renda_mensal <= 2000:
        print("Empréstimo negado. Renda mensal insuficiente.")
    elif valor_parcela >= ((30 * renda_mensal) / 100):
        print("Empréstimo negado. Valor da parcela excede 30% da renda mensal.")
    else:
        print("Empréstimo negado. Renda mensal insuficiente e valor da parcela excede 30% da renda mensal.")
