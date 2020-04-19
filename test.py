from pynput import keyboard #pip3 install pynput
import time

ti2 = 0

while True:

	def callb(key): 		#What to do on key-release
		global ti2
		ti1 = str(time.time() - t )[0:5] #converting float to str, slicing the float
		print('The key',key,'is pressed for',ti1,'seconds')
		ti2 = time.time()
		return False 		#stop detecting more key-releases
	def callb1(key):		#What to do on key-press
		return False		#stop detecting more key-presses

	with keyboard.Listener(on_press = callb1) as listener1:	#setting code for listening key-press
		listener1.join()

	t = time.time()
	czas2 = str(t - ti2)[0:6] # flight time latency - czas miedzy puszczeniem 1 klawisza a wcisnieciem nastepnego
	print("Flight time:", czas2)

	with keyboard.Listener(on_release = callb) as listener:	#setting code for listening key-release
		listener.join()