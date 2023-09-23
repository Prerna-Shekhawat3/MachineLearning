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

## *After applying log tranformer data get normaly distributed as seen in the QQ plot.* ##

!(https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day14/After%20applying%20log%20transformer.png)




