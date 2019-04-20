import keyboard
from PIL import ImageGrab
import time
from OCR import get_content
import pyperclip




def screen():
    #QQ截图
	keyboard.wait(hotkey='ctrl+alt+a')
	#阻塞程序运行
	keyboard.wait(hotkey='enter')
	#截图完成
	time.sleep(0.5)
	image = ImageGrab.grabclipboard()
	#print(image)
	image.save(r'C:\Users\Administrator\Pictures\Pictures.jpg')



while True:
	screen()
	data = get_content()
	print(data)
	pyperclip.copy(data)#复制到剪切板
	
