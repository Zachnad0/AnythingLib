# ========== AnythingLib ==========
# 
# Ayo uh yea this is my everything python library.
# Feel free to suggest additions, edit, and use this library for anything or whatever.
# The more random crap, the better.
#
# ========== AnythingLib ==========

class SortingAlgorithms: # Sorting algorithms and crap go here
    def BubbleSort(inArray:list):
        #sorts via bubblesorting algorithm
        itersXSwapsXCompares = [0, 0, 0] #iteration, swap counts and compares
        not_sorted = True
        while not_sorted:
            not_sorted = False
            for currIndex in range(1, len(inArray)):
                # print(currIndex) #debug
                prevNum = inArray[currIndex-1]
                currNum = inArray[currIndex]
                itersXSwapsXCompares[2] += 1
                if prevNum > currNum: #swap
                    # print(str(prevNum) + " > " + str(currNum)) #debug
                    inArray[currIndex-1] = currNum
                    inArray[currIndex] = prevNum
                    not_sorted = True #if it had to swap, then it should check again at least once more
                    itersXSwapsXCompares[1] += 1
            itersXSwapsXCompares[0] += 1
        
        return itersXSwapsXCompares
    
    def OptimalBubbleSort(inArray:list):
        #sorts via bubblesorting algorithm (but optimized with like 1 line)
        itersXSwapsXCompares = [0, 0, 0] #iteration, swap counts and compares
        not_sorted = True
        while not_sorted:
            not_sorted = False
            for currIndex in range(1, len(inArray) - itersXSwapsXCompares[0]): #literally just this
                # print(currIndex) #debug
                prevNum = inArray[currIndex-1]
                currNum = inArray[currIndex]
                itersXSwapsXCompares[2] += 1
                if prevNum > currNum: #swap
                    # print(str(prevNum) + " > " + str(currNum)) #debug
                    inArray[currIndex-1] = currNum
                    inArray[currIndex] = prevNum
                    not_sorted = True #if it had to swap, then it should check again at least once more
                    itersXSwapsXCompares[1] += 1
            itersXSwapsXCompares[0] += 1
        
        return itersXSwapsXCompares
    
    def SelectionSort(inArray:list):
        #sorts via lowest through iteration, which iterates for all above to obtain said lowest.
        itersXSwapsXCompares = [0, 0, 0] #iteration, swap counts and compares
        for indexAlpha in range(0, len(inArray) - 1):
            itersXSwapsXCompares[0] += 1
            currNum = inArray[indexAlpha]
            for indexBeta in range(indexAlpha + 1, len(inArray)):
                testNum = inArray[indexBeta]
                itersXSwapsXCompares[2] += 1
                # print("Cn: " + str(currNum) + "  Tn: " + str(testNum)) #debug
                if currNum > testNum:
                    # print("Swap!") #debug
                    itersXSwapsXCompares[1] += 1
                    inArray[indexBeta] = currNum
                    currNum = inArray[indexAlpha] = testNum
        
        return itersXSwapsXCompares

class CustomMath: # Put math related crap down here
    def CubicEquation(x: int,a: float,b: float,c: float, d: float):
        y = round((a*pow(x,3))+(b*pow(x,2))+(c*x)+d)
        return y
    
    def QuadraticEquation(x: int,a: float,b: float,c: float):
        # print("xabc: ",x,a,b,c) #debug
        y = round(a*pow(x,2)+(b*x)+c)
        return y
    
    def LinearEquation(x: int,a: float,b: float):
        y = round((a*x)+b)
        return y
