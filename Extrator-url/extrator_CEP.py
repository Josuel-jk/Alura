import re

endereco = "Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

# 5 dígitos + hífen(opcional) + 3 digitos

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
busca = padrao.search(endereco) # Match
if busca:
    cep = busca.group()
    print(cep)