# Steps to apply gradient Descent #
  
## 1) Take a random value of b and start the process <br>
## 2) Find slope of line <br>
     loss_slope=-2*np.sum(Y-m*X.ravel()-b)

## 3) Calculate the step size
    
    stepsize=learning_rate*loss_slope

## 4)Change the slope

    b=b-stepsize

# *Repeat this process to get the value of intercept*


# This is how the process goes

![Gradient Descent Step 1](https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day31-%3EGradient_Descent/step1.png)

![img](https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day31-%3EGradient_Descent/step2.png)

![img](https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day31-%3EGradient_Descent/step3.png)

![img](https://github.com/Prerna-Shekhawat3/MachineLearning/blob/main/Day31-%3EGradient_Descent/step4.png)
