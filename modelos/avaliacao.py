class Avaliacao:
    def avaliar(self, nome, avaliacao):
        if 0<avaliacao<=5:
            self._nome = nome
            self._avaliacao=avaliacao