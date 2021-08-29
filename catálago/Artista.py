class Artista:

    def __init__(self):
        self.__nome_artista = ''
        self.__músicas = ''

    def get_nome_artista(self, nome_artista):
        return self.__nome_artista

    def set_nome_artista(self, nome_artista):
        self.__nome_artista = nome_artista

    def get_músicas(self, músicas):
        return self.__músicas

    def _set_(self, músicas):
        self.músicas = músicas

    def cadastrar(self, artista, músicas):
        self.nome_artista = artista
        self.músicas = músicas

    def exclir_artista(self):
        self.nome_artista
        self.músicas

   
