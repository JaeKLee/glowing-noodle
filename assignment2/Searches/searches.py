# Jae Kyoung Lee
import linkedList
import random
import math

# Opening file containing a list of words
# open_file = open("C:\\Users\\Asuna\\Documents\\Marist\\Spring 2019\\glowing-noodle\\assignment2\\Searches\\magicitems.txt", "r") # This lets you read file content
open_file = open("magicitems.txt", "r") # This lets you read file content

magicValues = open_file.readlines()
open_file.close()

magicList=[]
i = 0
for line in magicValues:
  while i < 42:
    magicList.append(random.choice(magicValues).upper().strip("\n"))
    i+=1
  break
sortedList = magicList.sort()
print(magicList)

LScomparisons = 0
BScomparisons = 0
x = str(input("What are you looking for? "))

def linearSearch(inputList):
  global LScomparisons
  noVal = False
  # Traverse through the array
  for search in inputList:
    if search == x:
      noVal = True
      LScomparisons+=1
      return noVal
    else:
      LScomparisons+=1
      noVal = False
  return noVal

def binarySearch(inputList):
  global BScomparisons
  leftArray =[]
  rightArray=[]
  if len(inputList) == 1 and x != inputList[0]:
    return "ERROR"
  else:  
    midPoint = math.ceil(len(inputList) / 2)
    if x == inputList[midPoint]:
      BScomparisons+=1
      return inputList[midPoint] 
    elif x < inputList[midPoint]:
      BScomparisons+=1
      for search in range(0, midPoint):
        leftArray.append(inputList[search])
      return binarySearch(leftArray)
    else:
      BScomparisons+=1
      for search in range(midPoint, len(inputList)):
        rightArray.append(inputList[search])
      return binarySearch(rightArray)

if linearSearch(magicList) is True:
  print("Linear Search found ", x, ". Number of comparisons: ", LScomparisons)
else:
  print("Linear Search could not find", x, ". Number of comparisons: ", LScomparisons)

if x == binarySearch(magicList):
  print("Binary Search found ", x, ". Number of comparisons: ", BScomparisons)
else:
  print("Binary Search could not find ", x, ". Number of comparisons: ", BScomparisons)

