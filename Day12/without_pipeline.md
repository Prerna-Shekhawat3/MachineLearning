# *Without Pipeline* #

# *Applying Imputer* 

    si_age=SimpleImputer()
    si_embarked=SimpleImputer(strategy='most_frequent')

    X_train_age=si_age.fit_transform(X_train[['Age']])
    X_train_embarked=si_embarked.fit_transform(X_train[['Embarked']])

    X_test_age=si_age.fit_transform(X_test[['Age']])
    X_test_embarked=si_embarked.fit_transform(X_test[['Embarked']])

# *OHE on Embarked,Sex*

    ohe_sex=OneHotEncoder(sparse=False,drop='first',handle_unknown='ignore')
    ohe_Embarked=OneHotEncoder(sparse=False,drop='first',handle_unknown='ignore')

    X_train_sex=ohe_sex.fit_transform(X_train[['Sex']])
    X_train_embarked=ohe_Embarked.fit_transform(X_train[['Embarked']])

    X_test_sex=ohe_sex.fit_transform(X_test[['Sex']])
    X_test_embarked=ohe_Embarked.fit_transform(X_test[['Embarked']])

# *Now we have to combine all column*  

    X_train_transformed=np.concatenate((X_train_rem,X_train_age,X_train_sex,X_train_embarked),axis=1)



