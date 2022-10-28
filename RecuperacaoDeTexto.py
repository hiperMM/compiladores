import requests
from bs4 import BeautifulSoup

url1 = 'https://www.geeksforgeeks.org/natural-language-processing-overview/'
url2 = 'https://www.ibm.com/cloud/learn/natural-language-processing'
url3 = 'https://www.oracle.com/artificial-intelligence/what-is-natural-language-processing/'
url4 = 'https://www.deeplearning.ai/resources/natural-language-processing/'
url5 = 'https://monkeylearn.com/blog/natural-language-processing-techniques/'

page1 = requests.get(url1)
page2 = requests.get(url2)
page3 = requests.get(url3)
page4 = requests.get(url4)
page5 = requests.get(url5)

bsPage1 = BeautifulSoup(page1.text, "html.parser")
bsPage2 = BeautifulSoup(page2.text, "html.parser")
bsPage3 = BeautifulSoup(page3.text, "html.parser")
bsPage4 = BeautifulSoup(page4.text, "html.parser")
bsPage5 = BeautifulSoup(page5.text, "html.parser")

titulo1 = bsPage1.findAll('h1')
titulo1 = titulo1[0].get_text()
print("O titulo do Texto 1 é: " + titulo1)
#------------------------------------------------------------------
titulo2 = bsPage2.findAll('h1')
titulo2 = titulo2[0].get_text()
print("O titulo do Texto 2 é: " + titulo2)
#------------------------------------------------------------------
titulo3 = bsPage3.findAll('h1')
titulo3 = titulo3[0].get_text()
print("O titulo do Texto 3 é: " + titulo3)
#------------------------------------------------------------------
titulo4 = bsPage4.findAll('h1')
titulo4 = titulo4[0].get_text()
print("O titulo do Texto 4 é: " + titulo4)
#------------------------------------------------------------------
titulo5 = bsPage5.findAll('h1')
titulo5 = titulo5[0].get_text()
print("O titulo do Texto 5 é: " + titulo5)


paragrafosTexto1 = bsPage1.findAll('p')
paragrafosTexto1 = [paragrafosTexto1[i].get_text() for i in range(0, len(paragrafosTexto1))]
#----------------------------------------------------------------------------------------------------------------------
paragrafosTexto2 = bsPage2.findAll('p')
paragrafosTexto2 = [paragrafosTexto2[i].get_text() for i in range(0, len(paragrafosTexto2))]
#----------------------------------------------------------------------------------------------------------------------
paragrafosTexto3 = bsPage3.findAll('p')
paragrafosTexto3 = [paragrafosTexto3[i].get_text() for i in range(0, len(paragrafosTexto3))]
#----------------------------------------------------------------------------------------------------------------------
paragrafosTexto4 = bsPage4.findAll('p')
paragrafosTexto4 = [paragrafosTexto4[i].get_text() for i in range(0, len(paragrafosTexto4))]
#----------------------------------------------------------------------------------------------------------------------
paragrafosTexto5 = bsPage5.findAll('p')
paragrafosTexto5 = [paragrafosTexto5[i].get_text() for i in range(0, len(paragrafosTexto5))]




textoPage1 = ''.join([paragrafoTexto1 for paragrafoTexto1 in paragrafosTexto1])
#----------------------------------------------------------------------------------------------------------------------
textoPage2 = ''.join([paragrafoTexto2 for paragrafoTexto2 in paragrafosTexto2])
#----------------------------------------------------------------------------------------------------------------------
textoPage3 = ''.join([paragrafoTexto3 for paragrafoTexto3 in paragrafosTexto3])
#----------------------------------------------------------------------------------------------------------------------
textoPage4 = ''.join([paragrafoTexto4 for paragrafoTexto4 in paragrafosTexto4])
#----------------------------------------------------------------------------------------------------------------------
textoPage5 = ''.join([paragrafoTexto5 for paragrafoTexto5 in paragrafosTexto5])

import spacy

nlp = spacy.load("en_core_web_sm")
#----------------------------------------------------------------------------------------------------------------------
doc1 = nlp(textoPage1)
sentences1 = list(doc1.sents)
#----------------------------------------------------------------------------------------------------------------------
doc2 = nlp(textoPage2)
sentences2 = list(doc2.sents)
#----------------------------------------------------------------------------------------------------------------------
doc3 = nlp(textoPage3)
sentences3 = list(doc3.sents)
#----------------------------------------------------------------------------------------------------------------------
doc4 = nlp(textoPage4)
sentences4 = list(doc4.sents)
#----------------------------------------------------------------------------------------------------------------------
doc5 = nlp(textoPage5)
sentences5 = list(doc5.sents)
