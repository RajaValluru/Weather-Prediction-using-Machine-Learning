"""The main assumptions for a linear regression model are:
    1.Have a linear relationship between the dependent variable and each independent variable
    2.A uniform random distribution of spread along the points is also another important assumption of Linear Regression
    using Ordinary Least Squares algorithm."""



#SELECTING THE FEATURES FOR BUILDING LINEAR REGRESSION MODEL BASED ON PEARSON CORELATION COEFFICIENT
"""pearson coefficient value is between -1 to 1 and 0-1 indicates positive correlation and -1-0 indicates negative corelation"""
 
"""Type this df.corr()[['meantempm']].sort_values('meantempm') in console to find the amount of corelation between the 
  mean temperature and the other features and sort them according to their corelation values"""

"""removing the features that have correlation values less than the absolute value of 0.6. Also, since the "mintempm" 
and "maxtempm" variables are for the same day as the prediction variable "meantempm",we will be removing those also."""

#CREATING A DATAFRAME THAT CONTAINS VARIABLES OF OUR INTREST
predictors = ['meantempm_1',  'meantempm_2',  'meantempm_3',  
              'mintempm_1',   'mintempm_2',   'mintempm_3',
              'meandewptm_1', 'meandewptm_2', 'meandewptm_3',
              'maxdewptm_1',  'maxdewptm_2',  'maxdewptm_3',
              'mindewptm_1',  'mindewptm_2',  'mindewptm_3',
              'maxtempm_1',   'maxtempm_2',   'maxtempm_3']

df2 = df[['meantempm'] + predictors]

#VISUALIZING THE FEATURES 

import matplotlib  
import matplotlib.pyplot as plt  
import numpy as np  

#%matplotlib inline
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
 

# manually set the parameters of the figure to and appropriate size
plt.rcParams['figure.figsize'] = [21,21]  

# call subplots specifying the grid structure we desire and that 
# the y axes should be shared
fig, axes = plt.subplots(nrows=6, ncols=3, sharey=True)

# Since it would be nice to loop through the features in to build this plot
# let us rearrange our data into a 2D array of 6 rows and 3 columns
arr = np.array(predictors).reshape(6, 3)

# use enumerate to loop over the arr 2D array of rows and columns
# and create scatter plots of each meantempm vs each feature
for row, col_arr in enumerate(arr):  
    for col, feature in enumerate(col_arr):
        axes[row, col].scatter(df2[feature], df2['meantempm'])
        if col == 0:
            axes[row, col].set(xlabel=feature, ylabel='meantempm')
        else:
            axes[row, col].set(xlabel=feature)

plt.show()