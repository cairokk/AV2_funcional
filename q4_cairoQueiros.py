selecionar = lambda colunas: ", ".join(colunas)
da_tabela = lambda tabela: tabela
inner_join = lambda tabela1, tabela2, campo1, campo2: f"{tabela1} INNER JOIN {tabela2} ON {tabela1}.{campo1} = {tabela2}.{campo2}"

construir = lambda select, from_table, join, where: f"SELECT {select} FROM {from_table} {join} WHERE {where}"

# Exemplo de uso
colunas = lambda : selecionar(["name", "country"])
tabela = lambda : da_tabela("USERS")
join = lambda : inner_join("USERS", "GAMES", "id", "id_game")
condicao = lambda : "country = 'Brasil'"

consulta = construir(colunas(), tabela(), join(), condicao())
print(consulta)
