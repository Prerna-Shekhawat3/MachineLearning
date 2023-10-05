# *How to treat Outliers?* #
### ->Trimming which means removing the rows which have Outliers but this may lead to loss of relevant information so this method is not that appropriate.###

### ->Caping involves setting maximum and minimum threshold value for column inorder to control the impact of extreme values and when values exceed that threshold it will replaced with respective threshold value. ###

### ->Treating outliers as missing value. ###


# *Technique for outlier detection and removal* #

### ->Z-Score treatment: This is done when data is normally distributed ###

    z-score=(x-mean)/standard deviation


### IQR Based Filtering ###

    LowerrLimit=Q1-1.5 x Inter Quartile Range (IQR)

    UpperLimit=Q3 + 1.5 x IQR

### Percentile method ###

    LowerLimit=df.quantile(0.99)

    UpperLimit=df.quantile(0.01)





