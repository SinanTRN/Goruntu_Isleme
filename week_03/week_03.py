import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread('deneme.png', cv2.IMREAD_GRAYSCALE)


ortalama,stdSapma= cv2.meanStdDev(resim)

print(f"ortalama :{ortalama}")
print(f"standart sapma: {stdSapma}")

#enk,enb,enk_yer,enb_yer=cv2.minMaxLoc(resim)
#print(f"enk : {enk} pixel: {enk_yer}")
#print(f"enb : {enb} pixel: {enb_yer}")

#cv2.imshow('Image', resim)
#cv2.waitKey()

toplam=0
artis_mik=50
resim = resim.astype(np.int32)  # Verileri int32 yaparak taşmayı önleyin
for x in range(resim.shape[0]):
    for y in range(resim.shape[1]):
        toplam += resim[x][y]

print(f"toplam : {toplam}")

for x in range(resim.shape[0]):
    for y in range(resim.shape[1]):
        yenideger= resim[x, y] + artis_mik
        if yenideger>255:
            resim[x, y] = 255
        elif(yenideger<0):
            resim[x, y] = 0
        else:
            resim[x, y] = resim[x, y]+artis_mik


resim = np.clip(resim, 0, 255).astype(np.uint8)
cv2.imshow('resim',resim)
cv2.waitKey()

histogram = np.zeros(256,dtype=np.uint8)

for x in range(resim.shape[0]):
    for y in range(resim.shape[1]):
        gri_seviye=resim[x][y]
        histogram[gri_seviye] = histogram[gri_seviye] + 1

plt.plot(histogram)
#plt.bar(range(256),histogram.flatten())
plt.show()