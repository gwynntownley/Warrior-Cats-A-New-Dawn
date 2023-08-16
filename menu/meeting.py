## menuMeeting

from data.clock import clock
from data.parse import parseOpt
from entity.clan import clan
from entity.rank import rank, rankTemplates
import random

def menuMeeting():
  print("This command is still in the works! Come back later.")
  clock["turns"] -= 1

  cmd = "alfalfa"

  while not cmd in ["G", "I", ""]:
      
    cmd = input("""
    You have decided to call a meeting! What are you announcing? (press ENTER to quit)
    
    [G]roup Change = change something that affects the entire %s

    [I]ndividual Change = change something about a specific cat or cats
    
    > """ % (clan.clans["player_Clan"].noun)).upper()

  if cmd == "G":
    while not cmd in ["N", "R", "T"]:
      cmd = input("""
      What about %s are you changing?
      
      [N]ame = give your %s a new name

      [R]ank = introduce a new rank to %s

      [T]ype = change the type of group %s is (Clan, Tribe, etc)
      
      > """ % (clan.clans["player_Clan"].name, clan.clans["player_Clan"].noun, clan.clans["player_Clan"].name,
               clan.clans["player_Clan"].name)).upper()
    if cmd == "N":
      newName = input("""
      What would you like to change your %s's name to?

      > """ % (clan.clans["player_Clan"].noun))
      for c in clan.clans.copy():
        for x in clan.clans[c].cats.copy():
          if ("%s camp" % clan.clans["player_Clan"].name) in clan.clans[c].cats[x].loc:
            clan.clans[c].cats[x].loc = "%s camp" % newName
      clan.clans["player_Clan"].name = newName
      print("Your %s's new name is %s!" % (clan.clans["player_Clan"].noun, clan.clans["player_Clan"].name))
    elif cmd == "T":
      newType = input("""
      What type of group would you like %s to become?

      > """ % (clan.clans["player_Clan"].name))
      clan.clans["player_Clan"].noun = newType
      print("%s is now a %s!" % (clan.clans["player_Clan"].name, clan.clans["player_Clan"].noun))
    elif cmd == "R":
      newRank = rank("RANKNAME", 0, {
  "canFight" : False,
  "canHeal" : False,
  "canHunt" : False,
  "canPatrol" : False,
  "canTrain" : False,
  "canClaim" : False,
  "canMate" : False,
  "canInherit" : False,
  "isUnique" : False}, {
    "autoAge" : False,
    "sourceRank" : None,
    "ageMin" : None
    }, None, None)
      confirm = False
      while not confirm:

        cmd = input("""
        Welcome to the WCND Rank Builder! Here you can
        customize a rank to implement into your %s.
        You can modify each individual feature of the rank
        manually, or use a template as a blueprint.

        To modify a setting, enter the number next to the setting.
        The Builder will provide a list of options.

        [ [1] %s ] [ [2] #%d ]

        [ PRIVELEGES ]
          [3] Battle Patrols: %s
          [4] Border Patrols: %s
          [5] Exploratory Patrols: %s
          [6] Healing: %s
          [7] Heir: %s
          [8] Hunting Patrols: %s
          [9] Mates: %s
          [10] Training Parties: %s
          [11] Unique: %s
        
        [ PROMOTION ]
          [12] Automatic Promotion: %s
          [13] Old Rank: %s
          [14] Minimum Age: %s

        [ NAMING ]
          [15] Default Prefix: %s
          [16] Default Suffix: %s

        

        [F]inish = confirm this rank & add it to your %s
        [T]emplates = view & apply templates

        > """ % (clan.clans["player_Clan"].noun, newRank.name, newRank.order, str(newRank.privs["canFight"]),
                 str(newRank.privs["canPatrol"]), str(newRank.privs["canClaim"]), str(newRank.privs["canHeal"]),
                 str(newRank.privs["canInherit"]), str(newRank.privs["canHunt"]), str(newRank.privs["canMate"]),
                 str(newRank.privs["canTrain"]), str(newRank.privs["isUnique"]), str(newRank.autoAge["autoAge"]),
                 str(newRank.autoAge["sourceRank"]), str(newRank.autoAge["ageMin"]), str(newRank.prefix), str(newRank.suffix), clan.clans["player_Clan"].noun)).upper()
        if cmd == "F":
          print("Your %smates have accepted the '%s' rank into %s." % (clan.clans["player_Clan"].noun, newRank.name, clan.clans["player_Clan"].name))
          clan.clans["player_Clan"].ranks[newRank.name] = newRank
          confirm = True
          
        elif cmd == "T":
          print("Select the template you would like to use.")
          print("")
          parseOpt(list(rankTemplates))
          print("")
          template = input(" >")
          newRank = rankTemplates[list(rankTemplates)[int(template) - 1]]

        elif cmd == "1":
          newRank.name = input("""
          What would you like your new rank's name to be?

          > """)
        elif cmd == "2":
          newRank.order = int(input("""
          Enter the order in the allegiances
          you would like this rank to be listed.
          Use numbers. The lower the number, the higher
          up the rank will be placed.

          > """))
        elif cmd == "3":
          can = input("""
          Can this rank engage in battles?
          Enter 0 if no, and 1 if yes.

          > """)
          if can == "1":
            newRank.privs["canFight"] = True
          else:
            newRank.privs["canFight"] = False
        elif cmd == "4":
          can = int(input("""
          Can this rank join border patrols?
          Enter 0 if no, and 1 if yes.

          > """))
          if can == "1":
            newRank.privs["canPatrol"] = True
          else:
            newRank.privs["canPatrol"] = False
        elif cmd == "5":
          can = input("""
          Can this rank go beyond the borders to search for new land?
          Enter 0 if no, and 1 if yes.

          > """)
          if can == "1":
            newRank.privs["canClaim"] = True
          else:
            newRank.privs["canClaim"] = False
        elif cmd == "6":
          can = input("""
          Can this rank gather and use medicine to heal others?
          
          NOTE: Cats with this privelege will have their stats
          re-adjusted to suit their position! They may do more
          poorly in other areas, such as fighting and hunting.
          
          Enter 0 if no, and 1 if yes.

          > """)
          if can == "1":
            newRank.privs["canHeal"] = True
          else:
            newRank.privs["canHeal"] = False
        elif cmd == "7":
          can = input("""
          Can this rank inherit the leader rank, should the
          leader die or retire?
          
          NOTE: If there are multiple heirs, you will be prompted
          to select ONE to inherit the rank when your present leader
          dies or retires.
          
          Enter 0 if no, and 1 if yes.

          > """)
          if can == "1":
            newRank.privs["canInherit"] = True
          else:
            newRank.privs["canInherit"] = False
        elif cmd == "8":
          can = input("""
          Can this rank join hunting patrols?
          
          Enter 0 if no, and 1 if yes.

          > """)
          if can == "1":
            newRank.privs["canHunt"] = True
          else:
            newRank.privs["canHunt"] = False
        elif cmd == "9":
          can = input("""
          Can this rank take mates?
          
          Enter 0 if no, and 1 if yes.

          > """)
          if can == "1":
            newRank.privs["canMate"] = True
          else:
            newRank.privs["canMate"] = False
        elif cmd == "10":
          can = input("""
          Can this rank teach/participate in training lessons?
          
          Enter 0 if no, and 1 if yes.

          > """)
          if can == "1":
            newRank.privs["canTrain"] = True
          else:
            newRank.privs["canTrain"] = False
        elif cmd == "11":
          can = int(input("""
          Can there be only one of this rank?
          
          Enter 0 if no, and 1 if yes.

          > """))
          if can == "1":
            newRank.privs["isUnique"] = True
          else:
            newRank.privs["isUnique"] = False
        elif cmd == "12":
          can = input("""
          Will this rank be automatically given to
          cats at a certain age?
          
          Enter 0 if no, and 1 if yes.

          > """)
          if can == "1":
            newRank.autoAge["autoAge"] = True
          else:
            newRank.autoAge["autoAge"] = False
        elif cmd == "13":
          print("")
          parseOpt(list(rankTemplates))
          print("")

          can = int(input("""
          What rank will be promoted to this one?
          i.e. kit to apprentice, apprentice to warrior...

          > """))

          newRank.autoAge["sourceRank"] = list(rankTemplates)[can].name
        elif cmd == "14":

          can = int(input("""
          At what age will the old rank be promoted to this one?

          > """))

          newRank.autoAge["ageMin"] = can
        elif cmd == "15":

          can = (input("""
          What should the default prefix for this rank be?

          > """))

          newRank.prefix = can
        elif cmd == "16":

          can = (input("""
          What should the default suffix for this rank be?

          > """))

          newRank.suffix = can
        else:
          print("This feature hasn't been added yet!")

  elif cmd == "I":
    while not cmd in ["N", "R", "E"]:
      cmd = input("""
      What are you planning to change?

      [E]xile = chase one or multiple cats out of the %s
      
      [N]ame = change the name of one or multiple cats

      [R]ank = promote or demote one or multiple cats
      
      > """ % (clan.clans["player_Clan"].noun)).upper()
    selected = []
    done = False
    while not done:
      id = 1
      possibles = []
      for i in clan.clans["player_Clan"].cats.copy():
        if (("%s camp" % clan.clans["player_Clan"].name) in clan.clans["player_Clan"].cats[i].loc and not clan.clans["player_Clan"].cats[i].rank == "leader" and not i in selected):
          print("%d: %s (%s)" % (id, clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].rank))
          possibles.append(i)
          id += 1
      if id == 1:
        print("You cannot select any more cats.")
        done = True
      else:      
        correct_confirm = False
        sel = "alfalfa"
        while correct_confirm == False:
          try:
            if str(sel).lower() == "done":
              done = True
            else:
              selected.append(possibles[int(sel) - 1])
            correct_confirm = True
          except Exception as e:
            sel = input("""Enter the ID of the cat you would like to select below. Reply 'done' when you are done. You may
            select as many cats as you would like.
            
            > """)
    if cmd == "E":
      for x in selected:
        print(clan.clans["player_Clan"].cats[x].name)
      confirm = input("""
      Are you sure you would like to exile these cats? [Y/N]

      > """).lower()
      if confirm == "y":
        for x in selected:
          del clan.clans["player_Clan"].cats[x]
    elif cmd == "N":
      for x in selected:
        print("%s/%s/%s" % (clan.clans["player_Clan"].cats[x].prefix, clan.clans["player_Clan"].cats[x].root, clan.clans["player_Clan"].cats[x].suffix))
      nameTarget = input("""
      Which part of these cat's names do you want to change? If you have changed your mind, reply 'NO'.

      [P]refix
      [R]oot
      [S]uffix

      > """).upper()
      if nameTarget == "P":
        newPrefix = input("""
        What will the new prefix for these cats be?

        > """)
        for x in selected:
          clan.clans["player_Clan"].cats[x].prefix = newPrefix
      if nameTarget == "R":
        newRoot = input("""
        What will the new name-root for these cats be?

        > """)
        for x in selected:
          clan.clans["player_Clan"].cats[x].root = newRoot
      if nameTarget == "S":
        newSuffix = input("""
        What will the new suffix for these cats be?

        > """)
        for x in selected:
          clan.clans["player_Clan"].cats[x].suffix = newSuffix
          
      for x in selected:
        print("%s's new name is %s%s%s!" % (clan.clans["player_Clan"].cats[x].name, clan.clans["player_Clan"].cats[x].prefix,
                                            clan.clans["player_Clan"].cats[x].root, clan.clans["player_Clan"].cats[x].suffix))
        clan.clans["player_Clan"].cats[x].name = clan.clans["player_Clan"].cats[x].prefix + clan.clans["player_Clan"].cats[x].root + clan.clans["player_Clan"].cats[x].suffix
    if cmd == "R":
      for x in selected:
        print("%s (%s)" % (clan.clans["player_Clan"].cats[x].name, clan.clans["player_Clan"].cats[x].rank))
      id = 1
      for r in list(clan.clans["player_Clan"].ranks):
        print("[%d] %s" % (id, r))
        id += 1
      newRank = int(input("""
      What rank would you like to promote these cats to?

      > """))
      newRank = list(clan.clans["player_Clan"].ranks)[newRank - 1]
      hasRank = 0
      for x in list(clan.clans["player_Clan"].cats):
        if clan.clans["player_Clan"].cats[x].rank == newRank:
          hasRank += 1
      if clan.clans["player_Clan"].ranks[newRank].privs["isUnique"] and (len(selected) > 1 or hasRank > 0):
        print("You cannot have more than one cat in this rank!")
      else:
        for x in selected:
          clan.clans["player_Clan"].cats[x].rank = newRank
          yesName = input("""
          Would you like to change %s's name? [Y/N]

          > """ % clan.clans["player_Clan"].cats[x].name).upper()
          if yesName == "Y":
            nameTarget = input("""

            Which part of %s/%s/%s's name do you want to change? If you have changed your mind, reply 'NO'.

            [P]refix
            [R]oot
            [S]uffix

            > """ % (clan.clans["player_Clan"].cats[x].prefix,
                     clan.clans["player_Clan"].cats[x].root, clan.clans["player_Clan"].cats[x].suffix)).upper()
            if nameTarget == "P":
              newPrefix = input("""
              What will the new prefix for this cat be?

              > """)
              clan.clans["player_Clan"].cats[x].prefix = newPrefix
            if nameTarget == "R":
              newRoot = input("""
              What will the new name-root for this cat be?

              > """)
              clan.clans["player_Clan"].cats[x].root = newRoot
            if nameTarget == "S":
              newSuffix = input("""
              What will the new suffix for this cat be?

              > """)
              clan.clans["player_Clan"].cats[x].suffix = newSuffix
                
              print("%s's new name is %s%s%s!" % (clan.clans["player_Clan"].cats[x].name, clan.clans["player_Clan"].cats[x].prefix,
                                                  clan.clans["player_Clan"].cats[x].root, clan.clans["player_Clan"].cats[x].suffix))
              clan.clans["player_Clan"].cats[x].name = clan.clans["player_Clan"].cats[x].prefix + clan.clans["player_Clan"].cats[x].root + clan.clans["player_Clan"].cats[x].suffix
          
          print("%s is now a %s!" % (clan.clans["player_Clan"].cats[x].name, clan.clans["player_Clan"].cats[x].rank))

      print("This feature hasn't been added yet!")
    # Action





















  
