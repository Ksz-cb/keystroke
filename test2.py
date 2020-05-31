import numpy as np
import matplotlib.pyplot as plt
from pynput.keyboard import Key, Listener
import time
import os


def callb(key):
    t = time.time()

    if key != Key.enter:
        keyPressData.append("{0}-{1}".format(key,t))


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
    directory = "./adam/"
    data_file = open(directory + digraph, 'r+')
    data1 = []
    for line in data_file:
        data1.extend([float(i) for i in line.split()])

    mu = np.mean(data1)
    sigma = np.std(data1)

    return mu, sigma


def authenticate(digraphtime, digraphletters):
    score = 50
    for i in range(len(digraphtime)):
        mu, sigma = licz("{}.txt".format(digraphletters[i]))
        if mu - sigma < digraphtime[i] < mu + sigma:
            score += 2
        else:
            score -= 10
        print(score)


i=1
score = 50
meanlist= []
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
    # print(keyPressData)
    # print(keyReleaseData)
    # print(digraphtime(keyPressData, keyReleaseData))
    # print(digraphletters(keyPressData, keyReleaseData))
    keypress2 = backspaceKeys(keyPressData)
    keyrelease2 = backspaceKeys(keyReleaseData)
    digraphLetters = digraphletters(keypress2, keyrelease2)
    digraphTime = digraphtime(keypress2, keyrelease2)
    print(digraphLetters)
    print(digraphTime)
    authenticate(digraphTime, digraphLetters)