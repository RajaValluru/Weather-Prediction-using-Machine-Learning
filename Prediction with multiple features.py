
#importing and using the LinearRegression class from the sklearn.linear_model module
from sklearn.linear_model import LinearRegression 


Cdate=datetime(2015,1,4)
dates=[]
for l in range (0,998):
        dates.append(Cdate)
        Cdate+= timedelta(days=1)
   
datesDF = pd.DataFrame(dates) 
# instantiate the regressor class


# fit the build the model by fitting the regressor to the training data


dateP = pd.DataFrame([datetime(2018, 4, 24)]) 
#datesDF = datesDF.apply(pd.to_numeric, errors='coerce')
dateP = dateP.apply(pd.to_numeric, errors='coerce')
# make a prediction set using the test set
regressor=[]
prediction=[]

regressor.append(LinearRegression())
regressor[0].fit(datesDF,X['mintempm_3'])
prediction.append(regressor[0].predict(dateP))

regressor.append(LinearRegression())
regressor[1].fit(datesDF,X['maxdewptm_1'])
prediction.append(regressor[1].predict(dateP))

regressor.append(LinearRegression())
regressor[2].fit(datesDF,X['mindewptm_1'])
prediction.append(regressor[2].predict(dateP))

regressor.append(LinearRegression())
regressor[3].fit(datesDF,X['maxtempm_1'])
prediction.append(regressor[3].predict(dateP))

regressor.append(LinearRegression())
regressor[4].fit(datesDF,X['maxtempm_2'])
prediction.append(regressor[4].predict(dateP))

regressor.append(LinearRegression())
regressor[5].fit(datesDF,X['maxtempm_3'])
prediction.append(regressor[5].predict(dateP))


coefficients=regression.coef_
intercept=regression.intercept_

meantemp=intercept;
for i in range(0,6):
    meantemp+= prediction[i]*coefficients[i]
    






