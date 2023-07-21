import sqlite3

class Livro:

    def __init__(self, titulo, autor, ano_de_publicacao, numero_de_copias):
        self.titulo = titulo
        self.autor = autor
        self.ano_de_publicacao = ano_de_publicacao
        self.numero_de_copias = numero_de_copias

    def cadastrar(self):
        banco = sqlite3.connect('diretorio.db')
        cursor = banco.cursor()
        cursor.execute("INSERT INTO biblioteca_diretorio (titulo, autor, ano_de_publicacao, numero_de_copias) VALUES (?, ?, ?, ?)",
               (self.titulo, self.autor, self.ano_de_publicacao, self.numero_de_copias))


        banco.commit()
        banco.close()

    





