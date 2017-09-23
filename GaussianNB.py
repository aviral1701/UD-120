import numpy as np
from sklearn import GaussianNB
arr1  = np.arr
classi = GaussianNB()
# training data is X,y
classi.fit(X,Y)
classi.predict()