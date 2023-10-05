# *How to treat Outliers?* #
### ->Trimming which means removing the rows which have Outliers but this may lead to loss of relevant information so this method is not that appropriate.###

### ->Caping involves setting maximum and minimum threshold value for column inorder to control the impact of extreme values and when values exceed that threshold it will replaced with respective threshold value. ###

### ->Treating outliers as missing value. ###


# *Technique for outlier detection and removal* #


### Percentile method ###

    LowerLimit=df.quantile(0.99)

    UpperLimit=df.quantile(0.01)

## Outliers in the data 
![](https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day24-%3EOutlier_Detection_and_Removal/Before_Percentile.png)

## After Trimming the ouliers
![](https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day24-%3EOutlier_Detection_and_Removal/After_percentile.png)

## After Capping the data 
![](https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day24-%3EOutlier_Detection_and_Removal/After_capping.png)



