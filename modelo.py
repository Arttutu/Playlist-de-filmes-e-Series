class programa:
    def __init__(self, nome, ano):  # função incial da classe
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome_novo):
        self._nome = nome_novo.title()

    def dar_likes(self):
        self._likes += 1

    def __str__(self):  # função representação textual do objeto
        return (f'{self._nome} - {self.ano} - {self._likes} Likes')


class Filme(programa):  # herança da classe mãe
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):  # função representação textual do objeto
        return f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} Likes'


class Serie(programa):  # herança da classe mãe

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):  # função representação textual do objeto
        return f'{self._nome} - {self.ano} - {self.temporadas} temp - {self._likes} Likes'


class playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._Programas = programas

    def __getitem__(self, item):  # deixa interável, se comprta como uma lista mais não é uma lista
        return self._Programas[item]

    def __len__(self):
        return len(self._Programas)




# criando objetos
Game_of_Thrones = Serie("game of thrones", 2012, 8)
vingadores = Filme("ultimato - guerra infinita", 2012, 160)
de_repente_trinta = Filme("De repende 30", 2002, 160)
lupan = Serie("Lupan", 2021, 2)
la_casa_de_papel = Serie("La casa de papel", 2021, 5)
nao_olhe_para_cima = Filme("não olhe para cima", 2022, 120)

Game_of_Thrones.dar_likes()
de_repente_trinta.dar_likes()
lupan.dar_likes()
la_casa_de_papel.dar_likes()
lupan.dar_likes()
Game_of_Thrones.dar_likes()
vingadores.dar_likes()

series = [Game_of_Thrones, lupan, la_casa_de_papel]

filmes = [de_repente_trinta, vingadores, nao_olhe_para_cima]

Playlist = playlist("Series_fim_de_semana", series)
Playlist2 = playlist("Filmes_semana", filmes)

print(f'tamanho da playlist {len(Playlist)}')
print(vingadores in Playlist)

for programa in Playlist:
    print(programa)
