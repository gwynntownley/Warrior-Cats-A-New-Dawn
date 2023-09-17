import random
from bin.text import battleText
from entity.clan import clan
from entity.map import land, predators_ind
from event.death import death
from data.file import codebits

class enemy(object):
  def __init__(self, name, wp, lvl, stats):
    self.name = name
    self.wp = wp
    self.lvl = lvl
    self.stats = stats

def battle(battle_type, battler):
  
  # Define globals
  
  fighters = {}

  attackers = {}
  
  stunned = {}

  charging = {}

  charging_tar = []

  sneaking = {}

  sneaking_tar = []
  
  # Start
  
  for i in clan.clans["player_Clan"].cats.copy():
    if clan.clans["player_Clan"].cats[i].rank == "leader":
      leader = i
      break

  # Predator battle

  battleType = battle_type.split("-")
  
  if "predator" in battle_type:

    # Determine location of encounter

    y = int(battleType[2])
    battleloc = battleType[3]
        
    predator_type = (random.choice(list(land.coordinates[y][battleloc].predators)))
                                        
    # Determine predator level

    # Generate predators
    
    count = (random.randint(1, 4))
    for i in range(count):
      var_name = (random.choice(codebits))
      for i in range((random.randint(5, 15))):
        var_name = var_name + (random.choice(codebits))
      attackers[var_name] = enemy(predators_ind[predator_type], 0, (random.randint(0, 10)),
                                  {"Willpower" : 5, "Strength" : 1, "Toughness" : 1, "Speed" : 1, "Precision" : 1, "Charisma" : 1})
      for i in range(attackers[var_name].lvl * 5):
        upgrade = (random.choice(list((attackers[var_name].stats))))
        if upgrade == "Willpower":
          attackers[var_name].stats["Willpower"] += 5
        else:
          attackers[var_name].stats[upgrade] += 1
      attackers[var_name].wp = attackers[var_name].stats["Willpower"]
      
      print(battleText["predatorApproach"] % (attackers[var_name].lvl, attackers[var_name].name))

    # Form patrol
    
    print(battleText["partyPredator"] % predator_type)
    for i in range(4):
      id = 1
      possibles = []
      for i in clan.clans["player_Clan"].cats.copy():
        if ((clan.clans["player_Clan"].ranks[clan.clans["player_Clan"].cats[i].rank].privs["canFight"]) and ((
          "camp" in clan.clans["player_Clan"].cats[i].loc and battleType[1] == "n/a") or (battleType[1] in clan.clans["player_Clan"].cats and
          (i == battleType[1] or
          i in battleType)))
            and clan.clans["player_Clan"].cats[i].age_status["pregnant"] == 0 and not "fighting" in clan.clans["player_Clan"].cats[i].loc):
          print("%d: %s (Level: %d)" % (id, clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].lvl))
          possibles.append(i)
          id += 1
      if id == 1:
        print(battleText["partyNone"])
        break
      else:
        conf = False
        cmd = "alfalfa"
        while conf == False:
          try:

            target = possibles[int(cmd) - 1]
            fighters[target] = clan.clans["player_Clan"].cats[target]
            clan.clans["player_Clan"].cats[target].loc = "fighting"
            conf = True
          except:
            cmd = input(battleText["partyAdd"])

  # Clan battle
  
  if "enemy" in battle_type:

    if len(list(clan.clans[battler].cats)) > 0:

      # Determine enemy power
      
        count = (random.randint(1, 8))

        # Generate enemy squadron
        
        print(battleText["factionApproach"] % clan.clans[battler].name)
        for i in range(count):
          if len(list(clan.clans[battler].cats)) > 0:
            var_name = (random.choice(list(clan.clans[battler].cats)))
            attackers[var_name] = clan.clans[battler].cats[var_name]
            print("%s, level %d!" % (attackers[var_name].name, attackers[var_name].lvl))
            del clan.clans[battler].cats[var_name]

        # Form patrol
        
        print(battleText["partyFaction"] % clan.clans[battler].name)
        for i in range(8):
          id = 1
          possibles = []
          for i in clan.clans["player_Clan"].cats.copy():
            if ((clan.clans["player_Clan"].ranks[clan.clans["player_Clan"].cats[i].rank].privs["canFight"]) and ((
          "camp" in clan.clans["player_Clan"].cats[i].loc and battleType[1] == "n/a") or (battleType[1] in clan.clans["player_Clan"].cats and
          (i == battleType[1] or
          i in battleType)))
            and clan.clans["player_Clan"].cats[i].age_status["pregnant"] == 0 and not "fighting" in clan.clans["player_Clan"].cats[i].loc):
              print("%d: %s (Level: %d)" % (id, clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].lvl))
              possibles.append(i)
              id += 1
          if id == 1:
            print(battleText["partyNone"])
            break
          else:
            conf = False
            cmd = "alfalfa"
            while conf == False:
              try:
                target = possibles[int(cmd) - 1]
                fighters[target] = clan.clans["player_Clan"].cats[target]
                clan.clans["player_Clan"].cats[target].loc = "fighting"
                conf = True
              except:
                cmd = input(battleText["partyAdd"])
    else:
      print(battleText["factionDestroy"] % clan.clans[battler].name)
      over = True
      winner = "destroyed"

  # Traitor battle
  
  elif battle_type == "traitor":

    # Generate traitor
    
    attackers[battler] = enemy("traitor", clan.clans["player_Clan"].cats[battler].wp,
                               clan.clans["player_Clan"].cats[battler].lvl, clan.clans["player_Clan"].cats[battler].stats)
    attackers[battler].name = "traitor"

    print(battleText["traitorApproachA"])
    print(battleText["leaderBattle"])

    for i in clan.clans["player_Clan"].cats.copy():
      if clan.clans["player_Clan"].cats[i].rank == "leader":
        fighters[i] = clan.clans["player_Clan"].cats[i]
        break
    
  # Clanmate battle
  
  elif battle_type == "clanmate":

    # Identify attacker/attackee
    
    attackers[battler] = clan.clans["player_Clan"].cats[battler]

    print(battleText["duelApproach"] % attackers[battler].name)

    for i in clan.clans["player_Clan"].cats.copy():
      if clan.clans["player_Clan"].cats[i].rank == "leader":
        fighters[i] = clan.clans["player_Clan"].cats[i]
        break
  # Mercenary battle
  
  elif battle_type == "mercenary":

    # Generate mercenery
    
    mercenary = (random.choice(list(clan.clans[battler].cats)))
    attackers[mercenary] = clan.clans[battler].cats[mercenary]
    if attackers[mercenary].lvl < 0:
      attackers[mercenary].lvl = 0
    for i in range(attackers[mercenary].lvl * 5):
      upgrade = (random.choice(list(attackers[mercenary].stats)))
      if upgrade == "Willpower":
        attackers[mercenary].stats["Willpower"] += 5
      else:
        attackers[mercenary].stats[upgrade] += 1

    attackers[mercenary].wp = attackers[mercenary].stats["Willpower"]

    print(battleText["mercenaryApproach"] % (attackers[mercenary].name, clan.clans[battler].name))
    print(battleText["leaderBattle"])

    for i in clan.clans["player_Clan"].cats.copy():
      if clan.clans["player_Clan"].cats[i].rank == "leader":
        fighters[i] = clan.clans["player_Clan"].cats[i]
        break
    
  winner = "none"

  if winner == "destroyed":
    over = True
  else:
    over = False

  # Battle begin
  
  while over == False:
    for i in fighters.copy():
      cmd = "alfalfa"
      while not cmd == "A" and not cmd == "R" and not cmd == "F" and not cmd == "C":

        # Fighter stats + options
        
        cmd = input(battleText["action"] % (fighters[i].lvl, fighters[i].wp, fighters[i].stats["Willpower"], fighters[i].stats["Strength"], fighters[i].stats["Toughness"], fighters[i].stats["Speed"],fighters[i].stats["Precision"], fighters[i].stats["Charisma"], fighters[i].name))

        cmd = cmd.upper()

      # Attack
      
      if cmd == "A":

        # Select target
        
        id = 1
        for a in attackers.copy():
          print("[%d] lvl %d %s - %d/%d WP" % (id, attackers[a].lvl, attackers[a].name, attackers[a].wp, attackers[a].stats["Willpower"]))
          id += 1
        conf = False
        cmd = "alfalfa"
        while conf == False:
          try:
            target = list(attackers)[int(cmd) - 1]
            conf = True
          except:
            cmd = input(battleText["target"] % fighters[i].name)

        # Select move
        
        print(battleText["pounce"])
        id = 1
        for c in fighters[i].moves:
          if c == "Claw":
            print(battleText["claw"] % id)
          elif c == "Pin Down":
            print(battleText["pin"] % id)
          elif c == "Quick Claw":
            print(battleText["quick"] % id)
          elif c == "Sneak":
            print(battleText["sneak"] % id)
          elif c == "Fierce Bite":
            print(battleText["bite"] % id)
          elif c == "Rage":
            print(battleText["rage"] % id) 
          elif c == "Diplomacy":
            print(battleText["diplomacy"] % id) 
          elif c == "Meditate":
            print(battleText["meditate"] % id)
          elif c == "Killing Blow":
            print(battleText["instaKill"] % id) 
          id += 1
        conf = False
        cmd = "alfalfa"
        move = "Pounce"
        while conf == False:
          try:
            if int(cmd) == 0:
              move = "Pounce"
            else:
              move = fighters[i].moves[int(cmd) - 1]
            conf = True
          except:
            cmd = input(battleText["moveSel"])

        # Determine outcome of move

        print("%s used %s!" % (fighters[i].name, move))
        
        prs_min = int(cmd)

        if fighters[i].stats["Precision"] > prs_min * 2:
          odds = 100
        elif fighters[i].stats["Precision"] > prs_min * 1.5:
          odds = (random.randint(90, 100))
        elif fighters[i].stats["Precision"] > prs_min:
          odds = (random.randint(70, 90))
        elif fighters[i].stats["Precision"] > prs_min * 0.5:
          odds = (random.randint(30, 80))
        else:
          odds = (random.randint(0, 70))
        
        odd_min = (random.randint(0, 100))

        if odds < odd_min:
          print(battleText["playerMiss"] % fighters[i].name)
        else:
          
          if move == "Pounce" or move == "Pin Down" or move == "Quick Claw":
            dmg = fighters[i].stats["Strength"] * (random.uniform(0.2, 0.6))

          elif move == "Claw":
            dmg = fighters[i].stats["Strength"]

          elif move == "Rage":
            dmg = fighters[i].stats["Strength"] * (random.uniform(0.5, 2.5))
          
          if move == "Sneak":
            print(battleText["pUseSneak"] % fighters[i].name)
            sneaking[i] = fighters[i]

            sneaking_tar.append(target)

            del fighters[i]
          elif move == "Fierce Bite":
            print(battleText["pUseBite"] % fighters[i].name)
            charging[i] = fighters[i]

            charging_tar.append(target)

            del fighters[i]
          elif move == "Meditate":
            for h in fighters.copy():
              healed = fighters[i].stats["Precision"] + (random.randint(0, 6))
              fighters[h].wp += healed
              print(battleText["pHeal"] % (fighters[h].name, healed))
              if i == leader:
                fighters[h].rep += 1
          elif move == "Killing Blow":
            rando = (random.randint(0, 2))
            if rando == 0:
              print(battleText["pKillSuccess"] % fighters[i].name)
              attackers[target].wp = -1
            else:
              print(battleText["pKillFail"] % fighters[i].name)

            if i == leader:
              for h in fighters.copy():
                fighters[h].rep -= 2
          elif move == "Diplomacy":
            if fighters[i].stats["Charisma"] > attackers[target].stats["Charisma"]:
              odds = (random.randint(50, 100))
            else:
              odds = (random.randint(0, 50))
            
            rando = (random.randint(0, 100))

            if odds > rando:
              print(battleText["pDiplomacySuccess"] % (fighters[i].name, attackers[target].name))
              del attackers[target]
            else:
              print(battleText["pDiplomacyFail] % (fighters[i].name, attackers[target].name))
          else:
            if attackers[target].stats["Toughness"] >= fighters[i].stats["Strength"]:
              dmg = dmg * (random.uniform(0, 0.25))
            elif attackers[target].stats["Toughness"] / fighters[i].stats["Strength"] > 0.75:
              dmg = dmg * (random.uniform(0.25, 0.5))
            elif attackers[target].stats["Toughness"] / fighters[i].stats["Strength"] > 0.5:
              dmg = dmg * (random.uniform(0.5, 0.75))
            elif attackers[target].stats["Toughness"] / fighters[i].stats["Strength"] > 0.25:
              dmg = dmg * (random.uniform(0.75, 1))
            attackers[target].wp -= dmg
            print(battleText["pDamage"] % (fighters[i].name, dmg, attackers[target].name))
            if move == "Quick Claw":
              times = (random.randint(1, 2))
              if fighters[i].stats["Speed"] > attackers[target].stats["Speed"]:
                times = times * 2
              for b in range(times):
                rando = (random.randint(-2, 2))
                dmg += rando
                if dmg < 1:
                  dmg = 1
                attackers[target].wp -= dmg
                print(battleText["pDamage"] % (fighters[i].name, dmg, attackers[target].name))
            elif move == "Pin Down":
              stunned[target] = attackers[target]
              print(battleText["pStun"] % attackers[target].name)
            elif move == "Rage":
              recoil = dmg / 2
              print(battleText["pRecoil"] % (fighters[i].name, recoil))
              fighters[i].wp -= recoil
              rando = (random.randint(1, 4))
              if rando == 1:
                rando = (random.randint(-2, 2))
                dmg += rando
                if dmg < 1:
                  dmg = 1
                attackers[target].wp -= dmg
                print(battleText["pBonus"] % (fighters[i].name, dmg, attackers[target].name))
            if fighters[i].stats["Speed"] * 2 > attackers[target].stats["Speed"]:
                rando = (random.randint(-2, 2))
                dmg += rando
                if dmg < 1:
                  dmg = 1
                attackers[target].wp -= dmg
                print(battleText["pBonus"] % (fighters[i].name, dmg, attackers[target].name))
            for b in attackers.copy():
              if attackers[b].wp <= 0:
                if "predator" in battle_type:
                  print(battleText["eDeath"] % attackers[b].name)
                  for a in fighters.copy():
                    print(battleText["xpGain"] % (fighters[a].name, attackers[b].lvl))
                    fighters[a].xp += attackers[b].lvl
                elif "traitor" in battle_type:
                  cmd = input(battleText["traitorMercy"])
                  if cmd == "Y" or cmd == "y":
                    dead_guy = battler
                    death(dead_guy, " of their wounds")
                  elif cmd == "N" or cmd == "n":
                    print(battleText["traitorFlee"])
                    clan.clans["player_Clan"].cats[battler].wp = 0
                elif "clanmate" in battle_type:
                  cmd = input(battleText["mateMercy"] % attackers[battler].name)

                  if cmd == "Y" or cmd == "y":
                    dead_guy = battler
                    death(dead_guy, " of their wounds")
                  elif cmd == "N" or cmd == "n":
                    print(battleText["mateFlee"] % clan.clans["player_Clan"].cats[battler].name)
                    clan.clans["player_Clan"].cats[battler].wp = 0
                del attackers[b]

      # Rest
      
      elif cmd == "R":
        healed = (random.randint(1, 10))
        if fighters[i].wp + healed >= fighters[i].stats["Willpower"]:
          fighters[i].wp = fighters[i].stats["Willpower"]
          print(battleText["pRestMax"] % fighters[i].name)
        else:
          fighters[i].wp += healed
          print(battleText["pRest"] % (fighters[i].name, healed))

      # Check
      
      elif cmd == "C":
        id = 1
        for a in attackers.copy():
          print("[%d] lvl %d %s - %d/%d WP" % (id, attackers[a].lvl, attackers[a].name, attackers[a].wp, attackers[a].stats["Willpower"]))
          id += 1
        conf = False
        cmd = "alfalfa"
        while conf == False:
          try:
            target = list(attackers)[int(cmd) - 1]
            conf = True
          except:
            cmd = input(battleText["checkSelect"] % fighters[i].name)
        print(battleText["check"] % (attackers[target].name, attackers[target].lvl, attackers[target].wp, attackers[target].stats["Willpower"], attackers[target].stats["Strength"], attackers[target].stats["Toughness"], attackers[target].stats["Speed"],attackers[target].stats["Precision"], attackers[target].stats["Charisma"]))

      # Flee

      else:
        if len(attackers) > 0:
          catcher = (random.choice(list(attackers)))
          if attackers[catcher].stats["Speed"] > fighters[i].stats["Speed"] * 2:
            chance = 25
          elif attackers[catcher].stats["Speed"] > fighters[i].stats["Speed"]:
            chance = 50
          elif fighters[i].stats["Speed"] > attackers[catcher].stats["Speed"] * 2:
            chance = 100
          else:
            chance = 75
          rando = (random.randint(1, 100))
          if chance < rando:
            print(battleText["pFleeFail"] % (fighters[i].name, attackers[catcher].name))
          else:
            print(battleText["pFleeSuccess"] % fighters[i].name)
            clan.clans["player_Clan"].cats[i] = fighters[i]
            del fighters[i]
        else:
          print(battleText["pFleeSuccess"] % fighters[i].name)
          clan.clans["player_Clan"].cats[i] = fighters[i]
          del fighters[i]

      if len(list(fighters)) == 0 and len(list(sneaking)) == 0 and len(list(charging)) == 0:
        winner = "enemy"
        over = True

      elif len(list(attackers)) == 0:
        winner = "player"
        over = True
      
      else:
        winner = "none"
      
      if winner == "player" or winner == "enemy":
        break

    if winner == "player" or winner == "enemy":
      break

    # Sneak attack

    for i in sneaking.copy():
      if len(sneaking_tar) > 0:
        target = sneaking_tar[0]
        sneaking_tar.remove(target)

        print(battleText["pSneak"] % sneaking[i].name)

        if target in attackers:
          dmg = sneaking[i].stats["Strength"] + (random.randint(1, 4))

          if attackers[target].stats["Toughness"] >= sneaking[i].stats["Strength"]:
            dmg = dmg * (random.uniform(0, 0.25))
          elif attackers[target].stats["Toughness"] / sneaking[i].stats["Strength"] > 0.75:
            dmg = dmg * (random.uniform(0.25, 0.5))
          elif attackers[target].stats["Toughness"] / sneaking[i].stats["Strength"] > 0.5:
            dmg = dmg * (random.uniform(0.5, 0.75))
          elif attackers[target].stats["Toughness"] / sneaking[i].stats["Strength"] > 0.25:
            dmg = dmg * (random.uniform(0.75, 1))

          attackers[target].wp -= dmg

          print(battleText["pDamage"] % (sneaking[i].name, dmg, attackers[target].name))
          for b in attackers.copy():
            if attackers[b].wp <= 0:
              if "predator" in battle_type:
                print(battleText["eDeath"] % attackers[b].name)
                for a in fighters.copy():
                  print(battleText["xpGain"] % (fighters[a].name, attackers[b].lvl))
                  fighters[a].xp += attackers[b].lvl
              elif "traitor" in battle_type:
                cmd = input(battleText["traitorMercy"])

                if cmd == "Y" or cmd == "y":
                  dead_guy = battler
                  death(dead_guy, " of their wounds")
                elif cmd == "N" or cmd == "n":
                  print(battleText["traitorFlee"])
                  clan.clans["player_Clan"].cats[battler].wp = 0
              elif "clanmate" in battle_type:
                cmd = input(battleText["mateMercy"] % attackers[battler].name)

                if cmd == "Y" or cmd == "y":
                  dead_guy = battler
                  death(dead_guy, " of their wounds")
                elif cmd == "N" or cmd == "n":
                  print(battleText["mateFlee"] % clan.clans["player_Clan"].cats[battler].name)
                  clan.clans["player_Clan"].cats[battler].wp = 0
              del attackers[b]
        else:
          print(battleText["attackFail"])
      else:
        print(battleText["attackFail"])
        fighters[i] = sneaking[i]
        del sneaking[i]

      if len(list(fighters)) == 0 and len(list(sneaking)) == 0 and len(list(charging)) == 0:
        winner = "enemy"
        over = True

      elif len(list(attackers)) == 0:
        winner = "player"
        over = True

      else:
        winner = "none"
      
      if winner == "player" or winner == "enemy":
        break

    if winner == "player" or winner == "enemy":
      break

    # Charge attack
    
    for i in charging.copy():
      if len(charging_tar) > 0:
        target = charging_tar[0]
        charging_tar.remove(target)

        print(battleText["pBite"] % charging[i].name)

        if target in attackers:

          dmg = charging[i].stats["Strength"] + (random.randint(2, 6))

          if attackers[target].stats["Toughness"] >= charging[i].stats["Strength"]:
            dmg = dmg * (random.uniform(0, 0.25))
          elif attackers[target].stats["Toughness"] / charging[i].stats["Strength"] > 0.75:
            dmg = dmg * (random.uniform(0.25, 0.5))
          elif attackers[target].stats["Toughness"] / charging[i].stats["Strength"] > 0.5:
            dmg = dmg * (random.uniform(0.5, 0.75))
          elif attackers[target].stats["Toughness"] / charging[i].stats["Strength"] > 0.25:
            dmg = dmg * (random.uniform(0.75, 1))

          attackers[target].wp -= dmg

          print(battleText["pDamage"] % (charging[i].name, dmg, attackers[target].name))

          rando = (random.randint(1, 4))
          if rando == 1:
            
            stunned[target] = attackers[target]
            print(battleText["pStun"] % attackers[target].name)

            for b in attackers.copy():
              if attackers[b].wp <= 0:
                if battle_type == "predator":
                  print(battleText["eDeath"] % attackers[b].name)
                  for a in fighters.copy():
                    print(battleText["xpGain"] % (fighters[a].name, attackers[b].lvl))
                    fighters[a].xp += attackers[b].lvl
                elif battle_type == "traitor":
                  cmd = input(battleText["traitorMercy"])

                  if cmd == "Y" or cmd == "y":
                    dead_guy = battler
                    death(dead_guy, " of their wounds")
                  elif cmd == "N" or cmd == "n":
                    print(battleText["traitorFlee"])
                    clan.clans["player_Clan"].cats[battler].wp = 1
                elif battle_type == "clanmate":
                  cmd = input(battleText["mateMercy"] % attackers[battler].name)
                  if cmd == "Y" or cmd == "y":
                    dead_guy = battler
                    death(dead_guy, " of their wounds")
                  elif cmd == "N" or cmd == "n":
                    print(battleText["mateFlee"] % clan.clans["player_Clan"].cats[battler].name)
                    clan.clans["player_Clan"].cats[battler].wp = 1
                del attackers[b]

          fighters[i] = charging[i]
          del charging[i]

        else:
          print(battleText["attackFail"])
      else:
        print(battleText["attackFail"])
        fighters[i] = charging[i]
        del charging[i]
        
      if len(list(fighters)) == 0 and len(list(sneaking)) == 0 and len(list(charging)) == 0:
        winner = "enemy"
        over = True

      elif len(list(attackers)) == 0:
        winner = "player"
        over = True

      else:
        winner = "none"
      
      if winner == "player" or winner == "enemy":
        break

    if winner == "player" or winner == "enemy":
      break

    # Attacker's turn

    check_cool = 1

    for i in attackers.copy():
      if (attackers[i].wp / attackers[i].stats["Willpower"]) <= 0.25:
        rando = (random.randint(1, 3))
        if rando == 1:
          choice = "a"
        elif rando == 2:
          choice = "r"
        else:
          choice = "f"
      elif (attackers[i].wp / attackers[i].stats["Willpower"]) <= 0.5:
        rando = (random.randint(1, 3))
        if rando == 1:
          choice = "a"
        elif rando == 2:
          choice = "r"
        else:
          choice = "c"
      else:
        rando = (random.randint(1, 10))
        if rando <= 9:
          choice = "a"
        else:
          choice = "c"

      if i in stunned:
        print(battleText["eStunned"] % attackers[i].name)
      
      else:

        # Enemy attacks
        
        if choice == "a":
          if len(fighters) > 0:
            target = (random.choice(list(fighters)))
            dmg = (random.randint(1, 3)) * attackers[i].stats["Strength"]
            if fighters[target].stats["Toughness"] >= attackers[i].stats["Strength"]:
              dmg = dmg * (random.uniform(0, 0.25))
            elif fighters[target].stats["Toughness"] / attackers[i].stats["Strength"] > 0.75:
              dmg = dmg * (random.uniform(0.25, 0.5))
            elif fighters[target].stats["Toughness"] / attackers[i].stats["Strength"] > 0.5:
              dmg = dmg * (random.uniform(0.5, 0.75))
            elif fighters[target].stats["Toughness"] / attackers[i].stats["Strength"] > 0.25:
              dmg = dmg * (random.uniform(0.75, 1))
            fighters[target].wp -= dmg
            print(battleText["eDamage"] % (attackers[i].name, dmg, fighters[target].name))
            rando = (random.randint(1, 60))
            if rando == 1:
              new_scar = (random.choice(cat.scars))
              print(battleText["scar"] % (fighters[target].name, new_scar))
              fighters[target].scars.append(new_scar)
            for g in fighters.copy():
              mercy = 2
              if fighters[g].wp <= 0:
                clan.clans["player_Clan"].cats[g] = fighters[g]
                del fighters[g]
                if battle_type == "clanmate":
                  mercy = (random.randint(1, 2))
                  if mercy == 1:
                    
                    print(battleText["mateSpare"] % attackers[battler].name)
                    clan.clans["player_Clan"].cats[g].wp = 1
                    winner = "enemy"
                    break
                    
                elif battle_type == "clan":
                  rando = (random.choice(list(attackers)))
                  if attackers[rando].stats["Charisma"] <= clan.clans["player_Clan"].cats[g].stats["Charisma"]:
                    mercy = 1
                    print(battleText["factionSpare"] % (clan.clans["player_Clan"].cats[g].name, clan.clans["player_Clan"].cats[g].name))
                    clan.clans["player_Clan"].cats[g].wp = 1

                if mercy == 2:
                  if battle_type == "clanmate":
                      
                      print(battleText["mateKill"] % attackers[battler].name)
                      winner = "enemy"
                      
                  dead_guy = g
                  requirement = (random.randint(5, 10))
                  if clan.clans["player_Clan"].herbs >= requirement:
                    cmd = "alfalfa"
                    while not cmd == "Y" and not cmd == "y" and not cmd == "N" and not cmd == "n":
                      cmd = input(battleText["dying"] % (clan.clans["player_Clan"].cats[dead_guy].name, requirement, clan.clans["player_Clan"].herbs))
                      if cmd == "Y" or cmd == "y":
                        clan.clans["player_Clan"].herbs -= requirement
                        odds = (random.randint(1, 3))
                        if odds == 1:
                          death(dead_guy, " of their wounds")
                        else:
                          print(battleText["dyingSaved"] % clan.clans["player_Clan"].cats[dead_guy].name)
                          clan.clans["player_Clan"].cats[dead_guy].wp = 1
                      else:
                        death(dead_guy, " of their wounds")   
                  else:     
                    death(dead_guy, " of their wounds") 
          else:
            print(battleText["eWaiting"] % attackers[i].name)

        # Rest
        
        elif choice == "r":
          healed = (random.randint(1, 10))
          if attackers[i].wp + healed >= attackers[i].stats["Willpower"]:
            attackers[i].wp = attackers[i].stats["Willpower"]
            print(battleText["eRestMax"] % attackers[i].name)
          else:
            attackers[i].wp += healed
            print(battleText["eRest"] % (attackers[i].name, healed))

        # Check

        elif choice == "c" and check_cool > 0:
          print(battleText["ePause"] % attackers[i].name)
          attackers[i].stats["Strength"] += 1
          attackers[i].stats["Toughness"] += 1
          attackers[i].stats["Speed"] += 1
          attackers[i].stats["Precision"] += 1
          check_cool -= 1

        # Flee
        
        else:
          catcher = (random.choice(list(fighters)))
          if fighters[catcher].stats["Speed"] > attackers[i].stats["Speed"]:
            print(battleText["eFleeFail"] % (attackers[i].name, fighters[catcher].name))
          else:
            print(battleText["eFleeSuccess"] % attackers[i].name)
            if battle_type == "clan":
              clan.clans[battler].cats[i] = attackers[i].name
            del attackers[i]

      if i in stunned:
        unstun = (random.randint(0, 1))
        if unstun == 1:
          print(battleText["eStunRecover"] % attackers[i].name)
          del stunned[i]

      if len(list(fighters)) == 0 and len(list(sneaking)) == 0 and len(list(charging)) == 0:
        winner = "enemy"
        over = True

      elif len(list(attackers)) == 0:
        winner = "player"
        over = True
      
      else:
        winner = "none"

      if winner == "player" or winner == "enemy":
        break

    if winner == "player" or winner == "enemy":
      break

  # Battle loss
  
  if winner == "enemy":
    if battle_type == "predator":
      print(battleText["predatorLoss"] % predator_type)
    elif battle_type == "clan":
      print(battleText["factionLoss"] % clan.clans[battler].name)
      claimed = claim(battler)
      if claimed == True and (len(clan.clans["player_Clan"].coordinates) > 0):
        print(battleText["loseLand"] % clan.clans["player_Clan"].name)
        clan.clans[battler].land += 1
        tradeland = (random.choice(clan.clans["player_Clan"].location))
        for n in land.coordinates:
          if tradeland in land.coordinates[n]:
            y = n
            break
        clan.clans["player_Clan"].location.remove(tradeland)
        land.coordinates[y][tradeland].owner = battler
        clan.clans["player_Clan"].land -= 1

  # Battle win

  elif winner == "player":
    if battle_type == "predator":
      print(battleText["predatorWin"] % predator_type)
      clan.clans["player_Clan"].prey += 25
    elif battle_type == "clan":
      print(battleText["factionWin"] % clan.clans[battler].name)    
      claimed = claim("player_Clan")
      if claimed == True and (len(clan.clans[battler].coordinates) > 0):
        print(battleText["winLand"] % clan.clans[battler].name)
        clan.clans["player_Clan"].land += 1
        tradeland = (random.choice(clan.clans[battler].location))
        for n in land.coordinates:
          if tradeland in land.coordinates[n]:
            y = n
            break
        clan.clans[battler].location.remove(tradeland)
        land.coordinates[y][tradeland].owner = "player_Clan"
        clan.clans[battler].land -= 1

  for i in fighters.copy():
    clan.clans["player_Clan"].cats[i] = fighters[i]
    del fighters[i]
  for i in sneaking.copy():
    clan.clans["player_Clan"].cats[i] = sneaking[i]
    del sneaking[i]
  for i in charging.copy():
    clan.clans["player_Clan"].cats[i] = charging[i]
    del charging[i]

  for i in attackers.copy():
    if battle_type == "clan":
      clan.clans[battler].cats[i] = attackers[i]
    del attackers[i]

  for i in list(clan.clans["player_Clan"].cats):
    if "fighting" in clan.clans["player_Clan"].cats[i].loc:
      clan.clans["player_Clan"].cats[i].loc = "%s camp" % clan.clans["player_Clan"].name

  if winner == "player":
    return True
  else:
    return False
