# *Function transformer* #

### *They are used to convert distribution of any kind to normal  or gaussian distribution.* ###

#### *Log Transformation* #### 
    
    trf=FunctionTransformer(func=np.log1p)

#### *Square root Transformation* #### 

    trf=FunctionTransformer(func=np.sqrt)

#### *Reciprocal Transformation* #### 

    trf=FunctionTransformer(lambda x:1/x)

#### *Exponential Transformation* #### 

    trf=FunctionTransformer(lambda x:**x)



