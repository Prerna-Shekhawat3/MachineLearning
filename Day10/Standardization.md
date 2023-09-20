# *Standardiztion* #


### It is done to standardize independent features in a fixed range or else the big values will dominate ml model. ###

### Values are mean centered with unit standard deviation ###

# *Implentation of Standardiztion* #

    import pandas as pd
    from sklearn.preprocessing import StandardScaler
    columns_to_standardize = ['feature1', 'feature2']
    scaler = StandardScaler()
    data[columns_to_standardize] = scaler.fit_transform(data[columns_to_standardize])



# *When should we apply Standardiztion?* #

## i)k-mean
## ii)KNN
## iii)Gradient Descent
## iv)PCA
## v)Neural Network

