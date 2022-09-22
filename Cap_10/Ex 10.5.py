class Televisao:
    def __init__(self, canal_inicial, min=2, max=14):
        self.ligada = False
        self.canal = canal_inicial
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal -1 >= self.cmin:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal + 1 <= self.cmax:
            self.canal += 1


tv_sala = Televisao(4, 5, 25)
tv_sala.muda_canal_para_cima()
print(tv_sala.canal)
tv_sala.muda_canal_para_baixo()
print(tv_sala.canal)

tv_quarto = Televisao(10, 1, 32)
tv_quarto.muda_canal_para_baixo()
print(tv_quarto.canal)
tv_quarto.muda_canal_para_cima()
tv_quarto.muda_canal_para_cima()
print(tv_quarto.canal)
