import numpy as np
import os


def licz():
    directory = './adam/'
    print(directory)
    for file in os.listdir('./adam'):
        data_file = open(directory + file, 'r+')
        data1 = []
        for line in data_file:
            data1.extend([float(i) for i in line.split()])

        mu = np.mean(data1)
        sigma = np.std(data1)

        print(mu)
        print(sigma)

        data_file.truncate(0)
        data_file.close()
        data1 = [i for i in data1 if mu - sigma < i < mu + sigma]
        print(data1)

        f = open(directory + file, "a")

        for j in range(len(data1)):
            if j == len(data1) - 1:
                f.write(str(data1[j]))
            else:
                f.write(str(data1[j]) + "\n")
        f.close()


licz()



