class Programa:
    def __init__(self, nome, ano):
        self.ano = ano
        self._nome = nome.title()
        self._likes = 0

        @property
        def likes(self):
            return self._likes

        def dar_like(self):
            self._like += 1

        @property
        def nome(self):
            return self._nome

        @nome.setter
        def nome(self, novo_nome):
            self._nome = novo_nome.title()

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        self.ano = ano
        self._nome = nome.title()
        self.duracao = duracao
        self._likes = 0


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        self.ano = ano
        self._nome = nome.title()
        self.temporadas = temporadas
        self._likes = 0


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duracao: {vingadores.duracao} - Likes: {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}')
