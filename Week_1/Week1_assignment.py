import csv

%precision 2 #To set floating point precision(places after decimal)

with open('numberlist1.csv') as csvfile:
    numberlist = list(csv.DictReader(csvfile))

    datalen=len(numberlist)
#Here you write your function to check if a given no. is prime or not :
def findtype(inputnumber): 
    '''Here you write the code(for loop) for checking if inputnumber which is taken as argument to 
       this function is prime or composite or not 
                                                '''
        
    #if inputnumber is prime
    numtype = 'prime'
    #else if inputnumber is compostite
    numtype = 'composite'
    #else
    numtype = 'NA'
#Now that you have written your function, iterate through the csv file and use your function to check if the nos. in csv file are prime:
