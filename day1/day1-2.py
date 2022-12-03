tempSum = 0
sum1, sum2, sum3 = 0, 0, 0
topThreeSum = 0

with open('elves-food-2.txt') as f:
  for line in f:
    line = line.strip()
    print(line)
    if line == '':
      if tempSum > sum1:
        sum3 = sum2
        sum2 = sum1
        sum1 = tempSum
      elif tempSum > sum2:
        sum3 = sum2
        sum2 = tempSum
      elif tempSum > sum3:
        sum3 = tempSum
      tempSum = 0
    else:
      tempSum += int(line)
  
topThreeSum = sum1 + sum2 + sum3
print(topThreeSum)
