numOfWidgets = input ("Enter your number of widgets: ")
numofGizmos = input ("Enter your number of Gizmos: ")

converts1 = int(numOfWidgets) 
convert2 = int(numofGizmos)  

weightOfWidgets = converts1 * 75
weightOfGizmos = convert2 * 112


totalWeight = weightOfGizmos + weightOfWidgets

convert3 = str(totalWeight)
print ("") 
print ("The total weight of the order is " + convert3)