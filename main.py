from livro import Livro
import sqlite3


def pesquisar(criterio, coluna):
    banco = sqlite3.connect('diretorio.db')
    cursor = banco.cursor()
    cursor.execute(f"SELECT * FROM biblioteca_diretorio WHERE {coluna} = ?", (criterio,))
    resultado = cursor.fetchall()

    banco.close()

    return resultado


def gerenciador():

    print("\nBem-vindo ao Sistema de Gerenciamento de Biblioteca!\n")

    while True:

        print("""\nPor favor, selecione uma opção:\n
        1. Cadastro de livros\n
        2. Consulta de livros\n
        3. Empréstimo de livros\n
        4. Devolução de livros\n
        5. Sair\n""")
        
        escolha = int(input("Digite o número correspondente à opção desejada: "))
        

        if escolha < 1 or escolha > 5:
            print("\nEssa opção não existe. Tente novamente.\n")
        elif escolha == 1:
            titulo = input("\nInforme o nome do livro: ")
            autor = input("Informe o autor: ")
            ano_de_publicacao = input("informe o ano da publicação: ")
            numero_de_copias = int(input("Informe o número de cópias: "))

            novo_livro = Livro(titulo, autor, ano_de_publicacao, numero_de_copias)

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

                livro_encontrado = pesquisar(titulo_busca, coluna= 'titulo')

                if livro_encontrado:
                    print("\nLivro encontrado:\n")
                    for livro in livro_encontrado:
                        print("\nTítulo:", livro[0])
                        print("Autor:", livro[1])
                        print("Ano de Publicação:", livro[2])
                        print("Cópias disponíveis:", livro[3])
                else:
                    print("Livro não encontrado.")


            elif escolha == 2:
                autor_busca = input("Digite o autor do livro: ")

                livro_encontrado = pesquisar(autor_busca, coluna= 'autor')

                if livro_encontrado:
                    print("\nLivro encontrado:\n")
                    for livro in livro_encontrado:
                        print("\nTítulo:", livro[0])
                        print("Autor:", livro[1])
                        print("Ano de Publicação:", livro[2])
                        print("Cópias disponíveis:", livro[3])
                else:
                    print("Livro não encontrado.")


            else:
                ano_de_publicacao_busca = input("Digite o ano de publicação do livro: ")

                livro_encontrado = pesquisar(ano_de_publicacao_busca, coluna= 'ano_de_publicacao')

                if livro_encontrado:
                    print("\nLivro encontrado:\n")
                    for livro in livro_encontrado:
                        print("\nTítulo:", livro[0])
                        print("Autor:", livro[1])
                        print("Ano de Publicação:", livro[2])
                        print("Cópias disponíveis:", livro[3])
                else:
                    print("Livro não encontrado.")
        elif escolha == 3:
            titulo_busca = input("\nDigite o título do livro que deseja emprestar: ")

            banco = sqlite3.connect('diretorio.db')
            cursor = banco.cursor()
            cursor.execute(f"SELECT * FROM biblioteca_diretorio WHERE titulo = ?", (titulo_busca,))
            resultado = cursor.fetchone()

            if resultado[3] > 0:
                cursor.execute("UPDATE biblioteca_diretorio SET numero_de_copias = numero_de_copias - ? WHERE titulo = ?", (1, titulo))
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

            cursor.execute("UPDATE biblioteca_diretorio SET numero_de_copias = numero_de_copias + ? WHERE titulo = ?", (1, titulo_devolvido))
            banco.commit()
    
            banco.close()

            print("\nDevolução cadastrada com sucesso!")

        else:
            print("\nObrigado por usar o Sistema de Gerenciamento de Biblioteca. Até mais!")
            break




gerenciador()