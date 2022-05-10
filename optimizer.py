import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn import linear_model
import sympy as sy
########################################
# [!!!!!@중요@!!!!!]중간에 프린트 해놓은거 다 지우고 하기!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#########################################3
def optimizer():
    housing = pd.read_csv("saved.csv")

    temp = pd.DataFrame(housing['temperature'], columns=['temperature'])
    humi = pd.DataFrame(housing['humidity'], columns=['humidity'])
    target = pd.DataFrame(housing['tall'], columns=['tall'])

    df=pd.concat([temp, humi, target], axis =1)

    corr_order = df.corr().loc[:'temperature', 'tall'].abs().sort_values(ascending=False)


    plot_cols = ['tall', 'temperature', "humidity"]
    plot_df = df.loc[:, plot_cols]
    plot_df.head()

    x1 = df['temperature'] #dataframe에서 온도만 추출
    x2 = df['humidity'] #dataframe에서 습도만 추출
    y = df['tall'] #dataframe에서 키만 추출(타깃)

    plt.scatter(x1, y) # 점만 찍기
    fplot1 = np.polyfit(x1, y,30)  # 그림 그리기
    plt.scatter(x2, y) # 습도 데이터 점 찍기
    fplot2 = np.polyfit(x2, y,30)  #습도 데이터 그리기

    datatemp = [] # 온도 리스트
    datahumi = [] # 습도 데이터 리스트
    for a in range(len(x1)): # 온도 정리하는 과정
        for bin in range(1): # 온도 리스트와 습도 리스트를 합쳐서 이차원 리스트로 만듦
            tempx = x1[a]
            tempy = y[a]
            temp = [tempx, tempy]
            datatemp.append(temp)

    for a in range(len(x2)): # 위 반복문과 마찬가지로 습도와 키를 합쳐서 이차원 리스트로 만듦.
        for bin in range(1):
            tempx = x2[a]
            tempy = y[a]
            temp = [tempx, tempy]
            datahumi.append(temp)

    datatemp.sort() #온도 정렬
    datahumi.sort() 

    ####################################################################### 1번블록
    # 그림만 그림.
    # from sklearn.linear_model import LinearRegression

    # def fit_polynomial(x, y, degree): 
    #     model = LinearRegression() 
    #     # np.vander(x, degree+1)은 지정된 x를 1부터 시작해서 x의 N승까지 행
    #     # 렬로 표현해서 입력한 것이다. 
    #     model.fit(np.vander(x, degree + 1), y) 
    #     return model

    # def apply_polynomial(model, x): 
    #     degree = model.coef_.size - 1 
    #     y = model.predict(np.vander(x, degree + 1)) 
    #     return y

    # model = fit_polynomial(x1, y, 6)
    # p_y = apply_polynomial(model, x1)

    # print(p_y)

    # plt.plot(x1, y, 'k.')
    # plt.plot(x1, p_y,'.')
    ########################################################################### 1번블록
    #plt.show()
    ########################################################################## 2번블록
    # 함수 식 찾아내는 거
    XT = [[x1[k]**n for n in range(1,5)] for k in range(len(datatemp))]
    XH = [[x2[k]**n for n in range(1,5)] for k in range(len(datahumi))]

    reg = linear_model.LinearRegression() # 선그려주는 모듈

    reg.fit(XT, y)

    xtp = [0.1 * k for k in range(506)] # 
    Xtp = [[xtp[k]**n for n in range(1,5)] for k in range(506)]
    ytp = reg.predict(Xtp)

    # print(reg.intercept_) # 예측한 함수 식의 상수항 출력
    # print(reg.coef_) # 예측한 함수 식의 각 항 계수를 출력 ()

    tempcoef = list(reg.coef_)
    tempcoef.append(reg.intercept_) #위에서 예측한 계수와 상수를 합쳐서 리스트로 만듦.

    onetofour = [1,2,3,4,0] # 반복문 2중 을 막기 위한 어거지 리스트
    tempequ = ''
    for x in range(5):
        if('-' in str(tempcoef[x])): # 앞자리가 마이너스면 추가 안함
            tempequ += str(tempcoef[x]) +'*x^' + str(onetofour[x])
        else: #양수면 앞에 +추가
            tempequ += '+' + str(tempcoef[x]) +'*x^' + str(onetofour[x])
        
    # print("방정식:", tempequ) #방정식 출력하는 식

    reg.fit(XH, y) # 온도 예측
    xp = [0.1 * k for k in range(506)] # 
    Xp = [[xp[k]**n for n in range(1,5)] for k in range(506)]
    yp = reg.predict(Xp) # 예측 하기

    humicoef = list(reg.coef_) #리스트 만드는 작업
    humicoef.append(reg.intercept_) # "
    #방정식 제조하는 반복문
    humiequ = '' #빈 방정식 문자열
    for x in range(5):
        if('-' in str(humicoef[x])): #
            humiequ += str(humicoef[x]) +'*x^' + str(onetofour[x])  #반복문으로 문자열을 만듦. 방정식임.
        else:# 양수면 앞에 +추가
            humiequ += '+' + str(humicoef[x]) +'*x^' + str(onetofour[x])
            
    # print(reg.intercept_) # 예측한 함수 식의 상수항 출력
    # print(reg.coef_) # 예측한 함수 식의 각 항 계수를 출력 ()

    print("온도 방정식", tempequ)
    print("습도 방정식", humiequ) 

    x = sy.symbols('x') #심볼 x
    ###########################################################################이 블록은 온도 함수를 계산해서 극값을 알려주고 최적의 온도 찾아줌
    ftx = sy.sympify(tempequ) # 방정식을 sympy형식으로 변환
    diffedftx = sy.diff(sy.poly(ftx), x) # 함수를 x에 대해 미분
    tempextreme = sy.solve(diffedftx) # 미분된 함수를 풀어서 극값 계싼
    print(diffedftx) # 극값 한번 출력 해주고
    tempext = [] #이건 극값에 대한 함수값 배열
    tempextvalue = [] #이건 극값
    for j in range(3):
        #if((round(tempextreme[j],2)>0) and round(tempextreme[j],2)<100)
        tempext.append(round(tempextreme[j],2)) # 극값 x값 계산
        tempextvalue.append([round(tempextreme[j], 2), round(ftx.subs(x, tempext[j]), 2)]) #2차원 리스트로 만들어서 극값과 함숫값의 정보를 담아줌
        
        
    print(tempextvalue)
    ############################################################################################
    ##############################################################################################
    fhx = sy.sympify(humiequ) # 방정식을 sympy형식으로 변환
    diffedfhx = sy.diff(sy.poly(fhx), x) # 함수를 x에 대해 미분
    humiextreme = sy.solve(diffedfhx) # 미분된 함수를 풀어서 극값 계싼
    print(diffedfhx) # 극값 한번 출력 해주고
    humiext = [] #이건 극값에 대한 함수값 배열
    humiextvalue = [] #이건 극값
    for j in range(3):
        #if((round(humiextreme[j],2)>0) and round(humiextreme[j],2)<35):
        humiext.append(round(humiextreme[j],2)) # 극값 x값 계산
        humiextvalue.append([round(humiextreme[j], 2), round(fhx.subs(x, humiext[j]), 2)]) #2차원 리스트로 만들어서 극값과 함숫값의 정보를 담아줌
        
    tempextvalue.sort(key=lambda x: (x[0], -x[1]))
    humiextvalue.sort(key=lambda x: (x[0], -x[1]))
    
    returnvalue = []  
    
    for j in humiextvalue:# 습도가 일정 이하여야 최종 데이터 삽입
        if((j[0]>0) and (j[0]<100)):
            continue
        else:
            humiextvalue.remove(j)
            
    
    for j in tempextvalue: #온도도 위와 마찬가지
        if((j[0]>0) and (j[0]<100)):
            continue
        else:
            tempextvalue.remove(j)
    
    print(tempextvalue)
    print(humiextvalue)
    
    returnvalue.append(max(tempextvalue))  #최고의 온도 값 리스트에 삽입
    returnvalue.append(max(humiextvalue))   # 최고의 습도 값 리스트에 삽입
    
    # answer = [returnvalue[0][0], returnvalue[1][0]]
    print(returnvalue)
    ###################################################################################
    plt.plot(x1, y, 'g.') # 그림 그리기 
    plt.plot(x2, y, '.r') 
    plt.plot(xtp, ytp,'c')
    plt.plot(xp, yp, 'k')

    plt.xlim(10,60) # x는 10~ 35
    plt.ylim(0,8) # y는 0~8 까지

    plt.show() #그래프 보여줌
    #############################################################################
    print(returnvalue[0][0])
    print(returnvalue[1][0])
    return returnvalue # 리턴하는 값


optimizer()