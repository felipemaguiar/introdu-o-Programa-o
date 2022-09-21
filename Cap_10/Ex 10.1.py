class Televisao:
    def __init__(self, tamanho, marca):
        self.__tamanho = tamanho
        self.__marca = marca

    def tv(self):
        return f'Marca: {self.__marca} e Tamanho: {self.__tamanho}'


tv1 = Televisao("32'", 'LG')
tv2 = Televisao("50'", "samsung")
print(tv1.tv())
print(tv2.tv())

# Podemos resolver de outra maneira - tornando a marca e o tamanho público


class Televisao2:
    def __init__(self, tamanho, marca):
        self.tamanho = tamanho
        self.marca = marca


tv1 = Televisao2("32'", 'LG')
tv2 = Televisao2("50'", "samsung")
print(f'Marca {tv1.marca} e Tamanho: {tv1.tamanho}')
print(f'Marca {tv2.marca} e Tamanho: {tv2.tamanho}')
