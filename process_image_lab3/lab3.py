import os
import cv2 as cv
import numpy as np
import glob as gl
from matplotlib import pyplot as plt

def showDFFT(img, fft, name):
    
    magnitude = fft
    magnitude = np.fft.fftshift(magnitude)
    
    plt.subplot(121), plt.imshow(img, 'Greys', vmin = 0, vmax = 255)
    plt.title('Input Image: ' + name), plt.xticks([]), plt.yticks([])
    
    
    M, N = img.shape
    K = 8
    magnitude[M//2-K:M//2 + K,N//2-K:N//2+K] = 0
    
    for i in range(7):
        magnitude[M//2-K-15-(15*i):M//2-15-(15*i) + K,N//2-K+20+(20*i):N//2+K+20+(20*i)] = 0
        magnitude[M//2-K+15+(15*i):M//2+15+(15*i) + K,N//2-K-20-(20*i):N//2+K-20-(20*i)] = 0
        
    f_sh=np.fft.ifftshift(magnitude)
    image_filtered = np.real(np.fft.ifft2(f_sh))

    s_min = magnitude.min()
    s_max = magnitude.max()
    if s_min == s_max:
        plt.subplot(122), plt.imshow(magnitude, 'Greys', vmin = 0, vmax = 255)
    else:
        plt.subplot(122), plt.imshow(image_filtered, 'Greys')
        
    plt.title(name + ' Furie'), plt.xticks([]), plt.yticks([])
    plt.show()

folder_path = r'C:\Users\Dragonsnom\Desktop\new/'
images = gl.glob(folder_path + '*.png')

for full_name in images:
    img = np.float32(cv.imread(full_name, 0))
    name = os.path.basename(full_name)
    showDFFT(img, np.fft.fftn(img), name)


