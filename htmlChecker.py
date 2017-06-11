#  File:                htmlChecker.py
#  Description:         an "HTML Checker" program that takes as input an HTML file, and produces
#                       a report indicating whether or not the tags are correctly matched.                       
#  Student's Name:      Nicolas Key
#  Student's UT EID:    nak724
#  Course Name:         CS 313E 
#  Unique Number:       51915
#
#  Date Created:        2/26/2017
#  Date Last Modified:  3/02/2017

class Stack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return (self.items == [])

    def size(self):
        return(len(self.items))
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return(self.items.pop())

    def peek(self):
        return(self.items[-1])

    def __str__ (self):
        return str(self.items)

class Tags:

    def __init__(self, excepts):
        self.VALIDTAGS = []
        self.tagstack = Stack()
        self.EXCEPTIONS = excepts
        


    def getTag(self, tag):
        tagStr = ""
        for i in tag:
            if i == None:
                continue
            if i != ">":
                tagStr += i
            else:
                return tagStr


def main():
    file = open("htmlfile.txt")
    strFile = file.read()
    strList = strFile.split("<")

    EXCEPTIONS = ["br", "meta", "hr"]
    myTags = Tags(EXCEPTIONS)
    
    tagList = []
    for i in strList:
        tagStr = myTags.getTag(i)
        if(tagStr != None):
            tagList.append(tagStr)
            
    print(tagList)

    keepGoing = True
    while(tagList != [] and keepGoing):
        if(tagList[0][0] == "/"):       # ending tag
            if(myTags.tagstack.isEmpty()):
                print("Processing complete. Ending tag found but the stack is empty.")
                keepGoing = False
            elif(tagList[0][1:] == myTags.tagstack.peek()):
                myTags.tagstack.pop()
                print("Tag " + tagList[0] + " matches top of stack:  stack is now " + str(myTags.tagstack))
                del tagList[0]
            else:       # doesn't match
                print("Error:  tag is " + tagList[0] + " but top of stack is " + str(myTags.tagstack.peek()))
                keepGoing = False
        else:                           # opening tag
            if(tagList[0] in myTags.EXCEPTIONS or tagList[0][:4] in myTags.EXCEPTIONS):
               print("Tag " + tagList[0] + " does not need to match:  stack is still " + str(myTags.tagstack))
               del tagList[0]
            else:
                try:                    # Check if tag is already in VALIDTAGS
                    i = myTags.VALIDTAGS.index(tagList[0])
                except:
                    myTags.VALIDTAGS.append(tagList[0])
                    print("New tag " + myTags.VALIDTAGS[-1] + " found and added to list of valid tags")
                    
                myTags.tagstack.push(tagList[0])
                print("Tag " + myTags.tagstack.peek() + " pushed:  stack is now " + str(myTags.tagstack))
                del tagList[0]

    if(tagList == []):
        if(myTags.tagstack.isEmpty()):
            print("Processing complete.  No mismatches found.")
        else:
            print("Processing complete.  Unmatched tags remain on stack: " + str(myTags.tagstack))

    myTags.VALIDTAGS.sort()
    myTags.EXCEPTIONS.sort()

    print("\n\nValid tags: " + str(myTags.VALIDTAGS))
    print("Exceptions: " + str(myTags.EXCEPTIONS))

main()
