import pyautogui
import time
import pandas as pd


pyautogui.PAUSE=1

pyautogui.press
pyautogui.click
pyautogui.write

pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3    marca)

pyautogui.position(x=588, y=445)
pyautogui.click(x=588, y=445)
pyautogui.write("aaaaaaa@gmail.com")
pyautogui.click(x=609, y=570)#aqui se pode so usar tab tbm que funciona 
pyautogui.write("bbbbbbbbbbb")
pyautogui.press("enter")

time.sleep(2)

tabela = pd.read_csv("produtos.csv")

codigo = "MOLO000251"
pyautogui.click(x=596, y=295)
pyautogui.write(codigo)
pyautogui.press("tab")

pyautogui.write("marca")
pyautogui.press("tab")

pyautogui.write("tipo")
pyautogui.press("tab")

pyautogui.write("categoria")
pyautogui.press("tab")

pyautogui.write("preço")
pyautogui.press("tab")

pyautogui.write("custo")
pyautogui.press("tab")


pyautogui.write("obs")
pyautogui.press("tab")






