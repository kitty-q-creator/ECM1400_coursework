# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification.
# 
# This module will access data from the LondonAir Application Programming Interface (API)
# The API provides access to data to monitoring stations. 
# 
# You can access the API documentation here http://api.erg.ic.ac.uk/AirQuality/help
#

def get_live_data_from_api(site_code='MY1',species_code='NO',start_date=None,end_date=None):
    """
    Return data from the LondonAir API using its AirQuality API. 
    
    *** This function is provided as an example of how to retrieve data from the API. ***
    It requires the `requests` library which needs to be installed. 
    In order to use this function you first have to install the `requests` library.
    This code is provided as-is. 
    """
    import requests
    import datetime
    start_date = datetime.date.today() if start_date is None else start_date
    end_date = start_date + datetime.timedelta(days=1) if end_date is None else end_date
    
    
    endpoint = "https://api.erg.ic.ac.uk/AirQuality/Data/SiteSpecies/SiteCode={site_code}/SpeciesCode={species_code}/StartDate={start_date}/EndDate={end_date}/Json"
   
    url = endpoint.format(
        site_code = site_code,
        species_code = species_code,
        start_date = start_date,
        end_date = end_date
    )
    
    res = requests.get(url)
    return res.json()
import datetime 
from utils import *
def averagesForAWeek(pollutant):
    """
    Gets averages for the week for 3 different locations and displays them in a table next to each other
    'pollutant'--species code
    """
    mr=averagesForSite("MY1",pollutant)
    nk=averagesForSite("KC1",pollutant)
    h=averagesForSite("HRL",pollutant)
    #displaying what my abrivations mean for user to make the table more compact 
    print("mr-Marylebone Road")
    print("nk-North Kensington")
    print("h-Harlington")
    #placeholders to make formatting the display easier
    a="date"
    b="mr"
    c="nk"
    d="h"
    print(f"{a:12}{b:7}{c:7}{d:7}")
    for i in range(0,7):
        day=datetime.date.today() - datetime.timedelta(days=(i+1))
        #the same placeholders to make display easier to do
        a=str(day)
        b=str(mr[i]) if mr[i]!=0 else "-"
        c=str(nk[i]) if nk[i]!=0 else "-"
        d=str(h[i]) if h[i]!=0 else "-"
        print(f"{a:12}{b:7}{c:7}{d:7}")

def averagesForSite(site,pollutant):
    """
    Input of a site and pollutant and then outputs the average values for a week

    'site'--the site code
    'pollutant--the species code
    """
    averages=[]
    for i in range(1,8):
        start=datetime.date.today() - datetime.timedelta(days=i)
        data=get_live_data_from_api(site_code=site,species_code=pollutant,start_date=start,)
        day=data["RawAQData"]["Data"]
        dayList=[]
        for item in day:
            if item["@Value"]!="":
                dayList.append(item["@Value"])
        averages.append(round(meannvalue(dayList),1))
    return averages

def textForAveragesForSite(site,pollutant):
    averages=averagesForSite(site,pollutant)
    for i in range(1,8):
        day=datetime.date.today() - datetime.timedelta(days=i)
        text=str(day)+":"+str(averages[i-1])
        print(text)

def averagesForPollutants(list):
    """
    
    """
    dictionary=dict()
    for i in range(1,8):
        day=datetime.date.today() - datetime.timedelta(days=i)
        dictionary[day]=[]
    for speciesCode in list:
        temp=averagesForSite(speciesCode,"MY1")
        for i in range(1,8):
            day=datetime.date.today() - datetime.timedelta(days=i)
            dictionary[day].append(temp[i-1])
    #print data
    for i in range(1,8):
        day=datetime.date.today() - datetime.timedelta(days=i)
        text=str(day)+":"
        for j in range(0,len(list)):
            text+=list[j]+"="+str(dictionary[day][i]+",")
        print(text)

def getMonitoringInput():
    valid=False
    done=False
    list=[]
    while done==False:
        answer=input("Please enter a species code or D for done").upper
        if answer=="D":
            done=True
        else:
            list.append(answer)
    averagesForPollutants(list)



#averagesForPollutants(["NO"])