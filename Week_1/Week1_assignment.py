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
   An yield statement( must be in a function) returns a generator. [Read more on Generators and Iterators]
'''
   
