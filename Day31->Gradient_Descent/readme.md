# Steps to apply gradient Descent #
  
## 1) Take a random value of b and start the process <br>
## 2) Find slope of line <br>
     loss_slope=-2*np.sum(Y-m*X.ravel()-b)

## 3) Calculate the step size
    
    stepsize=learning_rate*loss_slope

## 4)Change the slope

    b=b-stepsize

# *Repeat this process to get the value of intercept*

