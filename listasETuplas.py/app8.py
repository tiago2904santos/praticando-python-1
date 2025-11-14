'''Uma escola está organizando os dados dos alunos para criar 
um relatório resumido. Cada aluno tem seus dados registrados 
em uma única entrada, incluindo nome, idade e nota final no 
semestre. Esses dados devem ser exibidos separadamente para 
cada aluno no formato abaixo:

Aluno: Nome
Idade: Idade
Nota: Nota

Ajude a escola a desenvolver um programa que registre as 
informações dos alunos, organize os dados e exiba um 
relatório detalhado com as informações separadamente.

Exemplo de Entrada:

Digite os dados do aluno no formato Nome, Idade, Nota 
separados por vírgula: João, 16, 8.5, 
Maria, 17, 9.2, Pedro, 15, 7.8'''

lista_de_alunos = []
dados = input("Digite os dados do aluno no formato Nome, Idade, Nota separados por vírgula: ").split(", ")
aluno = [
    dados[0],
    int(dados[1]),
    float(dados[2])
]
lista_de_alunos.append(aluno)
for aluno in lista_de_alunos:
    
    print(lista_de_alunos)