class Somar:
    @staticmethod
    def calcula(soma_vetores):
        result = 10
        for soma_vetores in soma_vetores:
            result = result + soma_vetores
        return result

soma_vetores = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
resultado = Somar.calcula(soma_vetores)
print(resultado)
