class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)

conta_do_ze = ContaCorrente(15)
conta_do_ze.deposita(500)
print(conta_do_ze)

conta_da_chica = ContaCorrente(47685)
conta_da_chica.deposita(1000)
print(conta_da_chica)

contas = [conta_do_ze, conta_da_chica]
for conta in contas:
    print(conta)