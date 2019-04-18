import random
import math

# graph_file = open("C:\\Users\\Owner\\Documents\\glowing-noodle\\assignment3\\graphs.txt", "r")
open_file = open("magicitems.txt", "r")
# Creating list of individual contents in the file
magicValues = open_file.readlines()

open_file.close()

comparison = 0

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

# This is for inserting values into the BST
def insertValue(root, value):
  # global comparison
  if not root:
    return Node(value)
  elif value < root.value:
    # comparison+=1
    root.left = insertValue(root.left, value)
  else:
    # comparison+=1
    root.right = insertValue(root.right, value)
  return root

# depth is used for counting the level
def search(root, word, depth=1):
  global comparison
  if not root:
    return 0, 0
  elif root.value == word:
    return depth
  elif word < root.value:
    comparison+=1
    return search(root.left, word, depth + 1) # This makes it O(log n) with base 2
  else:
    comparison+=1
    return search(root.right, word, depth + 1)


magicList=[]
i = 0
for line in magicValues:
  while i < 42:
    magicList.append(random.choice(magicValues).upper().strip("\n"))
    i+=1
  break


root = None
for word in magicList:  
  root = insertValue(root, word)
  search(root, word)
  print("Number of comparisons: ", comparison)
  comparison = 0
# x = str(input("What are you looking for? "))

# Order of n is about 200 because it's searching for each items
# from random items