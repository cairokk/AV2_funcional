import mysql.connector


# Função para conectar ao banco de dados MySQL
funcaoConectar = lambda host, user, password, database: f"mysql.connector.connect(host='{host}', user='{user}', password='{password}', database='{database}')"

# Função para criar uma tabela no banco de dados
create = lambda tabela, colunas: f"CREATE TABLE IF NOT EXISTS {tabela} ({', '.join(f'{campo} {tipo}' for campo, tipo in colunas.items())})"

def insert(cursor, tabela, colunas,valores):
    placeholders = ', '.join(['%s'] * len(valores))
    colunas = ', '.join(colunas)
    query = f"INSERT INTO {tabela} ({colunas}) VALUES ({placeholders})"
    cursor.execute(query, valores)

remove = lambda cursor,tabela, condicao: cursor.execute(f"DELETE FROM {tabela} WHERE {condicao}")

select = lambda cursor, tabela, colunas, condicao: cursor.execute(f"SELECT {colunas} FROM {tabela} WHERE {condicao}")

def generate_select(tabelas, colunas, condicoes=None):
    from_clause = " INNER JOIN ".join(tabelas)
    select_clause = ", ".join(colunas)
    query = f"SELECT {select_clause} FROM {from_clause}"
    if condicoes:
        query += f" WHERE {condicoes}"
    return query

def generate_inner_join(tabelas, on_conditions):
    join_clause = " INNER JOIN ".join([
        f"{tabela1} ON {tabela1}.{campo} = {tabela2}.{campo2}"
        for (tabela1, tabela2, campo, campo2) in on_conditions
    ])
    return join_clause

# Definindo os esquemas das tabelas
USERS_SCHEMA = lambda: ("USERS", {
    "id": "INT AUTO_INCREMENT PRIMARY KEY",
    "name": "VARCHAR(100)",
    "country": "VARCHAR(100)",
    "id_console": "INT"
})

VIDEOGAMES_SCHEMA = lambda: ("VIDEOGAMES", {
    "id_console": "INT",
    "name": "VARCHAR(100)",
    "id_company": "INT",
    "release_date": "DATE"
})

GAMES_SCHEMA = lambda: ("GAMES", {
    "id_game": "INT AUTO_INCREMENT PRIMARY KEY",
    "title": "VARCHAR(100)",
    "genre": "VARCHAR(100)",
    "release_date": "DATE",
    "id_console": "INT"
})

COMPANY_SCHEMA = lambda: ("COMPANY", {
    "id_company": "INT AUTO_INCREMENT PRIMARY KEY",
    "name": "VARCHAR(100)",
    "country": "VARCHAR(100)"
})
# Função para criar as tabelas no banco de dados
def create_tables(cursor):
    cursor.execute(create(USERS_SCHEMA()[0], USERS_SCHEMA()[1]))
    cursor.execute(create(VIDEOGAMES_SCHEMA()[0], VIDEOGAMES_SCHEMA()[1]))
    cursor.execute(create(GAMES_SCHEMA()[0], GAMES_SCHEMA()[1]))
    cursor.execute(create(COMPANY_SCHEMA()[0], COMPANY_SCHEMA()[1]))

# Exemplo de uso
def connect_to_database(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        print("Conexão com o banco de dados estabelecida com sucesso!")
        return connection
    except mysql.connector.Error as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        return None
def main():
        connection = connect_to_database('localhost', 'root', 'senha', 'mydb')
        cursor = connection.cursor()
        insert(cursor, "USERS", ["name", "country", "id_console"], ["Cairo Queiros", "Brazil", 1])

if __name__ == "__main__":
    main()
