# Metrics in Linear regression

### Linear regression metrics are used to assess the performance of a linear regression model, which predicts a continuous target variable based on one or more input features. Common metrics include: ###

- Mean Absolute Error (MAE): It calculates the average absolute differences between predicted and actual values.

      Mae=mean_absolute_error(y_pred,y_test)

- Mean Squared Error (MSE): It squares the differences, penalizing larger errors more heavily.

      Mse=mean_squared_error(y_pred,y_test)

- Root Mean Squared Error (RMSE): The square root of MSE, providing a measure in the same units as the target variable.

      Rmse=np.sqrt(mean_squared_error(y_pred,y_test))

- R-squared (R2): It measures the proportion of variance in the target explained by the model, with higher values indicating better fit.

      r2_score=r2_score(y_pred,y_test)

- Adjusted R-squared: It adjusts R2 for the number of predictors, penalizing excessive features.

      Adjusted_r2_score=1-(((1-R2)(N-1))/(N-P-1))

