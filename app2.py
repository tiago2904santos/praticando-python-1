'''

Ana está desenvolvendo um programa que precisa processar 
uma lista de 5 nomes de clientes para gerar relatórios mensais. 
Para isso, ela precisa escrever um programa que percorra 
a lista de nomes e exiba cada cliente.

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]
Copiar código
Ajude Ana a decidir entre usar um laço for ou while. 
Escreva o programa usando o laço que você acredita ser mais adequado
para essa tarefa e explique por que escolheu esse laço.

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)

'''

'''

André está testando um novo recurso no backend do Buscante 
que processa dados em um loop. Durante os testes, ele percebeu 
que o sistema parou de responder, e suspeita que o 
problema está em um loop infinito.


contador = 0

while contador < 10:
    print("Processando dados...")
    contador += 1

'''

'''

Marcos está desenvolvendo um programa para exibir uma mensagem 
de boas-vindas repetidamente no console, como parte de uma campanha 
de marketing de sua plataforma chamada Buscante. Ele quer garantir 
que a mensagem seja exibida 5 vezes.

Ajude Marcos a escrever um programa que exiba a mensagem: 
"Bem-vindo ao Buscante!" o número exato de vezes que ele precisa.

for i in range(5):
    print("Bem-vindo ao Buscante!")

# contador = 0
# while contador < 5:
#    print("Bem-vindo ao Buscante!")

'''

'''
Você está recebendo uma lista de valores representando os produtos 
de sua loja virtual e gostaria de calcular a soma total desses 
produtos para entender o desempenho financeiro semanal.

valores = [10, 20, 30, 40, 50]


valores = [10, 20, 30, 40, 50]

soma = 0 
for valor in valores:
    soma += valor
    print(f"Soma total dos produtos: R$ {soma}")    

'''



'''
Ana está desenvolvendo seu portfólio para exibir os projetos de Python que concluiu. 
Ela organizou uma lista com o nome de cada projeto, mas percebeu que alguns 
itens podem estar ausentes, aparecendo como None:

projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

Crie um programa que ajude Ana a percorrer a lista de projetos e exiba os nomes dos projetos válidos. 
Se encontrar um item None, o programa deve exibir a mensagem: "Projeto ausente".


projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]

for projeto in projetos:
    if projeto is None:
        print("Projeto ausente")
    else:
        print(projeto)

        
'''

'''

José está desenvolvendo uma funcionalidade no sistema do Buscante 
para interromper a busca assim que um livro específico é encontrado. 
A lista de livros já cadastrados no sistema é a seguinte:

livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

Ajude José a criar um programa que percorra a lista e exiba a mensagem 
"Livro encontrado: <nome do livro>" assim que o livro "O Hobbit" for encontrado. 
Após encontrar o livro, o programa deve parar imediatamente a busca,
sem verificar os livros restantes.


livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

for livro in livros:
    if livro == "O Hobbit":
        print(f"livro encontado: {livro}\n")
    break
    
    
'''


'''

Você está desenvolvendo um sistema de controle de estoque para o Buscante. 
Um dos requisitos é verificar a quantidade de exemplares de um livro em 
estoque e continuar vendendo até que o estoque se esgote. Sempre que uma 
venda é realizada, o sistema deve informar o usuário e atualizar a 
quantidade disponível.

Crie um programa que simule as vendas de um livro com o estoque inicial 
de 5 exemplares. O programa deve exibir a mensagem "Venda realizada!
Estoque restante: <quantidade>" a cada venda e, ao final, exibir a 
mensagem "Estoque esgotado".


livros_em_estoque = 5

while livros_em_estoque > 0:
    livros_em_estoque -= 1
    print(f"Venda realizada! Estoque restante: {livros_em_estoque}")

print("Estoque esgotado.") 


'''


'''

Aline está implementando uma funcionalidade que exibe mensagens personalizadas 
para os clientes durante uma promoção especial da sua nova loja de livros. 
O sistema deve exibir uma mensagem de contagem regressiva personalizada para 
cada número de 10 até 1, e ao final exibir a mensagem: "Aproveite a promoção agora!".

Crie um programa que utilize um laço for para exibir as seguintes mensagens:

Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".

segundos = 10

while segundos > 0:
    if segundos % 2 == 0:
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua: {segundos} segundos restantes.")
    segundos -=1

print("Aproveite a promoção agora!")


    # ou


print("Aproveite a promoção agora!")
for segundos in range(10, 0, -1):
    if segundos % 2 == 0:
        print(f"Faltam apenas {segundos} segundos - Não perca essa oportunidade!")
    else:
        print(f"A contagem continua: {segundos} segundos restantes.")
    segundos -=1

print("Aproveite a promoção agora!")

'''



'''

Ana está implementando um sistema de filtragem de livros no Buscante. 
A funcionalidade deve percorrer uma lista de livros e exibir o nome 
de cada livro disponível em estoque. No entanto, se o livro estiver 
esgotado, ele deve ser ignorado durante a iteração.

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

Crie um programa que ajude Ana a exibir somente os livros que 
possuem estoque disponível, no formato: "Livro disponível: ".

livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

for livro in livros:
    if livro["estoque"] == 0:
        continue

    print(f"Livro disponivel: {livro["nome"]}")


'''



'''

João está desenvolvendo um sistema de cadastro para um site de leitura. 
Ele precisa garantir que os usuários insiram um nome de usuário e 
uma senha válidos. As regras são as seguintes:

O nome de usuário deve ter pelo menos 5 caracteres.
A senha deve ter pelo menos 8 caracteres.
João quer que o sistema continue solicitando as informações até que ambas 
as condições sejam atendidas. Quando o usuário insere dados válidos, 
o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

Crie um programa que implemente essa lógica usando um laço while.

'''

while True:
    usuario = input("Digite o nome de Usuario: ")
    senha = input("Digite a senha: ")

    if len(usuario) < 5:
        print("O nome de usuário deve ter pelo menos 5 caracteres.")
        continue
        

    if len(senha) < 8:
            
        print("A senha deve ter pelo menos 8 caracteres.")
        continue

    print("Cadastro realizado com sucesso!")
    break
    
