### Copyright 2018 by A.R. Plummer


### import numpy and matplotlib

import numpy as np
import matplotlib.pyplot as plt



### using an np.array to represent out data.  the first column is the
### bias term x0. the second and third columns are the truth values of
### the propositions X and Y.  The fourth column is the truth value of
### the proposition X and Y, which we take to be the class value C.

andFunction = np.array([[1,1,1,1],
                       [1,0,1,0],
                       [1,1,0,0],
                       [1,0,0,0]])



### the lines below are used to plot the data. 

for dataPoint in andFunction:
    plt.plot(dataPoint[1:3], 'ro',ms=10)

plt.plot(andFunction[0,1],andFunction[0,2],'bo',ms=10)
plt.ylim((-1,2))
plt.xlim((-1,2))


### you need to initialize the weights for your perceptron (I suggest
### using an np.array).

andWeights = np.array([0,0,0],dtype=np.float64)
#Do the formate alignment.


### A function for the input value of a perceptron.  It should compute
### the dot product of a weight vector and an input vector.

def inValue (weights, featureVals):
   return sum(weights*featureVals)
    


### You need to implement a step activation function here.  This
### function should return a 1 or 0 to match the class values defined
### in the andFunction above.

def stepActivation(z):
    return 0 if z<0 else 1


### Weight update goes here. This function should return an np.array
### with 3 components.

def stepUpdate(weights, featureVals, observedClass, learningRate):
   delta = observedClass - stepActivation(inValue(weights, featureVals))
   x = np.array(featureVals,dtype=np.float64)
   #Formate alignment
   weights += learningRate*delta *x
   

### Suggested learning rate and epoch numbers.  
   
learningRate = 0.09
epoch = 5000



### loop running training over the suggested number of epochs and an
### embedded loop over each data point. 

for i in range(epoch):
    for dataPoint in andFunction:
        label = dataPoint[3]
        x = dataPoint[0:3]
        stepUpdate(andWeights,x,label,learningRate)
        

### after the loop above, your weights should be able to correctly
### classify the training data.  Plot the training data and the
### decision boundary that your trained weights yield.

x1 = np.linspace(-1,2,5000)
plt.plot(x1,-((andWeights[1]/andWeights[2])*x1+(andWeights[0]/andWeights[2])))
plt.title('andFunction')
plt.show()


