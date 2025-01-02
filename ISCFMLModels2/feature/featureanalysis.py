import concurrent

import pandas as pd
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import Lasso
from sklearn.feature_selection import RFE
from sklearn.svm import SVC
from concurrent.futures import ThreadPoolExecutor


def correlation_analysis(data, target):
    df = pd.concat([pd.DataFrame(data), pd.Series(target, name='target')], axis=1)

    correlation = df.corr()['target'].abs().sort_values(ascending=False)
    print(correlation)

def tree_based_model_feature_importance(data, target):
    model = RandomForestClassifier()
    model.fit(data, target)

    feature_importance = model.feature_importances_
    pretty_print(feature_importance)

def univariate_feature_selection(data, target):
    selector = SelectKBest(score_func=f_classif, k=10)  # Select top 10 features
    X_new = selector.fit_transform(data, target)
    selected_feature_indices = selector.get_support(indices=True)
    pretty_print(selected_feature_indices)

def lasso_regression(data,target):
    lasso = Lasso(alpha=0.1)  # You can tune the alpha value
    lasso.fit(data, target)
    pretty_print(lasso.coef_)

def recursive_elemination(data, target, n_features):
    estimator = SVC(kernel="linear")
    selector = RFE(estimator, n_features_to_select=n_features)
    selector = selector.fit(data, target)
    selected_feature_indices = selector.support_
    pretty_print(selected_feature_indices)
    pretty_print(selector.ranking_)



def pretty_print(coefs):
    for index, coef in enumerate(coefs):
        print(f"{index}: {coef}")

def pca(data):
    pca = PCA(n_components=2)
    return pca.fit_transform(data)