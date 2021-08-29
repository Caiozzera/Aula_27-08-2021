class Discos:

    def __init__(self):
        self.__nome = ''
        self.__artista = ''
        self.__ano = ''
        self.__gênero = ''

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_artista(self):
        return self.__artista

    def set_artista(self, artista):
        self.__artista = artista

    def get_ano(self):
        return self.__ano

    def set_ano(self, ano):
        self.__ano = ano

    def get_gênero(self):
        return self.__gênero

    def set_cpf(self, gênero):
        self.__gênero = gênero
