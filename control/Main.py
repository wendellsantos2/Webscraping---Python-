
from time import sleep
from unittest import result
import requests
from bs4 import BeautifulSoup
from Conexao import Conexao
 
 


    
 
from time import sleep
from unittest import result
import requests
from bs4 import BeautifulSoup
from Conexao import Conexao
class Main():
  
    def ler_tudo():
            global resultados
            resultados = list()
            global crashou 
            crashou = 0
            global subiu 
            subiu = 0
            global ant
            ultimo_numero = 0
            while True != False:
                url = 'https://www.historicosblaze.com/smash/crashes'
                headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}
                site = requests.get(url, headers=headers)
                soup = BeautifulSoup(site.content, 'html.parser')
                dados = soup.findAll('span')
                markets = []
                for x in dados:
                    market = {}
                    market['crash'] = soup.find('span',class_='crash-table').text.strip()
                    market['data'] = soup.find('span',class_='date-table').text.strip()
                    resultado = (market['crash'],market['data']) 

                    markets.append(market)
                    conversao = resultado[0].strip('X')
                    data = resultado[1]
                    numero_atual = float(conversao)
                    if numero_atual != ultimo_numero:
                        if numero_atual < 2:
                            crashou = crashou+ 1
                            resultado_geral = numero_atual,data,crashou,subiu
                            Conexao.inserir_desceu(resultado_geral)
                            subiu = 0
                            crash = print(f'crashou {crashou} vezes')
                            resultado_crash= print(f'crashou em {numero_atual}')
                            Main.calcular(crashou)
                            ultimo_numero = numero_atual
                            
                            
                        elif numero_atual > 2 :
                            subiu = subiu+ 1
                            print(f'subiu {subiu} vezes')
                            resultado_geral = numero_atual,data,crashou,subiu
                            Main.subir(subiu)
                            Conexao.inserir_desceu(resultado_geral)
                            resultados.append(crashou)
                            
                            crashou = 0
                            print(f'Subiu até {numero_atual}')   
                            ultimo_numero = numero_atual
                            

    def calcular(crashou):
        if crashou == 2 :
            print("pode entrar") 
        if crashou == 3:
            print("pode entrar mais cuidado " )   
        if crashou > 6:
            print("pode ir ate 5X")
         
    def subir(numero_atual): 
        if numero_atual == 4:
            print("cuidado com o crash")            
Main.ler_tudo()            
 

    
    