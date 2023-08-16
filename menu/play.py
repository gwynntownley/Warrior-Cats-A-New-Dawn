import random
import os
import pickle
import traceback

def menuPlay(clock, symbols):

  from action.select import actionSelect
  from data.clock import timer, returnClaim
  from data.file import filePreview
  from data.parse import parseOpt, parseSel
  from entity.cat import genCat
  from entity.clan import clan
  from entity.map import seeMap, land
  from event.battle import battle
  from event.event import warriorCode, possibleCode
  from event.report import daily
  from menu.explore import menuExplore
  from menu.meeting import menuMeeting
  from menu.social import menuSocial
  from view.allegiances import allegiances
  from storage import disease

  cheats = ["FASTTRAVEL", "SUMMONFRIEND"]

  while len(clan.clans["player_Clan"].cats) >= 1:

    # Set player

    for i in clan.clans["player_Clan"].cats.copy():
      if clan.clans["player_Clan"].cats[i].rank == "leader":
        leader = i
        break

    cmd = "alfalfa"

    # Select A-V-S
    skip = False
    
    for t in list(clock):
      if "True" in t:
        print(t)
        skip = True

    if skip == True:
      clock["turns"] -= 1
      print("You are away from camp! Skipping turn...")
      timer()
    else:
      while not cmd in ["A", "V", "S", "R", ""] and not cmd in cheats:

        if clock["turns"] >= 11:
          approxTime = "Dawn"
        elif clock["turns"] >= 9:
          approxTime = "Morning"
        elif clock["turns"] >= 7:
          approxTime = "Sunhigh"
        elif clock["turns"] >= 5:
          approxTime = "Dusk"
        elif clock["turns"] >= 3:
          approxTime = "Night"
        else:
          approxTime = "Moonhigh"
          
        cmd = input("""== %s of Day %d, Moon %d ==

        You have %d turns left. What would you like to do? (to skip this turn and rest instead, press ENTER)
        
        [A]ction = Use a turn to make an action.

        [R]est OR [enter] = Skip a turn to pass time and recover.
        
        [V]iew = View your allegiances or other Clan's stats. Does not use up one turn.

        [S]ave = Save your current game.
        
        > """ % (approxTime, clock["day"], clock["moon"], clock["turns"])).upper()

      # Action

      if cmd == "FASTTRAVEL":
        print("YOU HAVE UNLOCKED FAST TRAVEL !!!!")
        for p in list(clock):
          if "claim" in p:
            clock[p] = 0
            returnClaim(p)

      elif cmd == "SUMMONFRIEND":
        print("YOU HAVE SUMMONED A NEW FRIEND !!!!")
        genCat("player_Clan", None)

      elif cmd in ["R", ""]:
        print("You have chosen to sleep in your den for a little while. Following your lead, every cat at camp begins to rest and recover.")
        for i in clan.clans["player_Clan"].cats.copy():
          if "camp" in clan.clans["player_Clan"].cats[i].loc.lower() and (clan.clans["player_Clan"].cats[i].wp < clan.clans["player_Clan"].cats[i].stats["Willpower"]):
            clan.clans["player_Clan"].cats[i].wp += 1
        clock["turns"] -= 1
        timer()

      elif cmd == "A":
        cmd = "alfalfa"
        while not cmd in ["A", "M", "S", "E"]:

          cmd = input("""What kind of [A]ction would you like to take?

          [A]ssign = assign cats to patrols and other duties.

          [M]eeting = change group structure or cat status. [WIP]

          [S]ocial = interact with your Clanmates.

          [E]xplore = travel & do personal tasks.
          
          > """).upper()

        # Social
          
        if cmd == "S":
          menuSocial()

        elif cmd == "M":
          menuMeeting()

        # Leader
        
        elif cmd == "E":
          menuExplore()

        # Executive

        else:

          cmd = "alfalfa"

          while not cmd in ["B", "H", "C", "F", "G", "T"]:

            cmd = input("""What task would you like to assign cats to ?

            == RESOURCES ==

            [B]order = check your borders, and collect resouces
            & recruits along the way. [WIP]

            [H]unt = collect prey for the fresh-kill pile.

            == EXPANSION ==

            [C]laim = search for new territory.

            == BATTLE ==

            [F]ight = engage in battle with another Clan.

            [G]ift = give a peace offering to another Clan.

            [T]rain = prepare your cats for battle.
            
            > """).upper()

          if cmd == "H":
            actionSelect("hunt")
          
          elif cmd == "C":
            actionSelect("claim")
          
          elif cmd == "T":
            actionSelect("train")

          elif cmd == "B":
            actionSelect("patrol")
              
          elif cmd == "F":
            if len(clan.clans) > 2:
              displayTargets = []
              targets = []

              for i in clan.clans.copy():
                if not i == "player_Clan":
                  targets.append(i)
                  displayTargets.append(clan.clans[i].name)
                  
              parseOpt(displayTargets)
              target = parseSel(targets, """Who do you want to fight? You cannot choose yourself.

                  > """)

              battle("clan", target)
            else:
              print("There aren't any nearby factions to fight!")
              clock["turns"] += 1
              
          elif cmd == "G":

            id = 1
            possibles = []
            for i in clan.clans.copy():
              if not i == "player_Clan":
                print("%d : %s" % (id, clan.clans[i].name))
                possibles.append(i)
                id += 1
            correct_confirm = False
            target = "alfalfa"
            while correct_confirm == False:
              try:
                target = possibles[int(target) - 1]
                correct_confirm = True
              except:
                target = input("""Who do you want to send a gift to? You cannot choose yourself.
                
                > """)
            correct_confirm = False
            amount = "alfalfa"
            while correct_confirm == False:
              try:
                amount = int(amount)
                correct_confirm = True
              except:
                amount = input("""How much prey would you like to gift them?
                
                > """)
            clan.clans["player_Clan"].prey -= amount
            if amount <= 25:
              clan.clans[target].rep += (random.randint(0, 2))
            elif amount <= 50:
              clan.clans[target].rep += (random.randint(1, 3))
            elif amount <= 100:
              clan.clans[target].rep += (random.randint(2, 4))
            elif amount <= 175:
              clan.clans[target].rep += (random.randint(3, 5))
            elif amount <= 275:
              clan.clans[target].rep += (random.randint(4, 6))
            else:
              clan.clans[target].rep += (random.randint(5, 7))
            if clan.clans[target].rep > 5:
              clan.clans[target].rep = 5
            print("I'm sure %s really appreciates it." % clan.clans[target].name)

        clock["turns"] -= 1
        timer()
        
      elif cmd == "S":

        # set save previews

        with open('temp.dat', 'wb') as file:
          pickle.dump((
            # data to save
          clan.clans,
          disease.diseases,
          land.communer,
          land.coordinates,
          clock,
          possibleCode,
          warriorCode,
          symbols
            ), file)

        print("""
        Enter the ID of the file you would like to save your game on.
        """)

        filePreview((clan.clans, disease.diseases,
        land.communer, land.coordinates, clock,
          possibleCode,
          warriorCode, symbols))

        # select save

        save = input("> ")

        with open('temp.dat', 'rb') as file:
          (clan.clans,
          disease.diseases,
          land.communer,
          land.coordinates,
          clock,
          possibleCode,
          warriorCode,
          symbols) = pickle.load(file)

        with open("save_%s.dat" % save, 'wb') as file:
          pickle.dump((
            # data to save
          clan.clans,
          disease.diseases,
          land.communer,
          land.coordinates,
          clock,
          possibleCode,
          warriorCode,
          symbols), file)

        print("Your game has saved successfully.")

      elif cmd == "V":
        while not cmd in ["M", "O", "C", "G", "Q", "T", "W", "I"]:
          cmd = input("""What would you like to view?
          ==FACTIONS==
          [M]y Faction
          [O]ther Factions

          ==YOUR CATS==
          [C]ats
          [G]raveyard

          ==THE WORLD==
          [T]erritory Map
          [W]arrior Code
          [I]nventory
          
          > """)

          cmd = cmd.upper()
          
        if cmd == "M":
          print("""
  ===%s's Stats===

  " %s "

  Population: %d (capacity, %d)
  Feedings: %d
  Herbs: %d""" % (clan.clans["player_Clan"].name, clan.clans["player_Clan"].motto, len(clan.clans["player_Clan"].cats),
                  (20 + ((len(clan.clans["player_Clan"].location) - 5) * 2)), clan.clans["player_Clan"].prey,
                  clan.clans["player_Clan"].herbs))

          print("=Allegiances=")
          allegiances("player_Clan")
          print("=Territory=")
          currentBiomes = {}
          for x in clan.clans["player_Clan"].location:
            b = land.coordinates[x[0]][x[1]].biome
            if b in currentBiomes:
              currentBiomes[b] += 1
            else:
              currentBiomes[b] = 1
          for b in list(currentBiomes):
            print("- %s (%d controlled)" % (b, currentBiomes[b]))
        elif cmd == "C":
          id = 1
          for i in clan.clans["player_Clan"].cats.copy():
            print("%d: %s" % (id, clan.clans["player_Clan"].cats[i].name))
            id += 1
          correct_confirm = False
          cmd = "alfalfa"
          while correct_confirm == False:
            try:
              target = list(clan.clans["player_Clan"].cats)[int(cmd) - 1]
              correct_confirm = True
            except:
              cmd = input("""Which cat would you like to view? Type in their assigned ID.
              
              > """)
          print("""
  ===%s (%s)===

  " %s "

  Location: %s

  =Identity=

  Gender: %s
  Rank: %s
  Age: %d moons
  Description: %s
  Personality: %s
  Faith: %s
          """ % (clan.clans["player_Clan"].cats[target].name, clan.clans["player_Clan"].cats[target].title, clan.clans["player_Clan"].cats[target].quote,
                 clan.clans["player_Clan"].cats[target].loc, clan.clans["player_Clan"].cats[target].pronoun, clan.clans["player_Clan"].cats[target].rank, clan.clans["player_Clan"].cats[target].age,
                 clan.clans["player_Clan"].cats[target].description, ", ".join(clan.clans["player_Clan"].cats[target].personality), clan.clans["player_Clan"].cats[target].faith))
          print("=Stats [LVL %d (%d xp)]" % (clan.clans["player_Clan"].cats[target].lvl, clan.clans["player_Clan"].cats[target].xp,))
          if len(clan.clans["player_Clan"].cats[target].scars) > 0:
            print("Scars-")
            for i in clan.clans["player_Clan"].cats[target].scars:
              print("* %s" % i)
          if len(clan.clans["player_Clan"].cats[target].mutations) > 0:
            print("Mutations-")
            for i in clan.clans["player_Clan"].cats[target].mutations:
              print("* %s" % i)
          if len(clan.clans["player_Clan"].cats[target].disabilities) > 0:
            print("Disabilities-")
            for i in clan.clans["player_Clan"].cats[target].disabilities:
              print("* %s" % i)
          print("""

  %d/%d WP (willpower)
  %d STR (strength)
  %d TGH (toughness)
  %d SPD (speed)
  %d PRS (precision)
  %d CHA (charisma)
          """ % (clan.clans["player_Clan"].cats[target].wp, clan.clans["player_Clan"].cats[target].stats["Willpower"], clan.clans["player_Clan"].cats[target].stats["Strength"],
                 clan.clans["player_Clan"].cats[target].stats["Toughness"], clan.clans["player_Clan"].cats[target].stats["Speed"], clan.clans["player_Clan"].cats[target].stats["Precision"],
                 clan.clans["player_Clan"].cats[target].stats["Charisma"]))
          print("=Relationships=")
          
          for r in list(clan.clans["player_Clan"].cats[target].relationships):
            for x in list(clan.clans):
              if r in clan.clans[x].cats:
                print("%s - %s" % (clan.clans[x].cats[r].name, clan.clans["player_Clan"].cats[target].relationships[r][0]))
                break
          print("=Item Preferences=")
          if not clan.clans["player_Clan"].cats[target].found_favourite == "":
            print("Favourite: %s" % clan.clans["player_Clan"].cats[target].found_favourite)
          if len(clan.clans["player_Clan"].cats[target].found_likes) > 0:
            print("Likes-")
            for i in clan.clans["player_Clan"].cats[target].found_likes:
              print("* %s" % i)
          
          print("NOTE : If you came here looking for a cat reference, those are under maintenance. You will be able to access new and improved references in an upcoming update.")

        elif cmd == "O":
          id = 1
          for i in clan.clans.copy():
            if not i == "player_Clan":
              print("%d: %s" % (id, clan.clans[i].name))
              id += 1
          correct_confirm = False
          cmd = "alfalfa"
          while correct_confirm == False:
            try:
              target = list(clan.clans)[int(cmd)]
              correct_confirm = True
            except:
              cmd = input("""Which Clan would you like to view? Enter their ID.
              
              > """)
          print("""
  ===%s's Stats===

  " %s "
  """ % (clan.clans[target].name, clan.clans[target].motto))
          if clan.clans[target].rep <= -3:
            print("Status: Hates %s" % clan.clans["player_Clan"].name)
          elif clan.clans[target].rep < 0:
            print("Status: Dislikes %s" % clan.clans["player_Clan"].name)
          elif clan.clans[target].rep == 0:
            print("Status: Indifferent About %s" % clan.clans["player_Clan"].name)
          elif clan.clans[target].rep < 4:
            print("Status: Likes %s" % clan.clans["player_Clan"].name)
          else:
            print("Status: Allies With %s" % clan.clans["player_Clan"].name)
          print("=Allegiances=")
          allegiances(target)
          print("=Territory=")
          currentBiomes = {}
          for x in clan.clans[target].location:
            b = land.coordinates[x[0]][x[1]].biome
            if b in currentBiomes:
              currentBiomes[b] += 1
            else:
              currentBiomes[b] = 1
          for b in list(currentBiomes):
            print("- %s (%d controlled)" % (b, currentBiomes[b]))
        elif cmd == "T":

          # Generate map

          y, target = seeMap(None)
          
          if not target == None:

                    
            print("""
    ===%s===

    Biome : %s

    """ % (land.coordinates[y][target].name, land.coordinates[y][target].biome))

            print("- Prey -")
            print("")

            if len(list(land.coordinates[y][target].prey)) == 0:
              print("There are no huntable prey in this territory.")
            else:
              for p in list(land.coordinates[y][target].prey):
                print("- %s" % p)
            print("")
            print("- Plantlife -")
            print("")
            if len(list(land.coordinates[y][target].plants)) == 0:
              print("There are no forageable plants in this territory.")
            else:
              for p in list(land.coordinates[y][target].plants):
                print("- %s" % p)
            print("")
            print("- Predators -")
            print("")
            if len(list(land.coordinates[y][target].predators)) == 0:
              print("There are no hostile predators in this territory.")
            else:
              for p in list(land.coordinates[y][target].predators):
                print("- %s" % p)
                
            rename = input("""
      If you would like to rename this territory, enter [R]. Press enter to close this and return to the actions menu.

      > """).lower()

            if rename == "r":
              newName = input("""
        What would you like to name this territory?

        > """)

              land.coordinates[y][target].name = newName

              print("This %s is now known as %s." % (land.coordinates[y][target].biome, land.coordinates[y][target].name))

        elif cmd == "W":
          id = 1
          if len(warriorCode) > 0:
            for i in warriorCode:
              print("Rule %d: %s" % (id, i))
              id += 1
          else:
            print("There are no rules in the Warrior Code! ANARCHY!")
        elif cmd == "I":
          inven_count = 0
          for i in list(clan.clans["player_Clan"].inv):
            if clan.clans["player_Clan"].inv[i] > 0:
              print("%s : %d" % (i, clan.clans["player_Clan"].inv[i]))
              inven_count += 1
          if inven_count == 0:
            print("You don't have any items. Try foraging?")
        elif cmd == "H":
          print("===HISTORY OF THE CLANS===")
          print("Sorry, the Clan history log hasn't been implemented yet ! Come back another update ?")
        elif cmd == "G":
          print("Sorry, the Graveyard is still under development!")

    if clock["turns"] <= 0:
      
      # insert a day summary here ?

      # note : set cat's pregnancy meter to 720 turns, meaning they give birth in around 60 days

      # random events can happen at any turn, though Gatherings will ALWAYS happen at the end of each moon
      # ( you can always arrange meetings very easily between that time, but they will cost turns - Gatherings are free )

      # include in day summary patrols sent, changes in allegiances, and other Clan's shenanigans along with any random events experienced in the day
      
      input("It's time to rest now ... Press enter to proceed to the next day.")
      
      clock["turns"] = 12
      clock["day"] += 1

      if clock["day"] == 30:
        clock["day"] = 1
        clock["moon"] += 1
        
      print("")
      print("=== Daily Report ===")

      daily()
      
      print("")
      print("=== Allegiances ===")
      print("")
        
      allegiances("player_Clan")
      
      print("")
      print("===================")
      print("")
