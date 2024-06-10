print('Olá, bem-vindo ao sistema bancário! Para realizar um depósito, digite d, para fazer um saque, digite s, digite '
      'e para extrato ou q para sair!')

menu = ''

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        deposito = float(input('Digite o valor que você gostaria de depositar: '))
        if deposito > 0:
            saldo = saldo + deposito
            extrato = extrato + f'Depósito: R$ {deposito:.2f}\n'
            print(f'Valor depositado com sucesso, seu novo saldo é de R$ {saldo:.2f}!')

        else:
            print('Você tentou depositar um valor inválido, tente novamente mais tarde!')


    elif opcao == 's':
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



    elif opcao == 'e':
        print('================= EXTRATO =================')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('==================================')

    elif opcao == 'q':
        break

    else:
        print('Você digitou uma opção inválida, digite d para depósito, s para saque, e para extrato ou q para sair!')