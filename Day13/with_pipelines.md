# *Pipeline* #

# *Impute tranformer*

    transformer1=ColumnTransformer([
    ('impute_age',SimpleImputer(),[2]),
    ('impute_embark',SimpleImputer(strategy='most_frequent'),[6])],remainder='passthrough')

# *Ohe transformer*

    transformer2=ColumnTransformer([
    ('ohe_sex_embarked',OneHotEncoder(sparse=False,handle_unknown='ignore'),[1,6])],remainder='passthrough')


# *Scaling*

    transformer3=ColumnTransformer([
    ('scale',MinMaxScaler(),slice(0,10))
])


# *feature selecton*

    transformer4=SelectKBest(score_func=chi2,k=8)

# *Decision Tree*

    transformer5= DecisionTreeClassifier()

# *Make Pipeline*

    pipe=Pipeline([
    ('tranforemer1',transformer1),
    ('tranforemer2',transformer2),
    ('tranforemer3',transformer3),
    ('tranforemer4',transformer4),
    ('tranforemer5',transformer5)
])

# *Fitting pipe*

    pipe.fit(X_train,y_train)

![](https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day11/alcohol.png)
in/Day11/both.png)

