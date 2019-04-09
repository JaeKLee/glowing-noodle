import re
# For dynamic test inputs
# x = str(input("Enter the test file: "))

# Opening as read mode to read the test files
graph_file = open("C:\\Users\\Owner\\Documents\\glowing-noodle\\assignment3\\graphs.txt", "r")
# Creating list of individual contents in the file
listFile = graph_file.readlines()
# Close file
# graph_file.close()

# print(listFile)
indexCounter = 0
vertexCounter = 0
# for x in listFile:
#     # if re.search(r"--", x):
#         # print(x)
#     if re.search(r"new graph", x):
#         # print(x)
#         vertexList = []
#     if re.search(r"add vertex", x):
#         # test = list(x, " ")
#         test = x.split()
#         # print(test)
#         # while re.search(r"--", x):
#         if re.search(r"\d", test[indexCounter]):
#             print(test)

while indexCounter < len(listFile):
    if re.search(r"new graph", listFile[indexCounter]):
        print("New Graph")
        vertexList = []
    elif re.search(r"add vertex", listFile[indexCounter]):
        test = listFile[indexCounter].split()
        # print(test)
        # if re.search(r"\d", test[vertexCounter]):
        for x in test:
            if re.search(r"\d", x):
                # print(x)
                vertexList.append(x)
                print(vertexList)
        # vertexCounter+=1
    indexCounter+=1
