from entity.clan import clan
from entity.cat import cat
from data.clock import clock
import random

def menuSocial():

  # Start

  for i in clan.clans["player_Clan"].cats.copy():
    if clan.clans["player_Clan"].cats[i].rank == "leader":
      leader = i
      break
  
  if clan.clans["player_Clan"].cats[leader].loc == ("%s quarantine" % clan.clans["player_Clan"].name):
    print("You cannot socialize with cats while in quarantine!")
  else:  
    if clock["turns"] >= 1:
        cmd = 0
        while not cmd in ["A", "O", "C", "G", "F", "E", "P", "K", "R", "B", "I", "S"]:
          id = 1
          possibles = []

          # Display cats
          
          for i in clan.clans["player_Clan"].cats.copy():
            if not i == leader and clan.clans["player_Clan"].cats[i].loc == "%s camp" % clan.clans["player_Clan"].name:
              print("%d: %s (%d)" % (id, clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].rep))
              id += 1
              possibles.append(i)
          correct_confirm = False
          cmd = "alfalfa"

          # Select cat
          
          while correct_confirm == False:
            try:
                target = possibles[int(cmd) - 1]
                correct_confirm = True
            except:
                cmd = input("""Which cat would you like to interact with? Type in their assigned ID.
                
                > """)

          # Special actions

          if clan.clans["player_Clan"].cats[target].age >= 12:
            isGrown = "[A]sk for Advice = Request advice."
          else:
            isGrown = "[O]ffer Advice = Give guidance."

          if target in clan.clans["player_Clan"].cats[leader].relationships:
            if clan.clans["player_Clan"].cats[leader].relationships[target][0] == "mate":
              action2 = "[S]nuggle = have a cuddle puddle with your mate/kit"
              action = "[B]reak Up = End your relationship"
            elif clan.clans["player_Clan"].cats[leader].relationships[target][0] in ["mother", "father", "parent"]:
              action2 = "[S]nuggle = have a cuddle puddle with your mate/kit"
              action = ""
            else:
              action2 = ""
              action = "[P]ropose = Try to become mates"
          else:
            action = ""
            action2 = ""
            clan.clans["player_Clan"].cats[target].relationships[leader] = ["%smate" % clan.clans["player_Clan"].noun, 0]
            

          if True in clan.clans["player_Clan"].events["traitor"] or True in clan.clans["player_Clan"].events["disease"]:
            event = "[I]nvestigate"
          else:
            event = ""

          # Select action

          cmd = input("""What action would you like to do with %s?

          %s
          
          [C]hat = Make small talk.

          [G]ift = Give them something special.

          [F]ight = Challenge them to a duel.
          
          %s

          %s
          
          [K]its = Try to have kits.

          %s
          
          > """ % (clan.clans["player_Clan"].cats[target].name, isGrown, action, action2, event))

          cmd = cmd.upper()

        if cmd in ["A", "O"]:
          print("This command is still in the works! Come back later!")

          if cmd == "O":
            advice = input("""What would you like to advise %s on?

          [1] Faith

          [2] Courage

          [3] Persevereance

          [4] Wisdom

          [5] Awareness

          [6] Wit

          > """)

            success = clan.clans["player_Clan"].cats[target].stats["Charisma"] + clan.clans["player_Clan"].cats[leader].stats["Charisma"]

            rando = (random.randint(1, 20))
            if rando < (success):
              print("%s took what you said to heart. They seem a lot more confident now.")
              if advice == "1":
                clan.clans["player_Clan"].cats[target].stats["Willpower"] += 5
              elif advice == "2":
                clan.clans["player_Clan"].cats[target].stats["Strength"] += 1
              elif advice == "3":
                clan.clans["player_Clan"].cats[target].stats["Toughness"] += 1
              elif advice == "4":
                clan.clans["player_Clan"].cats[target].stats["Precision"] += 1
              elif advice == "5":
                clan.clans["player_Clan"].cats[target].stats["Speed"] += 1
              elif advice == "6":
                clan.clans["player_Clan"].cats[target].stats["Charisma"] += 1
            else:
              print("%s listened, but didn't seem to absorb much of it. Oh well.")
          else:
            possibleAdvice = []
            if (clan.clans["player_Clan"].prey * 2) < len(list(clan.clans["player_Clan"].cats)):
              possibleAdvice.append("""The fresh-kill pile could use some restocking. Remember- each cat only needs one feeding,
                                       but the more prey there is, the more WP they may recover.
                                       Having twice as many prey as you have cats is a good way of going about it.""")
            if (len(list(clan.clans["player_Clan"].cats)) * 2) < len(list(clan.clans["player_Clan"].location)):
              possibleAdvice.append("""A strong %s is one with plenty of cats to defend and care for it. You can recruit more
                                       cats by sending [B]order patrols with the goal of finding allies.""" % clan.clans["player_Clan"].noun)
            else:
              possibleAdvice.append("""We need to begin expanding our borders. [E]xploratory patrols allow you to send a
                                       search party to scout for suitable land. Be sure to send healthy, strong cats--
                                       exploratory patrols are long and far more dangerous than patrols within our own
                                       borders.""")

            if len(possibleAdvice) < 4:
              while len(possibleAdvice) < 4:
                miniAdvice = ["""WP stands for Willpower, or how long a cat can carry on before succumbing. Cats regenerate
                                   WP naturally when they are not 'active' a.k.a not on patrol. The more excess prey in the
                                   fresh-kill pile, the more they will regenerate at the start of each day. In battle,
                                   [R]est can also give a handful of WP.""",
                              """STR stands for Strength, and it is the primary indicator for damage dealt in battle. As it isn't
                                   used much outside of battle, I recommend giving just a few of your cats-- your designated fighters--
                                   a bunch of STR, and applying the stat minimally to your more peaceful members.""",
                              """TGH stands for Toughness, and while it's useful for mitigating damage in battle, it also helps cats
                                   survive difficult situations such as disaster, disease, and potentially fatal accidents. To prevent
                                   future heartbreak, I recommend developing plenty of TGH in cats you really care about-- mates, kits,
                                   and potential heirs.""",
                              """PRS stands for Precision, which is one of the most vital tools a cat can have. It influences
                                   a cat's accuracy and dexterity when doing tasks like hunting, healing, or fighting. There is
                                   a cap to PRS effectiveness, though, and to get the most out of a cat's stats I recommend
                                   ensuring that the cat's PRS is at or 1-2 points above their level.""",
                              """SPD stands for Speed, an important consideration for cats who will spend a lot of time out
                                   of camp. Not only is it the primary stat (along with PRS) used in hunting, but it is also
                                   used to help cats flee dangerous situations. My recommendation is to focus on SPD when a
                                   cat is very young, and less effective in battle, so they may protect themselves long
                                   enough to get stronger later on.""",
                              """CHA stands for Charisma, or a cat's social skill. This is the MOST important trait you, as our leader,
                                   can have, but other cats can get good use out of it, too. The higher a cat's CHA, the more
                                   successful both social interactions initiated by or with them will be. It can also save their
                                   pelt in battle by persuading rivals to spare them. I even heard that one of the most powerful
                                   moves a cat can learn is based entirely on CHA..."""]
                possibleAdvice.append(random.choice(miniAdvice))
            rando = (random.randint(1, 2))
            if rando == 1 and "deafness" in clan.clans["player_Clan"].cats[target].disabilities:
              print("%s didn't hear what you said, but just taking the time to try to get their attention used up a social turn." % clan.clans["player_Clan"].cats[target].name)
            else:
              if "muteness" in clan.clans["player_Clan"].cats[target].disabilities:
                method = "%s signs: " % clan.clans["player_Clan"].cats[target].name
              else:
                method = "[%s] : " % clan.clans["player_Clan"].cats[target].name

              print("%s%s" % (method, random.choice(possibleAdvice)))

        # Chat

        elif cmd == "C":

          # Check for disabilities
          
          rando = (random.randint(1, 2))
          if rando == 1 and "deafness" in clan.clans["player_Clan"].cats[target].disabilities:
            print("%s didn't hear what you said, but just taking the time to try to get their attention used up a social turn." % clan.clans["player_Clan"].cats[target].name)
          else:
            if "muteness" in clan.clans["player_Clan"].cats[target].disabilities:
              method = "%s signs: " % clan.clans["player_Clan"].cats[target].name
            else:
              method = "[%s] : " % clan.clans["player_Clan"].cats[target].name

            print("You had a chat with %s." % clan.clans["player_Clan"].cats[target].name)

            # Determine reputation change

            if clan.clans["player_Clan"].cats[leader].stats["Charisma"] * 2 > clan.clans["player_Clan"].cats[target].stats["Charisma"]:
              luck = 2
            elif clan.clans["player_Clan"].cats[leader].stats["Charisma"] > clan.clans["player_Clan"].cats[target].stats["Charisma"]:
              luck = 1
            elif clan.clans["player_Clan"].cats[target].stats["Charisma"] * 2 > clan.clans["player_Clan"].cats[leader].stats["Charisma"]:
              luck = -2
            elif clan.clans["player_Clan"].cats[target].stats["Charisma"] > clan.clans["player_Clan"].cats[leader].stats["Charisma"]:
              luck = -1
            else:
              luck = 0
            
            rando = (random.randint(1, 7)) + luck
              
            if rando > 7:
              rando = 7
            elif rando < 1:
              rando = 1

            if clan.clans["player_Clan"].cats[target].rank == "kit":
              diatype = 0 
            else:
              trait = random.choice(clan.clans["player_Clan"].cats[target].personality)
              if trait in ["proud", "impulsive", "passionate"]:
                diatype = 1
              elif trait in ["caring", "kind", "loving", "peaceful"]:
                diatype = 2
              elif trait in ["cold", "calm", "resolute", "durable"]:
                diatype = 3
              elif trait in ["determined", "devoted", "loyal", "hardworking"]:
                diatype = 4
              elif trait in ["intelligent", "observant", "sharp"]:
                diatype = 5
              elif trait in ["moral", "spiritual", "wise"]:
                diatype = 6
              elif trait in ["expressive", "feisty", "scrappy"]:
                diatype = 7
              else:
                diatype = 8

            print("%s%s" % (method, random.choice(cat.dialogue[rando][diatype])))

            clan.clans["player_Clan"].cats[target].rep += (rando - 4)

            print("Your reputation with %s changed by %d." % (clan.clans["player_Clan"].cats[target].name, (rando - 4)))
                
            # Learn item preferences
            
            if "muteness" in clan.clans["player_Clan"].cats[target].disabilities:
              rando = (random.randint(1, 12))
            else:
              rando = (random.randint(1, 6))
            if rando == 1 and len(clan.clans["player_Clan"].cats[target].personality) < 3:
              trait = (random.choice(cat.traits))
              while trait in clan.clans["player_Clan"].cats[target].personality:
                trait = (random.choice(cat.traits))
              print("You learned that %s is %s!" % (clan.clans["player_Clan"].cats[target].name, trait))
              clan.clans["player_Clan"].cats[target].personality.append(trait)
              if trait == "spiritual":
                rando2 = (random.randint(1, 2))
                if rando2 == 1:
                  clan.clans["player_Clan"].cats[target].faith = "StarClan"
                else:
                  clan.clans["player_Clan"].cats[target].faith = "The Dark Forest"
            elif rando == 2:
              print("%s gushes about the item %s. They seem really fond of it." % (clan.clans["player_Clan"].cats[target].name,
                                                                                   clan.clans["player_Clan"].cats[target].favourite))
              if clan.clans["player_Clan"].cats[target].found_favourite == "":
                clan.clans["player_Clan"].cats[target].found_favourite = clan.clans["player_Clan"].cats[target].favourite
            elif rando == 3:
              like = (random.choice(clan.clans["player_Clan"].cats[target].likes))
              print("%s seems interested in another Clanmate's %s. Maybe even a little jealous?" % (clan.clans["player_Clan"].cats[target].name, like))
              if not like in clan.clans["player_Clan"].cats[target].found_likes:
                clan.clans["player_Clan"].cats[target].found_likes.append(like)

        # Gift
            
        elif cmd == "G" or cmd == "g":
          item_count = 0
          unlocked = []
          for i in folder.folders["inventory"].contents.copy():
            if folder.folders["inventory"].contents[i] > 0:
              print("[%d] %s : %d" % (item_count, i, folder.folders["inventory"].contents[i]))
              unlocked.append(i)
              item_count += 1
          if item_count == 0:
            print("You have nothing to give them!")
            clock["turns"] += 1
          else:
            correct_confirm = False
            cmd = "alfalfa"

            # Give item
            
            while correct_confirm == False:
              try:
                cmd = unlocked[int(cmd)]
                correct_confirm = True
              except:
                cmd = input("""Which item would you like to give them? Enter their ID.
                
                > """)

            # Gift result
            
            if clan.clans["player_Clan"].cats[target].favourite == cmd:
              print("That's %s's favourite item! They will never forget your thoughtfulness." % clan.clans["player_Clan"].cats[target].name)
              clan.clans["player_Clan"].cats[target].rep += 5
            elif cmd in clan.clans["player_Clan"].cats[target].likes:
              print("%s seems to appreciate your gift!" % clan.clans["player_Clan"].cats[target].name)
              clan.clans["player_Clan"].cats[target].rep += (random.randint(1, 3))
            else:
              print("%s thanks you and acts polite, but you can tell they don't really know what to do with your 'gift'..." % clan.clans["player_Clan"].cats[target].name)
              clan.clans["player_Clan"].cats[target].rep += (random.randint(-1, 1))
            folder.folders["inventory"].contents[cmd] -= 1

        # Propose
          
        elif cmd == "P" or cmd == "p":

          # Calculate chances
          
          if not clan.clans["player_Clan"].cats[target].age < 12:
            if clan.clans["player_Clan"].cats[target].rep > 20:
              odds = 10
            elif clan.clans["player_Clan"].cats[target].rep > 15:
              odds = 30
            elif clan.clans["player_Clan"].cats[target].rep > 10:
              odds = 60
            elif clan.clans["player_Clan"].cats[target].rep > 5:
              odds = 80
            elif clan.clans["player_Clan"].cats[target].rep > 0:
              odds = 90
            else:
              odds = 100
            odds -= clan.clans["player_Clan"].cats[leader].stats["Charisma"] * 2.5
            rando = (random.randint(1, 100))
            if rando > odds:

              # Accept
              
              print("%s accepted!" % clan.clans["player_Clan"].cats[target].name)
              clan.clans["player_Clan"].cats[target].mate.append(leader)
              clan.clans["player_Clan"].cats[leader].mate.append(target)
            else:

              # Reject
              
              print("Unfortunately, %s doesn't feel the same way, and in fact this has only dug a deeper rift between you both." % clan.clans["player_Clan"].cats[target].name)
              clan.clans["player_Clan"].cats[target].rep -= (random.randint(3, 8))
          else:
            print("You cannot propose to %s right now." % clan.clans["player_Clan"].cats[target].name)

        # Breakup
        
        elif cmd == "B":
          if leader in clan.clans["player_Clan"].cats[target].mate:
            print("You and %s have broken up." % clan.clans["player_Clan"].cats[target].name)
            clan.clans["player_Clan"].cats[target].mate.remove(leader)
            clan.clans["player_Clan"].cats[leader].mate.remove(target)
            clan.clans["player_Clan"].cats[target].rep -= (random.randint(1, 10))

        # Kits
        
        elif cmd == "K":
          rando = (random.randint(1, 4))
          if (leader in clan.clans["player_Clan"].cats[target].mate or rando == 1) and not clan.clans["player_Clan"].cats[target].rank == "kit" and not clan.clans["player_Clan"].cats[target].rank == "apprentice" and not clan.clans["player_Clan"].cats[target].age_status["isqueen"] == True:

            # Pregnancy

            Aparent = leader
            Bparent = target
            kit_count = (random.randint(1, 5))
            if len(clan.clans["player_Clan"].cats) + kit_count < (20 + ((clan.clans["player_Clan"].land - 5) * 2)):
              clan.clans["player_Clan"].power += 1
              if not clan.clans["player_Clan"].cats[Aparent].pronoun == clan.clans["player_Clan"].cats[Bparent].pronoun:
                if clan.clans["player_Clan"].cats[Aparent].pronoun == "she-cat":
                  preggo = Aparent
                  pregnator = Bparent
                elif clan.clans["player_Clan"].cats[Bparent].pronoun == "she-cat":
                  preggo = Bparent
                  pregnator = Aparent
                else:
                  preggo = (random.randint(0, 1))
                  if preggo == 0:
                    preggo = Aparent
                    pregnator = Bparent
                  else:
                    preggo = Bparent
                    pregnator = Aparent
                clan.clans["player_Clan"].cats[preggo].age_status["isqueen"] = True
                clan.clans["player_Clan"].cats[preggo].age_status["pregnant"] = 1

                clan.clans["player_Clan"].cats[preggo].age_status["pregnator"] = clan.clans["player_Clan"].cats[pregnator]
                
                print("%s is pregnant with %s's kits!" % (clan.clans["player_Clan"].cats[preggo].name,
                                                          clan.clans["player_Clan"].cats[preggo].age_status["pregnator"].name))
              else:

                # Adopt
                
                kit_count = (random.randint(1, 4))
                for i in range(0, kit_count):
                  
                  var_name = ""
                  rando = (random.randint(5, 15))
                  for i in range(rando):
                    var_name = var_name + (random.choice(codebits))

                  prefix = (random.choice(prefixes))

                  pronoun = (random.choice(pronouns))
                  
                  size = (random.choice(body_size))

                  build = (random.choice(body_build))

                  coat = (random.choice(coats))

                  pattern = (random.choice(patterns))

                  eye = (random.choice(eyes))
      
                  if "-" in pattern:
                    pelt_coat = coat.replace(" ", "-")
                  else:
                    pelt_coat = coat
                  
                  if "with" in pattern:
                    pelt = "%s %s%s" % (pelt_coat, pronoun, pattern)
                  else:
                    pelt = "%s%s %s" % (pelt_coat, pattern, pronoun)

                  if coat == "pale ginger" and pattern == "-and-black":
                      pelt = "pale tortoiseshell %s" % pronoun
                  elif (coat == "ginger" or coat == "flame-coloured") and pattern == "-and-black":
                      pelt = "tortoiseshell %s"  % pronoun
                  elif coat == "reddish-brown" and pattern == "-and-black":
                      pelt = "dark tortoiseshell %s"  % pronoun
                  if coat == "black" and pattern == "-and-black":
                      pelt = "black %s" % pronoun
                  elif coat == "black" and pattern == " with darker patches":
                      new_pat = "black"
                      while new_pat == "black":
                        new_pat = (random.choice(coats))
                      pattern = " with %s patches" % new_pat
                      pelt = "%s %s%s" % (coat, pronoun, pattern)
                  elif coat == "white" and pattern == "-and-white":           
                      pelt = "white %s" % pronoun
                  elif coat == "white" and pattern == " with lighter patches":
                      new_pat = "white %s" % pronoun
                      while new_pat == "white":
                        new_pat = (random.choice(coats))
                      pattern = " with %s patches" % new_pat
                      pelt = "%s %s%s" % (coat, pronoun, pattern)

                  if "with" in pattern:
                      description = ("%s and %s %s and %s eyes" % (size, build, pelt, eye))
                  else:
                      description = ("%s and %s %s with %s eyes" % (size, build, pelt, eye))
         
                  clan.clans["player_Clan"].cats[var_name] = cat(

                  "", prefix, "kit", "kit",
                  description, pronoun, coat, pattern, eye, size, build, 0, {"isqueen" : False, "pregnant" : 0}, [], [], [],
                  "Kit", [], "", 0, [], [], "", "",
                  [], "", "unknown", "unknown",
                  5, 0, 0, {"Willpower" : 5, "Strength" : 1, "Toughness" : 1, "Speed" : 1, "Precision" : 1, "Charisma" : 1}, [], "Neutral")

                  for i in range(random.randint(1, 3)):
                    clan.clans["player_Clan"].cats[var_name].likes.append(random.choice(list(folder.folders["inventory"].contents)))
                  clan.clans["player_Clan"].cats[var_name].favourite = (random.choice(list(folder.folders["inventory"].contents)))

                  clan.clans["player_Clan"].cats[var_name].Aparent = Aparent
                  clan.clans["player_Clan"].cats[var_name].Bparent = Bparent

                  rando = (random.randint(1, 28))
                  clan.clans["player_Clan"].cats[var_name].personality.append(cat.traits[rando - 1])
                  clan.clans["player_Clan"].cats[var_name].quote = quotes[rando - 1] 
                  if cat.traits[rando - 1] == "spiritual":
                    rando = (random.randint(1, 2))
                    if rando == 1:
                      clan.clans["player_Clan"].cats[var_name].allegiance = "StarClan"
                    elif rando == 2:
                      clan.clans["player_Clan"].cats[var_name].allegiance = "The Dark Forest"

                  for i in disabilities:
                    rando = (random.randint(1, 40))
                    if rando == 1:
                      clan.clans["player_Clan"].cats[var_name].disabilities.append(i)

                  for i in mutations:
                    rando = (random.randint(1, 40))
                    if rando == 1:
                      if i == "heterochromia":
                        i = (random.choice(eyes)) + " heterochromia"
                      clan.clans["player_Clan"].cats[var_name].mutations.append(i)

                  if "blindness" in clan.clans["player_Clan"].cats[var_name].disabilities:
                    clan.clans["player_Clan"].cats[var_name].stats["Toughness"] += 2
                    clan.clans["player_Clan"].cats[var_name].stats["Precision"] -= 2
                  if "spinal paralysis" in clan.clans["player_Clan"].cats[var_name].disabilities:
                    clan.clans["player_Clan"].cats[var_name].stats["Willpower"] += 20
                    clan.clans["player_Clan"].cats[var_name].stats["Speed"] -= 4
                  if "facial paralysis" in clan.clans["player_Clan"].cats[var_name].disabilities:
                    clan.clans["player_Clan"].cats[var_name].stats["Strength"] += 2
                    clan.clans["player_Clan"].cats[var_name].stats["Precision"] -= 2
                      
                  clan.clans["player_Clan"].cats[var_name].name = clan.clans["player_Clan"].cats[var_name].prefix + clan.clans["player_Clan"].cats[var_name].suffix
                  clan.clans["player_Clan"].cats[var_name].Aparent = Aparent
                  clan.clans["player_Clan"].cats[var_name].Bparent = Bparent
                  if clan.clans["player_Clan"].cats[var_name].prefix in prefixes:
                    prefixes.remove(clan.clans["player_Clan"].cats[var_name].prefix)
                  print("%s was adopted from a local kittypet!" % clan.clans["player_Clan"].cats[var_name].name)
                
                queen = (random.randint(0, 1))
                if queen == 0:
                  queen = Aparent
                else:
                  queen = Bparent
              
                clan.clans["player_Clan"].cats[queen].age_status["isqueen"] = True
            else:
              print("%s and %s tried to have kits, but they must wait until the Clan population has lowered." % (clan.clans["player_Clan"].cats[Aparent].name,
                                                                                                                 clan.clans["player_Clan"].cats[Bparent].name))
          else:
            print("You cannot have kits with %s right now." % clan.clans["player_Clan"].cats[target].name)

        # Investigate
        
        elif cmd == "I":
          if clan.clans["player_Clan"].traitor_event == True and not clan.clans["player_Clan"].disease_event == False:
            cmd = "alfalfa"
            while not cmd == "D" and not cmd == "T":
              cmd = input("""
              What would you like to investigate %s for?

              [D]isease

              [T]raitor
              
              > """ % clan.clans["player_Clan"].cats[target].name)

              cmd = cmd.upper()
          elif clan.clans["player_Clan"].traitor_event == True:
            cmd = "T"
          elif not clan.clans["player_Clan"].disease_event == False:
            cmd = "D"

          # Traitor investigation
          
          if cmd == "T":
            if hasattr(clan.clans["player_Clan"].cats[target], 'traitor'):
              if settings["tutorial"] == True and settings["tutorial_part"] == 101:
                settings["tutorial_part"] = 102
              while not cmd == "Y" and not cmd == "y" and not cmd == "N" and not cmd == "n":
                cmd = input("""The traitor was revealed to be %s! Do you wish to exile them? [Y]/[N] 
                
                > """ % clan.clans["player_Clan"].cats[target].name)
              if cmd == "Y" or cmd == "y":
                print("%s has been exiled. The other cats are grateful, for now they can rest easily." % clan.clans["player_Clan"].cats[target].name) 
                for i in clan.clans["player_Clan"].cats.copy():
                  if clan.clans["player_Clan"].cats[i].mentor == target:
                    clan.clans["player_Clan"].cats[i].mentor = "None"
                    # make you choose a new mentor
                  if target in clan.clans["player_Clan"].cats[i].mate:
                    clan.clans["player_Clan"].cats[i].mate.remove(target)
                del clan.clans["player_Clan"].cats[target]
                for i in clan.clans["player_Clan"].cats.copy():
                  clan.clans["player_Clan"].cats[i].rep += (random.randint(1, 3))
              else:
                print("You have decided to forgive %s for their crimes. They swear they will redeem themselves, but the other cats are distrustful of both them and you." % clan.clans["player_Clan"].cats[target].name)
                for i in clan.clans["player_Clan"].cats.copy():
                  if not clan.clans["player_Clan"].cats[i] == clan.clans["player_Clan"].cats[target]:
                    clan.clans["player_Clan"].cats[i].rep -= (random.randint(1, 3))
                  else:
                    clan.clans["player_Clan"].cats[i].rep += (random.randint(1, 3))

                delattr(folder.folders["traitors"].contents[target], 'traitor')

            else:
              if settings["tutorial"] == True and settings["tutorial_part"] == 101:
                settings["tutorial_part"] = 103
              print("You cannot find any evidence that %s is the traitor." % clan.clans["player_Clan"].cats[target].name)

          # Disease investigation
          
          elif cmd == "D":

            quarantine = []

            for c in clan.clans["player_Clan"].cats:
              if clan.clans["player_Clan"].cats[c].loc == ("%s quarantine" % clan.clans["player_Clan"].name):
                quarantine.append(c)
                
            rando = 1
            if clan.clans["player_Clan"].disease_event == "redcough":
              rando = (random.randint(0, 1))
            if rando == 1 and hasattr(clan.clans["player_Clan"].cats[target], 'infected'):
              
              cmd = "alfalfa"

              herb_price = (random.randint(1, 3))

              capacity = 0

              for i in clan.clans["player_Clan"].cats:
                if rank.ranks[clan.clans["player_Clan"].cats[i].rank].privs["canHeal"] == True:
                  capacity += 2

              while not cmd == "T" and not cmd == "Q" and not cmd == "N":
    
                statement = ""

                catmint_needed = 0
                violet_needed = 0
                if clan.clans["player_Clan"].disease_event == "blackcough":
                  catmint_needed = 1
                  statement = "Blackcough also requires one 'Catmint' to treat. You have %d." % folder.folders["inventory"].contents["Cat Mint"]

                elif clan.clans["player_Clan"].disease_event == "yellowcough":
                  violet_needed = 1
                  statement = "Yellowcough also requires one 'Violet Flower' to treat. You have %d." % folder.folders["inventory"].contents["Violet Flower"]

                cmd = input("""
                %s is infected! You may try to treat them or contain them. If you would like to do nothing, press ENTER.

                [T]reatment (price: %d herbs - you have %d)

                [Q]uarantine (capacity: %d / %d cats)

                %s
                
                > """ % (clan.clans["player_Clan"].cats[target].name, herb_price, clan.clans["player_Clan"].herbs, len(quarantine), capacity, statement))

                cmd = cmd.upper()
                
                if cmd == "T":
                  if clan.clans["player_Clan"].herbs >= herb_price and folder.folders["inventory"].contents["Cat Mint"] >= catmint_needed and folder.folders["inventory"].contents["Violet Flower"] >= violet_needed :
                    clan.clans["player_Clan"].herbs -= herb_price
                    folder.folders["inventory"].contents["Cat Mint"] -= catmint_needed
                    folder.folders["inventory"].contents["Violet Flower"] -= violet_needed
                    rando = (random.randint(1, 3))
                    if rando == 1:
                      print("The treatment failed! You still lost %d herbs in the attempt. It may work if you try again." % herb_price)
                    else:
                      print("Using %d herbs, you managed to heal %s!" % (herb_price, clan.clans["player_Clan"].cats[target].name))
                      delattr(clan.clans["player_Clan"].cats[target], 'infected')
                  
                  if cmd == "Y":
                    if len(quarantine) < capacity:
                      clan.clans["player_Clan"].cats[target].loc = "%s quarantine" % clan.clans["player_Clan"].name
                      print("%s has been quarantined!" % clan.clans["player_Clan"].cats[target].name)
                    else:
                      print("The medicine den is too full! Try training some more medicine apprentices?")

                elif cmd == "Q":
                  if len(quarantine) < capacity:
                    clan.clans["player_Clan"].cats[target].loc = "%s quarantine" % clan.clans["player_Clan"].name
                    print("%s has been quarantined!" % clan.clans["player_Clan"].cats[target].name)
                  else:
                    print("The medicine den is too full! Try training some more medicine apprentices?")
            else:
              print("You don't notice any signs of illness in %s." % clan.clans["player_Clan"].cats[target].name)

          elif cmd == "S":
            if clan.clans["player_Clan"].cats[target].rep > 0:
              repinc = (random.randint(1, 3))

              print("You snuggled with %s and increased your reputation by %d." % (clan.clans["player_Clan"].cats[target].name, repinc))

              clan.clans["player_Clan"].cats[target].rep += repinc
              
        unchanging = ["Mate", "Kit", "Mentor"]

        if target in clan.clans["player_Clan"].cats:
          
          if not clan.clans["player_Clan"].cats[target].title in unchanging:
            if clan.clans["player_Clan"].cats[target].title == "Neutral":
              rando = (random.randint(1, 5))
              if rando == 1:
                clan.clans["player_Clan"].cats[target].title = "Rival"
            elif clan.clans["player_Clan"].cats[target].rep > 24:
              clan.clans["player_Clan"].cats[target].title = "Best Friend"
            elif clan.clans["player_Clan"].cats[target].rep > 0 and not clan.clans["player_Clan"].cats[target].title == "Rival":
              clan.clans["player_Clan"].cats[target].title = "Friend"
            elif clan.clans["player_Clan"].cats[target].rep == 0 and not clan.clans["player_Clan"].cats[target].title == "Rival":
              clan.clans["player_Clan"].cats[target].title = "Neutral"
            elif clan.clans["player_Clan"].cats[target].rep < 0 and not clan.clans["player_Clan"].cats[target].title == "Rival":
              clan.clans["player_Clan"].cats[target].title = "Bully"
            elif clan.clans["player_Clan"].cats[target].rep < -24:
              clan.clans["player_Clan"].cats[target].title = "Enemy"
            
    else:
      print("It's too late to socialize. You can rest [enter] to move to the next day.")


