from chefboost import Chefboost as chef
import pandas as pd
df = pd.read_csv("BostonHousing.csv")
predata = pd.read_csv("predictdata.txt")
print(df)
print(predata)
if __name__=='__main__':
    config = {'algorithm': 'C4.5'}
    model = chef.fit(df.copy(), config = config, target_label = 'MEDV')
    print('-----------------------')
    prediction = chef.predict(model, predata.iloc[0])
    print(prediction)
    