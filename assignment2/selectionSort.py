# Jae Kyoung Lee (LJ)

# This will store the comparisons
comparisons = 0

def selectionSort(inputList):
  global comparisons
  for i in range(0, len(inputList)):
    # Settting minimum value in the list as temp
    minVal = i
    for j in range(i+1, len(inputList)):
      # Checks whether the value in minVal is bigger than 
      # the list of array besides minVal
      if inputList[minVal] > inputList[j]:
        # Increment how many times we've compared so far
        comparisons+=1
        # If it's true, then change minVal to current value
        minVal = j
      # End of if statement
    # Do the swapping
    temp = inputList[i]
    inputList[i] = inputList[minVal]
    inputList[minVal] = temp
    # end of for loop
  # end of for loop
  return inputList

# Opening file containing a list of words
open_file = open("magicitems.txt", "r") # This lets you read file content
write_file = open("selectionSortResult.txt", "w") # This lets you write to the file
append_file = open("selectionSortResult.txt", "a") # This lets you append to the file

# Assigning value to each line
magicValues = open_file.readlines()

# List that will contain unsorted list of items
magicList = []

# This is to convert the texts into capitals
for line in range(len(magicValues)):
  upperValue = magicValues[line].upper()
  magicList.append(upperValue)
sortedList = selectionSort(magicList)

for i in sortedList:
  write_file.writelines(i)

append_file.write("\nThe number of comparisons: ")
append_file.write(str(comparisons))

open_file.close()
