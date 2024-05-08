import textwrap
from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime


class Cliente:
    pass


class Cliente:
    def __init__(self, endereco, cidade):
        self.endereco = endereco
        self.cidade = cidade
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    class PessoaFisica(Cliente):
        def __init__(self, nome, data_nascimento, cpf, cidade, endereco):
            super().__init__(cidade)
            self.nome = nome
            self.data_nascimento = data_nascimento
            self.cpf = cpf
            self.endereco = endereco

            class Conta:
                def __init__(self, numero, cliente):
                    self.saldo = 0
                    self.numero = numero
                    self.agencia = "9212"
                    self._cliente = cliente
                    self.historico = Historico()

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
                        saldo(self.saldo)
                        excedeu_saldo = valor > saldo()

                        if excedeu_saldo:
                            print("\n@@@ A operação falhou! Você não tem saldo suficiente. @@@")

                        elif valor > 0:
                            self._saldo -= valor
                            print("\n--- Saque realizado com sucesso! ---")

                            return True
                        else:
                            print("\n@@@ A operação falhou! Saldo insuficiente. @@@")
                            return False

                        def depositar(self, valor):
                            if valor > 0:
                                self._saldo += valor
                                print("\n--- Depósito realizado com sucesso! ---")

                            else:
                                print("\n@@@ A operação falhou! Valor informado inválido.@@@ ")
                                return False

                            return True

                        class ContaCorrente(Conta):
                            def __init__(self, numero, cliente, limite=700, limite_saques=4):
                                super().__init__(numero, cliente)
                                self._limite = limite
                                self._limite_saques = limite_saques

                            def sacar(self, valor):
                                numero_saques = len(
                                    [transacao for transacao in self.historico.transacoes if
                                     transacao["tipo"] == Saque.__name__]
                                )

                                excedeu_limite = valor > self._limite
                                excedeu_saques = numero_saques >= self._limite_saques

                                if excedeu_limite:
                                    print("\n@@@ A operação falhou! O valor do saque excede o limite. @@@")

                                elif excedeu_saques:
                                    print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

                                else:
                                    return super().sacar(valor)
                                return False

                            def __str__(self):
                                return f"""\Agência:\t{self.agencia}
C/C:\t\t{self.numero}
Titular:\t{self.cliente.nome}"""

                            class Hisorico:
                                def __init__(self):
                                    self._transacoes = []

                                    @property
                                    def transacoes(self):
                                        return self._transacoes

                                    def adicionar_transacao(self,transacao):
                                        self._transacoes.append(
                                            {
                                                "tipo": transacao.__class__.__name__,
                                                "valor": transacao.valor,
                                                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
                                            }
                                        )
                                        class Transacao(ABC):
                                            @property
                                            @abstractproperty
                                            def valor(self):
                                                pass
                                            @abstractmethod
                                            def registrar(self,conta):
                                                pass

                                            class Saque(Transacao):
                                                def __init__(self,valor):
                                                    self._valor = valor

                                                    @property
                                                    def valor(self):
                                                        return self._valor
                                                    def registrar(self,conta):
                                                        sucesso_transacao = conta.sacr(self.valor)

                                                        if sucesso_transacao:
                                                            conta.historico.adicionar_transacao(self)




