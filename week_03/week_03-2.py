import cv2
import numpy as np
import matplotlib.pyplot as plt


resim = cv2.imread('deneme.png')
gri_resim=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
histogram=cv2.calcHist([gri_resim],[0],None,[256],[0,256])

plt.bar(range(256),histogram.flatten())
plt.show()

yeni_goruntu= np.clip(gri_resim-100,0,255)
histogram2=cv2.calcHist([yeni_goruntu],[0],None,[256],[0,256])
plt.bar(range(256),histogram2.flatten())
plt.show()
