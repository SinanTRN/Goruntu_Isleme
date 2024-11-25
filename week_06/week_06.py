import cv2
import numpy as np

#fourier dönüşümü
orj_resim = cv2.imread('cameraman.png', cv2.IMREAD_GRAYSCALE)

f_resim=np.fft.fft2(orj_resim)
f_resim=np.fft.fftshift(f_resim)

m,n=f_resim.shape

#en değerli frekansları sıfırlama
# f_resim[m//2:m//2,n//2]=0
# f_resim[m//2-20:m//2+20,n//2-20:n//2+20]=0

mask=np.zeros(f_resim.shape,dtype='uint8')
# mask[m//2-100:m//2+100,n//2-100:n//2+100]=1
# mask[m//2-100:m//2+100,n//2-100:n//2+100]=1
r=100
mask=cv2.circle(mask,(m//2,n//2),r,1,-1)
mask=cv2.circle(mask,(m//2,n//2),3*r//4,0,-1)
mask=1-mask

f_resim=f_resim*mask


g_resim=np.abs(f_resim)
# g_resim=np.abs(f_resim)

g_resim=g_resim/np.max(g_resim)*255

y_resim=np.fft.ifftshift(f_resim)
y_resim=np.fft.ifft2(y_resim)
y_resim=np.abs(y_resim).astype(np.uint8)
y_resim=(y_resim/np.max(y_resim)*255).astype(np.uint8)

cv2.imshow('orjinal',orj_resim)
cv2.imshow('frekans',g_resim)
cv2.imshow('yeni',y_resim)
cv2.imshow('mask',mask*255)
cv2.waitKey()