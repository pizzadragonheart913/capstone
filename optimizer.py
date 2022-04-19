import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets
from sklearn import linear_model

housing = pd.read_csv("saved.csv")

temp = pd.DataFrame(housing['temperature'], columns=['temperature'])
humi = pd.DataFrame(housing['humidity'], columns=['humidity'])
target = pd.DataFrame(housing['tall'], columns=['tall'])

df=pd.concat([temp, humi, target], axis =1)

corr_order = df.corr().loc[:'temperature', 'tall'].abs().sort_values(ascending=False)


plot_cols = ['tall', 'temperature', "humidity"]
plot_df = df.loc[:, plot_cols]
plot_df.head()

x1 = df['temperature']
x2 = df['humidity']
y = df['tall']

plt.scatter(x1, y)
fplot1 = np.polyfit(x1, y,30) 
plt.scatter(x2, y)
fplot1 = np.polyfit(x2, y,30) 
data = []

for a in range(len(x1)):
    for bin in range(1):
        tempx = x1[a]
        tempy = y[a]
        temp = [tempx, tempy]
        data.append(temp)

data.sort()

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
X = [[x1[k]**n for n in range(1,5)] for k in range(len(data))]

reg = linear_model.LinearRegression()

reg.fit(X, y)
print(reg.intercept_)
print(reg.coef_)

xp = [0.1 * k for k in range(506)]
Xp = [[xp[k]**n for n in range(1,5)] for k in range(506)]
yp = reg.predict(Xp)
print(reg.score(X,y))
plt.plot(x1, y, 'g.')
plt.plot(xp, yp, 'k')

plt.xlim(10,35)
plt.ylim(0,8)

plt.show()
#############################################################################
 