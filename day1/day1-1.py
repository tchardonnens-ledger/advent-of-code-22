maxSum, tempSum, elveId = 0, 0, 0

with open('elves-food.txt') as f:
  for line in f:
    line = line.strip()
    print(line)
    if line == '':
      elveId+=1
      if tempSum > maxSum:
        maxSum = tempSum
      tempSum = 0
    else:
      tempSum += int(line)
  
print(maxSum, elveId)
