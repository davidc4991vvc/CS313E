#  File:                sortng.py
#  Description:         Testing and comparing the run time of
#                       5 different sorting algorithms
#  Student's Name:      Nicolas Key
#  Student's UT EID:    nak724
#  Course Name:         CS 313E 
#  Unique Number:       51915
#
#  Date Created:        4/17/2017
#  Date Last Modified:  4/18/2017


import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

def makeAlmost(myList):
    n = len(myList)
    swaps = n // 10
    count = 0
    while(count < swaps):
        num1 = random.randint(0, n - 1)
        num2 = random.randint(0, n - 1)
        if(num1 != num2):
            val1 = myList[num1]
            val2 = myList[num2]
            myList[num1] = val2
            myList[num2] = val1
            count += 1
    return myList

def main():
    
    sorts = ["bubble", "insertion", "selection", "merge", "quick"]
    listTypes = ["random", "sorted", "reverse", "almost"]
    sizes = [10, 100, 1000]
    bubbleT = [[], [], [], []]
    insertionT = [[], [], [], []]
    selectionT = [[], [], [], []]
    mergeT = [[], [], [], []]
    quickT = [[], [], [], []]
    for algo in sorts:                  #loop for sort algorithms
        for listType in listTypes:      #loop random list, sorted list, reverse order list, almsot sorted list
            for size in sizes:          #loop n = 10, 100, 1000
                temp = 0
                flag = -1
                for trial in range(5):  #loop for 5 trials
                    myList = []
                    for n in range(size):
                        myList.append(n)
                    if(listType == "random"):
                        random.shuffle(myList)
                        flag = 0
                    elif(listType == "sorted"):
                        flag = 1
                    elif(listType == "reverse"):
                        myList.reverse()
                        flag = 2
                    elif(listType == "almost"):
                        myList = makeAlmost(myList)
                        flag = 3
                    elapsedTime = 0
                    if(algo == "bubble"):
                        startTime = time.perf_counter()
                        bubbleSort(myList)
                        endTime = time.perf_counter()
                        elapsedTime = endTime - startTime
                    elif(algo == "insertion"):
                        startTime = time.perf_counter()
                        insertionSort(myList)
                        endTime = time.perf_counter()
                        elapsedTime = endTime - startTime
                    elif(algo == "selection"):
                        startTime = time.perf_counter()
                        selectionSort(myList)
                        endTime = time.perf_counter()
                        elapsedTime = endTime - startTime
                    elif(algo == "merge"):
                        startTime = time.perf_counter()
                        mergeSort(myList)
                        endTime = time.perf_counter()
                        elapsedTime = endTime - startTime
                    elif(algo == "quick"):
                        startTime = time.perf_counter()
                        quickSort(myList)
                        endTime = time.perf_counter()
                        elapsedTime = endTime - startTime
                    temp += elapsedTime
                avg = temp / 5
                if(algo == "bubble"):
                    bubbleT[flag].append(avg)
                elif(algo == "insertion"):
                    insertionT[flag].append(avg)
                elif(algo == "selection"):
                    selectionT[flag].append(avg)
                elif(algo == "merge"):
                    mergeT[flag].append(avg)
                elif(algo == "quick"):
                    quickT[flag].append(avg)

    inputTypes = ["Random", "Sorted", "Reverse", "Almost sorted"]
    i = 0
    for iType in inputTypes:
        print("Input type =", iType)
        print("                    avg time   avg time   avg time")
        print("   Sort function     (n=10)    (n=100)    (n=1000)")
        print("-----------------------------------------------------")
        print("      bubbleSort    %.6f   %.6f   %.6f" %(bubbleT[i][0],bubbleT[i][1],bubbleT[i][2]))
        print("   selectionSort    %.6f   %.6f   %.6f" %(selectionT[i][0], selectionT[i][1], selectionT[i][2]))
        print("   insertionSort    %.6f   %.6f   %.6f" %(insertionT[i][0], insertionT[i][1], insertionT[i][2]))
        print("       mergeSort    %.6f   %.6f   %.6f" %(mergeT[i][0], mergeT[i][1], mergeT[i][2]))
        print("       quickSort    %.6f   %.6f   %.6f" %(quickT[i][0], quickT[i][1], quickT[i][2]))
        print("\n")
        i += 1
    
main()













