import re
x = str(input("Enter the test file: "))

graph_file = open(x, "r")
# Creating list of individual contents in the file
listFile = graph_file.readlines()

indexCounter = 0    
priceList = []
qtyList = []
spiceList = []    
capList = []  

while indexCounter < len(listFile):
  test = listFile[indexCounter].split(";")
  for x in test:
    newX = x.split()
    for i in newX:
      if re.search(r"red|green|blue|orange", i):
        spiceList.append(i)
      if re.search(r"price", listFile[indexCounter]):
        if re.search(r"\d+(\.\d+)", i):
          priceList.append(i)
      if re.search(r"qty", listFile[indexCounter]):
        if re.search(r"\b(?<!\.)\d+(?!\.)\b", i): # Regex credit to Wiktor Stribizew
          qtyList.append(i)
      if re.search(r"capacity", listFile[indexCounter]):
        if re.search(r"\b(?<!\.)\d+(?!\.)\b", i):
          capList.append(i)
  indexCounter+=1
# print(spiceList)
# print(priceList)
# print(qtyList)
# print(capList)
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
    knapsackBag = [] 
    for i in range(len(qty)): 
      knapsackBag.append(spice(qty[i], price[i], i)) 

    # sorting items by price 
    knapsackBag.sort(reverse = True)

    totalPrice = 0
    for i in knapsackBag: 
      curQty = int(i.qty) 
      curPrice = float(i.price)
      capacity = int(capacity) 
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
  qty = qtyList#[4, 6, 8, 2] 
  price = priceList#[1.0, 2.0, 5.0, 9.0] 
  capacity = capList
  for i in capList:
    maxValue = knapsack.getMaxValue(qty, price, i) 
    print("The capacity is: ", i)
    print("Maximum price in Knapsack =", maxValue)

