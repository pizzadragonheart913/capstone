import cv2
import matplotlib.pyplot as plt

image = cv2.imread("capstone\computerVision\hi.jpg")
plt.subplot(233),plt.imshow(image),plt.title('mask')

plt.show()