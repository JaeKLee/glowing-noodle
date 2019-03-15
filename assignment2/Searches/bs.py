# Jae Kyoung Lee(LJ)
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
    # Converting to upper case for comparison later
    magicList.append(random.choice(magicValues).upper().strip("\n"))
    i+=1
  break
sortedList = magicList.sort()
print(magicList)

comparisons = 0
x = str(input("What are you looking for? "))

def binarySearch(inputList):
  global comparisons
  leftArray =[]
  rightArray=[]
  midPoint = math.ceil(len(inputList) / 2)
  if x == inputList[midPoint]:
    comparisons+=1
    return inputList[midPoint] 
  else:
    if x < inputList[midPoint]:
      comparisons+=1
      for search in range(0, midPoint):
        leftArray.append(inputList[search])
      return binarySearch(leftArray)
    else:
      comparisons+=1
      for search in range(midPoint, len(inputList)):
        rightArray.append(inputList[search])
      return binarySearch(rightArray)
  
if x == binarySearch(magicList):
  print(x, "found. Number of comparisons: ", comparisons)
else:
  print(x, "not found. Number of comparisons: ", comparisons)

