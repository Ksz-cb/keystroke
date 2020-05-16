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


def digraphletters(keypress, keyrelease):
    keyPressLetter = [letter.split('-')[0] for letter in keypress]
    keyReleaseLetter = [letter.split('-')[0] for letter in keyrelease]
    return [i + j for i, j in zip(keyReleaseLetter[1:], keyPressLetter[:-1])]

def digraphtime(keypress, keyrelease):
    keyPress = [float(times.split('-')[1]) for times in keypress]
    keyRelease = [float(times.split('-')[1]) for times in keyrelease]

    return [i - j for i, j in zip(keyRelease[1:], keyPress[:-1])]

def dataProcessKeyPress(keyPress):
    # remove backspace and the key for which it was used
    for index, data in enumerate(keyPress):
        if data.split('-')[0] == 'Key.backspace':
            keyPress = [j for i, j in enumerate(keyPress) if i not in (index, index - 1)]
            keyPress = dataProcessKeyPress(keyPress)
            return keyPress
    return keyPress

keyPressData = []
keyReleaseData = []
text = ["Jak"]

i=1
for textlist in text:
    print("Entry", i, "text: ")
    print(textlist)
    with Listener(on_press=callb, on_release=callb1) as listener:
        x = input()
        listener.join()
    i += 1
    x=0
    #print('\n' * 80)
    clear_screen()

print(keyPressData)
print(keyReleaseData)
#print(dell(keyPressData))
#print(dataProcessKeyPress(keyPressData))
print(digraphletters(keyPressData, keyReleaseData))
keyPressData2 = [float(data.split('-')[1]) for data in keyPressData]
keyReleaseData2 = [float(times.split('-')[1]) for times in keyReleaseData]
#print(keyPressData2)
#print(keyReleaseData2)
#x = list(zip(keyReleaseData2[1:], keyPressData2[:-1]))
#print(x)
print(digraphtime(keyPressData, keyReleaseData))

