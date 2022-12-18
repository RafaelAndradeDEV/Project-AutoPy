#Incrição em um canal de Youtube

#Incrementos:
# *Função prompt:Colocar uma lista, com pontuação numerada atrás;
# *Abrir Browser automaticamente após o input;
# *Transformar hotkeys em váriaveis ou funções
# *pyautogui.KEYBOARD_KEYS para ver as teclas que o pyautogui reconhece

#Passos:
"""
1°: Abrir o Browser(Chrome) #Depois fazer com que seja para qualquer browser
2°: Usar ferramenta de pesquisa do Youtube

"""
import pyautogui
from time import sleep

nome_do_canal = pyautogui.prompt(text="Which of Channels Below you want to subscribe?", title="Enter the channel name")
print(nome_do_canal)
pyautogui.press("winleft")
sleep(1)
pyautogui.write("chrome")
pyautogui.press('enter')
sleep(2)

x3,y3 = pyautogui.locateCenterOnScreen("gabriel.png", confidence=0.9)
pyautogui.moveTo(x3,y3)
pyautogui.click()
sleep(1)

#Open new window at chrome
pyautogui.hotkey("ctrl", "t")
sleep(1)

#Search in Youtube
pyautogui.write("https://www.youtube.com/")
pyautogui.hotkey("enter")
sleep(3)

x,y = pyautogui.locateCenterOnScreen("pesquisar.png", confidence=0.9)
pyautogui.moveTo(x,y)
pyautogui.click()
pyautogui.write(nome_do_canal)

x1,y1 = pyautogui.locateCenterOnScreen('Search.png')
pyautogui.moveTo(x1,y1)
pyautogui.click()
sleep(3)

x2,y2 = pyautogui.locateCenterOnScreen('Subscribe.png')
if x2 == None:
    pyautogui.alert('Channel miss!')
pyautogui.moveTo(x2,y2)
pyautogui.click()
