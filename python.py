import pyautogui
import time
import pandas as pd
pyautogui.PAUSE = 1

# Passo 1: Abrir o sistema da empresa
pyautogui.press("win")
pyautogui.write("microsoft edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)

#Passo 2: Fazer login
pyautogui.click(x=535, y=364)
pyautogui.write("pugedoj@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(1)

#Passo 3: Importar a base de dados de produtos
tabela = pd.read_csv("produtos.csv")
print(tabela)

time.sleep(1)

#Passo 4: Cadastrar um novo produto
for linha in tabela.index:
    pyautogui.click(x=500, y=261)
    
    #codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    
    #marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    
    #tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    
    #categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    
    #preço unitario
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    
    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    
    #obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
        pyautogui.press("tab")    
        
    pyautogui.press("enter")

    #repete até cadastrar todos os produtos
    
    pyautogui.scroll(5000)