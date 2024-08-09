import mysql.connector
from mysql.connector import Error
import pandas as pd

def create_connection(servidor, usuario, senha, nome_do_banco): # Conecta ao banco de dados
    connection = None
    try:
        connection = mysql.connector.connect(
            host = servidor,
            user = usuario,
            passwd = senha,
            database = nome_do_banco
        )
        print("Conexão bem sucedida.")
    except Error as err:
        print(f"Erro: '{err}'")

    return connection

def read_query(connection, query): # Executa a query no banco
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Erro: '{err}'")
    
query_clientes = "SELECT * FROM clientes;" # Cria a variavel com a query

connect_db = create_connection("servidor", "usuario", "senha", "nome_do_banco") # Cria a variavel de conexão
results = read_query(connect_db,query_clientes) # Cria a variavel com o resultado da pesquisa

list_db = [] # Cria uma lista vazia, que será preenchida com os dados das tuplas trazidas do banco, será uma lista de listas

for result in results: # Itera sobre as tuplas trazidas do banco e insere na lista list_db em formato de lista
    result = list(result)
    list_db.append(result)

colunas_df_clientes = ["cliente_id", "nome", "cpf", "contato"] # Define os nomes das colunas do dataframe
df = pd.DataFrame(list_db, columns= colunas_df_clientes) # Cria um dataframe com a lista criada e dá nome às colunas
df.set_index("cliente_id", inplace= True) # Usa o indice da coluna cliente_id no lugar do indice gerado automaticamente pelo pd.Dataframe

print(df) # Imprime o dataframe
