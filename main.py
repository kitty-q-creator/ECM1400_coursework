# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
from reporting import *
from intelligence import *
from monitoring import *

def printData(list1,list2):
    for i in range(0,len(list1)):
        print(f"{list1[i]}:{list2[i]}")

def getDataForStation(dictionary,station):
    """
    Gets data from file for a specified station

    'dictionary'--the dictionary of data for the station
    'station'--the name of the station
    """
    filename="./data/" + station +".csv"

    with open(filename) as file:
        #creates 5 lists for each column
        date=[]
        time=[]
        no=[]
        pm10=[]
        pm25=[]
        for line in file:
            temp=line.split(",")
            date.append(temp[0])
            time.append(temp[1])
            no.append(temp[2])
            pm10.append(temp[3])
            pm25.append(temp[4].strip("\n"))
        #remove the heading from each list and sets this as the key
        dictionary[date.pop(0)]=date
        dictionary[time.pop(0)]=time
        dictionary[no.pop(0)]=no
        dictionary[pm10.pop(0)]=pm10
        dictionary[pm25.pop(0)]=pm25

def getData(data):
    """
    Gets all the data

    'data'--the dictionary for all the data from all 3 files
    """
    #dictionary for each location
    LondonHarlington=dict()
    LondonMarylebone=dict()
    LondonKensington=dict()
    #gets data from each of the 3 files
    (LondonHarlington,"Pollution-London Harlington")
    getDataForStation(LondonMarylebone,"Pollution-London Marylebone Road")
    getDataForStation(LondonKensington,"Pollution-London N Kensington")
    #create a dictionary of all the data
    data["Harlington"]=LondonHarlington
    data["Marylebone"]=LondonMarylebone
    data["Kensington"]=LondonKensington

def main_menu():
    """The main menu"""
    data=dict()
    getData(data)#decided to get data when program opens to save time loading from file everytime PR module accessed
    quit= False#allows menu to repeat until exited
    while quit==False:
        print("Access the PR module(R)")
        print("Access the MI module(I)")
        print("Access the RM module(M)")
        print("Print the About text(A)")
        print("Quit the application(Q)")
        answer=input("Please enter the letter corrisponding to your choice\n").upper()
        if answer=="R":
            reporting_menu(data)
        elif answer=="I":
            intelligence_menu()
        elif answer =="M":
            monitoring_menu()
        elif answer=="A":
            about()
        elif answer=="Q":
            quit=quit()
        else: print("Invalid input")

def getInput():
    """
    Used to take user input of location and polutant for options in the PR module which require it
    """
    valid=False#allows repeates until user inputs a valid choice
    while valid==False:
        print("London harlington(H)")
        print("London marylebone Road(M)")
        print("North Kensington(K)")
        responce=input("Please enter the letter of the monitering station you use to view\n").upper()
        if responce=="H":
            station="Harlington"
            valid=True
        if responce=="M":
            station="Marylebone"
            valid=True
        if responce=="K":
            station="Kesington"
            valid=True
    valid=False#allows repeates until user inputs a valid choice
    while valid==False:
        print("(1)no")
        print("(2)pm10")
        print("(3)pm25")
        responce=input("Please enter the number of the pollutant\n").upper()
        if responce=="1":
            polutant="no"
            valid=True
        if responce=="2":
            polutant="pm10"
            valid=True
        if responce=="3":
            polutant="pm25"
            valid=True
    return station,polutant

def reporting_menu(data):
    """
    Allows user to input a number to select what they want to do

    'data'--to be passed on to necessary function
    """
    valid=False
    while valid==False:
        print("(1) daily average")
        print("(2) daily median")
        print("(3) hourly average")
        print("(4) monthly average")
        print("(5) peak hour")
        print("(6) count missing data points")
        print("(7) edit missing data points")
        print("(8) return to menu")
        answer=input("please enter the number of your choice\n")
        valid=True#put this here to avoid repeating the line many times and just change it back if the input is invalid
        if answer=="1":
            monitoringStation,pollutant=getInput()
            printData(daily_average(data, monitoringStation,pollutant))
        elif answer=="2":
            monitoringStation,pollutant=getInput()
            printData(daily_median(data, monitoringStation,pollutant))
        elif answer=="3":
            monitoringStation,pollutant=getInput()
            printData(hourly_average(data, monitoringStation,pollutant))
        elif answer=="4":
            monitoringStation,pollutant=getInput()
            printData(monthly_average(data, monitoringStation,pollutant))
        elif answer=="5":
            monitoringStation,pollutant=getInput()
            date=input("Please enter the date")#add some sort of validation but currently cba
            peak_hour_date(data,date, monitoringStation,pollutant)
        elif answer=="6":
            monitoringStation,pollutant=getInput()
            count =count_missing_data(data, monitoringStation,pollutant)
            print (f"There are {count} instances of missing data")
        elif answer=="7":
            monitoringStation,pollutant=getInput()
            newValue=input("Please enter replacement value\n")
            replacements=fill_missing_data(data,newValue, monitoringStation,pollutant)
            for i in range(0,len(replacements)):
                data[monitoringStation][pollutant][i]=replacements[i]
        elif answer!="8":#if user didn't select return to menu ask for input again
            valid=False

def monitoring_menu():
    """Your documentation goes here"""
    valid=False
    while valid==False:
        print("(1) average levels of a pollutant for a station for a week")
        print("(2) average levels of a pollutant for 3 stations for a week")
        print("(3) average levels of multiple pollutants for Marylebone Road for a week")
        print("(4) return to menu")
        answer=input("please enter the number of your choice\n")
        valid=True#put this here to avoid repeating the line many times and just change it back if the input is invalid
        if answer=="1":
            valid=False#allows repeates until user inputs a valid choice
            while valid==False:
                print("London harlington(H)")
                print("London marylebone Road(M)")
                print("North Kensington(K)")
                responce=input("Please enter the letter of the monitering station you use to view\n").upper()
                if responce=="H":
                    site="HRL"
                    valid=True
                if responce=="M":
                    site="MY1"
                    valid=True
                if responce=="K":
                    site="KC1"
                    valid=True
            pollutant=input("Please enter species code\n")
            textForAveragesForSite(site,pollutant)
        elif answer=="2":
            pollutant=input("Please enter species code\n")
            averagesForAWeek(pollutant)
        elif answer=="3":
            getMonitoringInput()
        elif answer!="4":#if user didn't select return to menu ask for input again
            valid=False

def intelligence_menu():
    """Allows user to choose what they want to do"""
    colourPicked=False
    while colourPicked==False:#repeats until valid input
        answer=input("Would you like to work with cyan(C) or red(R) pixels\n").upper() 
        if answer=="R":
            image=find_red_pixels("data\map.png")
            colourPicked=True
        elif answer=="C":
            find_cyan_pixels("data\map.png")
            colourPicked=True
    returnToMenu=False
    while returnToMenu==False:#again allows repeat until valid input
        print("Generate list of connected components(C)")
        print("Generate ordered list of connected components with the largest 2 output to image file(O)")
        print("Return to menu(R)")
        answer=input("Please enter the letter of your choice\n").upper() 
        if answer=="C":
            detect_connected_components(image)
            returnToMenu=True
        elif answer=="O":
            detect_connected_components_sorted(detect_connected_components(image))
            returnToMenu=True
        elif answer=="R":
            returnToMenu=True

def about():
    """about me"""
    print("ECM14002")
    print("244438")

def quit():
    """
    Asks user if their sure they want to quit
    if yes program terminates
    """
    while True:
        print("Are you sure you want to quit?")
        answer=input("y/n\n").upper()
        if answer=="Y":
            return True
        elif answer=="N":
            return False

if __name__ == '__main__':
    main_menu()
