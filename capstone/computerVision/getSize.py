#####################
#실행 전 가상환경 실행하기 capstone 경로에서 source bin/activate로 실행!!!!!!!!!!!
#아나콘다 프롬프트 열고 conda activate capstone 후 code 로 vscode실행 그리고 코드에서 우클릭 후 RUN PYTHON FILE IN TERMINAL로 실해하기
#####################
import numpy as np
import matplotlib.pyplot as plt
import cv2

def getImage():
    image = cv2.imread("capstone\computerVision\hi.jpg")#이미지 읽기r
    image = cv2.resize(image, dsize=(640,480))
    plt.subplot(231),plt.imshow(image),plt.title('Input')
    return image

def getBlur(image):
    blur = cv2.blur(image,(5,8))
    return blur

def getgray(image):  
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plt.subplot(235),plt.imshow(gray, cmap='gray'),plt.title('gray')
    return gray

def getCircleCenterPoint(image): #graysclae을 인풋으로 넣어줘야 함!!!!!!!!!!!!!!!!!!!!!
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 300,
                               param1=200, param2=30, minRadius=40, maxRadius=150)
    print(circles)
    
    point = [[0,0],[0,0],[0,0],[0,0]]

    # 원 중심 좌표 얻은 리스트로 작은 원을 그려서 표시
    if circles is not None:
        for i in range(circles.shape[1]):
            cx, cy, radius = circles[0][i]
            point[i] = [cx, cy]

    rows,cols = image.shape

    #point = [[45,140],[600,67],[50,986],[612,1051]]

    pts1 = np.float32(point)
    rightUnderPoint = [pts1[0][0],pts1[1][1]] 
    leftUpperPoint = [pts1[1][0],pts1[0][0]]
    pts1[2]=rightUnderPoint
    pts1[3]=leftUpperPoint
    
    return pts1

def tiltAndCrop(pts1, image): #원의 중심좌표 있는거로 넣어줄 것. 입력은 블러 이미지로 인풋!!!!!!!
    pts2 = np.float32([[0,0],[150,175],[0,175],[150,0]]) #일단은 변수를 하드코딩으로 넣었지만 나중에 자동으로 계산해서 넣을 수 있게 하기.
    if(pts1.min() == 0.0):
        return("error")

    M = cv2.getPerspectiveTransform(pts1,pts2)# a4용지에 맞춰서 tilt, crop한다.

    dst = cv2.warpPerspective(image,M,(175,150))# a4용지에 맞춰서 tilt, crop한다.
    plt.subplot(232),plt.imshow(dst),plt.title('Output')
    return dst

def getMask(image): #인풋을 dst로 줘야함.
    img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) # cvtColor 함수를 이용하여 hsv 색공간으로 변환5
    lower_green = np.array([32, 80, 80]) # hsv 이미지에서 바이너리 이미지로 생성 , 적당한 값 30
    upper_green = np.array([75, 255, 255])
    img_mask = cv2.inRange(img_hsv, lower_green, upper_green) # 범위내의 픽셀들은 흰색, 나머지 검은색
    plt.subplot(233),plt.imshow(img_mask),plt.title('mask')
    return img_mask

def getTall(img_mask): # 키 구하는 함수 마스크를 인풋으로 줘야함!
    cardCanny = cv2.Canny(img_mask,100,550)

    corners = cv2.goodFeaturesToTrack(cardCanny, 100, 0.1, 0, blockSize=5, useHarrisDetector=True, k =0.03) # 엣지 디텍션 하기. 
    #print(corners)
    
    #root  # 뿌리 부근 좌표 리스트
    #leaf # 이파리 끝 부분 좌표 리스트
    total = []
    
    for i in range(len(corners)): 
        temp = corners[i][0][1]
        total.append(temp)
        
    uppertemp = []
    lowertemp = []
        
    total.sort()
    uppertemp = total
    leaf = sum(uppertemp[0:5])

    total.reverse()
    lowertemp = total
    root = sum(lowertemp[0:5])

    rootstartavg = root / 5
    leafstartavg = leaf / 5
    tall = rootstartavg - leafstartavg
    tall = tall.__round__(2)
    print("키는:",tall)
    return(tall)

def erroroccur():
    print("원인식 불가")
    return 1

if __name__ == "__main__":
    print("직접 실행")
    image = getImage()
    blur = getBlur(image)
    blurgray = getgray(blur)
    points = getCircleCenterPoint(blurgray)
    dst = tiltAndCrop(points, image)
    if(dst == "error"):
        print("원 인식 실패")
    imagemask = getMask(dst)
    tall = getTall(imagemask)

    plt.show()
else:
    print("임포트되어 사용됨")
    print(__name__)