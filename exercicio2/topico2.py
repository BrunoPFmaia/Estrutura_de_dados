class Livro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def detalhes(self):
        print(f'Livro: {self.titulo}, autor: {self.autor}')

livro1 = Livro('As aventuras de pi', 'Yann Martel')
livro1.detalhes()