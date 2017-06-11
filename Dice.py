# File:                 Dice.py
# Description:          This program prompts the user for how many dice rolls should occur.
#                       It then records the outcome of each roll and prints a list and a histogram of the results.
# Student's Name:       Nicolas Key
# Sudent's EID:         nak724
# Course Name:          CS 313E
# Unique Number:        51915
#
# Date Created:         1/27/17
# Date Last Modified:   2/1/17


import random


class diceRolls():

    def __init__(self, numRuns):
        self.arr = [0,0,0,0,0,0,0,0,0,0,0]
        self.numRuns = int(numRuns)
        self.rollDice()

    def __str__(self):
        if(self.numRuns >= 100):
            for i in range(len(self.arr)):
                self.arr[i] = int(round(self.arr[i] * (100/self.numRuns),0))

        max = self.arr[0]
        for i in range(len(self.arr)):
            if(max < self.arr[i]):
                max = self.arr[i]
                
        strHistogram = ""
        while(max > 0):
            strHistogram = strHistogram + "|  "
            for i in range(len(self.arr)):
                if(self.arr[i] == max):
                    strHistogram = strHistogram + "*  "
                    self.arr[i] -= 1
                else:
                    strHistogram = strHistogram + "   "
            strHistogram = strHistogram + "\n"
            max -=1

        strHistogram = strHistogram + "+--+--+--+--+--+--+--+--+--+--+--+-\n   2  3  4  5  6  7  8  9 10 11 12"   
        return strHistogram


    def rollDice(self):
        for i in range(self.numRuns):
            sum = random.randint(1, 6) + random.randint(1,6)
            self.arr[sum-2] +=1


def main():
    random.seed(1314)
    numRuns = input("How many times do you want to roll the dice? ")
    myRolls = diceRolls(numRuns)
    print("Results: ", myRolls.arr)
    print(myRolls)
        
main()

