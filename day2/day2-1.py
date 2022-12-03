totalScore = 0

def action_to_score(action):
    switcher = {
        'X': 1,
        'Y': 2,
        'Z': 3
    }
    return switcher.get(action)

def get_round_score(elve, you):
  roundScore = 0
  roundScore += action_to_score(you)
  # Draw +3
  if (elve == 'A' and you == 'X') or (elve == 'B' and you == 'Y') or (elve == 'C' and you == 'Z'):
    roundScore += 3
  # Won +6
  elif (elve == 'A' and you == 'Y') or (elve == 'B' and you == 'Z') or (elve == 'C' and you == 'X'):
    roundScore += 6
  # If lost +0
  return roundScore

with open('rock-paper-scissors.txt') as f:
  for line in f:
    line = line.strip()
    print(line)
    totalScore += get_round_score(line[0], line[2])

print(totalScore)
