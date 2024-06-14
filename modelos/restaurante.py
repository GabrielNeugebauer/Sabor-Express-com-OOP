from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes=[]
    
    def __init__(self,nome,categoria):
        self._nome=nome.title()
        self._categoria=categoria.title()
        self._ativo=False
        self._avaliacao=[]
        Restaurante.restaurantes.append(self)
    
    def __str__(self):
        return f'{self._nome} | {self._categoria} | {self.ativo}'
    @classmethod
    def listar_restaurantes(cls):
        if len(Restaurante.restaurantes) == 0:
            print("Sem restaurantes cadastrados.")
        else:
            print(f'{'Nome do restaurante: '.ljust(20)}| {'Categoria: '.ljust(20)} | {"Avaliação: ".ljust(20)}| Status:')
            for restaurante in cls.restaurantes:
                print(f'{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.calcular_media).ljust(20)}| {restaurante.ativo}')
        
    def verifica_contido(nome_restaurante):
        for restaurante in Restaurante.restaurantes:
            if nome_restaurante.title() == restaurante._nome:
                return True
        return False


    def alterar_situacao_restaurante(nome_restaurante):
        restaurante_encontrado=False
        for restaurante in Restaurante.restaurantes:
            if restaurante._nome == nome_restaurante.title():
                restaurante._ativo=not restaurante._ativo
                restaurante_encontrado=True
                print(f'{restaurante._nome} {"Ativado" if restaurante._ativo == True else "Desativado"}\n')
                break
        if not restaurante_encontrado:
            print("O restaurante não foi encontrado. ")
        
    def receber_avaliacao(self, cliente, nota):
        self._avaliacao.append(Avaliacao.avaliar(cliente,nota))
        
    @property
    def ativo(self):
        return 'Ativo✅' if self._ativo else 'Inativo❌'
    
    @property
    def calcular_media(self):
        
        if not self._avaliacao:
            return ""
        
        total_avaliacoes=sum(avaliacao._nota for avaliacao in self._avaliacao)
        media=round(total_avaliacoes/len(self._avaliacao), 1)
        return media