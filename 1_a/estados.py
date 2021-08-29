class UnidadeFederativa:
    def __init__(self):
        self.nome = ''
        self.sigla = ''

    def main(self):
        estadoSelecionado = str(input("Informe uma sigla "))

        lista = [["Acre","AC"],
                       ["Alagoas", "AL"],
                       ["Amapá", "AP"],
                       ["Amazonas", "AM"],
                       ["Bahia", "BA"],
                       ["Ceará", "CE"],
                       ["Espiro Santo", "ES"],
                       ["Goias", "GO"],
                       ["Maranhão", "MA"],
                       ["Mato Grosso", "MT"] ,
                       ["Mato Grosso do Sul", "MS"],
                       ["Minas Gerais", "MG"],
                       ["Pará", "PA"],
                       ["Paraíba", "PB"],
                       ["Paraná", "PR"],
                       ["Pernambuco", "PE"],
                       ["Piauí", "PI"],
                       ["Rio de Janeiro", "RJ"],
                       ["Rio grande do Norte", "RN"],
                       ["Rio Grande do Sul", "RS"],
                       ["Rondônio", "RO"],
                       ["Roraima", "RR"],
                       ["Santa Catarina", "SC"],
                       ["São Paulo", "SP"],
                       ["Sergipe", "SE"],
                       ["Tocantins", "TO"],
                       ["Distrito Federal", "DF"]]

        for i in lista:
            if(estadoSelecionado == i[1]):
                print("O estado e sigla digitado é: " + str(i))

UnidadeFederativa().main()
