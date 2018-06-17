#importing and using the LinearRegression class from the sklearn.linear_model module
from sklearn.linear_model import LinearRegression 

# instantiate the regressor class
regression = LinearRegression()
regressionTrain = LinearRegression()

# fit the build the model by fitting the regressor to the training data
regression.fit(X, y)
regressionTrain.fit(X_train,y_train)
# make a prediction set using the test set
prediction1 = regressionTrain.predict(X_test)

# Evaluate the prediction accuracy of the model
from sklearn.metrics import mean_absolute_error, median_absolute_error  
print("The Explained Variance: %.2f" % regression.score(X_test, y_test))  
print("The Mean Absolute Error: %.2f degrees celsius" % mean_absolute_error(y_test, prediction1))  
print("The Median Absolute Error: %.2f degrees celsius" % median_absolute_error(y_test, prediction1))

#finding accuracy:
###we need to get the coefficient values of each variable to get most accurate results with the command: reggressor.coef_'''
