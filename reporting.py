# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
from utils import *

def getRequiredData(data,dateTime, monitoring_station, pollutant):
    """Returns a list of either the dates or the times.
    Also returns the data related to the particular pollutant for the required monitoring station."""
    list1=data[monitoring_station][dateTime]
    list2=data[monitoring_station][pollutant]
    return list1,list2

def daily_average(data, monitoring_station, pollutant):
    """
    Calculates average for each day
    
    Arguements:
    'data'--full dictonary of all the data
    'monitoring_station'--desired station
    'pollutant'--desired pollutant

    returns:
    'singleDates'--a list of all the dates in the data
    'averages'--a list of all the averages calculated
    """
    dates,pollutionData=getRequiredData(data,"date",monitoring_station,pollutant)
    #sets up lists to be added to later
    averages=[]
    singleDates=[]
    temp=[]#temporary list for purpose of collecting data for one day
    counter=1

    for i in range(0,len(dates)):
        temp.append(pollutionData[i])
        counter+=1
        if counter==24:
            #if we have counted through an entired day calculate the average then reset variables    
            averages.append(meannvalue(temp))
            singleDates.append(dates[i])
            temp=[]
            counter =1
            
    return(singleDates,averages)

def daily_median(data, monitoring_station, pollutant):
    """
    Calculates median for each day
    
    Arguements:
    'data'--full dictonary of all the data
    'monitoring_station'--desired station
    'pollutant'--desired pollutant

    returns:
    'singleDates'--a list of all the dates in the data
    'medians'--a list of all the medians calculated
    """
    dates,pollutionData=getRequiredData(data,"date",monitoring_station,pollutant)
    #sets up lists to be used later in function
    medians=[]
    singleDates=[]
    temp=[]#temporary list for purpose of collecting data for one day
    counter=1

    for i in range(0,len(dates)):
        temp.append(pollutionData[i])
        counter+=1
        if counter==24:
            #when data for an entire day has been added to temp calculate median and reset variables
            medians.append(median(temp))
            singleDates.append(dates[i])
            counter =1
            temp=[]
      
    return (singleDates,medians)

def hourly_average(data, monitoring_station, pollutant):
    """
    Calculates average for each hour
    
    Arguements:
    'data'--full dictonary of all the data
    'monitoring_station'--desired station
    'pollutant'--desired pollutant

    returns:
    'singleTimes'--a list of 24 possible times
    'averages'--a list of all the 24 averages calculated
    """
    times,pollutionData=getRequiredData(data,"time",monitoring_station,pollutant)
    #sets up lists for later use
    averages=[]
    singleTimes=[]
    temp=[]
    for i in range(0,24):#start at a specific hour
        for j in range(i,len(times),24):#skip 24 to only get data for the one specific time
            temp.append(pollutionData[j])
        averages.append(meannvalue(temp))
        singleTimes.append(times[i])
    return(singleTimes,averages)
    
def monthly_average(data, monitoring_station, pollutant):
    """
    Calculates average for each mpnth
    
    Arguements:
    'data'--full dictonary of all the data
    'monitoring_station'--desired station
    'pollutant'--desired pollutant

    returns:
    'month'--a list of all 12 months for the purpose of easier display in main as it allows me to use 1 function to display data
    'averages'--a list of te averages for each month
    """
    dates,pollutionData=getRequiredData(data,"date",monitoring_station,pollutant)
    index=0
    averages=[]
    for i in range(1,13):
        temp=[]#will temporarily store the data for each month to be passed to the average function
        while int(dates[index][5:7])==(i):
            temp.append(pollutionData[index])
            index+=1
        averages.append(meannvalue(temp))
    months=["jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"]
    return(months,averages)
   
def peak_hour_date(data, date, monitoring_station,pollutant):
    """
    Calculates median for each day
    
    Arguements:
    'data'--full dictonary of all the data
    'date'--the specified date
    'monitoring_station'--desired station
    'pollutant'--desired pollutant

    returns:
    'singleDates'--a list of all the dates in the data
    'medians'--a list of all the medians calculated
    """
    dates,pollutionData=getRequiredData(data,"date",monitoring_station,pollutant)
    count=0
    while dates[count]!=date:
        #checks for the correct date and skips through for each time
        count+=24
    values=[]    
    for i in range(count,count+24):
        values.append(pollutionData[i])
    #again returns both for ease of display in main
    return date,values[maxvalue(values)]

def count_missing_data(data,  monitoring_station,pollutant):
    """
    counts number of missing data points
    
    Arguements:
    'data'--full dictonary of all the data
    'monitoring_station'--desired station
    'pollutant'--desired pollutant

    returns:
    'count'--the number of missing data points
    """
    values =data[monitoring_station][pollutant]
    count=countvalue(values,"no data")
    return count    

def fill_missing_data(data, new_value,  monitoring_station,pollutant):
    """
    replaces no data with input value
    
    Arguements:
    'data'--full dictonary of all the data
    'new_value'--the replacement value
    'monitoring_station'--desired station
    'pollutant'--desired pollutant

    returns:
    'values'--the new list of values
    """
    values =data[monitoring_station][pollutant]
    if is_a_number(new_value)==False:
        new_value=0
    for i in range(0,len(values)):
        if values[i]=="no data":
            values[i]=new_value
    return values
