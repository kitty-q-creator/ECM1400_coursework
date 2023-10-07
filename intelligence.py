# This is a template. 
# You should modify the functions below to match
# the signatures determined by the project specification
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def find_red_pixels(map_filename, upper_threshold=100, lower_threshold=50):
    """
    Creates an image file with just the map of white pixels and returns the array of where the red pixels are
    
    'map_filename'--the image file to be read
    'upper_threshold=100'--number the red value should be higher than
    'lower_threshold=50'--number the green and blue values should be lower than

    "map-red-pixels.jpg"--the output image file which will be saved

    'redPixelsImage'--the output array containing the representation of the image file
    """
    RGBimage=mpimg.imread(map_filename)
    RGBimage=RGBimage*255
    redPixelsImage=RGBimage.copy()
    for i in range (0,1140):
        for j in range(0,1053):
            if (RGBimage[i,j,0]>upper_threshold) and (RGBimage[i,j,1]<lower_threshold)and (RGBimage[i,j,2]<lower_threshold):
                redPixelsImage[i,j]=[1,1,1,1]     
            else:
                redPixelsImage[i,j]=[0,0,0,1]
    plt.imsave("map-red-pixels.jpg",redPixelsImage)
    return redPixelsImage

def find_cyan_pixels(map_filename, upper_threshold=100, lower_threshold=50):
    """
    Creates an image file with just the map of white pixels and returns the array of where the red pixels are
    
    'map_filename'--the image file to be read
    'upper_threshold=100'--number the green and blue values  should be higher than
    'lower_threshold=50'--number the red value should be lower than

    "map-cyan-pixels.jpg"--the output image file which will be saved

    'cyanPixelsImage'--the output array containing the representation of the image file
    """
    RGBimage=mpimg.imread(map_filename)
    RGBimage=RGBimage*255
    cyanPixelsImage=RGBimage.copy()
    for i in range (0,1140):
        for j in range(0,1053):
            if (RGBimage[i,j,0]<lower_threshold) and (RGBimage[i,j,1]>upper_threshold)and (RGBimage[i,j,2]>upper_threshold):
                cyanPixelsImage[i,j]=[1,1,1,1]     
            else:
                cyanPixelsImage[i,j]=[0,0,0,1]
    plt.imsave("map-cyan-pixels.jpg",cyanPixelsImage)
    return cyanPixelsImage

def detect_connected_components(IMG):
    """
    Introduces a variable named componentNumber to keep track of which component we are on

    When setting mark as visited I used the component number. 
    I then went through the mark array in the putComponenetsIntoList function to get the list of components.
    """
    mark=np.zeros([1140,1053])
    Q=np.zeros([10000000,2],int)
    
    componentNumber=1
    for i in range (0,1140):
            for j in range(0,1053):
                if IMG[i,j,0]==1 and mark[i,j]==0:
                    mark[i,j]=componentNumber
                    count=1
                    Q[0]=[i,j]
                    head=0
                    tail=1
                    while head!=tail:
                        a =Q[head,0]
                        b=Q[head,1]
                        head+=1
                        for k in range(a-1,a+2):
                            for l in range(b-1,b+2):
                                if k!=a or b!=l:
                                    if k>=0 and l>=0 and k<1140 and l<1053:
                                        if IMG[k,l,0]==1  and mark[k,l]==0:
                                            mark[k,l]=componentNumber
                                            Q[tail,0]=k
                                            Q[tail,1]=l
                                            tail+=1
                                            count+=1
                    
                    componentNumber+=1
    
    with open(" cc-output-2a.txt","w")as file:
        components=putComponenetsIntoList(mark)
        file.write(putComponentsIntoText(components))
    return mark

def detect_connected_components_sorted(mark):
    """
    Generate list of connected components from mark
    Sort this list and output it to text
    Create an image file containing just the 2 largest paths

    'mark'--the array returned from detect_connected_components

    "cc-output-2b.txt"--the text file the sorted array is output to
    "cc-top-2.jpg.jpg"--the output image file
    """
    components=putComponenetsIntoList(mark)
    sortedComponents=mergeSort(components)

    with open("cc-output-2b.txt","w")as file:
        #write sorted list to file
        file.write(putComponentsIntoText(sortedComponents))

    #put the largest 2 components into image file
    #get the component number for the 2 largest
    largest=sortedComponents[0][0]
    secondLargest=sortedComponents[1][0]
    largestComponents=np.zeros([1140,1053,3])#make a black image the correct size
    for i in range (0,1140):
        for j in range(0,1053):
            #sort through the mark array and when you find the component number for the 2 largest make that pixel white
            if mark[i,j]==largest or mark[i,j]==secondLargest:
                largestComponents[i,j]=[1,1,1]
    plt.imsave("cc-top-2.jpg.jpg",largestComponents)
    
def putComponentsIntoText(list):
    """
    Used to output text which can then be saved to relevant text file in both the detect_connected_components and  detect_connected_components_sorted functions

    'list'--the list of components

    'text'--the text which can then be saved to relevant text file
    """
    text=""
    for component in list:
        text+="Component "+str(component[0])+" has "+str(component[1])+" pixels\n"     
    text+="Total number of connected components is "+str(len(list))
    return text

def mergeSort(components):
    """
    Used to sort the connected components

    'components'--the list of connected components

    'sorted'--the sorted list of connected components
    """
    if len(components)<2:
        return components
    else:
        mid=len(components)//2
        leftList=components[0:mid]
        rightList=components[mid:]
        sortedLeft=mergeSort(leftList)
        sortedRight=mergeSort(rightList)
        sorted=[]
        while sortedLeft!=[] and sortedRight!=[]:
            if sortedLeft[0][1]>sortedRight[0][1]:
                #just looks at the second element as the components are stored [number,size]
                sorted.append(sortedLeft.pop(0))
            else:
                sorted.append( sortedRight.pop(0))

        #when one of the lists is empty the other is sorted so can just be added onto the end       
        if sortedLeft!=[]:
            sorted=sorted+sortedLeft
        else:
            sorted=sorted +sortedRight
    return sorted

def putComponenetsIntoList(mark):
    """
    Takes the mark array and outputs a list of the component number and size of the component

    'mark'--the array outputted from detect_connected_components

    'component list'--the list of connected components
    """
    components=dict()#used a dictionary and then a list because it's easier to check if a key is present and create one if the component has not yet been found
    for i in range (0,1140):
            for j in range(0,1053):
                x=int(mark[i,j])#for ease of not having to repeat this 
                if x!=0:
                    if x in components:
                        components[x]+=1
                    else:
                        components[x]=1
    #turned the dictionary into a list as the sorted components part requires an ordered data type
    componentList=[]
    for i in range(1,len(components)+1):
        componentList.append((i,components[i]))  
    return componentList


