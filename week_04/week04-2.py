import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread('tire.png')
gri_resim=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
histogram=cv2.calcHist([gri_resim],[0],None,[256],[0,256])


#kümülatif histogram fonksiyonu ile
# histogram_kum=np.cumsum(histogram)

#kümülatif histogram

sat, sut = gri_resim.shape
toplam_pikel = sat * sut
print("Toplam piksel sayısı: ", toplam_pikel)

kum_hist= np.zeros(256)
kum_hist[0]=histogram[0].item()
for i in range(1,256):
    kum_hist[i]=np.round(kum_hist[i-1].item()+histogram[i].item())

kum_hist=np.round(kum_hist*255/toplam_pikel).astype(np.uint8)

yeni_resim=np.zeros_like(gri_resim)
for sat in range(gri_resim.shape[0]):
    for sut in range(gri_resim.shape[1]):
        yeni_resim[sat][sut]=kum_hist[gri_resim[sat][sut]]

histogram2=cv2.calcHist([yeni_resim],[0],None,[256],[0,256])
plt.bar(range(256),histogram.flatten())
plt.show()
plt.bar(range(256),histogram2.flatten())
plt.show()

yeni_resim2=cv2.normalize(gri_resim,None,0,255,cv2.NORM_MINMAX)

yeni_resim3=cv2.equalizeHist(gri_resim)# opencv ile histogram eşitleme

yeni_resim4= cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8)).apply(gri_resim) #CLAHE(Contrast Limited Adaptive Histogram Equalization)

cv2.imshow('germe', yeni_resim2)
cv2.imshow('orijinal', gri_resim)
cv2.imshow('esitleme', yeni_resim)
cv2.imshow('openCv ile eşitleme', yeni_resim3)
cv2.imshow('CLAHE', yeni_resim4)
cv2.waitKey()