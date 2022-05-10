import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

housing = pd.read_csv('saved.csv')# csv 파일 읽어로기

temp = housing['temperature'] # 온도 데이터 만 추출
humi = housing['humidity'] #습도 데이터만 추출
tall =housing['tall'] # 키 데이터만 추출

df=pd.concat([temp, humi, tall], axis =1) # 합쳐서 데이터 프레임으로 읽어오기 (판다스)


corr_order = df.corr().loc[:'temperature', 'tall'].abs().sort_values(ascending=False) # 정렬하기. 

# print(corr_order)
# plot_cols = ['tall', 'temperature', "humidity"]
# plot_df = df.loc[:, plot_cols]
# plot_df.head()

# plt.figure(figsize=(10,10))
# for idx, col in enumerate(plot_cols[1:]):
#   ax1=plt.subplot(2, 2, idx+1)
#   sns.regplot(x=col, y=plot_cols[0], data=plot_df, ax=ax1)
# plt.show()

# sns.displot(x= 'Target', kind='hist', data=df)
# plt.show()

# from sklearn.preprocessing import MinMaxScaler
# scaler=MinMaxScaler()

# df_scaled=df.iloc[:, :-1]   #마지막열임을 나타내는 -1은 포함하지 않음
# scaler.fit(df_scaled)
# df_scaled=scaler.transform(df_scaled)

# #스케일링 변환된 값을 데이터프레임에 반영
# df.iloc[:, :-1]=df_scaled[:, :]
# print(df.head())

from sklearn.model_selection import train_test_split
x = df[['temperature', 'humidity']]
y = df['tall']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)
# print(x_train.shape, y_train.shape)
# print(x_test.shape, y_test.shape)

# from sklearn.linear_model import LinearRegression # 리니어 리그레서
# lr=LinearRegression() # 모델
# lr.fit(x_train, y_train) # 훈련
# y_test_pred=lr.predict(x_test) # 테스트 데이터 입력
# #############################################################################
# from sklearn.tree import DecisionTreeRegressor #그냥 디시전 트리

# model = DecisionTreeRegressor(max_depth=5) #트리의 깊이 지정 및 모델 지정

# from sklearn.ensemble import RandomForestRegressor    # 랜덤포레스트 사용

# model = RandomForestRegressor(n_estimators = 200)  #나무의 그루 수 및 모델 지정

from sklearn.svm import SVR # 서포트벡터 리그레서
model = SVR() #모델 지정하기
#######################################################################
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

result = pd.DataFrame({'pred' : y_pred, 'real' : y_test})

result.head()

result['ratio(%)'] = abs((result['pred'] - result['real']) / result['real']) * 100

print(result)

mean_ratio = np.mean(result['ratio(%)'])

print(mean_ratio)

x_testing = ([[16., 30.]])

y_predict = model.predict(x_testing)
print(y_predict)


#예측값과 실제값의 분포
plt.figure(figsize=(10, 5)) #표 크기 지정
plt.scatter(x_test['LSTAT'], y_test, label='y_test')  #파란점, 실제값
plt.scatter(x_test['LSTAT'], y_test, c='r', label='y_pred')  #빨간점, 예측값
plt.legend(loc='best')  #범례(오른쪽 상단 박스)가 표시되는 위치 지정
plt.show()

