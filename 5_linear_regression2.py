"""using stepwise regression to build a robust model"""

"""A robust Linear Regression model should utilize statistical tests for selecting meaningful, statistically significant,
   predictors to include. To select statistically significant features, I will utilize the Python statsmodels library."""
   
"""key aspect of using statistical methods such as Linear Regression in an analytics project is to validate
   the significance of assumptions made about the data under study."""
   
"""There are numerous hypothesis tests that have been developed to test the robustness of a linear regression
   model against various assumptions that are made.One such hypothesis test is to evaluate the significance of
   each of the included predictor variables."""

"""The formal definition of the hypothesis test for the significance of a βj parameters are as follows:
   1)H0: βj = 0, the null hypothesis states that the predictor has no effect on the outcome variable's value
   2)Ha: βj ≠ 0, the alternative hypothesis is that the predictor has a significant effect on the outcome variable's value"""
    
"""However, in many datasets there can be interactions that occur between variables that can lead to false interpretations
   of these simple hypothesis tests. To test for the effects of interactions on the significance of any one variable in a 
   linear regression model a technique known as step-wise regression is often applied."""
   
"""Using step-wise regression you add or remove variables from the model and assess the statistical significance of each 
   variable on the resultant model."""
   
# import the relevant module
import statsmodels.api as sm

# separate our my predictor variables (X) from my outcome variable y
X = df2[predictors]  
y = df2['meantempm']

# Add a constant to the predictor variable set to represent the Bo intercept?
X = sm.add_constant(X)  
X.iloc[:5, :5] 

# (1) select a significance value?
alpha = 0.05

# (2) Fit the model?
model = sm.OLS(y, X).fit()

# (3) evaluate the coefficients' p-values by typing model.summary() in console 

#applying step wise backward elimination technique 


# (3) cont. - Identify the predictor with the greatest p-value and assess if its > our selected alpha.
#             based off the table it is clear that mindewptm_2 has the greatest p-value and that it is
#             greater than our alpha of 0.05

# (4) - Use pandas drop function to remove this column from X
X = X.drop('mindewptm_2', axis=1)

# (5) Fit the model 
model = sm.OLS(y, X).fit()

X = X.drop('meantempm_1', axis=1)
model = sm.OLS(y, X).fit()

X = X.drop('maxdewptm_3', axis=1)
model = sm.OLS(y, X).fit()

X = X.drop('meantempm_3', axis=1)
model = sm.OLS(y, X).fit()

X = X.drop('maxdewptm_2', axis=1)
model = sm.OLS(y, X).fit()

X = X.drop('mindewptm_3', axis=1)
model = sm.OLS(y, X).fit()

X = X.drop('meandewptm_2', axis=1)
model = sm.OLS(y, X).fit()

X = X.drop('meandewptm_3', axis=1)
model = sm.OLS(y, X).fit()

X = X.drop('meandewptm_1', axis=1)
model = sm.OLS(y, X).fit()

X = X.drop('meantempm_2', axis=1)
model = sm.OLS(y, X).fit()

X = X.drop('mintempm_1', axis=1)
model = sm.OLS(y, X).fit()

X = X.drop('mintempm_2', axis=1)
model = sm.OLS(y, X).fit()

"""From the final model.summary() we can observe the folllowing things
   (1) the R-squared and Adj. R-squared values are both equal which suggests there is minimal risk that our model is 
   being over fitted by excessive variables and
   (2) the value of 0.895 is interpreted such that our final model explains about 90% of the observed variation in 
   the outcome variable, the "meantempm"."""