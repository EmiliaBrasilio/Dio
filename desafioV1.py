from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    #métodos da classe
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, dt_nasc, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.dt_nasc = dt_nasc
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
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
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n --> Operação inválida! Sem saldo suficiente!")
        elif valor > 0:
            self.saldo -= valor
            print("\n --> Saque realizado com sucesso!!")
            return True
        else: 
            print("Operação inválida. Valor inválido!!!")
        
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print("\n Depósito realizado com sucesso!!")
        else:
            print("Operacão inválida. Valor informado inválido!")
            return False
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.
             transacoes if transacao["tipo"]== Saque.__name__] )
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Saque excede o limite")
        elif excedeu_saques:
            print("Excede numero de saques")
        else:
            return super().sacar(valor)

        return False
        
    def __str__(self):
        return "Agencia: {self.agencia}\n C/C: {self.numero}\nTitular:{self.cliente.nome}"

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            
        })

class Transacao(ABC):
    pass

class Saque(Transacao):
    pass

class Deposito(Transacao):
    pass
























