from time import sleep
import pyautogui as p
import cv2
import time
import win32api
import win32con
import ctypes
import pyperclip

# Configurações iniciais 
p.PAUSE = 3
p.FAILSAFE = False

# Abre a janela "active"
p.press('winleft')
p.typewrite('active')
p.press('enter')

# Carrega as imagens 
ad_l = cv2.imread(r"ad2.png") 
ad_2 = cv2.imread(r"ad3.png")
ad_3 = cv2.imread(r"ad4.png") 

# Localiza e clica na imagem ad_l
img_ad_l = p.locateOnScreen(ad_l)
p.click(img_ad_l)

# Lê o conteúdo do arquivo 'usuario.txt'
with open ('usuario.txt', 'r') as arquivo: 
    conteudo = arquivo.read() 
   
# Escreve o conteúdo lido
p.write(conteudo)

# Pressiona Enter e a tecla Down
p.press('enter')
p.keyDown('down')

# Localiza e clica na imagem ad_2
img_ad_2 = p.locateOnScreen(ad_2)
time.sleep(0.2)
p.click(img_ad_2)

# Código de tecla para o Shift e F10
shift_key = win32con.VK_SHIFT
f10_key = win32con.VK_F10

# Pressiona Shift e F10
win32api.keybd_event(shift_key, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
win32api.keybd_event(f10_key, 0, win32con.KEYEVENTF_EXTENDEDKEY, 0)
win32api.keybd_event(f10_key, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(shift_key, 0, win32con.KEYEVENTF_KEYUP, 0)

# Configura o tempo de pausa
p.PAUSE = 0.5

# Pressiona a tecla Down várias vezes
num_process_down  = 6
for _ in range(num_process_down):
   p.keyDown('down')

# Pressiona Enter e confiogura o Pause
p.press('enter')
p.PAUSE = 3

# Lê o conteúdo do arquivo 'sprovisoria.txt'
with open('sprovisoria.txt', 'r') as arquivo:
    conteudo2 = arquivo.read()
    
# Copia o conteúdo para a área de transferência
pyperclip.copy(conteudo2)

# Cola o conteúdo
p.hotkey('ctrl', 'v') 

img_ad_3 = p.locateOnScreen(ad_3)
time.sleep(0.2)
p.click(img_ad_3)
time.sleep(0.2)

p.hotkey('ctrl', 'v') 

# Confirmando a senha nova
p.press('enter')
p.press('enter')

# Fechando o programa
p.hotkey('alt', 'f4')
p.hotkey('alt', 'f4')