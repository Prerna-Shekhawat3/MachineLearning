
# *Arbitary Value Imputation* #

### *As the name suggest we enter Arbitary values.This is done using Pandas library* ###

    X_train['age_99']=X_train['Age'].fillna(99)
    X_train['age_minus']=X_train['Age'].fillna(-1)

    X_train['fare_99']=X_train['Fare'].fillna(99)
    X_train['fare_minus']=X_train['Fare'].fillna(-1)


[I'm an inline-style link](https://www.google.com)







