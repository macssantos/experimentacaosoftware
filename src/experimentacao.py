class Livro:
    def __init__(self, titulo, autor, isbn, preco):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.preco = preco

    def __str__(self):
        return f"{self.titulo} - {self.autor}"

class Livraria:
    def __init__(self):
        self.catalogo = {}

    def adicionar_livro(self, livro, quantidade=1):
        if livro.isbn in self.catalogo:
            self.catalogo[livro.isbn]['quantidade'] += quantidade
        else:
            self.catalogo[livro.isbn] = {'livro': livro, 'quantidade': quantidade}

    def remover_livro(self, isbn, quantidade=1):
        if isbn in self.catalogo:
            self.catalogo[isbn]['quantidade'] -= quantidade
            if self.catalogo[isbn]['quantidade'] <= 0:
                del self.catalogo[isbn]

    def buscar_livro(self, isbn):
        if isbn in self.catalogo:
            return self.catalogo[isbn]['livro']
        else:
            return None

    def listar_livros(self):
        return [livro_info['livro'] for livro_info in self.catalogo.values()]

    def verificar_disponibilidade(self, isbn):
        if isbn in self.catalogo:
            return self.catalogo[isbn]['quantidade']
        else:
            return 0

# Exemplo de Uso
livraria = Livraria()

livro1 = Livro("Python para Iniciantes", "João Silva", "978-3-16-148410-0", 50.0)
livro2 = Livro("Algoritmos e Estruturas de Dados", "Maria Souza", "978-3-16-148411-0", 80.0)

livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2, 3)

print("Lista de Livros:")
for livro in livraria.listar_livros():
    print(livro)

livraria.remover_livro("978-3-16-148411-0", 2)

print("\nLista de Livros após remover alguns:")
for livro in livraria.listar_livros():
    print(livro)
