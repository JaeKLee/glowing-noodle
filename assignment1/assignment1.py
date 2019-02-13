# Author: Jae Kyoung Lee (LJ)

# Opening file containing a list of words
open_file = open("magicitems.txt", "r")

# magicList = open_file.readline()
# for x in open_file:
#   print(x)

# Creating the node to store data
class node:
  def createNode(self, value):
    self.value = value # Assigning object name to the value of " value "
    self.next = None # Because whatever is created is the last node'
  def printNode(self):
    print(self.value)

# Linked List
class linkedList:
  # Initializing the head
  def listHead(self):
    self.head = None

# Assigning node class to an assignment for easy access
nodeCreation = node()
linkList = linkedList()
# headCounter = 0
for line in open_file:
  nodeCreation.printNode()
  linkList.head = nodeCreation.createNode(line)
  

  # linkList.listHead(headCounter+=1)
  # first.printNode()