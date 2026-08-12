from bs4 import BeautifulSoup
import requests

## AULA EXTRAINDO TEXTO DE UM SITE COM PYTHON ##

# DADOS QUE NOSSA APLICAÇÃO VAI PEGAR 
url = "https://quotes.toscrape.com/" 

# ACESSAR O MEU CORPO DA APLICAÇÃO 
pagina = requests.get(url) 

# LER AS INFORMAÇÕES DO MEU HTML DA PAGINA 
site = BeautifulSoup(pagina.text, "html.parser") 

# PARAMETRO PARA APLICAÇÃO PEGAR TODAS AS FRASES 
frases = site.find_all("span", {"class": "text"}) 

# IMPRIMIR AS FRASES QUE COLOQUEI COMO PARAMETRO ACIMA 
for frase in frases: print(frase.text)