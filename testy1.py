from pynput import keyboard #pip3 install pynput
import time

def callb(key): 		#What to do on key-release
	ti1 = str(time.time() - t )[0:5] #converting float to str, slicing the float
	print('The key',key,'is pressed for',ti1,'seconds')

	print(t)	#t sie nie zmienia
	tmp = time.time()	#tmp sie zmienia w tym miejscu na bierzaco
	print(tmp)			#ale ti1 uzywa t wiec nie mozna znowu przypisywac tu niczego do t

	#return False		#stop detecting more key-releases 
	
	#sytuacja wyglada tak ze time.time przypisany do T daje nam czas przy uruchomieniu programu wiec jesli zbadamy wiecej niz jedna litere czas sie nie zmienia
	#nie mozemy go dodac do sekcji po print tmp 

def callb1(key):		#What to do on key-press
	return False	#stop detecting more key-presses

with keyboard.Listener(on_press = callb1) as listener1:	#setting code for listening key-press
	listener1.join()
	
t = time.time()

with keyboard.Listener(on_release = callb) as listener:	#setting code for listening key-release
	listener.join()
