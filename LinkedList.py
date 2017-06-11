#  File:                LinkedLists.py
#  Description:         Definition of member funtions for LinkedList(). Perform multiple 
#                       operations to ordered an unordered linked lists.
#  Student's Name:      Nicolas Key
#  Student's UT EID:    nak724
#  Course Name:         CS 313E 
#  Unique Number:       51915
#
#  Date Created:        3/21/2017
#  Date Last Modified:  3/24/2017

# This class definition was taken from Dr. Bulko's website.
# File: NodesAndLists.py
class Node (object):
    def __init__(self,initdata):
        self.data = initdata
        self.next = None            # always do this – saves a lot
                                    # of headaches later!
    def __str__(self):
        return str(self.data)
        
    def getData (self):
        return self.data            # returns a POINTER

    def getNext (self):
        return self.next            # returns a POINTER

    def setData (self, newData):
        self.data = newData         # changes a POINTER

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
            self.head = Node(item)
            return
        
        previous = self.head
        current = self.head.getNext()
        stop = False

        while current != None:
            previous = current
            current = current.getNext()

        myNode = Node(item)
        previous.setNext(myNode)


    def addInOrder (self, item):
        if(self.head == None):
            self.head = Node(item)
            return

        if(strBigger(self.head.data, item)):
            myNode = Node(item)
            myNode.setNext(self.head)
            self.head = myNode
            return

        stop = False
        previous = self.head
        current = self.head.getNext()
        while not stop:
            if(current == None):
                previous.setNext(Node(item))
                return
            elif(strBigger(item, current.data)):
                previous = current
                current = current.getNext()
            else:
                myNode = Node(item)
                previous.setNext(myNode)
                myNode.setNext(current)
                return
            

    def getLength (self):
        count = 0
        current = self.head
        while(current != None):
            count = count + 1
            current = current.getNext()
        return count

     
    def findUnordered (self, item):
        current = self.head
        while (current != None):
            if(item == current.data):
                return True
            current = current.getNext()
        return False


    def findOrdered (self, item):
        current = self.head
        while (current != None):
            if(current.data == item):
                return True
            if(strBigger(current.data, item)):
                return False
            current = current.getNext()
        return False
            

    def delete (self, item):
        if(item == self.head.data):
            self.head = self.head.getNext()
            return True

        previous = self.head
        current = self.head.getNext()

        while(current != None):
            if(current.data == item):
                previous.setNext(current.getNext())
                return True
            previous = current
            current = current.getNext()
        return False


    def copyList (self):
        myLL = LinkedList()
        if(self.head == None):
            return myLL

        currentSelf = self.head
        myLL.head = Node(self.head.data)
        currentSelf = currentSelf.getNext()
        currentLL = myLL.head

        while(currentSelf != None):
            currentLL.setNext(Node(currentSelf.data))
            currentLL = currentLL.getNext()
            currentSelf = currentSelf.getNext()
        return myLL
            

    def reverseList (self):
        myLL = LinkedList()
        myLL.head = Node(self.head.data)
        current = self.head.getNext()

        while(current != None):
            myLL.addFirst(current.data)
            current = current.getNext()
        return myLL


    def orderList (self):
        myLL = LinkedList()
        myLL.head = Node(self.head.data)
        current = self.head.getNext()

        while(current != None):
            myLL.addInOrder(current.data)
            current = current.getNext()
        return myLL
            

    def isOrdered (self):
        previous = self.head
        current = self.head.getNext()

        while(current != None):
            if(strBigger(previous.data, current.data)):
                return False
            previous = current
            current = current.getNext()
        return True
            

    def isEmpty (self):
        if(self.getLength() == 0):
            return True
        return False


    def mergeList (self, b):
        myLL = self.copyList()
        current = b.head
        
        while(current != None):
            myLL.addInOrder(current.data)
            current = current.getNext()
        return myLL
    

    def isEqual (self, b):
        currentA = self.head
        currentB = b.head

        if(currentA == None and currentB == None):
            return True
        if(currentA == None or currentB == None):
            return False

        while(currentA.data == currentB.data):
            currentA = currentA.getNext()
            currentB = currentB.getNext()
            if(currentA == None and currentB == None):
                return True
            if(currentA == None or currentB == None):
                return False
        return False
    

    def removeDuplicates (self):
        myLL = LinkedList()
        current = self.head

        while(current != None):
            if(not myLL.findUnordered(current.data)):
                myLL.addLast(current.data)
            current = current.getNext()
        return myLL
        

def strBigger(str1, str2):     # return true if str1 > str2
    count = 0
    for i in str1:
        try:
            if(i < str2[count]):
                return False
            elif(i > str2[count]):
                return True
        except IndexError:
            return True     #str1 starts with all letters in str2 and is longer
        count = count + 1
    return False            #str2 starts with all letters in str1 and is longer



# Copy and paste the following after your class definitions for
# Nodes and LinkedLists.  Do NOT change any of the code in main()!

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)
    
main()
