# Batch Gradient Descent-> This is the traditinal technique which works well for smaller dataset .

## m=100,b=-120

    class GDRegressor:

    def __init__(self,learning_rate,epoch):
      self.m=100
      self.b=-120
      self.lr=learning_rate
      self.epoch=epoch
  
    def fit(self,X,y):
      for i in range(self.epoch):
        loss_slope_b=-2*np.sum(y-self.m*X.ravel()-self.b)
        loss_slope_m=-2*np.sum((y-self.m*X.ravel()-self.b)*X.ravel())
  
        self.b=self.b-(self.lr*loss_slope_b)
        self.m=self.m-(self.lr*loss_slope_m)
  
      print(self.b,self.m)
  
    def predict(self,X):
      return X*self.m+self.b
  
## res: m=0.156,b=58.38
