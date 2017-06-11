#  File:                Friends.py
#  Description:         
#                       
#  Student's Name:      Nicolas Key
#  Student's UT EID:    nak724
#  Course Name:         CS 313E 
#  Unique Number:       51915
#
#  Date Created:        3/24/2017
#  Date Last Modified:  4/6/2017

# This class definition was modified from Dr. Bulko's website.
# File: NodesAndLists.py
class User (object):
    def __init__(self,name):
        self.name = name
        self.next = None            # always do this – saves a lot
                                    # of headaches later!
        self.friends = LinkedList()
        
    def __str__(self):
        return str(self.name)
        
    def getName (self):
        return self.name            # returns a POINTER

    def getNext (self):
        return self.next            # returns a POINTER

    def setName (self, newName):
        self.data = newName         # changes a POINTER

    def setNext (self,newNext):
        self.next = newNext         # changes a POINTER

        
class LinkedList():
    def __init__(self):
        self.head = None

    def __str__ (self):
        current = self.head
        count = 0
        myStr = ""

        while(current != None):
            count = count + 1
            myStr = myStr + str(current) + "  "
            current = current.getNext()
            if(count % 10 == 0):
                myStr = myStr + "\n"

        return myStr

    def addFirst (self, item):
        myNode = Node(item)
        myNode.setNext(self.head)
        self.head = myNode
        

    def addLast (self, item):
        if(self.head == None):
            self.head = User(item)
            return
        
        previous = self.head
        current = self.head.getNext()
        stop = False

        while current != None:
            previous = current
            current = current.getNext()

        myNode = User(item)
        previous.setNext(myNode)

    def findUnordered (self, item):
        current = self.head
        while (current != None):
            if(item == current.name):
                return True
            current = current.getNext()
        return False

    def delete (self, item):
        if(self.head == None):
            return False
        if(item == self.head.name):
            self.head = self.head.getNext()
            return True

        previous = self.head
        current = self.head.getNext()

        while(current != None):
            if(current.name == item):
                previous.setNext(current.getNext())
                return True
            previous = current
            current = current.getNext()
        return False




def main():
    file = open("Friends.txt")
    stop = False
    AccountsList = LinkedList()
    
    while(not stop):
        line = file.readline()
        splitLine = line.split()
        #print(splitLine)

        if(splitLine[0] == "Person"):
            if(AccountsList.findUnordered(splitLine[1])):
                print(splitLine[1], "already has an account.")
            else:
                AccountsList.addLast(splitLine[1])
                print(splitLine[1], "now has an account.")


                
        elif(splitLine[0] == "Friend"):
            if(not AccountsList.findUnordered(splitLine[1]) or not AccountsList.findUnordered(splitLine[2])):
                #print("One or both of these users does not have an account yet.")
                if(not AccountsList.findUnordered(splitLine[1])):
                    print(splitLine[1] + " does not have an account")
                if(not AccountsList.findUnordered(splitLine[2])):
                    print(splitLine[2] + " does not have an account")
            elif(splitLine[1] == splitLine[2]):
                print("You can't friend yourself.")
            else:
                current = AccountsList.head
                found = False
                while(current != None and not found):
                    if(current.getName() == splitLine[1]):
                        if(current.friends.findUnordered(splitLine[2])):
                            print(splitLine[1] + " and " + splitLine[2] + " are already friends.")
                        else:
                            current.friends.addLast(splitLine[2])
                        found = True
                    current = current.getNext()

                current = AccountsList.head
                found = False
                while(current != None and not found):
                    if(current.getName() == splitLine[2]):
                        if(not current.friends.findUnordered(splitLine[1])):
                            current.friends.addLast(splitLine[1])
                            print(splitLine[1] + " and " + splitLine[2] + " are now friends.")
                        found = True
                    current = current.getNext()
                
                
        elif(splitLine[0] == "Unfriend"):
            if(not AccountsList.findUnordered(splitLine[1]) or not AccountsList.findUnordered(splitLine[2])):
                #print("One or both of these users does not have an account yet.")
                if(not AccountsList.findUnordered(splitLine[1])):
                    print(splitLine[1] + " does not have an account")
                if(not AccountsList.findUnordered(splitLine[2])):
                    print(splitLine[2] + " does not ahve an account")
            elif(splitLine[1] == splitLine[2]):
                print("You can't unfriend yourself.")
            else:
                current = AccountsList.head
                found = False
                while(current != None and not found):
                    if(current.getName() == splitLine[1]):
                        if(current.friends.delete(splitLine[2])):
                            print(splitLine[1] + " and " + splitLine[2] + " are no longer friends.")
                        else:
                            print(splitLine[1] + " and " + splitLine[2] + " weren't friends to begin with.")
                        found = True
                    current = current.getNext()

                current = AccountsList.head
                found = False
                while(current != None and not found):
                    if(current.getName() == splitLine[2]):
                        current.friends.delete(splitLine[1])
                        found = True
                    current = current.getNext()
                    
        elif(splitLine[0] == "List"):
            if(AccountsList.findUnordered(splitLine[1])):
                current = AccountsList.head
                found = False
                while(current != None and not found):
                    if(current.getName() == splitLine[1]):
                        currentFriend = current.friends.head
                        if(currentFriend == None):
                            print(splitLine[1] + " doesn't have any friends. How sad.")
                        else:
                            print(splitLine[1] + "'s friends:")
                            while(currentFriend != None):
                                print(currentFriend.getName())
                                currentFriend = currentFriend.getNext()
                        found = True
                    current = current.getNext()
            else:
                print(splitLine[1] + " does not have an account.")

                
        elif(splitLine[0] == "Query"):
            if(splitLine[1] == splitLine[2]):
                print("A person cannot query themselves")
            elif(AccountsList.findUnordered(splitLine[1]) and AccountsList.findUnordered(splitLine[2])):
                current = AccountsList.head
                found = False
                areFriends = False
                while(current != None and not found):
                    if(current.getName() == splitLine[1]):
                        found = True
                        currentFriend = current.friends.head
                        while(currentFriend != None and not areFriends):
                            if(currentFriend.getName() == splitLine[2]):
                                areFriends = True
                            currentFriend = currentFriend.getNext()
                    current = current.getNext()
                if(areFriends):
                    print(splitLine[1], "and", splitLine[2], "are friends.")
                else:
                    print(splitLine[1], "and", splitLine[2], "are not friends.")
            else:
                if(not AccountsList.findUnordered(splitLine[1])):
                    print(splitLine[1], "doesn't have an account")
                if(not AccountsList.findUnordered(splitLine[2])):
                    print(splitLine[2], "doesn't have an account")

                    
        elif(splitLine[0] == "Exit"):
            print("Exiting...")
            stop = True

        #print("\nPrinting account...\n" + str(AccountsList) + "\n")
        print("")



main()
             
