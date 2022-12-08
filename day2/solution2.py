'''
Problem statement - https://adventofcode.com/2022/day/2
'''

def find_rps_score(opponent_choice, what_to_do):
  score = 0

  # Create dicts for winning, draw and loss combos

  winning_combos = {
      "B" : "Z",
      "A" : "Y",
      "C" : "X"
  }

  draw_combos = {
      "A" : "X",
      "B" : "Y",
      "C" : "Z"
  }

  loss_combos = {
      "B" : "X",
      "C" : "Y",
      "A" : "Z"
  }

  # Based on the second value, decide whether you must win, draw or lise

  if what_to_do == 'X':
    # You must lose, so choose from loss_combos
    my_actual_choice = loss_combos.get(opponent_choice)
  elif what_to_do == 'Y':
    # You must draw, so choose from draw_combos
    my_actual_choice = draw_combos.get(opponent_choice)
    score += 3
  elif what_to_do == 'Z':
    # You must win, so choose from winning_combos
    my_actual_choice = winning_combos.get(opponent_choice)
    score += 6

  # Now, calculate first part of score based on the actual choice to be made
  # X (Rock) = 1, Y (Paper) = 3, Z (Scissors) = 3
  match my_actual_choice:
    case 'X':
      score += 1
    case 'Y':
      score += 2
    case 'Z':
      score += 3

  return score

f = open("input.txt", "r")

total_score = 0

for line in f:
  line_list = line.split()
  total_score += find_rps_score(line_list[0], line_list[1])

print(total_score)

