def mostrar_menu():
    print('=== MENU ===')
    print('1 - Ver mensagem')
    print('0 - Sair')
    print('2 - cadastrar produto')

def mostrar_mensagem():
    print('Bem-vindo!')

def cadastrar_produto(produtos):
    nome = input("Nome do produto: ")
    preco = float(input("Preço do produto: "))

    produtos.append(nome, preco)

    print("Produto cadastrado com sucesso!")

mostrar_menu()

opcao = input('Escolha: ')

if opcao == '1':
    mostrar_mensagem()
elif opcao == '2'
    cadastrar_produto()
elif opcao == '0':
        print('Encerrado...')
else:
    print('Opção inválida!')