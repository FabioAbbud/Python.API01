import json
import sqlite3
import os

database = './temp_db.db'

def get_all_owner():

    # Cria uma conexão com o banco de dados SQLite.
    conn = sqlite3.connect(database)

    # Define que a troca de dados entre Python e SQLite acontece na for a de Row.
    conn.row_factory = sqlite3.Row

    # Um cursor que aponta para a(s) linha(s) do SQLite.Row que está(ão) sendo acessadas.
    cursor = conn.cursor()

    # Query para consultar os registrosn na tabela 'item'.
    sql = "SELECT * FROM owner WHERE owner_status != 'off'"

    # Executa o SQL acima no banco de dados.
    cursor.execute(sql)

    # "Puxa" os dados do cursor para o Python.
    data = cursor.fetchall()

    # Desconecta do banco de dados.
    # Guarda recursos, aumenta a segurança, evita corrupção de dados.
    conn.close()

    # Uma 'list' para armazenar as SQLite.Row no forma de 'dict'.
    res = []

    # Loop que obtém cada SLite.Row da memória (data).
    for res_temp in data:

        # Converte a SQLite.Row em 'dict' e adiciona no final da 'list' 'res'.
        res.append(dict(res_temp))

    # Devolve os dados processados para quem solicitou.
    return res

def get_one_owner(id):

    # Incializa o banco de dados.
    conn = sqlite3.connect(database)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    # Query de consulta.
    sql = "SELECT * FROM owner WHERE owner_status != 'off' AND owner_id = ?"

    # Executa o código passando o valor do ID.
    cursor.execute(sql, (id,))

    # Retorna o resultado da busca para 'data'.
    data = cursor.fetchone()

    # Fecha a conexão com o banco de dados.
    conn.close()

    if data:  # Se o registro existir...

        # Retorna o registro em um 'dict'.
        return dict(data)

    else:  # Se o registro não chegou...

        # Retorna erro.
        return {"error": "Registro não encontrado."}
    
    
os.system('cls')

print(
json.dumps(
    get_all_owner(),
    ensure_ascii=False,
    indent=2
)
)

