import linkedList
import random
import math
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
  def __init__(self,   value):
    self.head = node(  value)
  # Inserting new value at the front
  def addValueFront(self,   data):
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

# Opening file containing a list of words
# open_file = open("C:\\Users\\Asuna\\Documents\\Marist\\Spring 2019\\glowing-noodle\\assignment2\\Searches\\magicitems.txt", "r") # This lets you read file content
open_file = open("magicitems.txt", "r") # This lets you read file content

magicValues = open_file.readlines()
open_file.close()

randomList = []
magicList=[]
i = 0
for line in magicValues:
  while i < 42:
    magicList.append(random.choice(magicValues).upper().strip("\n"))
    i+=1
  break
for j in magicValues:
  randomList.append(j.upper().strip("\n"))
sortedList = magicList.sort()

keyList = []
def hashKey(inputItem):
  for p in inputItem:
    keyList.append([len(p), p])
  return keyList # Returns list of lengths of strings in integer form

hashTable = [None] * 250
for u in magicList:
  sList = singleLinkedList(None)
  if hashTable[len(u)] is None:
    hashTable[len(u)] = sList.addValueFront(u)
  else:
    hashTable[len(u)] = sList.addValueFront(u)
print(hashTable[22])

# print(randomList)
# print(hashKey(randomList))