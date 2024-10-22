import os
import pyautogui
import keyboard
import subprocess
import time
from dotenv import load_dotenv

load_dotenv()

navegador = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
link_formulario = "https://dlp.hashtagtreinamentos.com/python/intensivao/login?ps=incompany"

email=os.getenv("EMAIL")
senha=os.getenv("SENHA")

#ABRIR NAVEGADOR
subprocess.run(navegador)
time.sleep(1)
keyboard.write(link_formulario)
time.sleep(0.5)
pyautogui.press("enter")

#LOGIN
time.sleep(2)
pyautogui.press("enter")
pyautogui.press("tab")
keyboard.write(email)
pyautogui.press("tab")
keyboard.write(senha)
pyautogui.press("tab")
pyautogui.press("enter")

# #ABRIR ARQUIVO PRODUTOS.CSV
arquivo = open("produtos.csv", "r").read()
lista_produtos = arquivo.split("\n")

#CADASTRO
time.sleep(1)
pyautogui.press("tab")

for item in lista_produtos[1:]:
    produto = item.split(",")

    for info in produto:
        keyboard.write(info)
        time.sleep(0.5)
        pyautogui.press("tab")
    
    pyautogui.press("enter")

    time.sleep(1)
    
    for i in range(7):
        pyautogui.hotkey("shift","tab")



