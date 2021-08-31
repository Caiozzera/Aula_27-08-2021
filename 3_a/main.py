from artista import Artista
from genero import Genero
from catalogo import Catalogo

class Main:

    def v_principal(self):

        self.artistas = []
        self.generos = []
        self.discos = []

        menu = "0"
        while menu != "99":
            print("---------------------------------------")
            print("Cadastrar Artista - 1                 |")
            print("Excluir Artista - 2                   |")
            print("Cadastrar Gênero - 3                  |")
            print("Excluir Gênero - 4                    |")
            print("Cadastrar Disco - 5                   |")
            print("Excluir Disco - 6                     |")
            print("Listar os Discos de uma categoria - 7 |")
            print("Listar os Discos de um artista - 8    |")
            print("Listar Artistas - 9                   |")
            print("Listar Gêneros - 10                   |")
            print("Listar Discos - 11                    |")
            print("Sair do menu - 99                     |")
            print("---------------------------------------")
            menu = input("Escolha uma opção do Menu! ")

            if(menu == "1"):
                artista = input("Digite o nome do artista: ")
                cpf = input("Digite o CPF do artista: ")
                artistaCriado = Artista()
                artistaCriado.nome = artista
                artistaCriado.cpf = cpf
                self.artistas.append(artistaCriado)
                print("Artista cadastrado com sucesso!!!")

            elif(menu == "2"):
                cpf = input("Qual CPF deseja excluir?")
                for i in self.artistas:
                    if(i.cpf == cpf):
                        print("Excluíndo " + i.nome)
                        self.artistas.remove(i)
                        print("Excluído com sucesso")

            elif(menu == "3"):
                generoInformado = input("Informe o gênero: ")
                idInformado =  input("Informe o ID: ")
                generoCriado = Genero()
                generoCriado.genero = generoInformado
                generoCriado.id = idInformado
                self.generos.append(generoCriado)
                print("Artista cadastrado com sucesso!!!")

            elif(menu == "4"):
                id = input("Qual ID de Gênero deseja excluir?")
                for i in self.generos:
                    if(i.id == id):
                        print("Excluíndo " + i.genero)
                        self.artistas.remove(i)
                        print("Excluído com sucesso")

            elif(menu == "5"):
                discoID = input("Informe o ID: ")
                discoNome = input("Informe o nome do Disco: ")
                discoArtista =  input("Informe o nome do artista: ")
                discoAno = input("Informe o Ano: ")
                discoGenero = input("Informe o genero")
                discoCriado = Genero()
                discoCriado.id = discoID
                discoCriado.nome = discoNome
                discoCriado.artista = discoArtista
                discoCriado.ano = discoAno
                discoCriado.genero = discoGenero
                self.discos.append(discoCriado)
                print("Discos incluído com sucesso!!!")

            elif(menu == "6"):
                id = input("Qual ID de Disco deseja excluir?")
                for i in self.discos:
                    if(i.id == id):
                        print("Excluíndo " + i.genero)
                        self.discos.remove(i)
                        print("Excluído com sucesso")


            elif(menu == "9"):
                 for i in self.artistas:
                    print("-----------")
                    print("Artista: " + i.nome)
                    print("CPF: " + i.cpf)

            elif(menu == "10"):
                 for i in self.generos:
                    print("-----------")
                    print("Gênero: " + str(i.genero))
                    print("Id: " + str(i.id))

            elif(menu == "11"):
                 for i in self.discos:
                    print("-----------")
                    print("Disco: " + str(i.nome))
                    print("Id: " + str(i.id))

    def v_cadastrar(self, artista):
        artistaCriado = Artista(artista)
        self.artistas.append(artistaCriado)
        print("Artista cadastrado com sucesso!!!")

Main().v_principal()
