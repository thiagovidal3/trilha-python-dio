from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Transacao(ABC):

    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Deposito:
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self):
        sucesso_transacao = conta.depositar(self._valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Saque:

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self._valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Historico:

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo': transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime
                ('%d-%m-%Y %H: %M:%s'),
            }
        )

class Conta:

    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()


    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self._saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente!')

        elif valor > 0:
            self._saldo -= valor
            print('Saque efetuado com sucesso!')
            return True

        else:
            print('Operação falhou, o valor informado é inválido!')

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('Depósito efetuado com sucesso!')

        else:
            print('O valor informado é inválido, tente novamente mais tarde!')
            return False

        return True


class ContaCorrente(Conta):

    def __init__(self, numero, cliente, limite=500, limite_saques=3):

        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao['tipo'] = Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print('Falha! O valor máximo para saque é de 500 reais!')

        elif excedeu_saques:
            print('Falha! O limite diário de 3 saques já foi atingido!')

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""
            Agência: {self._agencia}
            C/C: {self._numero}
            Titular: {self._cliente.nome}
        """


class Cliente:
    def __init__(self, endereco):
        self._endereco = endereco
        self._contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self._contas.append(conta)


class PessoaFisica(Cliente):

    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._cpf = cpf