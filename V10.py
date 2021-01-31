#Version 10, works
import copy

def getPossible(startx, starty, dePizza):
    goodCoord = []
    for i in range(endCol):
        for j in range(endRow):
            if checkRange(startx,starty,i,j):
                lol = getValues(startx,starty,i,j,dePizza)
                if None not in lol:
                    mush = 0
                    tom = 0
                    for k in lol:
                        if k == "M":
                            mush += 1
                        elif k == "T":
                            tom += 1
                        elif k == "\n":
                            pass
                        elif k is None:
                            return []
                        else:
                            print("ERROR - '" + k + "'")

                        #Big area optismiser
                        if (mush >= minValue) and (tom >= minValue):
                            break
                    if (mush >= minValue) and (tom >= minValue):
                        yield [startx,starty,i,j]
    yield "Fin"    

def checkRange(x1, y1, x2, y2):
    return maxArea >= (abs(x1-x2)+1) * (abs(y1-y2)+1)

def calRange(x1, y1, x2, y2):
    return (abs(x1-x2)+1) * (abs(y1-y2)+1)

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
        temp.append("\n")
    return temp

def cutPizza(x1,y1,x2,y2,tempPizza):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            tempPizza[i][j] = None
    return tempPizza

def addPizza(x1,y1,x2,y2,tempPizza):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            tempPizza[i][j] = data[i][j]
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
    for i in asdf:
        for j in i:
            print(j, end = " ")
        print("")
#########################################
#########################################
#Start
deFile = open("example.in") #<-- change file name
file = deFile.read().split("\n")
inputter = file[0].split(" ")
#inputter = input("Info: ").split(" ") #<--Or input manually,
                    #Make sure to hide the file managing!
endCol = int(inputter[0])
endRow = int(inputter[1])
biggestArea = (endCol+1) * (endRow+1)
minValue = int(inputter[2])
maxArea = int(inputter[3])

data = []
#""" #For manual input delete the # at the front
for info in file[1:]:
    data.append([deT for deT in info])
#"""
""" #File input, add a # at the front
for _ in range(int(inputter[0])):
    a = input()
    temp = [a[i:i+1] for i in range(0, len(a), 1)]
    data.append(temp)
#"""
outLoop = []
maxSlice, maxAreaA, maxFormula = 0, 0, []

MAINLOOP = []

startx, starty, dePizza = 0,0,copy.deepcopy(data)
temp = [getPossible(startx, starty, copy.deepcopy(data))]
i = next(temp[len(temp)-1])

while True:
    if i == "Fin":
        num = calTotalArea(outLoop)
        MAINLOOP.append(copy.deepcopy(outLoop))
        if num > maxAreaA or num == maxArea and len(outLoop) > maxSlice:
            maxAreaA = num
            maxSlice = len(outLoop)
            maxFormula = copy.deepcopy(outLoop)

            if num == biggestArea:
                print(maxArea)
                print(maxSlice)
                endPrinter(maxFormula)
                print("HII")

        temp.pop()
        try:
            pizzaData = outLoop.pop()
        except IndexError:
            break

        dePizza = addPizza(pizzaData[0], pizzaData[1], pizzaData[2], pizzaData[3], copy.deepcopy(dePizza))
    else:
        dePizza = cutPizza(i[0],i[1],i[2],i[3],copy.deepcopy(dePizza))
        outLoop.append(i)
        
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
            dePizza = addPizza(pizzaData[0], pizzaData[1], pizzaData[2], pizzaData[3], copy.deepcopy(dePizza))
        

    
print(maxSlice)
#print(maxAreaA)
endPrinter(maxFormula)
