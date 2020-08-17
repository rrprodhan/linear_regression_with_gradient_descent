#For the given dataset running 1000 iterations should give: 
#Interseption: 0.95 and Slope = 0.64
#The program works for any number of independent variables

import pandas as pd

dataset = pd.read_csv('data.csv')

dataValues = dataset.iloc[:,:].values
datasetLength = len(dataset)
numberOfIndependentVariables = len(dataset.columns)-1
b = [] #list of new intercept and slope values
learningRate = 0.01

#Finding total number of columns
numberOfColumns = 0
for col in dataset.columns: 
    print(col) #prints individual column names
    numberOfColumns = numberOfColumns + 1

def linearRegWithGradDescent():
    #Finding sum of squared residuals
    squaredResiduals = 0
    ssr = 0
    for i in range(datasetLength):
        ssr = ssr+squaredResiduals
        for j in range(numberOfColumns-1):
            squaredResiduals = pow((dataValues[i][0]-(b[0]+(b[j+1]*dataValues[i][j+1]))),2)
           
    ssr = ssr+squaredResiduals #Final value of ssr after adding the value of the Last row
    
    #Derivating ssr by intercept and slope(s)
    slopes = [] #list of intercept-slope and other slopes after derivation
    
    #Derivating ssr by intercept
    residuals = 0
    slopeOfIntercept = 0
    for i in range(datasetLength):
        slopeOfIntercept = slopeOfIntercept+residuals
        for j in range(numberOfColumns-1):
            residuals = -2*(dataValues[i][0]-(b[0]+(b[j+1]*dataValues[i][j+1])))
          
    slopeOfIntercept = slopeOfIntercept+residuals #Final value of ssr after adding the value of the Last row
    slopes.append(slopeOfIntercept)
    
    #Derivating ssr by slope(s)
    for n in range(numberOfIndependentVariables):
        residuals = 0
        currentSlope = 0
        for i in range(datasetLength):
            currentSlope = currentSlope+residuals
            for j in range(numberOfColumns-1):
                residuals = -2*dataValues[i][j+1]*(dataValues[i][0]-(b[0]+(b[j+1]*dataValues[i][j+1])))
        
        currentSlope = currentSlope+residuals #Final value of ssr after adding the value of the Last row
        slopes.append(currentSlope)
        
    #Calculating step size
    slopes = [slopeValues * learningRate for slopeValues in slopes]
    
    #Calculating and updating new intercept and slope(s)
    b[0] = b[0]-slopes[0]
    for i in range(numberOfColumns-1):
        b[i+1] = b[i+1]-slopes[i+1]
        
def main():
    #interception and slope value initialization
    b.append(0) #initializing intercept with 0
    for i in range(numberOfColumns-1):
        b.append(1) #initializing slope(s) with 1
        
    slopes = [] #list of intercept-slope and other slopes after derivation
    
    iteration = int(input("Input iteration number: "))
    
    for i in range(iteration):
        linearRegWithGradDescent()
        slopes.append(9999) #Initializing it with 9999 to avoid list index out of range error
        if slopes[0]==0:
            break
        else:
            slopes.clear() #clearing junk values from slopes from previous iteration
    
    print("Result: \nIntercept: {}".format(b[0]))
    for i in range(numberOfColumns-1):
        print("Slope{}: {}".format(i+1,b[i+1]))

if __name__ == "__main__": 
    main() 












