
# *One Hot Encoding* #

OneHotEncoding is done on nominal categorical data. It's a method of converting categorical variables into a numerical format so that they can be used as input features for machine learning models.

Let's say you have a "Color" column with categories: "Red," "Blue," and "Green." After one-hot encoding, you would have three new columns: "Color_Red," "Color_Blue," and "Color_Green." 


## *Implementation of OneHotEncoding using Pandas* ##

    pd.get_dummies(df,columns=['owner'],drop_first=True)



## *Implementation of OneHotEncoding using sklearn* ##

    from sklearn.preprocessing import OneHotEncoding

    ohe=OneHotEncoding(drop='first',sparse=False)

    X_train=ohe.fit_transform(X_train)
