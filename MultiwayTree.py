#  File:                MultiwayTree.py
#  Description:         Creates trees and tests for isomorphism
#                       Input: "MultiwayTreeInput.txt" - must be even number of lines
#  Student's Name:      Nicolas Key
#  Student's UT EID:    
#  Course Name:         CS 313E 
#  Unique Number:       51915
#
#  Date Created:        4/27/2017
#  Date Last Modified:  4/28/2017

class Node:

    def __init__(self, data):
        self.data = data
        self.children = []

    def addChild(self, data):
        self.children.append(data)

    def __str__(self):
        return str(self.data)

class MultiwayTree:

    def __init__(self, pyTree):
        if(pyTree != []):
            self.root = Node(pyTree.pop(0))
            for i in pyTree[0]:
                self.root.addChild(MultiwayTree(i))

    def preOrder(self):
        print(self.root, end=' ')
        for i in self.root.children:
            i.preOrder()

    def isIsomorphicTo(self, other):
        if(len(self.root.children) != len(other.root.children)):
            return False
        else:
            for i in range(len(self.root.children)):
                if(not self.root.children[i].isIsomorphicTo(other.root.children[i])):
                    return False
            return True

def main():
    countFile = open("MultiwayTreeInput.txt")
    file = open("MultiwayTreeInput.txt")
    numLines = len(countFile.readlines())
    i = 1

    while(i <= numLines):
        line = file.readline()
        temp = eval(line)
        print("Tree ", i, ":  ", temp, sep="")
        tree1 = MultiwayTree(temp)
        print("Tree ", i, " preorder:   ", sep="", end="")
        tree1.preOrder()
        print("\n")
        #wait = input("")
        i += 1

        line = file.readline()
        temp = eval(line)
        print("Tree ", i, ":  ", temp, sep="")
        tree2 = MultiwayTree(temp)
        print("Tree ", i, " preorder:   ", sep="", end="")
        tree2.preOrder()
        print("\n")
        #wait = input("")

        if(tree1.isIsomorphicTo(tree2)):
            print("Tree ", i-1, " is isomorphic to Tree ", i, sep="")
        else:
            print("Tree ", i-1, " is not isomorphic to Tree ", i, sep="")
        print("\n")
        i += 1

main()
