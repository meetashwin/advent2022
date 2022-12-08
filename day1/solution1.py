'''
For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
In case the Elves get hungry and need extra snacks, they need to know which Elf to ask: they'd like to know how many Calories are being carried by the Elf carrying the most Calories. In the example above, this is 24000 (carried by the fourth Elf).

Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
'''
f = open("input.txt", "r")

maxCalories = 0 #holder for max calories carried by an elf
calorieCounter = 0 #counter to keep track of calories carried by an elf
currIndex = 0 #counter to keep track of indices
indexOfMaxCalories = 0 #hold for index of elf that has max calories

for line in f:
  if len(line.strip()) == 0 :
    #Encountered an empty line - if counter > previous max, replace the index with current
    currIndex += 1
    if calorieCounter > maxCalories:
      maxCalories = calorieCounter
      indexOfMaxCalories = currIndex


    calorieCounter = 0
  else:
    #Non empty line, add to the counter and continue
    calorieCounter += int(line)

#Max Calories carried by an elf and its index
print(indexOfMaxCalories)
print(maxCalories)
