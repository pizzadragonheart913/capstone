import cv2
import matplotlib.pyplot as plt
import numpy as np

def getResult():
    
    image = cv2.imread("capstone\computerVision\sprout.jpg")#이미지 읽기r
    image = cv2.resize(image, dsize=(720,720))
    print('shape : ', image.shape)

    height, width = image.shape[:2]

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green = (30, 50, 100)
    upper_green = (75, 255, 205)

    
    image_mask = cv2.inRange(image_hsv, lower_green, upper_green) # 범위내의 픽셀들은 흰색, 나머지 검은색

    reverse = image_mask.copy()
    reverse = 255 - reverse

    ret, imthres = cv2.threshold(reverse, 127, 255, cv2.THRESH_BINARY_INV)

    contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contourlist =[]

    for j in contour:
        if((cv2.contourArea(j)>10) and (cv2.contourArea(j)<100000)):
            contourlist.append(j)
        else:
            continue

    print('도형의 갯수: %d'% (len(contourlist)))

    for i in contourlist:
        for j in i:
            cv2.circle(image, tuple(j[0]), 1, (255,0,0), -1) 

    cv2.imshow("out", image)

    if(len(contourlist) > 10):
        print("새싹이 있어요!!")
    else:
        print("새싹 없음 ㅜㅜ")
        
    cv2.waitKey(0)

    # #############################################################################
    plt.subplot(131),plt.imshow(image),plt.title('Input')
    plt.subplot(132),plt.imshow(image_mask),plt.title('MASK')
    # plt.subplot(133),plt.imshow(image_result),plt.title('result')

    plt.show()
    
    
getResult()
