from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @abstractmethod
    def exibir_informacoes(self):
        pass

class UsuarioComum(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if len(self.livros_emprestados) < 3 and livro.disponivel:
            self.livros_emprestados.append(livro)
            livro.alterar_disponibilidade(False)
            return True
        return False

    def devolver_livro(self, livro):
        if livro in self.livros_emprestados:
            self.livros_emprestados.remove(livro)
            livro.alterar_disponibilidade(True)
            return True
        return False

    def exibir_informacoes(self):
        return f"Usuário: {self.nome}, Matrícula: {self.matricula}, Livros emprestados: {len(self.livros_emprestados)}"

class Administrador(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def cadastrar_livro(self, biblioteca, livro):
        biblioteca.adicionar_livro(livro)

    def cadastrar_usuario(self, biblioteca, usuario):
        biblioteca.adicionar_usuario(usuario)

    def exibir_informacoes(self):
        return f"Administrador: {self.nome}"

class ItemBiblioteca(ABC):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    @abstractmethod
    def exibir_informacoes(self):
        pass

    def alterar_disponibilidade(self, status):
        self.disponivel = status

class Livro(ItemBiblioteca):
    def __init__(self, titulo, autor, ano):
        super().__init__(titulo, autor)
        self.ano = ano

    def exibir_informacoes(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"Livro: {self.titulo}, Autor: {self.autor}, Ano: {self.ano}, Status: {status}"

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros_disponiveis(self):
        return [livro.exibir_informacoes() for livro in self.livros if livro.disponivel]

    def listar_usuarios_com_emprestimos(self):
        return [
            usuario.exibir_informacoes()
            for usuario in self.usuarios
            if usuario.livros_emprestados
        ]

biblioteca = Biblioteca()

admin = Administrador("Carla", 40)
usuario1 = UsuarioComum("João", 25, "20231001")
usuario2 = UsuarioComum("Ana", 22, "20231002")

livro1 = Livro("Python Básico", "Autor A", 2020)
livro2 = Livro("POO Avançado", "Autor B", 2022)
livro3 = Livro("Estruturas de Dados", "Autor C", 2018)
livro4 = Livro("Inteligência Artificial", "Autor D", 2021)

admin.cadastrar_livro(biblioteca, livro1)
admin.cadastrar_livro(biblioteca, livro2)
admin.cadastrar_livro(biblioteca, livro3)
admin.cadastrar_livro(biblioteca, livro4)

admin.cadastrar_usuario(biblioteca, usuario1)
admin.cadastrar_usuario(biblioteca, usuario2)

usuario1.emprestar_livro(livro1)
usuario1.emprestar_livro(livro2)
usuario2.emprestar_livro(livro3)

print("Livros disponíveis:")
for info in biblioteca.listar_livros_disponiveis():
    print(info)

print("\nUsuários com livros emprestados:")
for info in biblioteca.listar_usuarios_com_emprestimos():
    print(info)
