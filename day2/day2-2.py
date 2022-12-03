totalScore = 0

def result_to_score(action):
    switcher = {
        'X': 0,
        'Y': 3,
        'Z': 6
    }
    return switcher.get(action)

def get_round_score(elve, you):
  roundScore = 0
  roundScore += result_to_score(you)
  # Choose Rock (+1)
  if (elve == 'A' and you == 'Y') or (elve == 'B' and you == 'X') or (elve == 'C' and you == 'Z'):
    roundScore += 1
  # Choose Paper (+2)
  elif (elve == 'A' and you == 'Z') or (elve == 'B' and you == 'Y') or (elve == 'C' and you == 'X'):
    roundScore += 2
  # Choose Scissor (+3)
  else:
    roundScore +=3
  return roundScore

with open('rock-paper-scissors-2.txt') as f:
  for line in f:
    line = line.strip()
    print(line)
    totalScore += get_round_score(line[0], line[2])

print(totalScore)
