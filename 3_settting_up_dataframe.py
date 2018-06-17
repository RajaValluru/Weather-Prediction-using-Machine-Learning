#SETTING UP THE DATAFRAME
df = pd.DataFrame(records, columns=features).set_index('date')  

#DERIVING THE FEATURES
tmp = df[['meantempm', 'meandewptm']].head(10)
# 1 day prior
N = 1

# target measurement of mean temperature
feature = 'meantempm'

# total number of rows
rows = tmp.shape[0]

# a list representing Nth prior measurements of feature
# notice that the front of the list needs to be padded with N
# None values to maintain the constistent rows length for each N
nth_prior_measurements = [None]*N + [tmp[feature][i-N] for i in range(N, rows)]

# make a new column name of feature_N and add to DataFrame
col_name = "{}_{}".format(feature, N)  
tmp[col_name] = nth_prior_measurements 

#generalizing the above steps into an function to apply for all the features 
def derive_nth_day_feature(df, feature, N):  
    rows = df.shape[0]
    nth_prior_measurements = [None]*N + [df[feature][i-N] for i in range(N, rows)]
    col_name = "{}_{}".format(feature, N)
    df[col_name] = nth_prior_measurements

#applied for all the features for 1_day prior,2_day prior,3_day prior    
for feature in features:  
    if feature != 'date':
        for N in range(1, 4):
            derive_nth_day_feature(df, feature, N)
            

#DATA CLEANING PART
#As the data in the data frame is very large we are reducing the no.of columns in the dataframe by selecting
#necessary features for our project
#As the goal of this project is to predict the future temperature based off the past three days of weather
# measurements. With this in mind we only want to keep the min, max, and mean temperatures for each day            
# making a list of original features without meantempm, mintempm, and maxtempm
to_remove = [feature  
             for feature in features 
             if feature not in ['meantempm', 'mintempm', 'maxtempm']]

# make a list of columns to keep
to_keep = [col for col in df.columns if col not in to_remove]

# select only the columns in to_keep and assign to df
df = df[to_keep]#df.columns to confirm whether the columns are removed or not

#df.info() gives us the information of a dataframe.Initially the datatype of all the columns are object type,we need to 
#convert them into numericals for performing numerical analysis

#converting object type to numerical type
#to_numeric is a method in pandas library and errors='coerce' replaces missing values with some text
df = df.apply(pd.to_numeric, errors='coerce')
#df.info() to check whether the data type has changed or not


#describe() will produce a DataFrame containing the count, mean, standard deviation, min, 25th percentile,
#50th percentile (or median), the 75th percentile and, the max value. This can be very useful information
#to evaluating the distribution of the feature data.

# Call describe on df and transpose it due to the large number of columns
spread = df.describe().T
#enter spread in the console to look at the dataframe produced by describe()


#IDENTENTIFYING THE OUTLIERS
# precalculate interquartile range for ease of use in next calculation
IQR = spread['75%'] - spread['25%']

# create an outliers column which is either 3 IQRs below the first quartile or
# 3 IQRs above the third quartile
spread['outliers'] = (spread['min']<(spread['25%']-(3*IQR)))|(spread['max'] > (spread['75%']+3*IQR))

# just display the features containing extreme outliers
#spread.loc[spread.outliers,] or spread.loc[spread.outliers,] in console

#ANALYSING OUTLIERS USING HISTOGRAM IN NEW DOCUMENT

#DEALING WITH MISSING VALUES
#type df.info() to see the dataframe frame info and we can also see the no.of missing values of each feature
#fill the missing values with an interpolated value that is a reasonable estimation of the true values of a feature
#here as precipitation has most of the mising values we fill them with the majority value of precipitation i.e 0

# iterate over the precip columns
for precip_col in ['precipm_1', 'precipm_2', 'precipm_3']:  
    # create a boolean array of values representing nans
    missing_vals = pd.isnull(df[precip_col])
    df[precip_col][missing_vals] = 0

#we have taken care about all possible missing values and if still there are any missing we are going to dropthe rows containing missing values    
df = df.dropna() 
 












