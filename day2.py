fileObj = open('d2input.txt', 'r')
d2input = fileObj.read()
fileObj.close()

# D2P1 solution:

def day2(gameInput):
  total = 0
  # masterDict = {
  #   "g": 13,
  #   "r": 12,
  #   "b": 14
  # }
  splInput = gameInput.splitlines()

  for game in splInput:
    flag = False
    game = game.split("Game ")
    gameNum = game[1].split(":")
    # get the game number
    trueGameNum = gameNum[0]
    # print(trueGameNum)
    # get each mini game
    miniGames = gameNum[1].split("; ")
    # print(miniGames)

    # get each individual number:color combo per minigame
    for set in miniGames:
      set = set.strip()
      set = set.split(", ")
      # print(set)

      for roll in set:
        roll = roll.split(" ")
        # print(roll[1][0], roll[0])
        if roll[1][0] == "r" and int(roll[0]) > 12:
          flag = True
        elif roll[1][0] == "g" and int(roll[0]) > 13:
          flag = True
        elif roll[1][0] == "b" and int(roll[0]) > 14:
          flag = True
    if not flag:
      total += int(trueGameNum)

  return total
        

# print(day2(d2input))

#D2P2 solution:

def day2part2(gameInput):
  total = 0
  splInput = gameInput.splitlines()
  for game in splInput:
    gameTotal = 1
    gameDict = {
      "r": 1,
      "g": 1,
      "b": 1
    }
    game = game.split("Game ")
    gameNum = game[1].split(":")
    # get each mini game
    miniGames = gameNum[1].split("; ")
    # print(miniGames)
    # get each individual number:color combo per minigame

    for set in miniGames:
      set = set.strip()
      set = set.split(", ")
      # print(set)

      for roll in set:
        roll = roll.split(" ")
        # print(roll[1][0], roll[0])
        curVal = gameDict.get(roll[1][0])
        if roll[1][0] == "r" and int(roll[0]) > curVal:
          gameDict["r"] = int(roll[0])
        elif roll[1][0] == "g" and int(roll[0]) > curVal:
          gameDict["g"] = int(roll[0])
        elif roll[1][0] == "b" and int(roll[0]) > curVal:
          gameDict["b"] = int(roll[0])

    # print(gameDict)
    for value in gameDict.values():
      gameTotal = gameTotal * int(value)

    total += gameTotal

  return total

print(day2part2(d2input))







