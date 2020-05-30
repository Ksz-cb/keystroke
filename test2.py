import numpy as np
import matplotlib.pyplot as plt
from pynput.keyboard import Key, Listener
import time
import os


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

# def authenticate(keypress, keyrelease):
#     keypress2 = backspaceKeys(keypress)
#     keyrelease2 = backspaceKeys(keyrelease)
#     digraphLetters = digraphletters(keypress2, keyrelease2)
#     digraphTime = digraphtime(keypress2,keyrelease2)
#     for i in range(len(digraphTime)):
#         for fname in os.listdir('./adam'):
#             if digraphLetters[i] in fname:
#                 data_file = open(filepath, 'r')
#                 data1 = []
#                 for line in data_file:
#                     data1.extend([float(i) for i in line.split()])
#                     mu = np.mean(exam_data1)
#                     sigma = np.std(exam_data1)


def licz():
    filepath = "./el.txt"

    exam_data_file = open(filepath, 'r')
    exam_data1 = []

    for line in exam_data_file:
        exam_data1.extend([float(i) for i in line.split()])

    print(exam_data1)

    print(np.mean(exam_data1))
    print(np.std(exam_data1))

    mu = np.mean(exam_data1)
    sigma = np.std(exam_data1)
    return mu, sigma

#text = ["Jakaka"]
#TextDokumentowy =


i=1
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
    print(keyPressData)
    print(keyReleaseData)
    print(digraphtime(keyPressData, keyReleaseData))
    print(digraphletters(keyPressData, keyReleaseData))
    keypress2 = backspaceKeys(keyPressData)
    keyrelease2 = backspaceKeys(keyReleaseData)
    digraphLetters = digraphletters(keypress2, keyrelease2)
    digraphTime = digraphtime(keypress2, keyrelease2)
    print(digraphLetters)
    print(digraphTime)
    for j in range(len(digraphTime)):
        if digraphLetters[j] == 'el':
            meanlist.append(digraphTime[j])

    #authenticate(keyPressData, keyReleaseData)

print(meanlist)
print(np.mean(meanlist))
print(np.std(meanlist))

mu, sigma = licz()

# print(abs(mu - np.mean(s)) < 0.01)
# print(abs(sigma - np.std(s, ddof=1)) < 0.01)
#
# count, bins, ignored = plt.hist(s, 30, density=True)
# plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
#              np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
#        linewidth=2, color='r')
# plt.show()

