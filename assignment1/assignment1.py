# Author: Jae Kyoung Lee (LJ)

# Opening file containing a list of words
open_file = open("magicitems.txt", "r")

# Creating the node to store data
class node:
  def __init__(self, value):
    self.value = value # Assigning object name to the value of " value "
    self.next = None # Because whatever is created is the last node'
  def printNode(self):
    print(self.value)

# Linked List
class singleLinkedList:
  # Initializing the head
  def __init__(self, value):
    self.head = node(value)
  def addValueFront(self, data):
    newNode = node(data)
    newNode.next = self.head
  def addValueEnd(self, data): 
    nodePointer = self.head
    while (nodePointer.next is not None):
      nodePointer = nodePointer.next
    newNode = node(data)
    nodePointer.next = newNode
  def printList(self):
    nodePointer = self.head
    while (nodePointer.next is not None):
      print(nodePointer.value)
      nodePointer = nodePointer.next
    print(nodePointer.value)

isFirst = True
# Assigning node class to an assignment for easy access
# # headCounter = 0
for line in open_file:
  if isFirst:
    linkList = singleLinkedList(line)
    isFirst = False
  else: 
    linkList.addValueEnd(line)
linkList.printList()

#   newNode.createNode(line)
#   # newNode.printNode()
#   while linkList.head is None:
#     linkList.head = singleLinkedList()
#     print("after while")
#     # linkList.head = None
#     print(linkList.head)
    # newNode.printNode()
    # linkList.head = nodeCreation.createNode(line)
  

  # linkList.listHead(headCounter+=1)
  # first.printNode()
  