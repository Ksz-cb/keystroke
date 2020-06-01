import numpy as np
import matplotlib.pyplot as plt
from pynput.keyboard import Key, Listener
import time
import os


def callb(key):
    t = time.time()

    if key != Key.enter:
        keyPressData.append("{0}-{1}".format(str(key),t))


def callb1(key):
    t = time.time()

    if key != Key.enter:
        keyReleaseData.append("{0}-{1}".format(str(key), t))
    else:
        return False


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


def licz(digraph):
    directory = "./" + user + "/"
    try:
        data_file = open(directory + digraph, 'r+')
        data1 = []
        for line in data_file:
            data1.extend([float(i) for i in line.split()])

        mu = np.mean(data1)
        sigma = np.std(data1)

        return mu, sigma
    except FileNotFoundError:
        mu = 0
        sigma = 0
        return mu, sigma


def authenticate(digraphtime, digraphletters):
    global score
    for i in range(len(digraphtime)):
        mu, sigma = licz("{}.txt".format(digraphletters[i]))
        if mu == 0 and sigma == 0:
            continue
        else:
            if mu - 2*sigma < digraphtime[i] < mu + 2*sigma:
                score += 2
            else:
                score -= 10
            print(score)


keyPressData = []
keyReleaseData = []
run2 = True
i=1
# password = "UvJeh*c!5y"
password = "u"
meanlist= []
print("Zaloguj sie")
user = input("Podaj nazwe profilu: ")

if os.path.isdir('./' + user):
    while run2:
        score = 50
        password2 = input("Podaj hasło do profilu: ")
        if password == password2:
            while score > 0:
                keyPressData = []
                keyReleaseData = []
                with Listener(on_press=callb, on_release=callb1) as listener:
                    listener.join()
                i += 1
                # print(keyPressData)
                # print(keyReleaseData)
                # print(digraphtime(keyPressData, keyReleaseData))
                # print(digraphletters(keyPressData, keyReleaseData))
                keypress2 = backspaceKeys(keyPressData)
                keyrelease2 = backspaceKeys(keyReleaseData)
                digraphLetters = digraphletters(keypress2, keyrelease2)
                digraphTime = digraphtime(keypress2, keyrelease2)
                # print(digraphLetters)
                # print(digraphTime)
                authenticate(digraphTime, digraphLetters)
                print(score)
                if score <= 0:
                    continue
        else:
            print("Błędne hasło")
else:
    print("Nie ma takiego profilu")