# *Column Transformer* #


### Aim of Column Transfomer is to transform column in efficient manner. Suppose we have ###

#### Gender,City- Nominal categorical Data
#### Cough- Ordinal categorical Data
#### has_covid - Label Encoder

## *Either we can transform these columns separetely and join all together* ##

### Ordinal Encoding on cough column

    from sklearn.preprocessing import OrdinalEncoder

    oe=OrdinalEncoder(categories=[['Mild','Strong']])

    X_train_cough=oe.fit_transform(X_train[['cough']])
    X_test_cough=oe.fit_transform(X_test[['cough']])

    X_test_cough.shape

### One Hot Encoding on Gender and city column

    from sklearn.preprocessing import OneHotEncoder

    ohe=OneHotEncoder(drop='first',sparse=False)

    X_train_gender_city=ohe.fit_transform(X_train[['gender','city']])

    X_test_gender_city=ohe.fit_transform(X_test[['gender','city']])

    X_test_gender_city.shape

# *By Using Column Transformer*

#### By using Column transformer we can reduce the complexity of performing each column separately here we can do it all together

    from sklearn.compose import ColumnTransformer
    transformer=ColumnTransformer(transformers=[
    ('tranformer1',SimpleImputer(),['fever']),
    ('tranformer2',OrdinalEncoder(categories=[['Mild','Strong']]),['cough']),
    ('tranformer3',OneHotEncoder(drop='first',sparse=False),['gender','city'])],remainder='passthrough')


