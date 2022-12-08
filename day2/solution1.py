'''
Problem statement - https://adventofcode.com/2022/day/2
'''

def find_rps_score(opponent_choice, your_choice):
  score = 0

  # Calculate first part of score based on your choice
  # X (Rock) = 1, Y (Paper) = 3, Z (Scissors) = 3
  match your_choice:
    case 'X':
      score = 1
    case 'Y':
      score = 2
    case 'Z':
      score = 3

  # Calculate second part of score based on the game result

  winning_combos = {
      "X" : "C",
      "Y" : "A",
      "Z" : "B"
  }

  draw_combos = {
      "X" : "A",
      "Y" : "B",
      "Z" : "C"
  }

  # If the combination is in the winning combo or draw combo, calculate the score accordingly
  # we don't have to worry about the loss as the score isn't affected

  if winning_combos.get(your_choice) == opponent_choice:
    score += 6
  elif draw_combos.get(your_choice) == opponent_choice:
    score += 3

  return score

f = open("input.txt", "r")

total_score = 0

for line in f:
  line_list = line.split()
  total_score += find_rps_score(line_list[0], line_list[1])

print(total_score)

