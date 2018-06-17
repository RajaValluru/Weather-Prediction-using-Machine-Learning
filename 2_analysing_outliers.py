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
plt.rcParams['figure.figsize'] = [24,12]  

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



