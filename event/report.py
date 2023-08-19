from entity.clan import clan
from event.death import death
import random

# reformed daily report goes here

def daily():
  for c in list(clan.clans).copy():
    checkCats(c)
    feed(c)
  

def checkCats(c):
  for i in list(clan.clans[c].cats).copy():
    if clan.clans[c].cats[i].wp < 1:
      dead_guy = i
      if c == "player_Clan":
        requirement = (random.randint(5, 10))
        if clan.clans["player_Clan"].herbs >= requirement:
          cmd = "alfalfa"
          while not cmd == "Y" and not cmd == "y" and not cmd == "N" and not cmd == "n":
            cmd = input("""
            Attention! %s is dying, but if you use %d herbs you may be able to save them. You have %d herbs total.
            Would you like to try and save them? [Y/N]
            
            > """ % (clan.clans["player_Clan"].cats[dead_guy].name, requirement, clan.clans["player_Clan"].herbs))
            if cmd == "Y" or cmd == "y":
              clan.clans["player_Clan"].herbs -= requirement
              odds = (random.randint(1, 3))
              if odds == 1:
                death(dead_guy, " of exhaustion")
              else:
                print("You managed to save %s!" % clan.clans["player_Clan"].cats[dead_guy].name)
                clan.clans["player_Clan"].cats[dead_guy].wp = 5
            else:
              print("You failed to save %s." % clan.clans["player_Clan"].cats[dead_guy].name)
              death(dead_guy, " of exhaustion")
                
        else:     
          death(dead_guy, " of exhaustion")
      else:
        del clan.clans[c].cats[i]
    else:
      max = 999999
      if clan.clans[c].cats[i].age >= 80:
        max = 5
      if clan.clans[c].cats[i].age >= 90:
        max = 4
      if clan.clans[c].cats[i].age >= 100:
        max = 3
      if clan.clans[c].cats[i].age >= 110:
        max = 2
      if clan.clans[c].cats[i].age >= 120:
        max = 1
        
      rando = (random.randint(1, max))
      
      if rando == 1:

        aging = (random.randint(1, 10))
        clan.clans[c].cats[i].stats["Willpower"] -= aging
        clan.clans[c].cats[i].wp -= aging * 2

        if (clan.clans[c].cats[i].stats["Willpower"] == 0) or (clan.clans[c].cats[i].wp == 0):
          
          dead_guy = i
          if clan == "player_Clan":
            requirement = (random.randint(5, 10))
            if clan.clans["player_Clan"].herbs >= requirement:
              cmd = "alfalfa"
              while not cmd == "Y" and not cmd == "y" and not cmd == "N" and not cmd == "n":
                cmd = input("""
                Attention! %s is dying, but if you use %d herbs you may be able to save them. You have %d herbs total. Would you like to try and save them? Y/N
                
                > """ % (clan.clans["player_Clan"].cats[dead_guy].name, requirement, clan.clans["player_Clan"].herbs))
              
              if cmd == "Y" or cmd == "y":
                clan.clans["player_Clan"].herbs -= requirement
                odds = (random.randint(1, 3))
                if odds == 1:
                  death(dead_guy, " of old age")
                else:
                  print("You managed to save %s!" % clan.clans["player_Clan"].cats[dead_guy].name)
                  clan.clans["player_Clan"].cats[dead_guy].wp = 5
              else:
                print("You failed to save %s." % clan.clans["player_Clan"].cats[dead_guy].name)
                death(dead_guy, " of old age")   
            else:     
              death(dead_guy, " of old age")
          else:
            del clan.clans["player_Clan"].cats[dead_guy]
      if clan.clans[c].cats[i].xp >= ((clan.clans[c].cats[i].lvl + 1) * 5) and clan.clans[c].cats[i].lvl < 10:
        if c == "player_Clan":
          print("%s has leveled up!" % clan.clans["player_Clan"].cats[i].name)
          clan.clans["player_Clan"].cats[i].lvl += 1
          clan.clans["player_Clan"].cats[i].xp = 0
          points = 5
          while points > 0:
            cmd = "alfalfa"
            conf = False
            while conf == False:
              try:
                if int(cmd) == 1:
                  clan.clans["player_Clan"].cats[i].stats["Willpower"] += 5
                  print("WP has been increased by 5.")
                elif int(cmd) == 2:
                  clan.clans["player_Clan"].cats[i].stats["Strength"] += 1
                  print("STR has been increased by 1.")
                elif int(cmd) == 3:
                  clan.clans["player_Clan"].cats[i].stats["Toughness"] += 1
                  print("TGH has been increased by 1.")
                elif int(cmd) == 4:
                  clan.clans["player_Clan"].cats[i].stats["Speed"] += 1
                  print("SPD has been increased by 1.")
                elif int(cmd) == 5:
                  clan.clans["player_Clan"].cats[i].stats["Precision"] += 1
                  print("PRS has been increased by 1.")
                elif int(cmd) == 6:
                  clan.clans["player_Clan"].cats[i].stats["Charisma"] += 1
                  print("CHA has been increased by 1.")
                points -= 1
                conf = True
              except:
                cmd = input("""
                =%s's Stats [LVL %d (%d xp)]=
                %d/%d WP (willpower) [1]
                %d STR (strength) [2]
                %d TGH (toughness) [3]
                %d SPD (speed) [4]
                %d PRS (precision) [5]
                %d CHA (charisma) [6]

                You have %d points to distribute. Type in the ID of the stat you would like to upgrade.

                > """ % (clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].lvl, clan.clans["player_Clan"].cats[i].xp, clan.clans["player_Clan"].cats[i].wp,
                       clan.clans["player_Clan"].cats[i].stats["Willpower"], clan.clans["player_Clan"].cats[i].stats["Strength"], clan.clans["player_Clan"].cats[i].stats["Toughness"],
                       clan.clans["player_Clan"].cats[i].stats["Speed"], clan.clans["player_Clan"].cats[i].stats["Precision"], clan.clans["player_Clan"].cats[i].stats["Charisma"], points))

          # learn claw

          if clan.clans["player_Clan"].cats[i].lvl >= 2 and not "Claw" in clan.clans["player_Clan"].cats[i].moves:
            print("%s has learned Claw!" % clan.clans["player_Clan"].cats[i].name)
            clan.clans["player_Clan"].cats[i].moves.append("Claw")

          # learn tier I move

          elif (clan.clans["player_Clan"].cats[i].lvl >= 4
                and not "Pin Down" in clan.clans["player_Clan"].cats[i].moves
                and not "Quick Claw" in clan.clans["player_Clan"].cats[i].moves):
            cmd = "alfalfa"
            while not cmd == "Q" and not cmd == "q" and not cmd == "P" and not cmd == "p":
              cmd = input("""
              Attention! %s is ready to learn one of two moves. Their descriptions are as follows:
              
              [Q]uick Claw | The user swipes at their opponent many times in quick succession. Does little damage, but may attack multiple times in a turn.

              [P]in Down | The user shoves their opponent into the ground and holds them there. Does little damage, but stuns the opponent.
              
              Which move would you like %s to learn?
              
              > """ % (clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].name))

            if cmd == "Q" or cmd == "q":
              clan.clans["player_Clan"].cats[i].moves.append("Quick Claw")
              print("%s has learned Quick Claw!" % clan.clans["player_Clan"].cats[i].name)

            elif cmd == "P" or cmd == "p":
              clan.clans["player_Clan"].cats[i].moves.append("Pin Down")
              print("%s has learned Pin Down!" % clan.clans["player_Clan"].cats[i].name)

          # learn tier II move
              
          elif (clan.clans["player_Clan"].cats[i].lvl >= 6
                and not "Sneak" in clan.clans["player_Clan"].cats[i].moves
                and not "Fierce Bite" in clan.clans["player_Clan"].cats[i].moves):
            cmd = "alfalfa"
            while not cmd == "S" and not cmd == "s" and not cmd == "F" and not cmd == "f":
              cmd = input("""
              Attention! %s is ready to learn one of two moves. Their descriptions are as follows:
              
              [S]neak | The user disappears from view, to strike from the shadows a turn later. Does a basic amount of damage.

              [F]ierce Bite | The user shreds the opponent with a powerful bite attack. Does a high amount of damage, but takes a turn to charge.
              
              Which move would you like %s to learn?
              
              > """ % (clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].name))

            if cmd == "S" or cmd == "s":
              clan.clans["player_Clan"].cats[i].moves.append("Sneak")
              print("%s has learned Sneak!" % clan.clans["player_Clan"].cats[i].name)

            elif cmd == "F" or cmd == "f":
              clan.clans["player_Clan"].cats[i].moves.append("Fierce Bite")
              print("%s has learned Fierce Bite!" % clan.clans["player_Clan"].cats[i].name)

          # learn tier III move

          elif (clan.clans["player_Clan"].cats[i].lvl >= 8
                and not "Rage" in clan.clans["player_Clan"].cats[i].moves
                and not "Diplomacy" in clan.clans["player_Clan"].cats[i].moves):
            cmd = "alfalfa"
            while not cmd == "R" and not cmd == "r" and not cmd == "D" and not cmd == "d":
              cmd = input("""
              Attention! %s is ready to learn one of two moves. Their descriptions are as follows:
              
              [R]age | The user flies into an intense rage, attacking blindly. Random damage, 50% recoil and a chance to strike again in the same turn.

              [D]iplomacy | The user attempts to reason with the target. Success rate depends on user's personality traits and reputation.
              
              Which move would you like %s to learn?
              
              > """ % (clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].name))

            if cmd == "R" or cmd == "r":
              clan.clans["player_Clan"].cats[i].moves.append("Rage")
              print("%s has learned Rage!" % clan.clans["player_Clan"].cats[i].name)

            elif cmd == "D" or cmd == "d":
              clan.clans["player_Clan"].cats[i].moves.append("Diplomacy")
              print("%s has learned Diplomacy!" % clan.clans["player_Clan"].cats[i].name)

          # learn master move

          elif (clan.clans["player_Clan"].cats[i].lvl >= 10
                and not "Meditate" in clan.clans["player_Clan"].cats[i].moves
                and not "Killing Blow" in clan.clans["player_Clan"].cats[i].moves):
            cmd = "alfalfa"
            
            while not cmd == "S" and not cmd == "s" and not cmd == "D" and not cmd == "d":

              """

              concept : make Northstar and Thicketfang the defaults but try to find actual StarClan/Dark Forest
              cats from playerClan to fulfill this role if you can ?

              also maybe have Northstar and Thicketfang's argument change depending on the cat's ranking/stats ?

              """
              
              cmd = input("""
              %s finds themselves on the border between two very different worlds. To the left is a stunning, ethereal paradise, and on the other is a dark wasteland. A pale violet spectral form with stars dappling their fur approaches, along with a dark, spiky-furred beast with snakelike amber eyes.

              [Northstar] : I am Northstar, a StarClanner. We have been watching you with great interest, %s.
              StarClan is the protector of life and justice- align with us, and we will teach you the art of inner peace and healing.

              [Thicketfang] : No! Northstar lies. I am Thicketfang... I come from the Dark Forest, where independence and ambition reign supreme.
              Only cowards and weaklings side with the stars.
              Follow us, %s... work with the Dark Forest, and you will learn how to slay your enemies with a single blow!

              [Northstar] : Hmph... I suppose the decision is yours, %s, but please consider your options thoroughly.
              
              With which faction will %s align themselves?

              [S]tarClan

              [D]ark Forest
              
              > """ % (clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].name,
                       clan.clans["player_Clan"].cats[i].name,
                       clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].name))

            if cmd == "S" or cmd == "s":
              clan.clans["player_Clan"].cats[i].moves.append("Meditate")
              clan.clans["player_Clan"].cats[i].allegiance = "StarClan"
              print("%s has learned Meditate, StarClan's master skill!" % clan.clans["player_Clan"].cats[i].name)

            elif cmd == "D" or cmd == "d":
              clan.clans["player_Clan"].cats[i].moves.append("Killing Blow")
              clan.clans["player_Clan"].cats[i].faith = "The Dark Forest"
              print("%s has learned Killing Blow, the Dark Forest's master skill!" % clan.clans["player_Clan"].cats[i].name)

        else:
          clan.clans[c].cats[i].lvl += 1
          clan.clans[c].cats[i].xp = 0
          for x in range(5):
            selStat = (random.randint(1, 6))
            if int(selStat) == 1:
              clan.clans[c].cats[i].stats["Willpower"] += 5
            elif int(selStat) == 2:
              clan.clans[c].cats[i].stats["Strength"] += 1
            elif int(selStat) == 3:
              clan.clans[c].cats[i].stats["Toughness"] += 1
            elif int(selStat) == 4:
              clan.clans[c].cats[i].stats["Speed"] += 1
            elif int(selStat) == 5:
              clan.clans[c].cats[i].stats["Precision"] += 1
            elif int(selStat) == 6:
              clan.clans[c].cats[i].stats["Charisma"] += 1

def feed(c):
  if c == "player_Clan":
    print("")
    print("-- Prey Report --")
    print("")
    
    print("Your current number of feedings is %d." % (clan.clans["player_Clan"].prey))

    if clan.clans["player_Clan"].prey > len(clan.clans["player_Clan"].cats) * 2:
      print("What a feast ! There was more than enough prey for all of %s. Every cat rests with full bellies." % clan.clans["player_Clan"].name)
      wp_gain = 4
      clan.clans["player_Clan"].prey -= len(clan.clans["player_Clan"].cats) * 2
    elif clan.clans["player_Clan"].prey > len(clan.clans["player_Clan"].cats):
      print("%s is able to eat well, thanks to your patrols. No cat went to sleep hungry." % clan.clans["player_Clan"].name)
      wp_gain = 2
      clan.clans["player_Clan"].prey -= len(clan.clans["player_Clan"].cats) * 2
    elif clan.clans["player_Clan"].prey < (0 - len(clan.clans["player_Clan"].cats) * 0.5):
      print("Even the smallest mouths struggled to find food. %s withers under a fierce famine ..." % clan.clans["player_Clan"].name)
      wp_gain = -4
      clan.clans["player_Clan"].prey -= len(clan.clans["player_Clan"].cats)
    else:
      print("Your cats are beginning to show signs of weariness ... %s needs more prey if it is to survive." % clan.clans["player_Clan"].name)
      wp_gain = -2
      clan.clans["player_Clan"].prey -= len(clan.clans["player_Clan"].cats)
                                              
    print("Now you have %d feedings." % clan.clans["player_Clan"].prey)
    
    for i in clan.clans["player_Clan"].cats.copy():
      if (clan.clans["player_Clan"].cats[i].wp + wp_gain) < clan.clans["player_Clan"].cats[i].stats["Willpower"]:
        clan.clans["player_Clan"].cats[i].wp += wp_gain
      else:
        clan.clans["player_Clan"].cats[i].wp = clan.clans["player_Clan"].cats[i].stats["Willpower"]
      if wp_gain < 0:
        if clan.clans["player_Clan"].cats[i].wp < 1:
          dead_guy = i
          death(dead_guy, " of starvation")
