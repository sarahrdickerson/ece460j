import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib

import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.stats.stats import pearsonr
from sklearn.linear_model import Ridge, RidgeCV, ElasticNet
from sklearn.model_selection import cross_val_score

"""
    4.2
"""


def rmse_cv(model):
    rmse = np.sqrt(
        -cross_val_score(model, X_train, y, scoring="neg_mean_squared_error", cv=5)
    )
    return rmse


train = pd.read_csv("house-prices-advanced-regression-techniques/train.csv")
print("Read training set")
test = pd.read_csv("house-prices-advanced-regression-techniques/test.csv")
print("Read test set")

train.head()

all_data = pd.concat(
    (
        train.loc[:, "MSSubClass":"SaleCondition"],
        test.loc[:, "MSSubClass":"SaleCondition"],
    )
)

# Data preprocessing
matplotlib.rcParams["figure.figsize"] = (12.0, 6.0)
prices = pd.DataFrame(
    {"price": train["SalePrice"], "log(price + 1)": np.log1p(train["SalePrice"])}
)
prices.hist()

# log transform the target
train["SalePrice"] = np.log1p(train["SalePrice"])

# log transform skewed numeric features
numeric_features = all_data.dtypes[all_data.dtypes != "object"].index

skewed_features = train[numeric_features].apply(lambda x: skew(x.dropna()))

# compute skewness
skewed_features = skewed_features[skewed_features > 0.75]
skewed_features = skewed_features.index

all_data[skewed_features] = np.log1p(all_data[skewed_features])

all_data = pd.get_dummies(all_data)

# fill NA with mean of column
all_data = all_data.fillna(all_data.mean())

# separate out training and test data sets again
X_train = all_data[: train.shape[0]]
X_test = all_data[train.shape[0] :]
y = train.SalePrice


# ridge regression
ridge = Ridge(alpha=0.1)
ridge.fit(X_train, y)

y_prediction = ridge.predict(X_test)
y_prediction = np.expm1(y_prediction)
ridge_rmse = rmse_cv(Ridge(alpha=0.1)).mean()

print("Sales Price Prediction:", y_prediction)
print("RMSE:", ridge_rmse)


"""
    4.3
"""


"""
    4.4
"""


"""
    4.5
"""


"""
    4.6
"""


"""
    4.7
"""


"""
    4.8
"""
