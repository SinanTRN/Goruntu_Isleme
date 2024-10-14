import cv2
import numpy as np
import matplotlib.pyplot as plt


resim = cv2.imread('pout.png')
gri_resim=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
histogram=cv2.calcHist([gri_resim],[0],None,[256],[0,256])

min_I_eski=np.min(gri_resim)
max_I_eski=np.max(gri_resim)

min_I_yeni=0
max_I_yeni=255

print(f"min : {min_I_eski}")
print(f"max : {max_I_eski}")

plt.bar(range(256),histogram.flatten())
plt.show()

yeni_resim = np.round((max_I_yeni-min_I_yeni) * ((gri_resim-min_I_eski) / (max_I_eski-min_I_eski)) + min_I_yeni)
yeni_resim=yeni_resim.astype(np.uint8)

histogram2=cv2.calcHist([yeni_resim],[0],None,[256],[0,256])
plt.bar(range(256),histogram2.flatten())
plt.show()

cv2.imshow('Image', resim)
cv2.imshow('Image-2', yeni_resim)
# cv2.waitKey()

# OpenCV ile histogram germe
yeni_resim2=cv2.normalize(gri_resim,None,0,255,cv2.NORM_MINMAX)
cv2.imshow('Image-3', yeni_resim)
cv2.waitKey()