#  File:                ERsim.py
#  Description:         This program simulates the environment of a busy
#                       Emergency Room (ER) for a hospital.                      
#  Student's Name:      Nicolas Key
#  Student's UT EID:    
#  Course Name:         CS 313E 
#  Unique Number:       51915
#
#  Date Created:        3/3/17
#  Date Last Modified:  3/10/17


# This class definition was taken from "HotPotato.py" on Dr. Bulko's webpage
class Queue (object):
    def __init__(self):
        self.items = [ ]

    def __str__(self):
        return str(self.items)

    def isEmpty (self):
        return self.items == [ ]

    def enqueue (self, item):
        self.items.insert(0,item)

    def dequeue (self):
        return self.items.pop ()

    def size (self):
        return len(self.items)

    def peek (self):
        return self.items [len(self.items)-1]

criticalQ = Queue()
seriousQ = Queue()
fairQ = Queue()

# Print out all queue's to the screen followed by a new line
def showQs():
    print("   Queues are:")
    print("   Critical: " + str(criticalQ))
    print("   Serious:  " + str(seriousQ))
    print("   Fair:     " + str(fairQ))
    print("")

# Add patient @name to specified queue @condition
# Print out updated queues
def addPatient(name, condition):
    if(condition == "Critical"):
        criticalQ.enqueue(name)
        print(">>> Add patient " + name + " to Critical queue")
    elif(condition == "Serious"):
        seriousQ.enqueue(name)
        print(">>> Add patient " + name + " to Serious queue")
    elif(condition == "Fair"):
        fairQ.enqueue(name)
        print(">>> Add patient " + name + " to Fair queue")
    else:
        print("Error: There's an invalid contion for one of the patients.")
        return
    showQs()

# Treat the next patient in according to urgency
# Print updated queues
# If no patients to be treated, print "No patients in queues" and return
def treatNext():
    if(not criticalQ.isEmpty()):
        print("   Treating " +  criticalQ.dequeue() + " from Critical queue")
        showQs()
    elif(not seriousQ.isEmpty()):
        print("   Treating " +  seriousQ.dequeue() + " from Serious queue")
        showQs()
    elif(not fairQ.isEmpty()):
        print("   Treating " +  fairQ.dequeue() + " from Fair queue")
        showQs()
    else:
        print("   No patients in queues")

# Treat the next patient in specified queue @q
# Print updated queues
def treatQ(q):          
    if(q == "Critical"):
        print(">>> Treat next patient on Critical queue")
        if(not criticalQ.isEmpty()):
            print("   Treating " +  criticalQ.dequeue() + " from Critical queue")
        else:
            print("   No patients in queue")
    elif(q == "Serious"):
        print(">>> Treat next patient on Serious queue")
        if(not seriousQ.isEmpty()):
            print("   Treating " +  seriousQ.dequeue() + " from Serious queue")
        else:
            print("   No patients in queue")
    elif(q == "Fair"):
        print(">>> Treat next patient on Fair queue")
        if(not fairQ.isEmpty()):
            print("   Treating " +  fairQ.dequeue() + " from Fair queue")
        else:
            print("   No patients in queue")
    showQs()
         
# Find out who needs to be treated @who and call appropriate function        
def treatPatient(who):
    if(who == "all"):
        print(">>> Treat all patients")
        while(not criticalQ.isEmpty() or not seriousQ.isEmpty() or not fairQ.isEmpty()):
            treatNext()
        treatNext()     #Call one more time to get "No patients in queues"
    elif(who == "next"):
        print(">>> Treat next patient")
        treatNext()
    elif(who == "Critical" or who == "Serious" or who == "Fair"):
        treatQ(who)
    else:
        print("Error: Not a valid treat operation")
        

def main():
    myFile = open("ERsim.txt")

    keepGoing = True
    while(keepGoing):
        fileLine = myFile.readline()
        strList = fileLine.split()
        if(strList[0] == "add"):
            addPatient(strList[1], strList[2])
        elif(strList[0] == "treat"):
            treatPatient(strList[1])
        elif(strList[0] == "exit"):
            print("Exit")
            keepGoing = False
        else:
            print("Error: Invalid instruction in input file.")
            keepGoing = False

main()
