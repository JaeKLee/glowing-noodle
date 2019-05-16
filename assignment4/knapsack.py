import re

graph_file = open("spice.txt", "r")
# Creating list of individual contents in the file
listFile = graph_file.readlines()


indexCounter = 0
while indexCounter < len(listFile):
  if re.search(r"red|green|blue|orange", listFile[indexCounter]):
    test = listFile[indexCounter].split(";")
    # print(listFile[indexCounter])
    print(test)
    spiceList = []
    if re.search(r"qty", listFile[indexCounter]):
      for x in test:
        if re.search(r"\d", x):
          spiceList.append(x)
      # print(spiceList)
  indexCounter+=1
# wt = qty
# val = price
class spice:
  def __init__(self, qty, price, index):
    self.qty = qty 
    self.price = price
    self.index = index
    self.cost = price
  def __lt__(self, other):
    return self.cost < other.cost

class knapsack:
  @staticmethod
  def getMaxValue(qty, price, capacity):
    iVal = [] 
    for i in range(len(qty)): 
      iVal.append(spice(qty[i], price[i], i)) 

    # sorting items by price 
    iVal.sort(reverse = True)

    totalPrice = 0
    for i in iVal: 
      curQty = int(i.qty) 
      curPrice = int(i.price) 
      if capacity - curQty >= 0: 
        capacity -= curQty
        totalPrice += curPrice
      else: 
        fraction = capacity / curQty
        totalPrice += curPrice * fraction 
        capacity = int(capacity - (curQty * fraction)) 
        break
    return totalPrice

if __name__ == "__main__": 
  qty = [4, 6, 8, 2] 
  price = [1.0, 2.0, 5.0, 9.0] 
  capacity = 1

  maxValue = knapsack.getMaxValue(qty, price, capacity) 
  print("The capacity is: ", capacity)
  print("Maximum price in Knapsack =", maxValue)
# for i in spiceList:
#   print(i)