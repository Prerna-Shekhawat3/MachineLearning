
# *Arbitary Value Imputation* #

### *As the name suggest we enter Arbitary values.This is done using Pandas library* ###

    X_train['age_99']=X_train['Age'].fillna(99)
    X_train['age_minus']=X_train['Age'].fillna(-1)

    X_train['fare_99']=X_train['Fare'].fillna(99)
    X_train['fare_minus']=X_train['Fare'].fillna(-1)

## *Here ve have imputed 99 ,-1 in Fare and Age column as seen in graph it fits perfectly in Fare but does not fits in Age Column* ##

[Arbitary_value_imp](https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day20-%3EArbitary_Value_Imputation/arbitary_value_impute.png)


[Arbitary_value_imp](https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day20-%3EArbitary_Value_Imputation/arbitary_value_impute2.png)







