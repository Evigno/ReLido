import sqlite3
import os

def conectar_banco():
    return sqlite3.connect('relido.db')

def criar_tabela():
    conn = conectar_banco()
    cursor = conn.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS Obra (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        genero TEXT NOT NULL,
        edicao TEXT NOT NULL,
        idAdministrador INTEGER NOT NULL
    )
    """
    cursor.execute(sql)
    conn.commit()
    conn.close()

def inserir_obra(nome, genero, edicao, id_admin):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Obra (nome, genero, edicao, idAdministrador) VALUES (?, ?, ?, ?)", (nome, genero, edicao, id_admin))
    conn.commit()
    conn.close()
    print(f"\nObra '{nome}' inserida com sucesso.")

def listar_obras():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Obra")
    obras = cursor.fetchall()
    conn.close()
    
    if not obras:
        print("\nNenhuma obra cadastrada.")
    else:
        print("\n--- Lista de Obras ---")
        for obra in obras:
            print(f"ID: {obra[0]} | Nome: {obra[1]} | Gênero: {obra[2]} | Edição: {obra[3]} | Admin ID: {obra[4]}")
    return obras

def atualizar_obra(id_obra, novo_nome, novo_genero, nova_edicao):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("UPDATE Obra SET nome = ?, genero = ?, edicao = ? WHERE id = ?", (novo_nome, novo_genero, nova_edicao, id_obra))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"\nObra ID {id_obra} atualizada com sucesso.")
    else:
        print(f"\nObra ID {id_obra} não encontrada.")
    conn.close()

def excluir_obra(id_obra):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Obra WHERE id = ?", (id_obra,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"\nObra ID {id_obra} excluída com sucesso.")
    else:
        print(f"\nObra ID {id_obra} não encontrada.")
    conn.close()

def menu():
    criar_tabela()
    while True:
        print("\n--- Sistema ReLido: Gestão de Obras ---")
        print("1. Inserir Nova Obra")
        print("2. Listar Obras")
        print("3. Atualizar Obra")
        print("4. Excluir Obra")
        print("0. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome da Obra: ")
            genero = input("Gênero: ")
            edicao = input("Edição: ")
            id_admin = input("ID do Administrador responsável: ")
            try:
                inserir_obra(nome, genero, edicao, int(id_admin))
            except ValueError:
                print("Erro: O ID do Administrador deve ser um número.")
        
        elif opcao == '2':
            listar_obras()
            
        elif opcao == '3':
            id_obra = input("ID da Obra a atualizar: ")
            novo_nome = input("Novo Nome: ")
            novo_genero = input("Novo Gênero: ")
            nova_edicao = input("Nova Edição: ")
            try:
                atualizar_obra(int(id_obra), novo_nome, novo_genero, nova_edicao)
            except ValueError:
                 print("Erro: ID inválido.")
            
        elif opcao == '4':
            id_obra = input("ID da Obra a excluir: ")
            try:
                excluir_obra(int(id_obra))
            except ValueError:
                 print("Erro: ID inválido.")
            
        elif opcao == '0':
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
