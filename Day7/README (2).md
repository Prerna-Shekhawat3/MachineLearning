# *Ordinal Encoding* #

## *1. Introduction to Ordinal Encoding* ##

Ordinal encoding is a crucial technique in data preprocessing, primarily used to transform categorical data with ordered relationships into numerical format. Unlike one-hot encoding, which creates binary columns for each category, ordinal encoding assigns a single numeric value to each category based on its order or importance.

Ordinal Encoding give rank to columns on basis of there occurance.

## *2. Why Ordinal Encoding Matters* ##

Ordinal encoding is particularly valuable when dealing with categorical data that hold inherent orders, such as education levels (high school < bachelor's < master's) or star ratings (1-star < 2-star < 3-star).

## *3. Implementation Steps* ##

### *Step 1: Identify Ordinal Variables* ###
Identify categorical features with clear orders or levels in your dataset, like rankings or sizes.

Like Degree,Ranks,Grade,etc.

### *Step 2: Determine Encoding Scheme* ###
Decide whether to use natural numbers (1, 2, 3...) or other values that represent the order.

### *Step 3: Assign Values* ###
Map the categories to their corresponding numeric values according to the established order.

### *Step 4: Apply Signs* ###
Enhance ordinal encoding by incorporating signs (positive/negative) to indicate trends or directions within the ordered categories.

### *4. Handling Categorical Data with Signs* ###
Adding signs to the ordinal encoding brings an extra layer of meaning to the data. For example, in sentiment analysis, encoding positive, neutral, and negative sentiments as +1, 0, and -1 respectively adds valuable sentiment intensity information to the encoding.

    from sklearn.preprocessing import OrdinalEncoder

    oe=OrdinalEncoder(categories=[['Poor','Good'],['UG','PG']])

    X_train=oe.fit_transform(X_train)
