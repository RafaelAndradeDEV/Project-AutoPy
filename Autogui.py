import pyautogui
from time import sleep
#EXEMPLOS de projetos: *Automatização de inscrição em canais de youtube, instagram e outros; *Automatização de rotinas(Abertura de canais de notícia);

#Passo antes de começar: Mapear detalhadamente o que o programa deve fazer(Click, hotkeys)

#A função retorna uma tupla([]) com 4 inteiros (esquerda,topo,largura,altura) da imagem - localização da imagem na tela
'''coorde = pyautogui.locateOnScreen("edit.png")
print(coorde)
#Essa trabalha com a variável que armazena esses dados e transforma em uma coordenada(x,y) na tela - centro de coordernadas
xy = pyautogui.center(coorde)
print(xy)
#Localiza o centro da imagem diretamente
XY = pyautogui.locateCenterOnScreen("edit.png")
print(XY)'''
sleep(2)
#currentMouseX, currentMouseY = pyautogui.position() 
X1, Y1 = 587, 571
X2, Y2 = 518, 317
x = 1
while x != 50:
	sleep(1.5)
	pyautogui.click(X1, Y1)
	sleep(1)
	pyautogui.click(X2, Y2)
	pyautogui.press('left')
	pyautogui.write(',')
	x += 1
#pyautogui.click(currentMouseX, currentMouseY)



