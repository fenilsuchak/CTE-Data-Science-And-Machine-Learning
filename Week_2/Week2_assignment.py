%%matplotlib inline
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''Coding Gradient descent algorithm to optimize ordinary least squares estimates for Simple Linear Regression Model
	Y_i = B_o + B_1 * X_i is the equation. Now the OLS loss will be 
	loss = sum((Y_i - B_o + B_1*X_i)**2)/n , where n is the number of data points.
	There is a csv file called data_points.csv, that contains two columns  X, Y.
	You need to compute loss after 1000 iterations of Gradient Descent. The assignment is super easy and short.
	You can use derivatives used in class or recompute by hand or use wolfram alpha.'''


'''Let B_o and B_1 be any random values. But depending on initial weights answers can be different for different users. So use the commented
	values, they are just two random numbers nothing fancy'''

B_o = #0.1111
B_1 = #0.2222
prediction = B_o + B_1 * X
learning_rate = 0.01
loss_tracker = []

for i in range(1000):
	B_o = #code here. Update B_o in the direction of negative gradient. ie. dloss/dB_o
	B_1 = #code here. Update B_1  in the direction of negative gradient. ie. dloss/dB_1
	loss = #compute loss for updated parameters
	#Append the new loss after every iteration to the list named loss_tracker.

final_loss = loss_tracker[-1]

''' Now plot the losses in loss_tracker vs number of iterations '''







