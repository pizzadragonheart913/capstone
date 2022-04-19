import cv2
import matplotlib.pyplot as plt
import numpy as np

def getResult(Path):
    image = cv2.imread(Path)
    
    # image = cv2.imread("capstone\computerVision\sprout.jpg")#이미지 읽기r
    image = cv2.resize(image, dsize=(720,720))
    print('shape : ', image.shape)

    height, width = image.shape[:2]

    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green = (10, 20, 20)
    upper_green = (75, 255, 255)

    image_mask = cv2.inRange(image_hsv, lower_green, upper_green) # 범위내의 픽셀들은 흰색, 나머지 검은색

    reverse = image_mask.copy()
    reverse = 255 - reverse

    ret, imthres = cv2.threshold(reverse, 127, 255, cv2.THRESH_BINARY_INV)

    contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    contourlist =[]

    # for j in contour:
    #     if(len(j) > 20):
    #         contourlist.append(j)
    #     else:
    #         continue

    for j in contour:
        if((cv2.contourArea(j)>10) and (cv2.contourArea(j)<1000)):
            contourlist.append(j)
        else:
            continue

    print('도형의 갯수: %d'% (len(contourlist)))

    for i in contourlist:
        for j in i:
            cv2.circle(image, tuple(j[0]), 1, (255,0,0), -1) 

    cv2.imshow("out", image)


    ##############################################################################
    # image_result = cv2.bitwise_and(image, image, mask= image_mask)

    # cardCanny = cv2.Canny(image_mask,100,550)
    # corners = cv2.goodFeaturesToTrack(cardCanny, 100, 0.1, 15, blockSize=5, useHarrisDetector=True, k =0.03) # 엣지 디텍션 하기. 

    # total = []
    # for i in range(len(corners)): # 119 이상이면 풀의 대가리 , 80 이하면 풀의 뿌리 끝점
    #     tempx = corners[i][0][0]
    #     tempy = corners[i][0][1]
    #     temp = [tempx, tempy]
    #     total.append(temp)

    if(len(contourlist) > 10):
        print("새싹이 있어요!!")
    else:
        print("새싹 없음 ㅜㅜ")
        
    cv2.waitKey(0)

    # #############################################################################
    # plt.subplot(131),plt.imshow(image),plt.title('Input')
    # plt.subplot(132),plt.imshow(image_mask),plt.title('MASK')
    # # plt.subplot(133),plt.imshow(image_result),plt.title('result')

    # plt.show()
    
    

if __name__ == "__main__":
    print("직접 실행")
    result = getResult("capstone\computerVision\sprout.jpg")
else:
    print("임포트되어 사용됨")
    print(__name__)