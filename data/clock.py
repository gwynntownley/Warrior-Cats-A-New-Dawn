from event.battle import battle
from entity.clan import clan
from entity.map import land, landmarks
from entity.cat import genCat
import random

clock = {
  "turns" : 0,
  "day" : 0,
  "moon" : 0
  }

def timer():
  for f in list(clock):
    if "timer" in f and clock[f] > 0:
      print(clock[f])
      clock[f] -= 1
    elif "timer" in f:
      if "claim" in f:
        returnClaim(f)
      elif "hunt" in f:
        returnHunt(f)
      elif "train" in f:
        returnTrain(f)
      elif "patrol" in f:
        returnBorder(f)
    # daily tick events
  foundEnemy = (random.randint(1, 60))
  if foundEnemy == 1:
    enemies = []
    for c in list(clan.clans):
      if clan.clans[c].rep < 0:
        enemies.append(c)
    predChance = (random.randint(1,2))
    warChance = (random.randint(1, 3 + len(enemies)))
    if warChance <= len(enemies) and predChance == 1:
      campY = list(clan.clans["player_Clan"].location)[0][0]
      campX = list(land.coordinates[campY]).index(list(clan.clans["player_Clan"].location)[0][1])
      battleType = "enemy-n/a-%s-%s" % (campY, campX)
      battler = (random.choice(enemies))
      print("Cats from %s have invaded your camp!" % battler)
    else:
      campY = list(clan.clans["player_Clan"].location)[0][0]
      campX = list(clan.clans["player_Clan"].location)[0][1]
      battleType = "predator-n/a-%s-%s" % (campY, campX)
      battler = None
      print("Predators have discovered your camp!")

    won = battle(battleType, battler)

  # femine, prosperity, sudden death
  common = (random.randint(1, 180))

  # deforestation, mercenary, prophecy
  uncommon = (random.randint(1, 540))

  # traitor, disaster, disease
  rare = (random.randint(1, 1620))

  # code amendment, new Clan, leaving Clan
  lifetime = (random.randint(1, 4860))
  
  if lifetime == 1:
    pass
  elif rare == 1:
    pass
  elif uncommon == 1:
    pass
  elif common == 1:
    # famine
    eventType = (random.randint(1, 3))
    if eventType in [1,2]:
      if eventType == 1:
        eventType = "famine"
      else:
        eventType = "thriving"
      seedY = (random.choice(list(land.coordinates)))
      seedX = (random.choice(list(land.coordinates[seedY])))
      setattr(land.coordinates[seedY][seedX], "status", eventType)
      for x in range(random.randint(1, 12)):
        try:
          seedY = list(land.coordinates)[list(land.coordinates).index(seedY) + (random.randint(-1, 1))]
          seedX = list(land.coordinates)[seedY][list(land.coordinates)[seedY].index(seedX) + (random.randint(-1, 1))]
          setattr(land.coordinates[seedY][seedX], "status", eventType)
        except:
          pass
  
  for y in list(land.coordinates):
    for x in list(land.coordinates[y]):
      for p in list(land.coordinates[y][x].prey):
        if hasattr(land.coordinates[y][x], 'status'):
          if land.coordinates[y][x].status == "famine":
            morePrey = (random.randint(-6, 0))
          elif land.coordinates[y][x].status == "thriving":
            morePrey = (random.randint(0, 6))
        else:
          morePrey = (random.randint(-3, 3))
        land.coordinates[y][x].prey[p] += morePrey
        if land.coordinates[y][x].prey[p] < 0:
          land.coordinates[y][x].prey[p] = 0
            
        
# return

def returnClaim(parse):
  # patrol returns

  toDel = parse

  parse = parse.split("-")

  captain = parse[1]

  y = int(parse[2])

  target = parse[3]

  capName = clan.clans["player_Clan"].cats[captain].name
  
  print("%s and their patrol have returned!" % capName)

  for c in clan.clans["player_Clan"].cats.copy():
    if capName in clan.clans["player_Clan"].cats[c].loc or c == captain:
      clan.clans["player_Clan"].cats[c].loc = "%s camp" % clan.clans["player_Clan"].name
      ranxp = (random.randint(1, 5)) * 2
      clan.clans["player_Clan"].cats[c].xp += ranxp
      print("%s gained %d xp." % (clan.clans["player_Clan"].cats[c].name, ranxp))

  # claim chosen territory

  claimed = False

  claimy = y
  claimx = target

  if claimy >= 0:
    if land.coordinates[claimy][claimx].owner == None:
      claimed = True
      
  if claimed == True:
    land.coordinates[claimy][claimx].owner = "player_Clan"
    print("They have claimed new land for %s! Now you will catch more prey when you hunt, and you can recruit more cats." % clan.clans["player_Clan"].name)
    
    print('This land is a %s.' % land.coordinates[claimy][claimx].biome)
    clan.clans["player_Clan"].location.append([claimy, claimx])
    
    if not land.coordinates[claimy][claimx].landmark == None:
      print("This new land also included a landmark: %s!" % land.coordinates[claimy][claimx].landmark)
      if land.coordinates[claimy][claimx].landmark in clan.clans["player_Clan"].landmark:
        clan.clans["player_Clan"].landmark[land.coordinates[claimy][claimx].landmark] += 1
      else:
        clan.clans["player_Clan"].landmark[land.coordinates[claimy][claimx].landmark] = 1
      
  else:
    print("Unfortunately, the mission was unsuccessful - they found themselves unable to claim the chosen territory for their own.")

  del clock[toDel]

def returnHunt(parse):

  toDel = parse

  parse = parse.split("-")

  captain = parse[1]

  locY = int(parse[2])
  location = parse[3]

  increase_factor = 1
  
  if "Sunningrocks" in clan.clans["player_Clan"].landmark:
  
    increase_factor += clan.clans["player_Clan"].landmark["Sunningrocks"]

  capName = clan.clans["player_Clan"].cats[captain].name
  
  print("The hunting patrol led by %s has returned!" % capName)
  # Get prey

  total = 0

  for c in clan.clans["player_Clan"].cats.copy():
    if capName in clan.clans["player_Clan"].cats[c].loc or captain == c:


      caughtPrey = (random.choice(list(land.coordinates[locY][location].prey)))
      hurt = (random.randint(-5, 5))
      newPrey = 0
      if land.coordinates[locY][location].prey[caughtPrey] > 0:
        newPrey = (increase_factor * (clan.clans["player_Clan"].cats[c].stats["Speed"] +
                                       clan.clans["player_Clan"].cats[c].stats["Precision"]) * 0.33)
        newPrey = round(newPrey)

        if newPrey < 0:
          newPrey = 0
        if newPrey > 5:
          newPrey = 5
        land.coordinates[locY][location].prey[caughtPrey] -= 1

        print("%s has caught a(n) %s for %d feedings and gained %d xp." % (clan.clans["player_Clan"].cats[c].name,
                                                                           caughtPrey, newPrey, increase_factor))
      clan.clans["player_Clan"].cats[c].xp += increase_factor
      if hurt > 0:
        print("%s lost %d WP in the process." % (clan.clans["player_Clan"].cats[c].name, hurt))
        clan.clans["player_Clan"].cats[c].wp -= hurt
      clan.clans["player_Clan"].cats[c].loc = "%s camp" % clan.clans["player_Clan"].name
      total += newPrey
      print("preytotal: %d" % total)
  clan.clans["player_Clan"].prey += total
  if total == 0:
    print("Your cats couldn't find anything to catch. The prey might have gone somewhere else...")

  del clock[toDel]

def returnTrain(parse):

  toDel = parse

  parse = parse.split("-")

  captain = parse[1]

  increase_factor = 1
  
  if "Ancient Oak" in clan.clans["player_Clan"].landmark:
  
    increase_factor += clan.clans["player_Clan"].landmark["Ancient Oak"]

  print("ListB : %s" % list(clan.clans["player_Clan"].cats))

  capName = clan.clans["player_Clan"].cats[captain].name
  
  print("The training session taught by %s has finished!" % capName)

  for c in clan.clans["player_Clan"].cats.copy():
    if capName in clan.clans["player_Clan"].cats[c].loc or captain == c:
      if not captain == c:
        increase_factor += (clan.clans["player_Clan"].cats[captain].lvl * 0.25)
      total = round((random.randint(1, 5)) * increase_factor)
      if clan.clans["player_Clan"].cats[c].age < 2:
        hurt = (random.randint(3, 6))
      elif clan.clans["player_Clan"].cats[c].age < 4:
        hurt = (random.randint(2, 5))
      elif clan.clans["player_Clan"].cats[c].age < 6:
        hurt = (random.randint(1, 4))
      else:
        hurt = (random.randint(-3, 3))
      print("%s gained %d fighting xp from training." % (clan.clans["player_Clan"].cats[c].name, total))
      clan.clans["player_Clan"].cats[c].xp += total
      if hurt > 0:
        print("%s lost %d WP in the process." % (clan.clans["player_Clan"].cats[c].name, hurt))
        clan.clans["player_Clan"].cats[c].wp -= hurt
      clan.clans["player_Clan"].cats[c].loc = "%s camp" % clan.clans["player_Clan"].name

  del clock[toDel]

def returnBorder(parse):

  toDel = parse

  parse = parse.split("-")

  captain = parse[1]

  capName = clan.clans["player_Clan"].cats[captain].name

  y = int(parse[2])
  target = parse[3]
  
  print("The border patrol led by %s has returned!" % capName)

  # calculate returns

  totalPrey = 0
  encounter = False

  for c in clan.clans["player_Clan"].cats.copy():
    if capName in clan.clans["player_Clan"].cats[c].loc or captain == c:

      totalExp = 0

      # Found prey?
      
      foundPrey = (random.randint(1, 3))
      if foundPrey == 1:

        caughtPrey = (random.choice(list(land.coordinates[y][target].prey)))

        if land.coordinates[y][target].prey[caughtPrey] > 0:
          newPrey = (clan.clans["player_Clan"].cats[c].stats["Speed"] +
                                         clan.clans["player_Clan"].cats[c].stats["Precision"]) * 0.33
          newPrey = round(newPrey)
          hurt = (random.randint(-5, 5))
          if newPrey < 0:
            newPrey = 0
          if newPrey > 5:
            newPrey = 5
          land.coordinates[y][target].prey[caughtPrey] -= 1

          print("%s came back with a(n) %s worth %d feedings." % (clan.clans["player_Clan"].cats[c].name,
                                                                             caughtPrey, newPrey,))
          totalPrey += newPrey
      totalExp += 1

      # Found items?

      foundItem = (random.randint(1, 6))
      if foundItem == 1 and (len(list(clan.clans["player_Clan"].landmark)) > 0):
        markVisited = (random.choice(list(clan.clans["player_Clan"].landmark)))
        newItem = random.choice(landmarks[markVisited])
        print("%s found a(n) %s while exploring. It has been added to the Clan's inventory." % (clan.clans["player_Clan"].cats[c].name, newItem))
        if newItem in clan.clans["player_Clan"].inv:
          clan.clans["player_Clan"].inv[newItem] += 1
        else:
          clan.clans["player_Clan"].inv[newItem] = 1
      totalExp += 1

      # Found recruit?
      if "2" in parse[0]:
        foundRecruit = (random.randint(1, 6))
      else:
        foundRecruit = (random.randint(1, 9))
      if foundRecruit == 1:
        accepted = False
        var_name, accepted = genCat("player_Clan", "recruit")
        if accepted == False:
          totalExp += 1
        else:
          totalExp += 3

        encounter = True

      # Found enemy?
      foundEnemy = (random.randint(1, 6))
      if foundEnemy == 1:
        enemies = []
        for c in list(clan.clans):
          if clan.clans[c].rep < 0:
            enemies.append(c)
        warChance = (random.randint(1, 3 + len(enemies)))
        temParse = '-'.join(parse)
        if warChance <= len(enemies):

          battleType = "enemy" + temParse
          battler = (random.choice(enemies))
        else:
          battleType = "predator" + temParse
          battler = None

        won = battle(battleType, battler)

        if won == True:
          totalExp += 1
        else:
          totalExp += 3

        encounter = True

      if c in list(clan.clans["player_Clan"].cats):

        # Found hurt?
        foundHurt = (random.randint(1, 3))
        if foundHurt == 1:
          print("%s got injured during the patrol." % clan.clans["player_Clan"].cats[c].name)
          injury = (random.randint(1, 5))
          print("%s lost %d WP." % (clan.clans["player_Clan"].cats[c].name, injury))
          clan.clans["player_Clan"].cats[c].wp -= injury
          totalExp += 1

        clan.clans["player_Clan"].cats[c].xp += totalExp

        print("%s has earned %d experience points from this patrol." % (clan.clans["player_Clan"].cats[c].name, totalExp))

        clan.clans["player_Clan"].cats[c].loc = "%s camp" % clan.clans["player_Clan"].name

  preyTotal = 0
  for p in list(land.coordinates[y][target].prey):
    preyTotal += land.coordinates[y][target].prey[p]

  if preyTotal > 24:
    print("The patrol noticed that prey was running especially well here.")
  elif preyTotal > 12:
    print("The patrol found plenty of good hunting spots in that part of the territory.")
  elif preyTotal > 6:
    print("The patrol found hunting in the area to be poor, though there were still some prey about.")
  else:
    print("The patrol noticed this territory was almost completely bare of prey. Hunting there would be a waste of time.")

  if hasattr(land.coordinates[y][target], 'status'):
    if land.coordinates[y][target] == "famine":
      print("They also found signs of famine in the area--the hunting here may begin to suffer.")
    else:
      print("This part of the territory is showing signs of growth and prosperity. If it continues to thrive like this, the hunting conditions may improve.")
  
        
  clan.clans["player_Clan"].prey += totalPrey

  del clock[toDel]
