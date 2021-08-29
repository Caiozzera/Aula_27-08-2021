class UnidadeFederativa:
    def __init__(self):
        self.nome = ''
        self.sigla = ''

    def get_uf(self, sigla):
        teste=0

    def main(self, estados):
        estadoSelecionado = str(input("Informe uma sigla "))





    # vamos criar uma função de 'busca'
    def encontrar(elemento):

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
                       ["Distrito Federal - DS"]]

        pos_i = 0 # variável provisória de índice
        pos_j = 0 # idem

        for i in range (len(lista)): # procurar em todas as listas internas
            for j in range (i): # procurar em todos os elementos nessa lista
                if elemento in lista[i][j]: # se encontrarmos elemento ('ana')
                    pos_i = i # guardamos o índice i
                    pos_j = j # e o índice j
                    break # saímos do loop interno
                break # e do externo
        return (pos_i, pos_j) # e retornamos os índices


    r = encontrar('SC')  # chamamos a função e salvamos em r
    print(r) # imprime índices
    #print(lista[r[0]][r[1]])

UnidadeFederativa().encontrar()
