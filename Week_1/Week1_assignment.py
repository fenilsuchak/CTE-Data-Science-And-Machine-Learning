%precision 2    #To set floating point precision(places after decimal)
import csv
import numpy as np
import time

with open('numberlist1.csv') as csvfile:
    number_list = list(csv.DictReader(csvfile))

##Part 1
###Here you write your function to check if a given no. is prime or not:

def findtype(inputnumber): 
    '''Here you write the code(for loop) for checking if inputnumber which is taken as argument to 
       this function is prime or composite or not 
                                                '''
    #if inputnumber is prime return 'prime'

    #else if inputnumber is return 'composite'

    #else return 'NA'

    
'''Instructions:
   a.Now that you have written your function, iterate through the number_list list that is read from the csv file and use your function to return a list with
     name numtype_list and it should contain the number type('prime','composite','nan') of the corresponding numbers in number_list
     For example: 
     number_list = [2,3,4,5,6,'a','',5.3,6.7]
     numtype_list = ['prime','prime','composite','prime','composite','NA','NA','NA','NA']
   b.You might have to check if the number is an integer (Hint: Google a built-in function or write your own)
   c.numtype_list will be a python list rather than storing output in text file numpy offers .npy format to store numpy arrays
     reading .npy in python is blazing fast compared to .txt and .csv. So convert numtype_list to numpy array and store it in disk
     in .npy format with the name ''submit_assign_1_0.npy''.
   d.Measure time of execution of your loop with time module(Already imported)[Read documentation online how to use it].See the time
     of exececution for yourself. Could you be faster? Any solution with correct output is accepted as correct.
   e.The code that is fastest gets a treat.
   f.The code that is shortest(more Pythonic) also gets a treat.
'''

'''Lists can be so large that they cant be stored in the memory, suppose the list goes as [2,3,4,5,6....,a_very_large_number]. 
   Suppose this is a very large list to be stored on disk and so we cant loop through it in python.
   In our software program we need to find the sum of all the primes such that.
   We want prime numbers depending on number of customer logging into our website.
   Customer logins can end up being very large(big website). No way to estimate very_large_number.
   And every time a user logs in we need to get the next sum of prime.
   Because we need to record sum of primes at the end of the year.
   Here is the trick we dont want to store a very very big list whose size we cant estimate, what a wastage of memory.
   So why dont add primes as a customer logs in ie, "On the Fly". Meaning lets not store the primes at all, rather generate 
   numbers as a new customer logs in, and add them to existing sum.
   But how do we do it?
   Whats the minimum requirement to get an incremental number? The previous number.
   Whats the minimum requirement to get an incremental sum? The previous some.
   So. We just need to store two things in-order to get the next two things.
   So we virtually store nothing. And do exactly the number of operations required no more no less.
   But how do we implement it?
   A function, probably? No, a function is loses all its memory(I mean english language memory not computer memory) once it hits return statement, all its variables are lost.
   But what if function had some (english language memory), what if we could call the function over and over again and it remembers
   what happened in the previous call? Oh yeah. This should do it.
   Someone sitting late night sipping coffee surely came up with this idea, which is generally called coroutines
   Python has it implemented for you called "yield" statement.
   An yield statement makes a function generators. [Read more on Generators and Iterators]
   
   Below are some implementations which make you familiar with yield statement, iterators, generators.
'''
#First is range()
k_range = range(0, 10, 2)
print(type(k)) 
for elems in k:
    print(elems) #Now k is not a list, it generates the numbers only when queried.
#Range is an iterable not an iterator.
#But
k_iterator = iter(k) 
print(type(range(k)))
#Iterator is just a class with some methods(Read Docs),an iterator has the most useful is the next() function.[Thats the only thing we use]
next(k_range) #error
next(k_iter)
next(k_iter)
next(k_iter) 
#Iterators get exhausted. They are of one-time use. But Iterables are reusable to make iterators again.
#Lists also are iterables. Calling iter([1,2,3]) makes it an iterator
#A for loop implicitly converts [1,2,3] or range(0,10,2) to an interator by calling iter() on it.
#So all Iterators are Lazy, they give out numbers only when called next() on them
#But Iterables such as range(0,10,2) are lazy iterables. These dont store anything before hand. But Iterables such as lists are not
#Lazy iterables they consume space in memory.


#Now all generators are iterators but not vice-versa. Iterators have more flexibility than generators.
#But mostly in ML we probably dont need that distinction. You can look up on the web if interested.

generator1 = (x*x for x in range(10)) #This a generator expression.To do simple things.
type(generator1)
next(generator1)
next(generator1)
next(generator1)
next(generator1)
next(generator1) #Also get exhausted. And also are lazy.
list1 = [x*x for x in range(10)]   #List comprehension style list
#So lets get back to yield statement
def yield_me_even_sums(): #To get more complex generators we can use generator functions.
    sum = 0
    for i in range(30):
        if i%2 == 0:
            sum = sum + i
            yield sum
        else:
            yield sum
generator2 = yield_me_evens()
next(generator2)
next(generator2)
next(generator2)
next(generator2)
next(generator2)
next(generator2)
next(generator2)
next(generator2)
'''Note that we are not calling a function anymore, yield statement converts the function into generator
   a.Visualizing the flow.
     We first make a generator object by calling the function yield_me_evens() and assigning it to generator2
     When we call next on it. for loop is entered, until yield statement is hit, and corresponding is returned value is returned.
     And we are out of the function. Next time we call next(), the process is continued from yield statement and stops when loop 
     Again hits the yield statement and the value next to yield is put out. And On and on.'''

'''So here is your task. Write a function that returns sum of primes in imaginary list [2,3,4,5,6,7...,infinite], only as an when a customer logs in.
   Calling next() on customer_prime_sum for the first time must return 2
   Calling next() on customer_prime_sum for the second time must return 5
   Calling next() on customer_prime_sum for the third time must return 5
   Calling next() on customer_prime_sum for the infinite(th) time must return sum of all primes until inifinte+1.'''
def customer_login_func(*args, **kwargs):
    '''Your code here , Hint: you can call a function inside a function, 
        ie you can use previous prime checking function'''

    
customer_prime_sum = customer_login_func() #Add arguments if any.
    



#Part 3-Basic Matrix manipulations
"""
NumPy is one of the best ways to manipulate and do matrix operations in python.

The following code will take you through the basics of NumPy

"""

import numpy as np#importing NumPy module with name as np

#Initialising an array :

#creating an 1d array:
array1=np.array([2,3])
print(array1)

#creating an 2-d array:
array2=np.array([[3,8],[5,6],[7,2]])
print(array2)

#getting the shape of an array
print(array2.shape)

#arange returns evenly spaced values within a given interval.
array3 = np.arange(0, 15, 2) # start at 0 count up by 2, stop before 15
print(array3)

#reshaping an array
#reshape returns an array with the same data with a new shape.
array4=array2.reshape(2,3)
print(array4)

#resize changes the shape and size of array in-place.
array2.resize(2, 3) #no_need to do array2 = array2.reshape(2,3)
print(array2)

#linspace returns evenly spaced numbers over a specified interval
array5= np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4
print(array5)

#ones returns a new array of given shape and type, filled with ones.
print(np.ones((3, 2)))

#zeros returns a new array of given shape and type, filled with zeros.
print(np.zeros((2, 3)))

#eye returns a 2-D array with ones on the diagonal and zeros elsewhere.
print(np.eye(3))

#diag extracts a diagonal or constructs a diagonal array.
array5=np.array([[3,4,5],[5,6,4],[45,23,43]])
print(array5)
print(" the diagonal array: ",np.diag(array5))

#Create an array using repeating list (or see np.tile)
array6=np.array([1, 2, 3] * 3)
print(array6)

#Repeat elements of an array using repeat.
array7=np.repeat([1, 2, 3], 3)
print(array7)

#Slicing rows and coloumns 
array8 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
"""
  Two ways of accessing the data in the middle row of the array.
  Mixing integer indexing with slices yields an array of lower rank,
  while using only slices yields an array of the same rank as the 
"""
# original array:
row_r1 = array8[1, :]    # Rank 1 view of the second row of a
row_r2 = array8[1:2, :]  # Rank 2 view of the second row of a
print(row_r1, row_r1.shape)  # Prints "[5 6 7 8] (4,)"
print(row_r2, row_r2.shape)  # Prints "[[5 6 7 8]] (1, 4)"

# We can make the same distinction when accessing columns of an array:
col_r1 = array8[:, 1]
col_r2 = array8[:, 1:2]
print(col_r1, col_r1.shape)  # Prints "[ 2  6 10] (3,)"
print(col_r2, col_r2.shape)  # Prints "[[ 2]
                             #          [ 6]
                             #          [10]] (3, 1)"

#Datatypes
array9 = np.array([5, 10])   # Let numpy choose the datatype
print(array9.dtype)          # Prints "int64"

array9 = np.array([5.0, 10.0])   # Let numpy choose the datatype
print(array9.dtype)              # Prints "float64"

array9 = np.array([5, 10], dtype=np.float64)   # Force a particular datatype
print(array9.dtype)                         # Prints "float64"

#Transpose
array10 = np.array([[1,2], [3,4]])
print(array10)    # Prints "[[1 2]
            	  #          [3 4]]"
print(array10.T)  # Prints "[[1 3]
                  #          [2 4]]"

# Note that taking the transpose of a rank 1 array does nothing:
vector1 = np.array([1,2,3])
print(vector1)    # Prints "[1 2 3]"
print(vector1.T)  # Prints "[1 2 3]"

"""
NOTE: When you initialise 2 arrays and add(+),subtract(-), multiply(*), divide(/),
Operations would be ELEMENT-wise, array1*array2 won't give you matrix multiplication unlike in MATLAB.
Experiment with different datatypes and arraysizes while carrying out these operation show which one leads to errors.
TRY IT OUT below with x,y,v, or any other array you want.
"""

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
v = np.array([1, 0, 1])
y = np.empty_like(x)   # Create an empty matrix with the same shape as x

y = x + v  
print(y)
#What do you notice? How can we add 2 arrays of different sizes? What is happening?
"""
You just added v to each row of x using broadcasting.
The line y = x + v works even though x has shape (4, 3) and v has shape (3,) due to broadcasting;
this line works as if v actually had shape (4, 3), where each row was a copy of v,
and the sum was performed elementwise.

While working with array6, have you checked out np.tile? If not check it out.
"""
vv = np.tile(v, (4, 1))   # Stack 4 copies of v on top of each other
print(vv)                 # Prints "[[1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]
                          #          [1 0 1]]"
y = x + vv  # Add x and vv elementwise
print(y)  # Prints "[[ 2  2  4
          #          [ 5  5  7]
          #          [ 8  8 10]
          #          [11 11 13]]"

#This does the same job as above or else you could use a loop as well, like shown below
for i in range(4):
    y[i, :] = x[i, :] + v

# Now y is the following
# [[ 2  2  4]
#  [ 5  5  7]
#  [ 8  8 10]
#  [11 11 13]]
print(y)

#GOOD JOB!! CHECKOUT NUMPY DOCUMENTATION FOR MORE!!
