import random
from entity.map import autoClaim, seeMap

def menuExplore(turns):
  
  # Define globals

  global folder

  for i in clan.clans["player_Clan"].cats.copy():
    if clan.clans["player_Clan"].cats[i].rank == "leader":
      leader = i
      break

  # Start
  
  if turns >= 1:
    cmd = "alfalfa"
    while not cmd in ["B", "E", "G"]:
      cmd = input("""What would you like to do, now that you've left camp?

      [E]xplore = Take a walk around the wilderness.

      [G]arden = Care for the local wildlife.

      ---

      (SHORTCUT - TO BE REMOVED) [B]ackway Bazaar = Trade with the local outsiders.

      (SHORTCUT - TO BE REMOVED) [M][communer sans M] = Visit the [communer] and communicate with StarClan.
      
      > """).upper()

    # Explore
      
    if cmd == "E":

      explorey, explorex = seeMap(None)

      finished = False

      while finished == False and turns > 0:
        cmd = "alfalfa"

        while not cmd in ["B", "F", "E"]:
        
          cmd = input("""
          You have %d turns left. What would you like to do at the %s?

          [B]irdwatch = Find & capture birds for the aviary.

          [F]orage = Scrounge the territory for useful items.

          [E]xit = End your exploration. You can always come back and check out a different territory.""" %
                      (turns,
                      land.coordinates[explorey][explorex].name)).upper()

        # Exit

        if cmd == "E":
          finished = True

        # Birdwatch
        
        elif cmd == "B":
          bird_count = (random.randint(1, 10))
          birds = {}
          id = 1
          print("During your birdwatching session, you spy the following birds ...")

          # Generate birds
          
          for i in range(bird_count):
            var_name = ""
            for i in range(random.randint(5, 15)):
              var_name = var_name + (random.choice(codebits))
            birds[var_name] = bird("Unnamed", (random.choice(personality_traits)), "", "", "", 0, {"Willpower" : 0, "Precision" : 0, "Speed" : 0})
            
            rando = (random.randint(0, 100))
            while birds[var_name].species == "":
              species = (random.choice(list(bird_species)))
              if bird_species[species]["chance"] >= rando:
                birds[var_name].species = species

            rando = (random.randint(0, 100))
            while birds[var_name].colour == "":
              colour = (random.randint(0, 2))
              if colour == 0:
                birds[var_name].colour = bird_species[species]["colours"][colour]
              elif colour == 1 and rando <= 50:
                birds[var_name].colour = bird_species[species]["colours"][colour]
              elif colour == 2 and rando <= 25:
                birds[var_name].colour = bird_species[species]["colours"][colour]

            rarity = colour
            if bird_species[species]["chance"] == 100:
              rarity += 1
            elif bird_species[species]["chance"] == 50:
              rarity += 2
            else:
              rarity += 3

            for i in range(rarity):
              birds[var_name].rarity = birds[var_name].rarity + "*"
              rando = (random.randint(1, 3))
              if rando == 1:
                birds[var_name].stats["Willpower"] += (random.randint(1, 3))
              elif rando == 2:
                birds[var_name].stats["Precision"] += (random.randint(1, 3))
              else:
                birds[var_name].stats["Speed"] += (random.randint(1, 3))

            # Display birdwatch results
              
            print("[%d] A(n) %s %s (%s)" % (id, birds[var_name].colour, birds[var_name].species, birds[var_name].rarity))

            id += 1

          target = "alfalfa"

          target = input("""If you would like to attempt to capture any one of these birds, enter their ID below. If not, say 'NO'.

                        > """)
            
          try:

            target = list(birds)[int(target) - 1]

          except:

            target = input("""If you would like to attempt to capture any one of these birds, enter their ID below. If not, say 'NO'.

                          > """)

          # Attempt capture

          if target in list(birds):

            catskill = clan.clans["player_Clan"].cats[leader].stats["Precision"] + clan.clans["player_Clan"].cats[leader].stats["Speed"]

            birdskill = birds[var_name].stats["Precision"] + birds[var_name].stats["Speed"]

            # Capture fail

            if birdskill > catskill:
              print("You failed to capture the %s %s!" % (birds[target].colour, birds[target].species))

            # Capture success

            else:
  
              while not cmd in ["k", "r", "t"]:

                  cmd = input("""You have successfully captured a(n) %s %s (%s)! What would you like to do with it?

                  [K]ill = kill the bird for prey

                  [R]elease = let the bird back out into the wild

                  [T]ame = attempt to befriend the bird

                  > """ % (birds[target].colour, birds[target].species, birds[target].rarity)).lower()

                  # Kill

                  if cmd == "k":

                    print("You successfully killed the %s %s for %d prey!" % (birds[target].colour, birds[target].species, len(birds[target].rarity)))

                    clan.clans["player_Clan"].prey += len(birds[target].rarity)

                  # Release

                  elif cmd == "r":

                    print("The %s %s gratefully flies away." % (birds[target].colour, birds[target].species))

                  # Tame

                  elif cmd == "t":

                    print("You successfully tamed the %s %s. It has been sent to your Clan's Aviary." % (birds[target].colour, birds[target].species))

                    folder.folders["aviary"].contents[target] = birds[target]

                  clan.clans["player_Clan"].cats[leader].xp += len(birds[target].rarity)

                  print("You have earned %d xp from the encounter !" % (len(birds[target].rarity)))
                  
            turns -= 1

        # Forage
                  
        elif cmd == "F":
          
          forage_amount = (random.randint(0, 5))
          if forage_amount == 0:
            print("You looked around, but couldn't find anything of note.")
          else:
            for i in range(forage_amount):
              if not land.coordinates[explorey][explorex].landmark == None:
                item = (random.choice(folder.folders["landmark_items"].contents[land.coordinates[explorey][explorex].landmark]))
              else:
                item = random.choice(["Prey Leftovers", "Medicinal Herb"])
              print("You found: %s!" % item)
              if item == "Medicinal Herb":
                clan.clans["player_Clan"].herbs += 1
              elif "Leftovers" in item:
                clan.clans["player_Clan"].prey += 1
              else:
                folder.folders["inventory"].contents[item] += 1

          turns -= 1

    # Backway Bazaar
              
    elif cmd == "B":
      cmd = "alfalfa"
      while not cmd in ["E", "J", "L", "M"]:
        cmd = input("""Welcome to the Backway Bazaar, an alleyway hidden from prying eyes that is bustling with activity!
                       For a small fee you can trade prey for items, herbs, or even a new identity... why don't you take a look around?

        [E]ddie the Kittypet

        [J]ay the Healer
        
        [L]iz the Banker

        [M]erchant Hall
        
        """).upper()

      # Eddie
      
      if cmd == "E":
        purchased = False
        
        while purchased == False:
          cmd = "alfalfa"
          while not cmd == "I" and not cmd == "G" and not cmd == "A" and not cmd == "S" and not cmd == "R" and not cmd == "N":
            cmd = input("""
            [Eddie] : "Hey hey hey, my Clan friend! My name's Eddie, but you may call 
            me whatever you'd like. My shop's a bit of a catch-all for things you
            can't really do anywhere else ... yet. Keep an eye out for changes to the shop,
            as that usually means something new somewhere else is coming !"

            [S]tat Reset - 10 prey

            [I]dentity (name or gender) - 20 prey

            [R]eputation Booster - 150 prey

            ---> [N]evermind
            
            > """)
            cmd = cmd.upper()

          # Identity
          
          if cmd == "I":
            if clan.clans["player_Clan"].prey < 20:
              print("""
              [Eddie] : "Sorry, my-buddy-my-pal, but it appears you're a bit poor on the prey end. Come back when you have more, uh-huh?" """)
            else:
              clan.clans["player_Clan"].prey -= 20
              cmd = "alfalfa"
              conf = False
              while conf == False:
                id = 1
                for i in clan.clans["player_Clan"].cats.copy():
                  print("""
                  [%d] %s|%s
                  Gender: %s

                  -----
                  """ % (id, clan.clans["player_Clan"].cats[i].prefix, clan.clans["player_Clan"].cats[i].suffix,
                         clan.clans["player_Clan"].cats[i].pronoun))

                  id += 1
                try:
                  target = list(clan.clans["player_Clan"].cats)[int(cmd) - 1]
                  conf = True
                except:
                  cmd = input("""
                  [Eddie] : "Oh, excellent! Who's gonna be the benefactor of my services? Please enter their ID listed above."

                  > """)
              cmd = "alfalfa"
              while not cmd == "P" and not cmd == "S" and not cmd == "G" and not cmd == "C" and not cmd == "E":
                cmd = input("""
                ===%s|%s===
                Gender: %s

                [Eddie] : "Great, great! Now what'd you like me to change about them?"

                [P]refix
                [S]uffix
                [G]ender

                
                > """ % (clan.clans["player_Clan"].cats[target].prefix,
                         clan.clans["player_Clan"].cats[target].suffix,
                         clan.clans["player_Clan"].cats[target].pronoun,))

                cmd = cmd.upper()

              # Prefix
              
              if cmd == "P":
                prefix = input("""
                [Eddie] : "What should I change their prefix to?" 
                
                > """)

                clan.clans["player_Clan"].cats[target].prefix = prefix
                clan.clans["player_Clan"].cats[target].name = clan.clans["player_Clan"].cats[target].prefix + clan.clans["player_Clan"].cats[target].suffix
                print("""
                [Eddie] : "Excellent, their name is now %s!" """ % clan.clans["player_Clan"].cats[target].name)

              # Suffix
              
              elif cmd == "S":
                suffix = input("""
                [Eddie] : "What should I change their suffix to?" 
                
                > """)

                clan.clans["player_Clan"].cats[target].suffix = suffix
                clan.clans["player_Clan"].cats[target].name = clan.clans["player_Clan"].cats[target].prefix + clan.clans["player_Clan"].cats[target].suffix
                print("""
                [Eddie] : "Excellent, their name is now %s!" """ % clan.clans["player_Clan"].cats[target].name)

              # Gender
              
              elif cmd == "G":
                gender = input("""
                [Eddie] : "What should I change their gender to?" 
                
                > """)

                clan.clans["player_Clan"].cats[target].pronoun = gender
                if "with" in clan.clans["player_Clan"].cats[target].pattern:
                  description = ("%s and %s %s %s%s and %s eyes" % (clan.clans["player_Clan"].cats[target].size,
                                                                    clan.clans["player_Clan"].cats[target].build,
                                                                    clan.clans["player_Clan"].cats[target].coat,
                                                                    clan.clans["player_Clan"].cats[target].pronoun,
                                                                    clan.clans["player_Clan"].cats[target].pattern,
                                                                    clan.clans["player_Clan"].cats[target].eyes))
                else:
                  description = ("%s and %s %s%s %s with %s eyes" % (clan.clans["player_Clan"].cats[target].size,
                                                                     clan.clans["player_Clan"].cats[target].build,
                                                                     clan.clans["player_Clan"].cats[target].coat,
                                                                     clan.clans["player_Clan"].cats[target].pattern,
                                                                     clan.clans["player_Clan"].cats[target].pronoun,
                                                                     clan.clans["player_Clan"].cats[target].eyes))
                clan.clans["player_Clan"].cats[target].description = description
                print("""
                [Eddie] : "Excellent, they are now a %s!" """ % clan.clans["player_Clan"].cats[target].pronoun)

          # Stat Reset
          
          elif cmd == "S":
            if clan.clans["player_Clan"].prey < 75:
              print("""
              [Eddie] : "Sorry, my-buddy-my-pal, but it appears you're a bit poor on the prey end. Come back when you have more, uh-huh?" """)
            else:
              clan.clans["player_Clan"].prey -= 75
              conf = False
              cmd = "alfalfa"
              while conf == False:
                id = 1
                for i in clan.clans["player_Clan"].cats.copy():
                  print("""
                  [%d] %s - LVL %d
                  WP %d | STR %d | TGH %d | SPD %d | PRS %d | CHA %d
                  -----
                  """ % (id, clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].lvl,
                         clan.clans["player_Clan"].cats[i].stats["Willpower"],
                         clan.clans["player_Clan"].cats[i].stats["Strength"], clan.clans["player_Clan"].cats[i].stats["Toughness"],
                         clan.clans["player_Clan"].cats[i].stats["Speed"], clan.clans["player_Clan"].cats[i].stats["Precision"],
                         clan.clans["player_Clan"].cats[i].stats["Charisma"]))

                  id += 1
                try:
                  target = list(clan.clans["player_Clan"].cats)[int(cmd) - 1]
                  conf = True
                except:
                  cmd = input("""
                  [Eddie] : "Oh, excellent! Who's gonna be the benefactor of my services? Please enter their ID listed above."

                  > """)

              for i in clan.clans["player_Clan"].cats[target].stats.copy():
                if not i == "Willpower":
                  clan.clans["player_Clan"].cats[target].stats[i] = 1
                else:
                  clan.clans["player_Clan"].cats[target].stats[i] = 5
              
              points = clan.clans["player_Clan"].cats[target].lvl * 5
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
                    """ % (clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].lvl,
                           clan.clans["player_Clan"].cats[i].xp,
                           clan.clans["player_Clan"].cats[i].wp, clan.clans["player_Clan"].cats[i].stats["Willpower"],
                           clan.clans["player_Clan"].cats[i].stats["Strength"],
                           clan.clans["player_Clan"].cats[i].stats["Toughness"], clan.clans["player_Clan"].cats[i].stats["Speed"],
                           clan.clans["player_Clan"].cats[i].stats["Precision"], clan.clans["player_Clan"].cats[i].stats["Charisma"], points))

          # Reputation booster
          
          elif cmd == "R":
            if clan.clans["player_Clan"].prey < 150:
              print("""
              [Eddie] : "Sorry, my-buddy-my-pal, but it appears you're a bit poor on the prey end. Come back when you have more, uh-huh?" """)
            else:
              clan.clans["player_Clan"].prey -= 150
              for i in clan.clans["player_Clan"].cats.copy():
                clan.clans["player_Clan"].cats[i].rep += (random.randint(0, 5))
              print("""
              [Eddie] : "Okay, so I went around your Clan camp 'n' put some good words in for you, buddy! So, uh, you should find the 'social' aspect of Clan-running to be a tad easier now."
              """)
          elif cmd == "N":
            print("""
            [Eddie] : "See ya, then!"
            """)

            purchased = True

      # Jay
      
      elif cmd == "J": 
        price = (random.randint(1, 10))
        while not cmd == "Y" and not cmd == "N":
          cmd = input("""
          [Jay] : "Oi, Clan cat. I sell all kinds'a medicinal stuff here ... well,
          that's a lie, I just sell herbs. But in the future there might be more ... so
          keep an eye open if you got prey to fork over.
          
          That said, the current price per herb is %d prey. Do you wanna buy?"

          [Y/N]
          
          > """ % price)
          cmd = cmd.upper()
        if cmd == "Y":
          amt = "alfalfa"
          conf = False
          while conf == False:
            try:
              if (price * int(amt)) > clan.clans["player_Clan"].prey:
                print("""
                [Jay] : "Oi, what is it yer tryna pull? You can't afford these herbs! You tryna rip me off or somethin- think I'm stupid?!" """)
              else:
                clan.clans["player_Clan"].prey -= (price * int(amt))
                clan.clans["player_Clan"].herbs += int(amt)
                print("""
                [Jay] : "Here ya go. Have a day." """)
              conf = True
            except:
              amt = input("""
              [Jay] : "How many herbs we talkin' here? Don't worry about stock, I can get more in a flash if you order more than I got on me." 
              
              > """)
        else:
          print("""
          [Jay] : "Suuuure, dude. Just hold up the line for everyone else and *not* buy anything. You Clan cats are all the same... come back when you're going to actually buy something." """)
          purchased = True

      # Liz

      elif cmd == "L":
        cmd = "alfalfa"

        purchased = False

        while purchased == False:

          while not cmd in ["W", "D", "E"]:

            print("""

            [Liz] : "... huh? Oh, hi, customer! Welcome to the Backway Bank.
            We keep your prey, herbs, and items all safe in case of emergency.
            What would you like to do?"

            -- Contents --
            
            """)

            id = 1
            for i in folder.folders["bank"].contents.copy():
              if not i == "bank_level":
                print("[%d] %s: %d" % (id, i, folder.folders["bank"].contents[i]))
                id += 1

            cmd = input("""

            [W]ithdraw

            [D]eposit

            [E]xit

            > """).upper()
    
          # Set action

          if cmd == "E":
            conf = True
            action = "exit"
          elif cmd == "W":
            action = "withdraw"
          else:
            action = "deposit"
              
          cmd = "alfalfa"
          conf = False

          # Select

          while conf == False:
            try:
              target = list(folder.folders["bank"].contents)[int(cmd)]
              conf = True
            except:
              cmd = input("""

            [Liz] : Enter the ID of the item you'd like to %s.

            > """ % action)

          # Withdraw
          
          if action == "withdraw":
            if folder.folders["bank"].contents[target] > 0:
              amt = "alfalfa"
              conf = False
              while conf == False:
                try: 
                  if int(amt) > folder.folders["bank"].contents[target]:
                    amt = folder.folders["bank"].contents[target]

                  if target == "Prey":
                    clan.clans["player_Clan"].prey += amt
                    folder.folders["bank"].contents[target] -= amt

                    print("""[Liz] : "...enjoy your %d prey... have a good day." """ % amt)
                  elif target == "Herbs":
                    clan.clans["player_Clan"].herbs += amt
                    folder.folders["bank"].contents[target] -= amt

                    print("""[Liz] : "...enjoy your %d herbs... have a good day." """ % amt)
                  else:
                    folder.folders["inventory"].contents[target] += amt
                    folder.folders["bank"].contents[target] -= amt

                    print("""[Liz] : "...enjoy your %d %s... have a good day." """ % (amt, target))
                  
                  conf = True
                  purchased = True

                except:
                  amt = input("""
                  [Liz] "Sure... how much are you taking out? You have %d %s."
                  
                  > """ % (folder.folders["bank"].contents[target], target))

              
            else:
              print("""[Liz] : "Oh... it looks like you don't have any %s to withdraw." """ % target)

          # Deposit

          elif action == "deposit":
            if folder.folders["bank"].contents[target] == limit:
              amt = "alfalfa"
              conf = False
              while conf == False:
                try: 
                  if int(amt) > limit:
                    amt = folder.folders["bank"].contents[target]
                    print("""[Liz] : "Uh, it doesn't look like we have enough room for %d %s, so I rounded down to %d..." """)

                  if target == "Prey":
                    clan.clans["player_Clan"].prey += amt
                    folder.folders["bank"].contents[target] -= amt

                    print("""[Liz] : "...%d prey has been deposited... have a good day." """ % amt)
                  elif target == "Herbs":
                    clan.clans["player_Clan"].herbs += amt
                    folder.folders["bank"].contents[target] -= amt

                    print("""[Liz] : "...%s herbs has been deposited... have a good day." """ % amt)
                  else:
                    folder.folders["inventory"].contents[target] += amt
                    folder.folders["bank"].contents[target] -= amt

                    print("""[Liz] : "...%d %s has been deposited... have a good day." """ % (amt, target))
                  
                  conf = True
                  purchased = True

                except:
                  amt = input("""
                  [Liz] "Sure... how much are you taking out? You have %d %s."
                  
                  > """ % (folder.folders["bank"].contents[target], target))

              
            else:
              print("""[Liz] : "Oh... it looks like you have reached the %s cap, which is %d." """ % (target, limit))

          # Exit

          else:
            print("""[Liz] : "Come again!" """)

      # Merchant Hall

      elif cmd == "M":
        id = 1
        for i in folder.folders["merchants"].contents.copy():
          print("[%d] %s (wares: %s)" % (id, folder.folders["merchants"].contents[i].name,
                                         ", ".join(list(folder.folders["merchants"].contents[i].inventory))))
          id += 1
        cmd = "alfalfa"
        conf = False
        while conf == False:
          try:
            target = list(folder.folders["merchants"].contents)[int(cmd) - 1]
            conf = True
          except:
            cmd = input("""
            Which merchant would you like to visit? Please enter their ID.
            
            > """)

        purchased = False
        while purchased == False:
          print("""
          [%s] : "Hello, hello! Please examine my wares, and tell me what you'd like to purchase by entering the item's ID! If you don't wish to buy anything, just say 'no' or 'bye'!"
          """ % folder.folders["merchants"].contents[target].name)

          id = 1

          for i in folder.folders["merchants"].contents[target].inventory:
            print("""[%d] %s (price : %d prey) (stock : %s)
                  """ % (id, i, folder.folders["merchants"].contents[target].inventory[i]["price"],
                                                              folder.folders["merchants"].contents[target].inventory[i]["stock"]))

          cmd = input("> ")

          try:
            cmd = int(cmd)
            item = list(folder.folders["merchants"].contents[target].inventory)[cmd]
            
            if folder.folders["merchants"].contents[target].inventory[item]["stock"] < 1:
              print("""
              [%s] : "Oops, looks like we're fresh out of stock." """ % folder.folders["merchants"].contents[target].name)
            else:
              amt = "alfalfa"
              try:
                if int(amt) > folder.folders["merchants"].contents[target].stock_1:
                  print("""
                  [%s] : "I don't have enough of that item, I'm afraid." """ % folder.folders["merchants"].contents[target].name)
                elif folder.folders["merchants"].contents[target].inventory[item]["price"] * int(amt) > clan.clans["player_Clan"].prey:
                  print("""
                  [%s] : "It seems you can't afford this item. Come back when you can." """ % folder.folders["merchants"].contents[target].name)
                else:
                  folder.folders["merchants"].contents[target].inventory[item]["stock"] -= int(amt)
                  folder.folders["inventory"].contents[item] += int(amt)
                  clan.clans["player_Clan"].prey -= folder.folders["merchants"].contents[target].inventory[item]["price"] * int(amt)
                  print("""
                  [%s] : "Thank you so very much for your purchase!" """ % folder.folders["merchants"].contents[target].name)
                  purchased = True
              except:
                amt = input("""
                [%s] : "How many do you wish to purchase?"
                
                > """ % folder.folders["merchants"].contents[target].name)
          except:
            print("""
            [%s] : "Have a wonderful day!" """ % folder.folders["merchants"].contents[target].name)
            purchased = True
              
    # Garden

    elif cmd == "G":
      cmd = "alfalfa"
      while not cmd in ["A"]:
        cmd = input("""Welcome to the Clan garden, where you can
        care for any plants and animals your Clan has tamed or cultivated.
        
        [A]viary = where befriended birds are held. [WIP]
        
        > """).upper()

      # Aviary

      if cmd == "A":
        if len(folder.folders["aviary"].contents) == 0:
          print("The Clan aviary is empty! You can populate it by capturing birds you see while [B]irdwatching, which can be accessed via the [E]xplore menu.")
        else:

          # List birds
          
          id = 0
          for b in list(folder.folders["aviary"].contents):
            id += 1
            print("[%d] %s (%s %s - %s)" % (id, folder.folders["aviary"].contents[b].name, folder.folders["aviary"].contents[b].colour, folder.folders["aviary"].contents[b].species, folder.folders["aviary"].contents[b].rarity))

          target = "alfalfa"
          conf == False

          # Select bird

          while conf == False:
            try:
              target = list(folder.folders["aviary"].contents)[int(target) - 1]
            except:
              target = input("""Which bird would you like to select? Enter its ID number.

              > """)

          # View bird

          print("""

          === %s ===

          Personality : %s

          Species : %s (%s)

          = STATS =

          WP : %d / %d

          Precision : %d

          Speed : %d """ % (folder.folders["aviary"].contents[target].name,
                             folder.folders["aviary"].contents[target].personality,
                             folder.folders["aviary"].contents[target].species,
                             folder.folders["aviary"].contents[target].rarity,
                             folder.folders["aviary"].contents[target].wp,
                             folder.folders["aviary"].contents[target].stats["Willpower"],
                             folder.folders["aviary"].contents[target].stats["Precision"],
                             folder.folders["aviary"].contents[target].stats["Speed"],))

          target = list(folder.folders["aviary"].contents)[int(target)]
          while not cmd in ["R", "NO"]:
            cmd = input("""

            What would you like to do with %s? If you would not like to do anything, enter 'NO'.

            [R]ename = give the bird a name.

            > """ % folder.folders["aviary"].contents[target].colour)

            cmd = cmd.upper()

          # Rename

          if cmd == "R":
            
            name = input("""What would you like to name your %s %s?

            > """ % (folder.folders["aviary"].contents[target].colour, folder.folders["aviary"].contents[target].species))

            folder.folders["aviary"].contents[b].name = name

            print("Your %s %s is now named %s!" % (folder.folders["aviary"].contents[target].colour, folder.folders["aviary"].contents[target].species, folder.folders["aviary"].contents[target].name))
                
  else:
    print("You don't have the energy to go anywhere. You should wait a little while.")
    
  return turns
