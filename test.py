from pynput.keyboard import Key, Listener
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def callb(key): 		#What to do on key-release
    t = time.time()

    if key != Key.enter:
        #print('The key', key, 'hold', t)
        keyPressData.append("{0}-{1}".format(key,t))


def callb1(key):
    t = time.time()

    if key != Key.enter:
        #print('The key', key, 'hold', t)
        keyReleaseData.append("{0}-{1}".format(key,t))
    else:
        return False		#stop detecting more key-presses


def digraphtime(keypress, keyrelease):
    keyPress = [float(times.split('-')[1]) for times in keypress]
    keyRelease = [float(times.split('-')[1]) for times in keyrelease]

    return [i - j for i, j in zip(keyRelease[1:], keyPress[:-1])]

def dell(keypress):
    for index in enumerate(keypress):
        if keypress[index] == Key.shift:
            del keypress[index]
            return (keyPressData)
    return (keypress)

keyPressData = []
keyReleaseData = []
text = ["Jak glosi wielkie przyslowie, Nie ma nik",
      "ogo, kto lubilby bol dla samego bolu, szu",
      "kal go tylko po to, by go poczuc, po pros",
      "tu dlatego, ze to bol cos cos cos cos cos"]

i=1
for textlist in text:
    print("Entry", i, "text: ")
    print(textlist)
    with Listener(on_press=callb, on_release=callb1) as listener:
        listener.join()
    i += 1
    #print('\n' * 80)
    clear_screen()

print(keyPressData)
print(keyReleaseData)
#print(dell(keyPressData))
keyPressData2 = [float(data.split('-')[1]) for data in keyPressData]
keyReleaseData2 = [float(times.split('-')[1]) for times in keyReleaseData]
#print(keyPressData2)
#print(keyReleaseData2)
#x = list(zip(keyReleaseData2[1:], keyPressData2[:-1]))
#print(x)
#print(digraphtime(keyPressData, keyReleaseData))

