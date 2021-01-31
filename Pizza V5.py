from copy import deepcopy #used to copy data into new data
class subPizza:
    def __init__(self,coords):
        self.goodCoords = coords
        self.size = 0;
        self.calSize()
        
    def __repr__(self):
        #return '{},{} '.format(self.goodCoords, self.size)
        return '{}'.format(self.goodCoords)

    def __getitem__(self, i):
        return self.goodCoords[i]
    
    def calSize(self):
        deSize = calRange(self.goodCoords[0],self.goodCoords[1],
                           self.goodCoords[2],self.goodCoords[3])
        self.size = deSize
    
def getPossible(startx, starty):
    goodCoord = []
    for i in range(endCol):
        for j in range(endRow):
            if checkRange(startx,starty,i,j):
                lol = getValues(startx,starty,i,j)
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
                        pass
                    else:
                        print("ERROR - '" + k + "'")
                if (mush >= minValue) and (tom >= minValue):
                    goodCoord.append(subPizza([startx,starty,i,j]))

    return sorted(goodCoord, key = sort, reverse = False) #False is smallest to biggest, True reverse

def sort(asdf):
    return asdf.size

def checkRange(x1, y1, x2, y2):
    return maxArea >= (abs(x1-x2)+1) * (abs(y1-y2)+1)

def calRange(x1, y1, x2, y2):
    return (abs(x1-x2)+1) * (abs(y1-y2)+1)

def calTotalArea(lis):
    num = 0
    for i in lis:
        num += calRange(i[0],i[1],i[2],i[3])
    return num

def getValues(x1, y1, x2, y2):
    temp = []
    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            temp.append(data[i][j])
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

inputter = input("Info: ").split(" ")
endCol = int(inputter[0])
endRow = int(inputter[1])
biggestArea = (endCol+1) * (endRow+1)
minValue = int(inputter[2])
maxArea = int(inputter[3])

data = []
for _ in range(int(inputter[0])):
    a = input()
    temp = [a[i:i+1] for i in range(0, len(a), 1)]
    data.append(temp)

###################################

global outLoop, oldPizza, maxSlice, maxAreaA, maxFormula
outLoop = []
oldPizza = []
maxSlice, maxAreaA, maxFormula = 0, 0, []

def helpMEE(startx, starty, dePizza):
    temp = getPossible(startx, starty)
    
    if temp == []:
        #print(">>",outLoop) #cal
        num = calTotalArea(outLoop)
        global maxAreaA, maxSlice, maxFormula
        if num > maxAreaA or num == maxArea and len(outLoop) > maxSlice:
            maxAreaA = num
            maxSlice = len(outLoop)
            maxFormula = deepcopy(outLoop)

            if num == biggestArea:
                print(maxArea)
                print(maxSlice)
                endPrinter(maxFormula)
        
    else:
        for i in temp:
            
            dePizza = cutPizza(i[0],i[1],i[2],i[3],dePizza)

            try:
                startx, starty = getStart(dePizza)
            except TypeError as e:
                startx, starty = endCol, endRow
            outLoop.append(i)
            helpMEE(startx, starty, dePizza)
            
            pizzaData = outLoop.pop(len(outLoop)-1)
            dePizza = addPizza(pizzaData[0], pizzaData[1], pizzaData[2], pizzaData[3], dePizza)
    
            
            
helpMEE(0,0,deepcopy(data))
print(maxSlice)
#print(maxAreaA)
endPrinter(maxFormula)
