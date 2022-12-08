'''
Problem statement - https://adventofcode.com/2022/day/1
'''

#Function that takes a filename that contains list of numbers and what is the top "n" sum to find
#Returns the sum of top "n" elements
def find_max_calories(filename, topnum):
  calorieCounter = 0 #counter to keep track of calories carried by an elf
  maxCaloriesList = [0] #List to hold the calories by each elf

  for line in f:
    if len(line.strip()) == 0 :
      #Encountered an empty line - add calories of elf to the list
      maxCaloriesList.append(calorieCounter)

      calorieCounter = 0
    else:
      #Non empty line, add to the counter and continue
      calorieCounter += int(line)

  #List containing all calories - sort it, reverse it
  maxCaloriesList.sort()
  maxCaloriesList.reverse()

  #Find the top n based on parameter
  topCalories = 0

  for i in range(topnum):
    topCalories += maxCaloriesList[i]

  return topCalories

f = open("input.txt", "r")

#Find top element
print(find_max_calories(f, 1))

f.seek(0)

#Find top 3 elements
print(find_max_calories(f, 3))
