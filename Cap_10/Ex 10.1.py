class Televisao:
    def __init__(self, tamanho, marca):
        self.tamanho = tamanho
        self.marca = marca

    def tv(self):
        return f'Marca: {self.__marca} e Tamanho: {self.__tamanho}'


tv1 = Televisao("32'", 'LG')
tv2 = Televisao("50'", "samsung")
print(tv1.tv())
print(tv2.tv())
