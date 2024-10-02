import cv2
import numpy as np
#
# resim=cv2.imread('profil.jpg')
#
# cv2.imshow('Image',resim)
# cv2.waitKey()

#resim = cv2.imread('deneme.png')

#B, G, R = cv2.split(resim)

# resim[: , :,1]=0
# resim[: , :,2]=0
#
# cv2.imshow('Kırmızı Bant', resim)
# cv2.waitKey()

#resim = cv2.imread('deneme.png', cv2.IMREAD_GRAYSCALE)
# cv2.imshow('Image', resim)
# cv2.waitKey()

# R, G, B --> Gri
# gri =(R+G+B)/3
# gri = 0.59*R + 0.30*G + 0.11*B

# resim = cv2.imread('deneme.png')
# #deger = resim[100, 100]
# # deger = resim[200:250, 250:300]
# # print(deger)
#
# resim2 = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
# renkli2 = cv2.cvtColor(resim2, cv2.COLOR_GRAY2BGR)
#
# print(f"BGR Karşılığı={resim[100,100]}")
# print(f"Gri Karşılığı={resim2[100,100]}")
# print(f"Yalancı BGR Karşılığı={renkli2[100,100]}")
#
# resim2[100:150, 120:190]
# cv2.imshow('Image', resim2)
# cv2.waitKey()

#-----------------------------------------------------------------------

# resim1 = np.zeros((500,500),'uint8')
# resim1[150:250, 200:400]=255
#
# resim2 = np.zeros((500,500),'uint8')
# resim2[200:350, 300:450]=255
# resim3= cv2.add(resim1,resim2)
# print(resim3[220,320])
# cv2.imshow('resim1', resim1)
# cv2.imshow('resim2', resim2)
# cv2.imshow('resim3', resim3)
# cv2.waitKey()

#-----------------------------------------------------------------------
# resim1 = np.zeros((500,500),'uint8')
# resim1[150:250, 200:400]=120
#
# resim2 = np.zeros((500,500),'uint8')
# resim2[200:350, 300:450]=120
# resim3= cv2.add(resim1,resim2)
# print(resim3[220,320])
# cv2.imshow('resim1', resim1)
# cv2.imshow('resim2', resim2)
# cv2.imshow('resim3', resim3)
# cv2.waitKey()

#-----------------------------------------------------------------------
# resim1 = np.zeros((500,500),'uint8')
# resim1[150:250, 200:400]=120
#
# resim2 = np.zeros((500,500),'uint8')
# resim2[200:350, 300:450]=120
# resim3= cv2.subtract(resim1,resim2)
# print(resim3[220,320])
# cv2.imshow('resim1', resim1)
# cv2.imshow('resim2', resim2)
# cv2.imshow('resim3', resim3)
# cv2.waitKey()

# #-----------------------------------------------------------------------

# resim1 = np.zeros((500,500),'uint8')
# resim1[150:250, 200:400]=120
#
# resim2 = np.zeros((500,500),'uint8')
# resim2[200:350, 300:450]=120
# resim3= cv2.addWeighted(resim1,0.6,resim2,0.4,1)
# print(resim3[220,320])
# cv2.imshow('resim1', resim1)
# cv2.imshow('resim2', resim2)
# cv2.imshow('resim3', resim3)
# cv2.waitKey()

#-----------------------------------------------------------------------

# resim1 = np.zeros((500,500),'uint8')
# resim1[150:250, 200:400]=100
#
# resim2 = np.zeros((500,500),'uint8')
# resim2[200:350, 300:450] = 200
# resim3= cv2.addWeighted(resim1, 0.5, resim2, 0.5, 1)
# print(resim3[220,320])
# cv2.imshow('resim1', resim1)
# cv2.imshow('resim2', resim2)
# cv2.imshow('resim3', resim3)
# cv2.waitKey()

#-----------------------------------------------------------------------

# resim1 = np.zeros((500,500),'uint8')
# resim1[150:250, 200:400]=127
#
# resim2 = np.zeros((500,500),'uint8')
# resim2[200:350, 300:450]=127
# resim3= cv2.bitwise_and(resim1, resim2)
# print(resim3[220,320])
# cv2.imshow('resim1', resim1)
# cv2.imshow('resim2', resim2)
# cv2.imshow('resim3', resim3)
# cv2.waitKey()

#-----------------------------------------------------------------------

# resim1 = np.zeros((500,500),'uint8')
# resim1[150:250, 200:400]=100
#
# resim2 = np.zeros((500,500),'uint8')
# resim2[200:350, 300:450]=200
# resim3= cv2.bitwise_and(resim1, resim2)
# print(resim3[220,320])
# cv2.imshow('resim1', resim1)
# cv2.imshow('resim2', resim2)
# cv2.imshow('resim3', resim3)
# cv2.waitKey()

#-----------------------------------------------------------------------


# resim1 = np.zeros((500,500),'uint8')
# resim1[150:250, 200:400]=100
#
# resim2 = np.zeros((500,500),'uint8')
# resim2[200:350, 300:450]=200
# resim3= cv2.bitwise_or(resim1, resim2)
# print(resim3[220,320])
# cv2.imshow('resim1', resim1)
# cv2.imshow('resim2', resim2)
# cv2.imshow('resim3', resim3)
# cv2.waitKey()

#-----------------------------------------------------------------------

# resim1 = np.zeros((500,500),'uint8')
# resim1[150:250, 200:400]=255
#
# resim2 = np.zeros((500,500),'uint8')
# resim2[200:350, 300:450]=255
# resim3= cv2.bitwise_xor(resim1, resim2)
# print(resim3[220,320])
# cv2.imshow('resim1', resim1)
# cv2.imshow('resim2', resim2)
# cv2.imshow('resim3', resim3)
# cv2.waitKey()

#-----------------------------------------------------------------------
# resim1 = np.zeros((500,500),'uint8')
# resim1[150:250, 200:400]=255
#
# resim2 = np.zeros((500,500),'uint8')
# resim2[200:350, 300:450]=255
# resim3= cv2.bitwise_not(resim1)
# print(resim3[220,320])
# cv2.imshow('resim1', resim1)
# cv2.imshow('resim2', resim2)
# cv2.imshow('resim3', resim3)
# cv2.waitKey()

#-----------------------------------------------------------------------

resim = cv2.imread('deneme.png')
resim2= cv2.bitwise_not(resim)
cv2.imshow('resim1', resim)
cv2.imshow('resim2', resim2)
cv2.waitKey()
