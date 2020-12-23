with open('./1/input.txt') as input:
  data = [ int(x) for x in input ]

  # part one - loop through 2 times to get the value
  for i in data:
    for j in data:
      if 2020 == i + j:
        print(i*j)
  
  # part two - loop through 3 times to get the value
  for i in data:
    for j in data:
      for k in data:
        if 2020 == i + j + k:
          print(i*j*k)