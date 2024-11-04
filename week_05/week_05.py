#image filter
from pickletools import uint8

import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread('coins.png')
gri_resim=cv2.cvtColor(resim,cv2.COLOR_BGR2GRAY)
histogram=cv2.calcHist([gri_resim],[0],None,[256],[0,256])

# Zero padding: görüntü kenarlarına sıfır ekleyerek genişletme. filtrenin boyutunun 1 eksiği/2 kadar kenara sıfır eklenir.

h=np.array([[2, 5, 1],[-2, 2, -4],[3, -5, 2]])
filtre_resim=np.zeros_like(gri_resim)

#konvolüsyon işlemi
# for sat in range(1,gri_resim.shape[0]-1):
#     for sut in range(1,gri_resim.shape[1]-1):
#         bolge=gri_resim[sat-1:sat+2,sut-1:sut+2]
#         sonuc=np.sum(h*bolge)
#         filtre_resim[sat,sut]=sonuc


# filtre_resim[10,20] = (gri_resim[10,20]*h[1,1] + gri_resim[10-1,20-1]*h[0,0]+
#                        gri_resim[10-1,20]*h[0,1]+gri_resim[10-1,20+1]*h[0,2]+
#                        gri_resim[10,20-1]*h[1,0]+gri_resim[10,20+1]*h[1,2]+
#                        gri_resim[10+1,20-1]*h[2,0]+gri_resim[10+1,20]*h[2,1]+
#                        gri_resim[10+1,20+1]*h[2,2])

# x=10
# y=20
# filtre_resim[x,y]=(gri_resim[x,y]*h[1,1]+gri_resim[x-1,y-1]*h[0,0]+gri_resim[x-1,y]*h[0,1]+
#                    gri_resim[x-1,y+1]*h[0,2]+gri_resim[x,y-1]*h[1,0]+gri_resim[x,y+1]*h[1,2]+
#                    gri_resim[x+1,y-1]*h[2,0]+gri_resim[x+1,y]*h[2,1]+gri_resim[x+1,y+1]*h[2,2])

# for x in range(1,gri_resim.shape[0]-1):
#     for y in range(1,gri_resim.shape[1]-1):
#         # filtre_resim[x,y]=(gri_resim[x,y]*h[1,1]+gri_resim[x-1,y-1]*h[0,0]+gri_resim[x-1,y]*h[0,1]+
#         #                    gri_resim[x-1,y+1]*h[0,2]+gri_resim[x,y-1]*h[1,0]+gri_resim[x,y+1]*h[1,2]+
#         #                    gri_resim[x+1,y-1]*h[2,0]+gri_resim[x+1,y]*h[2,1]+gri_resim[x+1,y+1]*h[2,2])
#         patch=gri_resim[x-1:x+2,y-1:y+2]
#         filtre_resim[x,y]=np.sum(h*patch)

#fonksiyon ile
# filtre_resim= cv2.filter2D(gri_resim,-1,h)

#ones filter(görüntüyü yumuşatma)
# h2=(1/25)*np.ones((5,5),dtype='uint8')
# h3=(1/49)*np.ones((7,7),dtype='uint8')
# filtre_resim= cv2.filter2D(gri_resim,-1,h3)

#gaussian filter(görüntüyü yumuşatma)
# h4=cv2.getGaussianKernel(5,1)
# # filtre_resim= cv2.filter2D(gri_resim,-1,h4)
# filtre_resim=cv2.GaussianBlur(gri_resim,(7,7),2)

#sobel filter(görüntü kenarlarını belirleme)
# h5=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
# h6=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
# filtre_resim=cv2.Sobel(gri_resim,None,1,0,ksize=3)
# filtre_resim2=cv2.Sobel(gri_resim,None,0,1,ksize=3)
# filtre_resim3=cv2.Sobel(gri_resim,None,1,1,ksize=3)

#laplacian filter(görüntüdeki kenarları belirleme)
# h7=np.array([[0,1,0],[1,-4,1],[0,1,0]])
# filtre_resim=cv2.Laplacian(gri_resim,None)

#Laplace ile keskinleştirme: gri_resim+laplace

#median filter(görüntüdeki gürültüyü azaltma)
filtre_resim=cv2.medianBlur(gri_resim,7)


cv2.imshow('Image', gri_resim)
cv2.imshow('Image-2',filtre_resim)
# cv2.imshow('Image-3', filtre_resim2)
# cv2.imshow('Image-4', filtre_resim3)
cv2.waitKey()