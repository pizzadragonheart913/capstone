import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#보스턴 주택 데이터셋
from sklearn import datasets
housing = datasets.load_boston()

data = pd.DataFrame(housing['data'], columns=housing['feature_names'])
target = pd.DataFrame(housing['target'], columns=['Target'])

df=pd.concat([data, target], axis =1)


corr_order = df.corr().loc[:'LSTAT', 'Target'].abs().sort_values(ascending=False)


plot_cols = ['Target', 'LSTAT', "RM", "PTRATIO", "INDUS"]
plot_df = df.loc[:, plot_cols]
plot_df.head()

# plt.figure(figsize=(10,10))
# for idx, col in enumerate(plot_cols[1:]):
#   ax1=plt.subplot(2, 2, idx+1)
#   sns.regplot(x=col, y=plot_cols[0], data=plot_df, ax=ax1)
# plt.show()

# sns.displot(x= 'Target', kind='hist', data=df)
# plt.show()

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()

df_scaled=df.iloc[:, :-1]   #마지막열임을 나타내는 -1은 포함하지 않음
scaler.fit(df_scaled)
df_scaled=scaler.transform(df_scaled)

#스케일링 변환된 값을 데이터프레임에 반영
df.iloc[:, :-1]=df_scaled[:, :]
# print(df.head())

from sklearn.model_selection import train_test_split
x = df[['LSTAT', 'RM', 'PTRATIO', 'INDUS']]
y = df['Target']

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3)
# print(x_train.shape, y_train.shape)
# print(x_test.shape, y_test.shape)

# from sklearn.linear_model import LinearRegression
# lr=LinearRegression()
# lr.fit(x_train, y_train)
# y_test_pred=lr.predict(x_test)

from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor(max_depth=3)
model.fit(x_train, y_train)

y_perd = model.predict(x_test)

result = pd.DataFrame({'pred' : y_perd, 'real' : y_test})

result['ratio(%)'] = abs((result['pred'] - result['real']) / result['real']) * 100

print(y_test.shape)
print(result.head())

#예측값과 실제값의 분포
# plt.figure(figsize=(10, 5)) #표 크기 지정
# plt.scatter(x_test['LSTAT'], y_test, label='y_test')  #파란점, 실제값
# plt.scatter(x_test['LSTAT'], y_test, c='r', label='y_pred')  #빨간점, 예측값
# plt.legend(loc='best')  #범례(오른쪽 상단 박스)가 표시되는 위치 지정
# plt.show()