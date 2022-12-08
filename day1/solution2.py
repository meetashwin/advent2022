'''
By the time you calculate the answer to the Elves' question, they've already realized that the Elf carrying the most Calories of food might eventually run out of snacks.

To avoid this unacceptable situation, the Elves would instead like to know the total Calories carried by the top three Elves carrying the most Calories. That way, even if one of those Elves runs out of snacks, they still have two backups.

In the example above, the top three Elves are the fourth Elf (with 24000 Calories), then the third Elf (with 11000 Calories), then the fifth Elf (with 10000 Calories). The sum of the Calories carried by these three elves is 45000.

Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
'''
f = open("input.txt", "r")

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

#List containing all calories - sort it, reverse it and get top 3
maxCaloriesList.sort()
maxCaloriesList.reverse()

top3Calories = 0

for i in range(3):
  top3Calories += maxCaloriesList[i]

print(top3Calories)
