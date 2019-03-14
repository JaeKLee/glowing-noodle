# Jae Kyoung Lee

import random

# Opening file containing a list of words
# open_file = open("C:\\Users\\Asuna\\Documents\\Marist\\Spring 2019\\glowing-noodle\\assignment2\\Searches\\magicitems.txt", "r") # This lets you read file content
open_file = open("magicitems.txt", "r") # This lets you read file content

magicValues = open_file.readlines()
open_file.close()

randomList=[]
i = 0
for line in magicValues:
  while i < 42:
    randomList.append(random.choice(magicValues).strip("\n"))
    i+=1
  break
randomList.sort()
print(randomList)

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

if linearSearch(randomList) is True:
  print(x, "found. Number of comparisons: ", comparisons)
else:
  print(x, "not found. Number of comparisons: ", comparisons)

