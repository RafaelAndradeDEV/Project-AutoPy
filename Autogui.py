import pyautogui

#EXEMPLOS de projetos: *Automatização de inscrição em canais de youtube, instagram e outros; *Automatização de rotinas(Abertura de canais de notícia);

#Passo antes de começar: Mapear detalhadamente o que o programa deve fazer(Click, hotkeys)

#A função retorna uma tupla([]) com 4 inteiros (esquerda,topo,largura,altura) da imagem - localização da imagem na tela
coorde = pyautogui.locateOnScreen("edit.png")
print(coorde)
#Essa trabalha com a variável que armazena esses dados e transforma em uma coordenada(x,y) na tela - centro de coordernadas
xy = pyautogui.center(coorde)
print(xy)
#Localiza o centro da imagem diretamente
XY = pyautogui.locateCenterOnScreen("edit.png")
print(XY)




