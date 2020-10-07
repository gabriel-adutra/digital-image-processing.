"""
Neste arquivo, faça:

    * Importar as bibliotecas e pacotes
    * Analise os argumentos 'n_clusters' e 'image_path'
    * Carregue uma imagem com opencv e converta-a de bgr para rgb
    * Use o algoritmo k-means para extrair as cores
    * Converta as cores para hexadecimais
    * Imprima as cores em um arquivo com o nome descrito na descrição do projeto


    O uso deve ser:
        python3 colorize.py image_path n_clusters

"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from helper import nested_rgb2hex
from sklearn.cluster import KMeans

variavel = plt.figure()
variavel.add_subplot(222)
img = cv2.imread('data/sonico.jpg')
plt.imshow(img)
variavel.add_subplot(221)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
img = img.reshape(img.shape[0]*img.shape[1], 3)

algo = KMeans(n_clusters=4)
algo.fit(img)
hex = nested_rgb2hex([[int(i) for i in elem] for elem in algo.cluster_centers_])
with open('paleta-sonico.txt', 'w') as f:
    print(hex, file = f)

plt.figure()
plt.scatter(img[::, 0], img[::, 1], img[::,2])
plt.scatter(algo.cluster_centers_[::,0], algo.cluster_centers_[::,1], algo.cluster_centers_[::,2], c='r')
plt.show()
