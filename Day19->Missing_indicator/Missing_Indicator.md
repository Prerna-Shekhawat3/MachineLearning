# *Missing Indicator * #

### *There are two ways to implemd this either add missing indicator to model or add the add_indicator parameter to Simple Imputer* ###



### *Import Missing indicator class.* ###

    mi=MissingIndicator()

    mi.fit(X_train)

    X_train_missing_indi=mi.fit_transform(X_train)

    X_test_missing_indi=mi.fit_transform(X_test)

    X_train['age_na']=X_train_missing_indi
    X_test['age_na']=X_test_missing_indi

    from sklearn.impute import SimpleImputer

    si=SimpleImputer()

    X_train_trf=si.fit_transform(X_train)

    X_test_trf=si.transform(X_test)

    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score

    model=LogisticRegression()

    model.fit(X_train_trf,y_train)

    y_pred=model.predict(X_test_trf)

    accuracy_score(y_pred,y_test)


### *Use add_indicator in Simple Imputer.* ###

    from sklearn.impute import SimpleImputer

    si=SimpleImputer(add_indicator=True)

    X_train=si.fit_transform(X_train)

    X_test=si.transform(X_test)

    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score

    model=LogisticRegression()

    model.fit(X_train,y_train)

    y_pred=model.predict(X_test)

    accuracy_score(y_pred,y_test)







