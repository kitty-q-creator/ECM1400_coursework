# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification

def is_a_number (item):
    """
    My way of using regex instead of a predefined function to check if an input is numeric
    """
    import re
    if re.search("[^0-9+*|[^\.]",str(item))==None:
        return True
    else: return False

def median(values):
    """
    Calculated median from a list
    
    'values'--input list of values

    'medianValue'--the median of the list which will be returned
    """
    values.sort()
    mid=(len(values)//2)
    medianValue=values[mid]
    return medianValue

def sumvalues(values):
    """
    Calculates sum of list
    Uses floats not integers as those are the input numbers
    """    
    total=0
    for number in values:
        if is_a_number(number):
            total+=float(number)
        else:
            #exception
            print("error")
    return total

def maxvalue(values):
    """Takes input of a list of values and returns the index of the maximum element"""    
    ## Your code goes here
    max=0
    for index in range(0,len(values)):
        if is_a_number(values[index]) and float(values[index])>float(values[max]):
            max=index
        elif is_a_number(values[index])==False:
            #exception
            print("error")
    return max

def minvalue(values):
    """Takes input of a list of values and returns the index of the minimum element"""    

    min=12345678#just a random number that should be much higher than any data
    for index in range(0,len(values)):
        if is_a_number(values[index]) and float(values[index])<min:
            min=index
        elif is_a_number(values[index])==False:
            #exception
            print("error")
    return min

def meannvalue(values):
    """Takes input of a list of values and returns the mean of those values""" 
    sum=sumvalues(values)
    n=len(values)-countvalue(values,"no data")#ignores no data values when calculating the mean
    if n>0:
        mean=sum/n
    else:
        mean=0
    return mean

def countvalue(values,xw):
    """Takes input of a list of values and the item you want to count
    Returns the the number of elements which make this item"""     
    count=0
    for item in values:
        if item==xw:
            count+=1
    return count