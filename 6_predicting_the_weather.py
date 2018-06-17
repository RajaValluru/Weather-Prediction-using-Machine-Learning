#we use SciKit-Learn to create a prediction model and test its ability to predict the mean temperature

#SciKit-Learn is a very well established machine learning library that is widely used in both industry and academia

"""One thing that is very impressive about SciKit-Learn is that it maintains a very consistent API of "fit", "predict", 
   and "test" across many numerical techniques and algorithms which makes using it very simple."""

#split the training and testing datasets into 80% training and 20% testing 

#importing the train_test_split() function from sklearn.model_selection module
from sklearn.model_selection import train_test_split  

# first remove the const column because unlike statsmodels, SciKit-Learn will add that in for us
X = X.drop('const', axis=1)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=12)

