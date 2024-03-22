
import pandas as pd
train=pd.read_csv("train.csv")
train.head()

import pandas as pd
test=pd.read_csv("test.csv")
test.head()

train['temp'].describe()

train['weather'].describe()

train.info()

train2 = train.drop(['datetime' , 'casual' , 'registered' , 'count'], axis= 1 )
train2.head()

test2 = test.drop(['datetime'], axis= 1 )
test2.head()

from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()
#train 데이터로 학습시키기
rf.fit(train2, train["count"])
#test2로 예측하기
result = rf.predict(test2)
test["count"] = result
test.head()