#!/usr/bin/env python
# coding: utf-8

# In[6]:


get_ipython().system('pip install beautifulsoup4')
get_ipython().system('pip install PyAutoGUI')
get_ipython().system('pip install selenium')


# In[90]:


import pyautogui
import requests
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
import webbrowser


# In[ ]:


def consumoDiario():
    peso = float(input("Digite seu peso em Kg:"))
    numero = 1 / 3
    print("KCAL")
    print("Kcal perder peso: {0:.2f}Kcal".format(peso*25))
    print("Kcal manter peso: {0:.2f}Kcal".format(peso*35))
    print("Kcal manter peso: {0:.2f}Kcal".format(peso*45))
    print("M A C R O S:")
    print("Quantidade de Proteinas Diaria: {0:.2f}g".format(peso*1.5))
    print("Quantidade de Carboidrato Diaria: {0:.2f}g".format(peso*9))
    print("Quantidade de Agua Diaria: {0:.2f}ml".format(peso*45))
    print("Quantidade de Gordura Diaria: {0:.2f}g".format(peso*0.25))
    print("MICROS")
    print("Vitamina A minima Diaria: {0:.2f}Microgramas".format(peso*12))
    print("Vitamina B1 minima Diaria: {0:.2f}Microgramas".format(peso*17.15))
    print("Vitamina B2 minima Diaria: {0:.2f}Microgramas".format(peso*18.60))
    print("Vitamina B3 minima Diaria: {0:.2f}Microgramas".format(peso*230))
    print("Vitamina B5 minima Diaria: {0:.2f}Microgramas".format(peso*72))  
    print("Vitamina B6 minima Diaria: {0:.2f}Microgramas".format(peso*25))
    print("Vitamina B7 minima Diaria: {0:.2f}Microgramas".format(peso*1.5))
    print("Vitamina B9 minima Diaria: {0:.2f}Microgramas".format(peso*9))
    print("Vitamina B12 minima Diaria: {0:.2f}Microgramas".format(peso*0.035))
    print("Vitamina C minima Diaria: {0:.2f}Miligramas".format(peso*1.75))
    print("Vitamina D minima Diaria: {0:.2f}UI".format(peso*12))
    print("Vitamina E minima Diaria: {0:.2f}Miligramas".format(peso*0.22))
    print("Vitamina K minima Diaria: {0:.2f}Microgramas".format(peso*1.75))
    print("Ferro minima Diaria: {0:.2f}Miligramas".format(peso*145))
    print("Zinco minima Diaria: {0:.2f}Miligramas".format(peso*175))
    print("Iodo minima Diaria: {0:.2f}Microgramas".format(peso*2.15))
    print("Selênio minima Diaria: {0:.2f}Microgramas".format(peso*0.80))
    print("Cobre minima Diaria: {0:.2f}Microgramas".format(peso*13.50))
    print("Manganês minima Diaria: {0:.2f}Miligramas".format(peso*0.04))
    print("Molibdênio minima Diaria: {0:.2f}Miligramas".format(peso*0.65))
    print("Molibdênio minima Diaria: {0:.2f}Microgramas".format(peso*0.65))
    print("Cromo minima Diaria: {0:.2f}Microgramas".format(peso*0.5))
    print("Flúor minima Diaria: {0:.2f}Miligramas".format(peso*0.06))
    
consumoDiario()


# In[23]:


def calculo_do_IMC():
    peso = float(input("diga seu peso em Kg:"))
    altura = float(input("Diga sua altura em Metros:"))
    imc = peso / (altura ** 2)
    print("seu imc é de {0:.2f}".format(imc))
calculo_do_IMC()


# In[111]:


def abrirObsidian():
    pyautogui.press('win')
    pyautogui.write("Obsidian", interval=0.1)
    pyautogui.press('enter')
    
abrirObsidian()


# In[112]:


def abrirLeagueOfLegens():
    pyautogui.press('win')
    pyautogui.write("League Of Legends", interval=0.1)
    pyautogui.press('enter')
abrirLeagueOfLegens()


# In[113]:


def abrirGoogle():
    pyautogui.press('win')
    pyautogui.write("chrome", interval=0.1)
    pyautogui.press('enter')
abrirGoogle()


# In[56]:


def cotacaoDolar():
    
    url = 'https://www.remessaonline.com.br/cotacao/cotacao-dolar'
    response = requests.get(url)
    html = response.text
    
    soup = BeautifulSoup(html, 'html.parser')
    valor = soup.find(class_='style__Text-sc-1a6mtr6-2 ljisZu')
    conteudo = valor.text
    print("Dolar",conteudo)

cotacaoDolar()   


# In[114]:


def cotacaoEuro():
    url = 'https://www.remessaonline.com.br/cotacao/cotacao-euro'
    response = requests.get(url)
    html = response.text
    
    soup = BeautifulSoup(html, 'html.parser')
    valor = soup.find(class_='style__Text-sc-1a6mtr6-2 ljisZu')
    conteudo = valor.text
    print('Euro',conteudo)
    
cotacaoEuro()


# In[84]:


def cotacaoBitCoin():
    url = 'https://www.coingecko.com/pt/all-cryptocurrencies'
    response = requests.get(url)
    html = response.text
    
    soup = BeautifulSoup(html, 'html.parser')
    valor = soup.find(class_='no-wrap')
    conteudo = valor.text
    print('Bitcoin',conteudo,'em Dolares')
    
cotacaoBitCoin()


# In[110]:


def abrirChatGpt():
    webbrowser.open_new('https://chat.openai.com/')

abrirChatGpt()


# In[115]:


def abrirVsCode():
    pyautogui.press('win')
    pyautogui.write("VScode", interval=0.1)
    pyautogui.press('enter')

abrirVsCode()


# In[ ]:




