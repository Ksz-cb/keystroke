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
        keyReleaseData.append("{0}-{1}".format(str(key), t))
    else:
        return False		#stop detecting more key-presses


def digraphletters(keypress, keyrelease):
    keyPressLetter = [letter.split('-')[0] for letter in keypress]
    keyReleaseLetter = [letter.split('-')[0] for letter in keyrelease]
    y = [j + i for i, j in zip(keyReleaseLetter[1:], keyPressLetter[:-1])]
    return [''.join(e for e in string if e.isalnum()) for string in y]

def digraphtime(keypress, keyrelease):
    keyPress = [float(times.split('-')[1]) for times in keypress]
    keyRelease = [float(times.split('-')[1]) for times in keyrelease]

    return [i - j for i, j in zip(keyRelease[1:], keyPress[:-1])]

def backspaceKeys(keyPreRe):
    for index, keys in enumerate(keyPreRe):
        if keys.split('-')[0] == 'Key.backspace':
            keyPreRe = [j for i, j in enumerate(keyPreRe) if i not in (index, index - 1)]
            keyPreRe = backspaceKeys(keyPreRe)
            return keyPreRe
    return keyPreRe

def makefile(keypress, keyrelease):
    keypress2 = backspaceKeys(keypress)
    keyrelease2 = backspaceKeys(keyrelease)
    digraphLetters = digraphletters(keypress2, keyrelease2)
    digraphTime = digraphtime(keypress2,keyrelease2)
    for i in range(len(digraphTime)):
        f = open("{}.txt".format(digraphLetters[i]), "a")
        if os.path.getsize("{}.txt".format(digraphLetters[i])) > 0:
            f.write("\n" + str(digraphTime[i]))
        else:
            f.write(str(digraphTime[i]))



#text = ["Jakaka"]
#TextDokumentowy = 


i=1
for textlist in open('./textEXMPL.txt', 'r').readlines():
    print("Entry", i, "text: ")
    print(textlist)
    keyPressData = []
    keyReleaseData = []
    with Listener(on_press=callb, on_release=callb1) as listener:
        x = input()
        listener.join()
    i += 1
    x=''
    clear_screen()
    print(keyPressData)
    print(keyReleaseData)
    print(digraphtime(keyPressData, keyReleaseData))
    print(digraphletters(keyPressData, keyReleaseData))
    makefile(keyPressData, keyReleaseData)


