# Jae Kyoung Lee (LJ)

# For math.ceil function
import math

# This will store the comparisons
comparisons = 0

def merge(leftArr, rightArr):
  global comparisons
  # Empty array to store the sorted list of both inputs
  sortedList = []
  while len(leftArr) > 0 and len(rightArr) > 0:
    # Comparing to see the first element in both arrays
    if leftArr[0] < rightArr[0]:
      # Increment comparisons because we just compared
      comparisons+=1
      # Storing the first element because we just compared 
      # and found out that the element is less than the value in 
      # right array
      sortedList.append(leftArr[0])
      # Since we sorted the first element, we no longer have 
      # to check for that element again, so get rid of it
      leftArr.remove(leftArr[0])
    else:
      comparisons+=1
      sortedList.append(rightArr[0])
      rightArr.remove(rightArr[0])
  # If the initial array was an odd array, one of the array has one 
  # more element than the other
  if len(leftArr) == 0:
    sortedList += rightArr
  else:
    sortedList += leftArr
  return sortedList


def mergeSort(inputList):
  if len(inputList) <= 1:
    return inputList
  else:
    # Finding the mid point of the inputList
    midPoint = math.ceil(len(inputList) / 2)

    # This iterates from index 0 to midPoint because it's the first half
    leftArray = mergeSort(inputList[0:midPoint])
    # This iterates from midpoint to the end of inputList since it's
    # the second half
    rightArray = mergeSort(inputList[midPoint:len(inputList)])
    return merge(leftArray, rightArray)


# Opening file containing a list of words
open_file = open("magicitems.txt", "r") # This lets you read file content
write_file = open("mergeSortResult.txt", "w") # This lets you write to the file
append_file = open("mergeSortResult.txt", "a") # This lets you append to the file

# Assigning value to each line
magicValues = open_file.readlines()

# List that will contain unsorted list of items
magicList = []

# This is to convert the texts into capitals
for line in magicValues:
  upperValue = line.upper()
  magicList.append(upperValue)
sortedList = mergeSort(magicList)

for i in sortedList:
  write_file.writelines(i)

append_file.write("\nThe number of comparisons: ")
append_file.write(str(comparisons))

open_file.close()
