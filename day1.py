## define integers to find

integersToFind = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
valuesToFind = ("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine")

def findCalibrations(input):
  sumOfCalibration = 0
  listOfValues = input.split()
  for line in listOfValues:
    # print(line)
    first = findFirstNum(line)
    last = findLastnum(line)
    numToAdd = int(str(first)+str(last))
    # print(numToAdd)
    # print('\n')
    sumOfCalibration +=  numToAdd
  return sumOfCalibration
  
def findFirstNum(entry):
  strIndex = len(entry)
  newString = ''
  for strNum in valuesToFind:
    if strNum in entry:
      if entry.index(strNum) < strIndex:
        strIndex = entry.index(strNum)
        newString = entry.replace(strNum, str(integersToFind[valuesToFind.index(strNum)]))

  if not newString:
    for char in entry:
      try:
        if int(char) in integersToFind:
            return int(char)
      except:
        ValueError
  else:
    for char in newString:
      try:
        if int(char) in integersToFind:
            return int(char)
      except:
        ValueError

def findLastnum(entry):
  entry = entry[::-1]
  print(entry)
  strIndex = len(entry)
  newString = ''
  for strNum in valuesToFind:
    rStrNum = strNum[::-1]
    if rStrNum in entry:
      if entry.index(rStrNum) < strIndex:
        strIndex = entry.index(rStrNum)
        newString = entry.replace(rStrNum, str(integersToFind[valuesToFind.index(strNum)]))
        

  if not newString:
    for char in entry:
      try:
        if int(char) in integersToFind:
            return int(char)
      except:
        ValueError
  else:

    for char in newString:
      try:
        if int(char) in integersToFind:
            return int(char)
      except:
        ValueError
  
print(findCalibrations(calibrationDoc))


      








