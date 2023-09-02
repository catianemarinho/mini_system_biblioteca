from livro import Livro
import sqlite3


def pesquisar(criterio, coluna):
        db_connection = sqlite3.connect('diretorio.db')
        cursor = db_connection.cursor()
        query = f"""
                    SELECT * 
                      FROM biblioteca_diretorio 
                     WHERE {coluna} LIKE '%{criterio}%'
                       """
        cursor.execute(query)
        resultado = cursor.fetchall()
        db_connection.close()

        if resultado:
            num_livros = len(resultado)

            print(f"\n{num_livros} livro(s) encontrado(s):\n")
            for livro in resultado:
                titulo, autor, ano, copias = livro[1], livro[2], livro[3], livro[4]
                print("\nTítulo: ", titulo)
                print("Autor: ", autor)
                print("Ano de Publicação: ", ano)
                print("Cópias disponíveis: ", copias)
        else:
            print("Livro não encontrado.")

def gerenciador():

    print("\nBem-vindo ao Sistema de Gerenciamento de Biblioteca!\n")

    while True:
        # Print menu options
        print("""\nPor favor, selecione uma opção:\n
        1. Cadastro de livros\n
        2. Consulta de livros\n
        3. Empréstimo de livros\n
        4. Devolução de livros\n
        5. Sair\n""")
        
        # Get user choice
        escolha = int(input("Digite o número correspondente à opção desejada: "))
        
        # Validate user choice
        if escolha < 1 or escolha > 5:
            print("\nEssa opção não existe. Tente novamente.\n")
        elif escolha == 1:
            # Get book details
            titulo = input("\nInforme o nome do livro: ")
            autor = input("Informe o autor: ")
            ano_de_publicacao = input("informe o ano da publicação: ")
            numero_de_copias = int(input("Informe o número de cópias: "))

            # Create a new instance of the Book class
            novo_livro = Livro(titulo, autor, ano_de_publicacao, numero_de_copias)
            # Add the book to the database
            novo_livro.cadastrar()

            print("\nCadastro realizado com sucesso!\n")

        elif escolha == 2:
            print("""\nSelecione o critério de pesquisa:\n
            1. Título\n
            2. Autor\n
            3. Ano de publicação\n""")
        
            escolha = int(input("Digite o número correspondente ao critério de pesquisa: "))

            while escolha < 1 or escolha > 3:
                print("\nEssa opção não existe. Tente novamente.\n")
                escolha = int(input("Digite o número correspondente ao critério de pesquisa: "))

            if escolha == 1:
                titulo_busca = input("Digite o título do livro: ")
                pesquisar(criterio=titulo_busca, coluna= 'titulo')

            elif escolha == 2:
                autor_busca = input("Digite o autor do livro: ")
                pesquisar(criterio=autor_busca, coluna= 'titulo')

            else:
                ano_de_publicacao_busca = input("Digite o ano de publicação do livro: ")
                pesquisar(criterio=ano_de_publicacao_busca, coluna= 'titulo')

        elif escolha == 3:
            titulo_busca = input("\nDigite o título do livro que deseja emprestar: ")

            banco = sqlite3.connect('diretorio.db')
            cursor = banco.cursor()
            cursor.execute(f"SELECT * FROM biblioteca_diretorio WHERE titulo = ?", (titulo_busca,))
            resultado = cursor.fetchone()

            if resultado:
                cursor.execute("UPDATE biblioteca_diretorio SET numero_de_copias = numero_de_copias - 1  WHERE titulo = ?", (resultado[1],))
                banco.commit()
                banco.close()

                print("\nEmpréstimo cadastrado com sucesso!") 
            else:
                print("\nSem cópias disponíveis para este livro!") 

                    
        elif escolha == 4:

            titulo_devolvido = input("\nDigite o título do livro devolvido: ")

            banco = sqlite3.connect('diretorio.db')
            cursor = banco.cursor()
            cursor.execute(f"SELECT * FROM biblioteca_diretorio WHERE titulo = ?", (titulo_devolvido,))
            resultado = cursor.fetchone()

            if resultado:
                cursor.execute("UPDATE biblioteca_diretorio SET numero_de_copias = numero_de_copias + 1 WHERE titulo = ?", (titulo_devolvido,))
                banco.commit()
                banco.close()
                print("\nDevolução cadastrada com sucesso!")

            else:
                print("\nLivro não encontrado.")   

        else:
            print("\nObrigado por usar o Sistema de Gerenciamento de Biblioteca. Até mais!")
            break
