import mysql.connector
class Conexao():
      
    def connection():
        conn = mysql.connector.connect(
            host="localhost", port=3306, user="root",
            password="root", db="blaze"
        )
        return conn
     
  
    def inserir_desceu(resultado_geral):
        conn =  Conexao.connection()
        cursor = conn.cursor()
        sql = f"""INSERT INTO `resultado`(`numero`, `data`, `crashou`) VALUES ('{resultado_geral[0]}','{resultado_geral[1]}','{resultado_geral[2]}')"""
        cursor.execute(sql)
        conn.commit() 
        
    def inserir_subiu(resultado_geral):
        conn =  Conexao.connection()
        cursor = conn.cursor()
        sql = f"""INSERT INTO `resultado`(`numero`, `data`, `subiu`) VALUES ('{resultado_geral[0]}','{resultado_geral[1]}','{resultado_geral[3]}')"""
        cursor.execute(sql)
        conn.commit() 