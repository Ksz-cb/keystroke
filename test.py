from pynput import keyboard #pip3 install pynput
import time

def callb(key): 		#What to do on key-release
	ti1 = str(time.time() - t )[0:5] #converting float to str, slicing the float
	print('The key',key,'is pressed for',ti1,'seconds')
	return False 		#stop detecting more key-releases
def callb1(key):		#What to do on key-press
	return False		#stop detecting more key-presses

with keyboard.Listener(on_press = callb1) as listener1:	#setting code for listening key-press
	listener1.join()

t = time.time()

with keyboard.Listener(on_release = callb) as listener:	#setting code for listening key-release
	listener.join()