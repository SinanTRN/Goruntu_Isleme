import cv2
import numpy as np

#fourier dönüşümü
orj_resim = cv2.imread('s_cameraman.png',cv2.IMREAD_GRAYSCALE)

f_resim=np.fft.fft2(orj_resim)
f_resim=np.fft.fftshift(f_resim)

m,n=f_resim.shape

#en değerli frekansları sıfırlama
# f_resim[m//2:m//2,n//2]=0
# f_resim[m//2-20:m//2+20,n//2-20:n//2+20]=0

mask=np.zeros_like(f_resim,dtype='uint8')
mask[m//2-100:m//2+100,n//2-100:n//2+100]=1
mask[m//2-100:m//2+100,n//2-100:n//2+100]=1

f_resim=f_resim*mask


g_resim=np.abs(f_resim)
# g_resim=np.abs(f_resim)

g_resim=g_resim/np.max(g_resim)*255

y_resim=np.fft.ifftshift(f_resim)
y_resim=np.fft.ifft2(y_resim)
y_resim=np.abs(y_resim).astype(np.uint8)

cv2.imshow('orjinal',orj_resim)
cv2.imshow('frekans',g_resim)
cv2.imshow('yeni',y_resim)
cv2.imshow('mask',mask)
cv2.waitKey()