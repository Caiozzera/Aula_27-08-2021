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
            print("----------------MENU-------------------")
            print("01 - Cadastrar Artista                 |")
            print("02 - Excluir Artista                   |")
            print("03 - Cadastrar Gênero                  |")
            print("04 - Excluir Gênero                    |")
            print("05 - Cadastrar Disco                   |")
            print("06 - Excluir Disco                     |")
            print("07 - Listar os Discos de uma categoria |")
            print("08 - Listar os Discos de um artista    |")
            print("09 - Listar Artistas                   |")
            print("10 - Listar Gêneros                    |")
            print("11 - Listar Discos                     |")
            print("99 - Sair do menu                      |")
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
                        print("Excluído artista " + i.nome + " com sucesso")
                        artistaInformado = i.nome
                        for idiscos in self.discos:
                            if (idiscos.artista == artistaInformado):
                                print("Excluíndo discos de " + artistaInformado)
                                self.discos.remove(idiscos)
                                print("Excluído com sucesso os discos de " + artistaInformado)
                            print("Discos associado a este artista não foi mais encontrado.")
                    print("Não foi mais encontrado este artista cadastrado! ")


            elif(menu == "3"):
                generoInformado = input("Informe o gênero: ")
                generoCriado = Genero()
                generoCriado.genero = generoInformado
                self.generos.append(generoCriado)
                print("Gênero cadastrado com sucesso!!!")

            elif(menu == "4"):
                genero = input("Qual Gênero deseja excluir?")
                for i in self.generos:
                    if(i.genero == genero):
                        print("Excluíndo " + i.genero)
                        self.generos.remove(i)
                        print("Excluído Gênero " + i.genero + " com sucesso")
                        for discosinformado in self.discos:
                            if(discosinformado.genero == genero):
                                print("Excluindo os discos do Gênero " + discosinformado.genero)
                                self.discos.remove(discosinformado)
                                print("Discos do Gênero " + discosinformado.genero + " Excluído com sucesso!")
                            else:
                                print("Discos associado a este genero não foi mais encontrado.")
                    print("Não foi mais encontrado este Gênero cadastrado! ")

            elif(menu == "5"):
                discoID = input("Informe o ID: ")
                discoNome = input("Informe o nome do Disco: ")
                discoArtista =  input("Informe o nome do artista: ")
                discoAno = input("Informe o Ano: ")
                discoGenero = input("Informe o genero: ")
                discoCriado = Genero()
                discoCriado.id = discoID
                discoCriado.nome = discoNome
                discoCriado.artista = discoArtista
                discoCriado.ano = discoAno
                discoCriado.genero = discoGenero
                self.discos.append(discoCriado)
                print("Disco incluído com sucesso!!!")

            elif(menu == "6"):
                id = input("Qual ID de Disco deseja excluir?")
                for i in self.discos:
                    if(i.id == id):
                        print("Excluíndo " + i.genero)
                        self.discos.remove(i)
                        print("Excluído com sucesso")

            elif (menu == "7"):
                categoria = input("Qual categoria deseja visualizar? ")
                for i in self.generos:
                    if(i.genero == categoria):
                        for disco_atual in self.discos:
                            if(disco_atual.genero == categoria):
                                print("-- Discos da categoria " + categoria + " --")
                                print("Id: " + disco_atual.id)
                                print("Disco: " + disco_atual.nome)
                                print("Artista: " + disco_atual.artista)
                                print("Ano: " + disco_atual.ano)
                                print("Gênero: " + disco_atual.genero)
                                print("---------------------")

            elif (menu == "8"):
                artistaInformado = input("Qual Artista deseja visualizar? ")
                for i in self.artistas:
                    if(i.nome == artistaInformado):
                        for artista_atual in self.discos:
                            if(artista_atual.artista == artistaInformado):
                                print("-- Discos do artista " + artistaInformado + " --")
                                print("Id: " + artista_atual.id)
                                print("Disco: " + artista_atual.nome)
                                print("Artista: " + artista_atual.artista)
                                print("Ano: " + artista_atual.ano)
                                print("Gênero: " + artista_atual.genero)
                                print("---------------------")

            elif(menu == "9"):
                 for i in self.artistas:
                    print("-----------")
                    print("Artista: " + i.nome)
                    print("CPF: " + i.cpf)

            elif(menu == "10"):
                 for i in self.generos:
                    print("-----------")
                    print("Gênero: " + str(i.genero))

            elif(menu == "11"):
                 for i in self.discos:
                    print("-----------")
                    print("Disco: " + str(i.nome))
                    print("Id: " + str(i.id))
                    print("Gênero: " + str(i.genero))

Main().v_principal()
