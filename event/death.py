import random
import sys

from bin.text import deathText

from entity.clan import clan
from entity.cat import cat

class realm(object):
  def __init__(self, name, cats):
    self.name = name
    self.cats = cats

  realms = {}

realm.realms["star"] = realm("StarClan", {})
realm.realms["dark"] = realm("The Dark Forest", {})
realm.realms["ghost"] = realm("The Ghost Realm", {})

def death(dead_guy, cause):

  # Define globals

  # Start

  if clan.clans["player_Clan"].cats[dead_guy].root == "Kiwi":
    cause = deathText["kiwi"]
  
  print(deathText["death"] % (clan.clans["player_Clan"].cats[dead_guy].name, cause))

  # Player lifeloss
  
  if hasattr(clan.clans["player_Clan"].cats[dead_guy], "lives"):
    if clan.clans["player_Clan"].cats[dead_guy].lives > 1:
      clan.clans["player_Clan"].cats[dead_guy].lives -= 1
      print(deathText["lifeLoss"] % (clan.clans["player_Clan"].cats[dead_guy].name, clan.clans["player_Clan"].cats[dead_guy].lives))
      clan.clans["player_Clan"].cats[dead_guy].wp = 5
    
  else:

    # Player permadeath
    
    if clan.clans["player_Clan"].cats[dead_guy].rank == "leader":
      new_leader =  ""
      for i in clan.clans["player_Clan"].cats.copy():
        if clan.clans["player_Clan"].cats[i].rank["canInherit"] == True:
          new_leader = i
          break
      print(deathText["newLeader"] % (clan.clans["player_Clan"].cats[new_leader].name,
                                               clan.clans["player_Clan"].cats[new_leader].root + "star"))
      clan.clans["player_Clan"].cats[new_leader].suffix = "star"
      clan.clans["player_Clan"].cats[new_leader].name = clan.clans["player_Clan"].cats[new_leader].root + clan.clans["player_Clan"].cats[new_leader].suffix 
      clan.clans["player_Clan"].cats[new_leader].rank = "leader"
      clan.clans["player_Clan"].cats[new_leader].rep = 0

      # Nine lives ceremony
      
      print(deathText["lives"] % land.communer)

      temp_starclan = folder.folders["starclan"].contents

      for i in range(9):
        if len(list(temp_starclan)) < 1:
          temp_suffixes = suffixes + ["star", "star", "star", "star", "star", "star", "star", "star", "star", "star",
                                      "paw", "paw", "paw", "paw", "paw", "paw", "paw", "paw", "paw","paw",
                                      "kit", "kit", "kit", "kit", "kit", "kit", "kit", "kit", "kit", "kit",
                                      "", "",  "", "", "", "", "", "", "", ""]

          name = (random.choice(cat.roots)) + (random.choice(temp_suffixes))

          relation = (random.choice(cat.relationship))

          if "paw" in name or "kit" in name:
            while relation in ["mate","mother","father","parent":
              relation = (random.choice(cat.relationship))  

          virtue = (random.choice(cat.virtues))

          print(deathText["lifeRandom"] % (name, relation, virtue))
        else:
          giver = (random.choice(list(folder.folders["starclan"].contents)))
          name = folder.folders["starclan"].contents[giver].name

          rank = folder.folders["starclan"].contents[giver].rank

          virtue = (random.choice(cat.virtues))

          print(deathText["lifeChar"] % (name, rank, virtue))

          del temp_starclan[giver]
        
      print("")
      print("===END OF CUTSCENE===")
      setattr(clan.clans["player_Clan"].cats[i], 'lives', 9)
      choices = []
      id = 1
      for i in clan.clans["player_Clan"].cats.copy():
        if clan.clans["player_Clan"].cats[i].rank == "warrior":
          print("[%d] %s" % (id, clan.clans["player_Clan"].cats[i].name))
          id += 1
          choices.append(i)
      if id == 1:
        printprint(deathText["end"])
        sys.exit(0)
      else:
        conf = False
        cmd = "alfalfa"
        while conf == False:
          try:
            new_deputy = choices[int(cmd) - 1]
            clan.clans["player_Clan"].cats[new_deputy].rank = "deputy"
            conf = True
          except:
            cmd = input(deathText["selDeputy"])
      print(deathText["newDeputy"] % clan.clans["player_Clan"].cats[new_deputy].name)
      for i in clan.clans["player_Clan"].cats.copy():
        clan.clans["player_Clan"].cats[i].rep = (random.randint(-10, 10))
    # Process death

    cat.roots.append(clan.clans["player_Clan"].cats[dead_guy].root)

    if clan.clans["player_Clan"].cats[dead_guy].allegiance == "StarClan":
      realm.realms["star"].cats[dead_guy] = clan.clans["player_Clan"].cats[dead_guy]
      print(deathText["starClan"] % clan.clans["player_Clan"].cats[dead_guy].name)
    elif clan.clans["player_Clan"].cats[dead_guy].allegiance == "The Dark Forest":
      realm.realms["dark"].cats[dead_guy] = clan.clans["player_Clan"].cats[dead_guy]
      print( % clan.clans["player_Clan"].cats[dead_guy].name)
    else:
      rando = (random.randint(1, 6))
      if rando == 1:
        realm.realms["dark"].cats[dead_guy] = clan.clans["player_Clan"].cats[dead_guy]
        print(deathText["darkForest"] % clan.clans["player_Clan"].cats[dead_guy].name)
      elif rando == 2:
        realm.realms["ghost"].cats[dead_guy] = clan.clans["player_Clan"].cats[dead_guy]
        print(deathText["ghostRealm"] % clan.clans["player_Clan"].cats[dead_guy].name)
      else:
        realm.realms["star"].cats[dead_guy] = clan.clans["player_Clan"].cats[dead_guy]
        print(deathText["starClan"] % clan.clans["player_Clan"].cats[dead_guy].name)

    del clan.clans["player_Clan"].cats[dead_guy]


