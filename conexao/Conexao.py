from pathlib import Path
import mysql.connector
class Conexao():
    
    def connection():
        conn = mysql.connector.connect(
            host="localhost", port=3306, user="root",
            password="", db="blaze"
        )
        return conn
     
     
    def enviar_para_banco(result):
        conn = Conexao.connection() 
        cursor = conn.cursor()
        sql = f'INSERT INTO resultado (cor, hora) VALUES ("{result[0]}","{result[1]}")'
        
        cursor.execute(sql)
        conn.commit()
         
