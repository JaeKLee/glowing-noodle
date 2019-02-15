# Author: Jae Kyoung Lee (LJ)

# Opening file containing a list of words
open_file = open("magicitems.txt", "r")

# Creating the node to store data
class node:
  def __init__(self, value):
    self.value = value # Assigning object name to the value of " value "
    self.next = None # Because whatever is created is the last node
  def printNode(self):
    print(self.value)

# Linked List
class singleLinkedList:
  # Initializing the head
  def __init__(self, value):
    self.head = node(value)
  # Inserting new value at the front
  def addValueFront(self, data):
    newNode = node(data)
    newNode.next = self.head
  def addValueEnd(self, data): 
    # Start at the beginning of the list
    nodePointer = self.head
    # Find the end of the list
    while (nodePointer.next is not None):
      nodePointer = nodePointer.next
    # Create and add new node to the end of the list
    newNode = node(data)
    nodePointer.next = newNode
  # For debugging purpose
  def printList(self):
    nodePointer = self.head
    # Prints the list up to the end
    while (nodePointer.next is not None):
      print(nodePointer.value)
      nodePointer = nodePointer.next
    # Print the last value of the list
    print(nodePointer.value)

# Stack
class stack(singleLinkedList):
  def __init__(self, value):
    # Initializing stack with singleLinkedList constructor
    super().__init__(value)
  def isEmpty(self):
    noValue = False
    if self.head is None:
      noValue = True
    return noValue
  def pop(self):
    nodePointer = self.head
    prevNodePointer = None
    while nodePointer.next is not None: 
      prevNodePointer = nodePointer
      nodePointer = nodePointer.next
    print(nodePointer.value)
    prevNodePointer.next = None
  def push(self, data):
    self.addValueEnd(data)

# Queue
class queue(singleLinkedList):
  def __init__(self, value):
    super().__init__(value)
    self.queueHead = self.head

  def isEmpty(self):
    noValue = False
    if self.head is None:
      noValue = True
    return noValue
    
  def enqueue(self, data):
    queueCounter = 0
    while queueCounter < 100:
      newEmtpyNode = node(None)
      newEmtpyNode.next = self.head
      queueCounter+=1
    queueLength = queueCounter

    nodePointer = self.head
    lengthCounter = 0
    # Traversing to the end
    while (lengthCounter < queueLength) and (nodePointer.next is not None):
      nodePointer = nodePointer.next
      lengthCounter+=1
      print("test" , lengthCounter)
    # This will point after the end to the head
    nodePointer = self.queueHead
    print(nodePointer)
    # Once it reaches the end, add a value
  
    self.addValueEnd(data)
    
    # nodePointer = beginningPointer
  def dequeue(self, data):
    nodePointer = self.head
    if nodePointer.next is not None:
      nodePointer = nodePointer.next

# for line in open_file:



# isFirst = True
# for line in open_file:
#   if not isFirst: # Adds values after the first one
#     queueList.enqueue(line)
#   else: # Add the very first value
#     queueList = queue(line) 
#     isFirst = False
# queueList.enqueue("test")
# queueList.printList()


# Insert contents in magicitems.txt into linked list
# isFirst = True
# for line in open_file:
#   if isFirst is False: # Adds values after the first one
#     linkList.addValueEnd(line)
#   else: # Add the very first value
#     linkList = singleLinkedList(line) 
#     isFirst = False
# linkList.printList()

isFirst = True
for line in open_file:
  if not isFirst: # Adds values after the first one
    stackList.push(line)
  else: # Add the very first value
    stackList = stack(line) 
    isFirst = False
# stackList.printList()
# stackList.pop()
# stackList.push("Axe")
# stackList.printList()