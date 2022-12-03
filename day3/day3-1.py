total_priority = 0
comp1, comp2 = [], []
shared_items = []

with open('rucksacks.txt') as f:
  for line in f:
    line = line.strip()
    print(line)
    half_line_size = (int)(len(line)/2)
    for i in range(half_line_size):
      if line[i] not in comp1:
        comp1.append(line[i])
      if line[i+half_line_size] not in comp2:
        comp2.append(line[i+half_line_size])
    comp1.sort()
    comp2.sort()
    for i in comp1:
      for j in comp2:
        if i == j:
          shared_items.append(i)
          break
    comp1, comp2 = [], []
  for char in shared_items:
    if char.isupper():
      total_priority += ord(char)-38
    else:
      total_priority += ord(char)-96
    
print(total_priority)