import numpy as np
import cv2
import matplotlib.pyplot as plt

image = cv2.imread('redpoint.png') # 이미지 파일을 컬러로 불러옴

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.subplot(221),plt.imshow(image),plt.title('Input')

plt.plot( marker='.', color='r', ls='')


circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 50,
                               param1=150, param2=40, minRadius=1, maxRadius=100)
dst = gray.copy()

if circles is not None:
    for i in range(circles.shape[1]):
        cx, cy, radius = circles[0][i]  
        print(cx, cy)

cv2.imshow('img', dst)
plt.show()