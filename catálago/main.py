class Main:
    def __init__(self):
        self.artista = Artista()


    def mostrar_menu(self):
        print('CATALOGO')
        print('Selecione uma opção:')
        print('1. Cadastrar Artista')
        print('2. Exclir artista e discos associados')
        print('3. Cadastrar Gênero')
        print('4. Excluir Gênero e discos associados')
        print('5. Cadastrar Disco')
        print('6. Excluir Disco')
        print('7. Listar todos os discos')
        print('8. Listar os discos de uma categoria')
        print('0. Listar os discos de um artista')

