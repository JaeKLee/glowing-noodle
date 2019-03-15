# Jae Kyoung Lee (LJ)

# This will store the comparisons
comparisons = 0

def quickSort(inputList):
  global comparisons
  if len(inputList) <= 1:
    return inputList
  else:
    leftArray=[]
    rightArray=[]
    equalArray = []
    # Pivot will always start from the start
    pivot = inputList[0]
    # Traverse through the inputList
    for i in inputList:
      # Comparing each value to pivot then add to the 
      # corresponding array
      if i < pivot:
        comparisons+=1
        leftArray.append(i)
      elif i > pivot:
        comparisons+=1
        rightArray.append(i)
      # Check for equality since there might be another 
      # element that has the same value
      elif i == pivot:
        comparisons+=1
        equalArray.append(i)
    # Repeat this until the array is sorted
    sortedList = quickSort(leftArray)+equalArray+quickSort(rightArray)
    return sortedList

# Opening file containing a list of words
open_file = open("magicitems.txt", "r") # This lets you read file content
write_file = open("quickSortResult.txt", "w") # This lets you write to the file
append_file = open("quickSortResult.txt", "a") # This lets you append to the file

# Assigning value to each line
magicValues = open_file.readlines()

# List that will contain unsorted list of items
magicList = []

# This is to convert the texts into capitals
for line in magicValues:
  upperValue = line.upper()
  magicList.append(upperValue)
sortedList = quickSort(magicList)

for i in sortedList:
  write_file.writelines(i)

append_file.write("\nThe number of comparisons: ")
append_file.write(str(comparisons))

open_file.close()
