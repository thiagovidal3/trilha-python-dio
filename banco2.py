print('Olá, bem-vindo ao sistema bancário! Para realizar um depósito, digite d, para fazer um saque, digite s, digite '
      'e para extrato, c para criar um novo usuário, c para criar uma nova conta ou q para sair!')


menu = ''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
AGENCIA = '0001'
LIMITE_SAQUES = 3
lista_usuarios = []
lista_contas = []
nome = ''
data_nascimento = ''
cpf = ''
endereco = ''
usuario = ''
numero_conta = 0

def adicionar_usuario():
    global usuario
    cpf = input('Por favor, digite o seu cpf: ')
    for usuario in lista_usuarios:
        if usuario['cpf'] == cpf:
            print('Esse cpf já possui um cadastro em nosso sistema.')
            return
    nome = input('Por favor, digite o seu nome: ')
    data_nascimento = input('Por favor, digite a sua data de nascimento: ')
    endereco = input('Por favor, digite o seu endereço: ')
    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    lista_usuarios.append(usuario)
    print('Cadastro efetuado com sucesso!')

def adicionar_contas():
    cpf = input('Digite seu cpf: ')
    for user in lista_usuarios:
        if user['cpf'] == cpf:
            global numero_conta
            numero_conta += 1
            conta = {
                "Agência": AGENCIA,
                "Número da conta": numero_conta,
                "Usuário": user['nome']
            }
            lista_contas.append(conta)
            print('Conta cadastrada com sucesso para o usuário:', user['nome'])
            print(lista_contas)
            return

    print('Usuário com CPF', cpf, 'não encontrado.')


def deposito():
    global saldo
    global extrato
    deposito = float(input('Digite o valor que você gostaria de depositar: '))
    if deposito > 0:
        saldo = saldo + deposito
        extrato = extrato + f'Depósito: R$ {deposito:.2f}\n'
        print(f'Valor depositado com sucesso, seu novo saldo é de R$ {saldo:.2f}!')

    else:
        print('Você tentou depositar um valor inválido, tente novamente mais tarde!')

def saque():
    global saldo
    global extrato
    global numero_saques
    if numero_saques < LIMITE_SAQUES:
        saque = float(input('Digite o valor do saque: '))
        if saldo >= saque:
            if saque > 0 and saque <= 500:

                    print(f'Você fez um saque no valor de {saque:.2f} reais com sucesso!')
                    saldo = saldo - saque
                    extrato = extrato + f'Saque: R$ {saque:.2f}\n'
                    numero_saques = numero_saques + 1
                    print(f'Seu saldo atual é de R${saldo:.2f}!')

            else:
                    print('O valor que você escolheu é inválido ou ultrapassou o limite de 500 reais.')

        else:
                print('Você não tem o valor disponível na conta para realizar esse saque.')

    else:
            print('Você atingiu o número máximo de saques diários que é 3, tente novamente amanhã!')


def historico():
    global saldo
    global extrato
    print('================= EXTRATO =================')
    print('Não foram realizadas movimentações.' if not extrato else extrato)
    print(f'Saldo: R$ {saldo:.2f}')
    print('==================================')



while True:

    opcao = input(menu)
    if opcao == 'd':
        deposito()
    elif opcao == 's':
        saque()
    elif opcao == 'e':
        historico()
    elif opcao == 'q':
        print('Você encerrou sua sessão com sucesso!')
        break
    elif opcao == 'u':
        adicionar_usuario()
    elif opcao == 'c':
        adicionar_contas()

    else:
        print('Opcão inválida!')