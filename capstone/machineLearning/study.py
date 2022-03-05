# import sklearn
# from sklearn.datasets import load_iris
# from sklearn.metrics import accuracy_score
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import KFold, train_test_split
# import pandas as pd
# import numpy as np
# print(sklearn.__version__)
# iris = load_iris()
# iris_df = pd.DataFrame(data = iris.data, columns=iris.feature_names)
# iris_df['label'] = iris.target
# iris_df['label'].value_counts()

# print(iris_df['label'])
# #key = iris.keys()
# #print(key)




# features = iris.data

# label = iris.target

# dt_clf = DecisionTreeClassifier(random_state=156)

# kfold = KFold(n_splits=5)
# cv_accuracy = []

# n_iter = 0

# for train_index, test_index in kfold.split(features):
#     X_train, X_test = features[train_index], features[test_index]
#     y_train, y_test = label[train_index], label[test_index]
    
#     dt_clf.fit(X_train, y_train)
#     pred = dt_clf.predict(X_test)
#     n_iter += 1
    
#     accuracy = np.round(accuracy_score(y_test, pred), 4)
#     train_size = X_train.shape[0]
#     test_size = X_test.shape[0]
    
#     print('\n교차검증 정확도 :{1}, 학습데이터 크기:{2}, 검증데이터 크기: {3}'.format(n_iter, accuracy, train_size, test_size))
#     print('#{0} 검증 세트 인덱스: {1}'.format(n_iter, test_index))
#     cv_accuracy.append(accuracy)
    
# print('\n##평균 검증 정확도: ', np.mean(cv_accuracy))

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, train_test_split
import pandas as pd

iris = load_iris()
iris_data = iris.data

iris_label = iris.target

print(iris_label)
print(iris.target_names)

iris_df = pd.DataFrame(data = iris.data, columns=iris.feature_names)
iris_df['label'] = iris.target
iris_df.head(3)