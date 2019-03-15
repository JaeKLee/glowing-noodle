# Creating the node to store data
class node:
  def __init__(self,   value):
    # self.key = key
    self.value = value # Assigning object name to the value of " value "
    self.next = None # Because whatever is created is the last node
  def printNode(self):
    print(self.value)

# Linked List
class singleLinkedList:
  # Initializing the head
  def __init__(self, value):
    self.head = node(  value)
  # Inserting new value at the front
  def addValueFront(self, data):
    newNode = node(  data)
    newNode.next = self.head
  def addValueEnd(self,   data): 
    # Start at the beginning of the list
    nodePointer = self.head
    # Find the end of the list
    while (nodePointer.next is not None):
      nodePointer = nodePointer.next
    # Create and add new node to the end of the list
    newNode = node(  data)
    nodePointer.next = newNode
  # For debugging purpose
  def printList(self):
    nodePointer = self.head
    # Prints the list up to the end
    while (nodePointer.next is not None):
      print(nodePointer.value, "\n")
      nodePointer = nodePointer.next
    # Print the last value of the list
    print(nodePointer.value)