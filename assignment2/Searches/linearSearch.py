# Jae Kyoung Lee

import random

# Opening file containing a list of words
# open_file = open("C:\\Users\\Asuna\\Documents\\Marist\\Spring 2019\\glowing-noodle\\assignment2\\Searches\\magicitems.txt", "r") # This lets you read file content
open_file = open("magicitems.txt", "r") # This lets you read file content

magicValues = open_file.readlines()
open_file.close()

magicList=[]
i = 0
for line in magicValues:
  while i < 42:
    magicList.append(random.choice(magicValues).strip("\n"))
    i+=1
  break
sortedList = magicList.sort()
print(magicList)

comparisons = 0
x = str(input("What are you looking for? "))

def linearSearch(inputList):
  global comparisons
  noVal = False
  for search in inputList:
    if search == x:
      noVal = True
      comparisons+=1
      return noVal
    else:
      comparisons+=1
      noVal = False
  return noVal

if linearSearch(magicList) is True:
  print(x, "found. Number of comparisons: ", comparisons)
else:
  print(x, "not found. Number of comparisons: ", comparisons)

