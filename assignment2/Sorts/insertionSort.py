# Jae Kyoung Lee (LJ)

# This will store the comparisons
comparisons = 0

def insertionSort(inputList):
  global comparisons
  for i in range(1, len(inputList)):
    j = i-1
    while j >= 0 and inputList[j] > inputList[j+1]:
      # Increment how many times we've compared so far
      comparisons+=1
      # Temporary variable that stores the current value
      tempVal = inputList[j]
      # Current value becomes the next value
      # or next value becomes the current value
      inputList[j] = inputList[j+1]    
      # Next element overwrites the temporary value
      inputList[j+1] = tempVal
      j-=1
    # end of while loop
  # end of while loop
  return inputList

# Opening file containing a list of words
open_file = open("magicitems.txt", "r") # This lets you read file content
write_file = open("insertionSortResult.txt", "w") # This lets you write to the file
append_file = open("insertionSortResult.txt", "a") # This lets you append to the file

# Assigning value to each line
magicValues = open_file.readlines()

# List that will contain unsorted list of items
magicList = []

# This is to convert the texts into capitals
for line in magicValues:
  upperValue = line.upper()
  magicList.append(upperValue)
sortedList = insertionSort(magicList)

for i in sortedList:
  write_file.writelines(i)

append_file.write("\nThe number of comparisons: ")
append_file.write(str(comparisons))

open_file.close()
