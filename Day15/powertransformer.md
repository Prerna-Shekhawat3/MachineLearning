
# *Power transformer* #

### *Power transforms are a technique for transforming numerical input or output variables to have a uniform or a Gaussian probability distribution.* ###

### *This is often described as removing a skew in the distribution, although more generally described as stabilizing the variance of the distribution.* ###

### *Power Transform Method- ‘yeo-johnson’ works with positive and negative values and ‘box-cox’ only works with strictly positive values* ###


## Applying Box-Cox transformer

    trf=PowerTransformer(method='box-cox')

    X_train_trans=trf.fit_transform(X_train+0.0001)

    X_test_trans=trf.transform(X_test+0.0001)

    pd.DataFrame({'cols':X_train.columns,'box-cox lambda':trf.lambdas_})


![](https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day15/boxcox.png)


## Applying Joe Johnsom

    trf2=PowerTransformer()

    X_train_trans=trf2.fit_transform(X_train)
    X_test_trans=trf2.fit_transform(X_test)

![](https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day15/yeojohnson.png)

