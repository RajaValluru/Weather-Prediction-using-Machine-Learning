#%matplotlib inline 
"""Line magics are only supported by the IPython command line. You cannot use it inside a script like this because it 
 is not correct Python syntax."""

"""If you want to do this from a script you have to get access to the IPython API and then call the run_line_magic function.
Instead of %matplotlib inline, you will have to do something like this in your script:

from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline') """

#to study outlier in graphical way or by  histogram
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize'] = [9,9]  

"""Looking at the histogram of the values for maxhumidity the data exhibits quite a bit of negative skew. I will want to keep 
   this in mind when selecting prediction models and evaluating the strength of impact of max humidities. Many of the underlying 
   statistical methods assume that the data is normally distributed. For now I think I will leave them alone but it will be good
   to keep this in mind and have a certain amount of skepticism of it."""
   
#max humidity
df.maxhumidity_1.hist()  
plt.title('Distribution of maxhumidity_1')  
plt.xlabel('maxhumidity_1')  
plt.show() 

#minpressure
df.minpressurem_1.hist()  
plt.title('Distribution of minpressurem_1')  
plt.xlabel('minpressurem_1')  
plt.show()

#precipm
df.precipm_1.hist()  
plt.title('Distribution of precipm_1')  
plt.xlabel('precipm_1')
plt.show()



