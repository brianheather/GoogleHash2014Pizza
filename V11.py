from copy import deepcopy
#from numba import jit
import numpy as np
from datetime import datetime

def getPossible(startx, starty, dePizza):
    for i in range(endCol):
        for j in range(endRow):
            if checkRange(startx,starty,i,j):
                lol = getValues(startx,starty,i,j,dePizza)
                if None not in lol:
                    mush, tom = 0, 0
                    for k in lol:
                        if k == "M":
                            mush += 1
                        elif k == "T":
                            tom += 1
                        else:
                            print("ERROR - '" + k + "'")

                        #Big area optismiser
                        if (mush >= minValue) and (tom >= minValue):
                            break #Yield?
                    if (mush >= minValue) and (tom >= minValue):
                        yield [startx,starty,i,j]
                           
    yield "Fin"    

def checkRange(x1, y1, x2, y2):
    return maxArea >= (x2-x1+1) * (y2-y1+1)
    #(abs(x1-x2)+1) * (abs(y1-y2)+1)

def calRange(x1, y1, x2, y2):
    return (x2-x1+1) * (y2-y1+1)
    #(abs(x1-x2)+1) * (abs(y1-y2)+1)

def calTotalArea(lis):
    num = 0
    for i in lis:
        num += calRange(i[0],i[1],i[2],i[3])
    return num
    
def getValues(x1, y1, x2, y2,dePizza):
    temp = []
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            temp.append(dePizza[i][j])
        #temp.append("\n")
    return temp

def cutPizza(x1,y1,x2,y2,tempPizza):
    for i in range(x1,x2+1):
        tempPizza[i][y1:y2+1] = [None]*(y2-y1+1)
    return tempPizza

def addPizza(x1,y1,x2,y2,tempPizza):
    for i in range(x1,x2+1):
        tempPizza[i][y1:y2+1] = data[i][y1:y2+1]
    return tempPizza

def getStart(cut): #end
    for i in range(endCol):
        for j in range(endRow):
            if cut[i][j] is not None:
                return [i,j]
    return False

def printer(asdf):
    for i in asdf:
        for j in i:
            if j is None:
                print(end = " ")
            else:
                print(j, end = "")
        print("")

def endPrinter(asdf):
    temp = ""
    for i in asdf:
        for j in i:
            temp += str(j) + " "
        temp += "\n"
    return temp
#########################################
#########################################
#Start
deFileSize = "medium"
deFile = open(deFileSize+".in") #<-- change file name
file = deFile.read().split("\n")
inputter = file[0].split(" ")
#inputter = input("Info: ").split(" ") #<--Or input manually,
                    #Make sure to hide the file managing!
endCol = int(inputter[0])
endRow = int(inputter[1])
biggestArea = (endCol) * (endRow)
minValue = int(inputter[2])
maxArea = int(inputter[3])

tempData = []
#""" #For manual input delete the # at the front
for info in file[1:]:
    tempData.append([deT for deT in info])
data = np.array(tempData,dtype=object)
#"""
""" #File input, delete # at the front
for _ in range(int(inputter[0])):
    a = input()
    temp = [a[i:i+1] for i in range(0, len(a), 1)]
    data.append(temp)
#"""
outLoop, MAINLOOP, numArea = [], [], 0
maxSlice, maxAreaA, maxFormula = 0, 0, [] #many slices, as much pizza, the formula

startx, starty, dePizza = 0,0,deepcopy(data)
temp = [getPossible(startx, starty, deepcopy(data))]
i = next(temp[len(temp)-1])

fileCount = 0
while True:
    if i == "Fin":
        MAINLOOP.append(deepcopy(outLoop))
        if numArea > maxAreaA or numArea == maxArea and len(outLoop) > maxSlice:
            maxAreaA = numArea
            maxSlice = len(outLoop)
            maxFormula = deepcopy(outLoop)

            if numArea == biggestArea:
                a = open("deFile"+deFileSize+str(fileCount)+".txt","w")
                #print(maxArea)
                a.write(str(maxSlice)+"\n")
                a.write(endPrinter(maxFormula))
                a.close()
                print("Skipper")
                fileCount += 1
                now = datetime.now()
                print(now.strftime("%%H:%M:%S d/%m/%Y"))
        
        temp.pop()
        try:
            pizzaData = outLoop.pop()
        except IndexError:
            break

        dePizza = addPizza(pizzaData[0], pizzaData[1], pizzaData[2], pizzaData[3], deepcopy(dePizza))
        numArea -= calRange(pizzaData[0],pizzaData[1],pizzaData[2],pizzaData[3])
        
    else:
        outLoop.append(i)
        dePizza = cutPizza(i[0],i[1],i[2],i[3],deepcopy(dePizza))
        numArea += calRange(i[0],i[1],i[2],i[3])
        
        try:
            startx, starty = getStart(dePizza)
        except TypeError as e:
            startx, starty = endCol, endRow

        temp.append(getPossible(startx, starty, dePizza))
    while True:
        try:
            i = next(temp[len(temp)-1])
            break
        except StopIteration as e:
            temp.pop()
            pizzaData = outLoop.pop()
            dePizza = addPizza(pizzaData[0], pizzaData[1], pizzaData[2], pizzaData[3], deepcopy(dePizza))
            numArea -= calRange(pizzaData[0],pizzaData[1],pizzaData[2],pizzaData[3])

    
print(maxSlice)
#print(maxAreaA)
print(endPrinter(maxFormula))
