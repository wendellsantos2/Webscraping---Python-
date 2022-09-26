from lib2to3.pytree import convert
 
import requests
from bs4 import BeautifulSoup

from control.Main import Buscar
 
class Cont:
  @staticmethod
  def contagem():
    Buscar.buscar_dados(resultados)
    resultados = []
    conversao = resultados[0].strip('X')
    numero = float(conversao)
    cont = 0
    while len(resultados) < 20:
      if numero < 2:
         cont += 1
      elif numero > 2 :
         resultados.append(cont)
         cont = 0
         print('pode apostar')
      
      
    
      