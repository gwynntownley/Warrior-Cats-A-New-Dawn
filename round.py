from storage.storage import *
from events.death import death
from events.entity import catgen
from actions.battle import battle
from actions.map import claim

import random

def aging(patrol_time):

  # define globals

  global folder

  global disease

  print("--- ROUND SUMMARY ---")

  for i in clan.clans.copy():
    if not i == "player_Clan":

      print("")
      print("-- %s --" % clan.clans[i].name)
      print("")
      
      clan.clans[i].power += (random.randint(-1, 1))
      if len(clan.clans[i].cats) < 1 or len(clan.clans[i].location) < 1:

        # clan destroyed
        
        print("%s has been destroyed! No more cats live in %s and its camp is completely abandoned..." %
              (clan.clans[i].name, clan.clans[i].name))
        for y in land.coordinates:
          for x in land.coordinates[y]:
            if land.coordinates[y][x].owner == i:
              land.coordinates[y][x].owner = None
        symbols.append(clan.clans[i].symbol)
        del clan.clans[i]
      
      elif len(clan.clans[i].cats) < 5:
        rando = (random.randint(1, 2))
        if rando == 1:

          # clan + rogue group merge
          
          print("%s, being low on cats, has taken in a large group of rogues into their ranks!" % clan.clans[i].name)
          for g in range(random.randint(2, 8)):
            var_name = catgen(i, None)
            print("%s has joined %s!" % (clan.clans[i].cats[var_name].name, clan.clans[i].name))
      else:
        rando = (random.randint(1, 2))
        if rando == 1:

          # clan recruit
          
          print("%s has recruited an outsider into their ranks!" % clan.clans[i].name)
          var_name = catgen(i, None)
          print("%s has joined %s!" % (clan.clans[i].cats[var_name].name, clan.clans[i].name))
          
  for i in clan.clans["player_Clan"].cats.copy():
    if clan.clans["player_Clan"].cats[i].rank == "leader":
      leader = i
      clan.clans["player_Clan"].cats[i].rep = 0
      break

  # eat prey

  print("")
  print("-- Prey Report --")
  print("")
  
  print("Your current number of feedings is %d." % (clan.clans["player_Clan"].prey))
  clan.clans["player_Clan"].prey -= len(clan.clans["player_Clan"].cats)
  if clan.clans["player_Clan"].prey > len(clan.clans["player_Clan"].cats) * 2:
    print("What a feast ! There was more than enough prey for your entire Clan. Every cat rests with full bellies.")
    wp_gain = 10
  elif clan.clans["player_Clan"].prey > len(clan.clans["player_Clan"].cats):
    print("Your Clan is able to eat well, thanks to your warriors. No cat went to sleep hungry.")
    wp_gain = 5
  elif clan.clans["player_Clan"].prey < (0 - len(clan.clans["player_Clan"].cats) * 0.5):
    print("Even the smallest mouths struggled to find food. The Clan withers under a fierce famine ...")
    wp_gain = -10
  else:
    print("Your Clanmates are beginning to show signs of weariness ... your Clan needs more prey if it is to survive.")
    wp_gain = -5
                                            
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

  # traitor event

  traitors = []

  for t in clan.clans["player_Clan"].cats:
    if hasattr(t, 'traitor'):
      traitors.append(t)
  
  if len(traitors) > 0:
    for t in traitors:
      target = (random.choice(list(clan.clans["player_Clan"].cats)))
      while target == traitor:
        target = (random.choice(list(clan.clans["player_Clan"].cats)))

      print("")
      print("-- ! Special Event --")
      print("")
      if clan.clans["player_Clan"].cats[target].rank == "leader":
        battle("traitor", traitor)
      else:
        if clan.clans["player_Clan"].cats[t].stats["Strength"]  > clan.clans["player_Clan"].cats[target].stats["Toughness"]:
          dead_guy = target
          death(dead_guy, ", murdered")
          evidence = ["A tuft of %s fur was found near the victim." % clan.clans["player_Clan"].cats[t].coat,
                      "Near the victim's body, a(n) %s was discovered." % clan.clans["player_Clan"].cats[t].favourite,
                      "The killing marks seem to have been made by a %s cat." % clan.clans["player_Clan"].cats[t].size]
        else:
          print("%s managed to survive the traitor's blow! However, they escaped with severe injuries." %
                clan.clans["player_Clan"].cats[target].name)
          evidence = ["%s described their attacker as being %s." %
                      (clan.clans["player_Clan"].cats[target].name, clan.clans["player_Clan"].cats[t].build),
                      "%s claimed the attacker's eyes were %s." %
                      (clan.clans["player_Clan"].cats[target].name, clan.clans["player_Clan"].cats[t].eyes),
                      "%s believed the attacker must have been at least level %d." %
                      (clan.clans["player_Clan"].cats[target].name, clan.clans["player_Clan"].cats[t].lvl)]

        rando = (random.randint(1, 2))
        if rando == 1:
          print("You uncovered a clue !")
          print((random.choice(evidence)))

  # disease event
              
  if not clan.clans["player_Clan"].disease_event == False:

    print("")
    print("-- ! Special Event --")
    print("")

  infected = []

  for i in clan.clans["player_Clan"].cats:
    if hasattr(i, 'infected'):
      infected.append(i)
  
  if len(infected) > 0:

    for c in infected:
      if clan.clans["player_Clan"].cats[c].wp < 1:
        dead_guy = c
        death(dead_guy, " of %s" % (clan.clans["player_Clan"].disease_event))
      else:
        wp_loss = (disease.diseases[clan.clans["player_Clan"].disease_event].fatality)
        if c in infected:
            clan.clans["player_Clan"].cats[c].wp -= wp_loss
            statements = [
              "looking a little sluggish",
              "coughing a lot",
              "complaining of chest pain",
              "shirking their duties",
              "sleeping more than usual",
              "avoiding others"
            ]
            rando = 1
            if clan.clans["player_Clan"].disease_event == "redcough":
              rando = (random.randint(0, 1))
            if (wp_loss > (disease.diseases[clan.clans["player_Clan"].disease_event].fatality / 2)
                and rando == 1
                and c in clan.clans["player_Clan"].cats):
              print("%s has been %s lately..." % (clan.clans["player_Clan"].cats[c].name, random.choice(statements)))
            rando = (random.randint(0, disease.diseases[clan.clans["player_Clan"].disease_event].infectivity))
            if rando == 0:
              if not "quarantine" in clan.clans["player_Clan"].cats[c].loc:
                new_infectee = (random.choice(list(clan.clans["player_Clan"].cats)))
                while new_infectee in infected:
                  new_infectee = (random.choice(list(clan.clans["player_Clan"].cats)))
                setattr(clan.clans["player_Clan"].cats[new_infectee], 'infected', True)

  # disaster event

  if not clan.clans["player_Clan"].disaster_event == False:

    print("")
    print("-- ! Special Event --")
    print("")
    
    rando = (random.randint(1, 4))
    if rando == 1:
      if clan.clans["player_Clan"].disaster_event == "wildfire":
        print("""A wildfire rages through your Clan's territory, right to the heart of your camp !
                 Smoke covers the sky and cinders speckle your fur as you run to safety ...""")
      elif clan.clans["player_Clan"].disaster_event == "tsunami":
        print("""From the sea a great wave looms over your Clan, casting a dark, humid shadow.
              Frozen in fear, you watch helplessly as it strikes, destroying all in its path ...""")
      elif clan.clans["player_Clan"].disaster_event == "earthquake":
        print("""One day, you notice the earth begin to tremble.
              Then, without warning, the trembling turns to violent shaking as a great scar opens in the centre of camp ...""")
      elif clan.clans["player_Clan"].disaster_event == "tornado":
        print("""A tornado sweeps through the territory, an unstoppable whirlwind of fury that rips entire trees out of the
              ground and takes some of your cats with it ...""")
      elif clan.clans["player_Clan"].disaster_event == "hurricane":
        print("""From the sky rain and wind unite to create the greatest and most terrifying storm you have ever seen in your life !
              A hurricane, centered right above your camp ...""")
      elif clan.clans["player_Clan"].disaster_event == "blizzard":
        print("""One day you find it's snowing a little more heavily than usual.
              That snow eventually becomes a blanket of white, that buries your entire camp in deadly frost ...""")

      for i in clan.clans["player_Clan"].cats.copy():
        protected = []

        for a in folder.folders["shelters"].contents:
          destroyed = False
          folder.folders["shelters"].contents[a]["endurance"] - 1
          if folder.folders["shelters"].contents[a]["endurance"] < 0:
            print("Your %s shelter collapsed, rendering it unusable and slightly injuring some of the cats inside !")
            destroyed = True
          
          for b in folder.folders["shelters"].contents[a]["population"]:
            if destroyed == True:
              dmg_loss = (random.randint(-5, 5))

              if dmg_loss > 0:
                clan.clans["player_Clan"].cats[i].wp -= dmg_loss
                
                print("%s lost %d wp from the falling debris." % (folder.folders["shelters"].contents[a]["population"][b].name,
                                                                                 dmg_loss))
            protected.append(b)

          if destroyed == True:
            del folder.folders["shelters"].contents[a]
            
        min = (random.randint(1, 10))
        rando = (random.randint(1, 2))

        if rando == 1 and not i in protected:

          if clan.clans["player_Clan"].cats[i].stats["Toughness"] < min:
            dmg_loss = (random.randint(15, 30))
            clan.clans["player_Clan"].cats[i].wp -= dmg_loss
            
            print("%s got completely lost in the %s ... they lost %d wp." % (clan.clans["player_Clan"].cats[i].name,
                                                                             clan.clans["player_Clan"].disaster_event,
                                                                             dmg_loss))

          else:
            dmg_loss = (random.randint(1, 14))
            clan.clans["player_Clan"].cats[i].wp -= dmg_loss
            
            print("%s got caught in the %s, but thanks to their toughness they only lost %d wp." % (clan.clans["player_Clan"].cats[i].name,
                                                                             clan.clans["player_Clan"].disaster_event,
                                                                             dmg_loss))
          
    clan.clans["player_Clan"].disaster_event = False

  # banishment

  likes_you = 0
  hates_you = 0
  for i in clan.clans["player_Clan"].cats.copy():
    if clan.clans["player_Clan"].cats[i].rep <= -5:
      hates_you += 1
    else:
      likes_you += 1
  if "The word of the Clan leader is law." in folder.folders["warrior_code"].contents:
    margin_checker = 0.75
  else:
    margin_checker = 0.5
  if (hates_you / (hates_you + likes_you)) >= margin_checker:

    print("")
    print("-- ! Special Event --")
    print("")
    
    print("You wake up one day surrounded by your Clanmates...")
    print("But they look different. Angrier.")
    print("You try to retaliate, to struggle, but there's too many of them...")
    print("Your deputy stares you straight in the eyes, and orders you to leave.")
    print("Do you have any other choice?")
    print("...")
    print("You have been exiled.")
    print("But this does not mean the game is over yet! You will live on in the next leader...")
    for i in clan.clans["player_Clan"].cats.copy():
      if clan.clans["player_Clan"].cats[i].rank == "deputy":
        new_leader = i
        break
    print("The new leader is %s, now %s." % (clan.clans["player_Clan"].cats[new_leader].name,
                                             clan.clans["player_Clan"].cats[new_leader].prefix + "star"))
    for i in clan.clans["player_Clan"].cats.copy():
      if clan.clans["player_Clan"].cats[i].rank == "leader":
        for a in clan.clans["player_Clan"].cats.copy():
          if clan.clans["player_Clan"].cats[a].mentor == clan.clans["player_Clan"].cats[i]:
            clan.clans["player_Clan"].cats[a].mentor = (random.choice(list(clan.clans["player_Clan"].cats)))
            while (clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[a].mentor].rank == "elder"
                   or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[a].mentor].rank == "medicine cat"
                   or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[a].mentor].rank == "medicine apprentice"
                   or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[a].mentor].rank == "kit"
                   or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[a].mentor].rank == "apprentice"):
              clan.clans["player_Clan"].cats[a].mentor = (random.choice(list(clan.clans["player_Clan"].cats)))
          rando = (random.randint(1, 5))
          if clan.clans["player_Clan"].cats[i].mentor == a:
            clan.clans["player_Clan"].cats[a].title = "Mentor"
          elif rando == 1:
            clan.clans["player_Clan"].cats[a].title = "Rival"
          clan.clans["player_Clan"].cats[a].rep = (random.randint(-25, 25))
          
        del clan.clans["player_Clan"].cats[i]
    clan.clans["player_Clan"].cats[new_leader].suffix = "star"
    clan.clans["player_Clan"].cats[new_leader].name = (clan.clans["player_Clan"].cats[new_leader].prefix +
                                                            clan.clans["player_Clan"].cats[new_leader].suffix) 
    clan.clans["player_Clan"].cats[new_leader].rank = "leader"
    clan.clans["player_Clan"].cats[new_leader].rep = 0
    
    # Nine lives ceremony
    
    print("""===CUTSCENE===
    
    The first task of a new leader is receiving their nine lives.
    
    At the %s, you gain the following lives: 
    
    """ % land.communer)

    temp_starclan = realm.realms["star"].cats

    for i in range(9):
      if len(list(temp_starclan)) < 1:
        temp_suffixes = suffixes + ["star", "star", "star", "star", "star", "star", "star", "star", "star", "star",
                                    "paw", "paw", "paw", "paw", "paw", "paw", "paw", "paw", "paw","paw",
                                    "kit", "kit", "kit", "kit", "kit", "kit", "kit", "kit", "kit", "kit",
                                    "", "",  "", "", "", "", "", "", "", ""]

        name = (random.choice(prefixes)) + (random.choice(temp_suffixes))

        relation = (random.choice(relationship))

        if "paw" in name or "kit" in name:
          while relation == "mate" or relation == "mother" or relation == "father" or relation == "parent":
            relation = (random.choice(relationship))  

        virtue = (random.choice(virtues))

        print("From %s, your %s, the gift of %s." % (name, relation, virtue))
      else:
        giver = (random.choice(list(folder.folders["starclan"].contents)))
        name = folder.folders["starclan"].contents[giver].name

        rank = folder.folders["starclan"].contents[giver].rank

        virtue = (random.choice(virtues))

        print("From %s the %s, the gift of %s." % (name, rank, virtue))

        del temp_starclan[giver]
      
    print("")
    print("===END OF CUTSCENE===")
    setattr(clan.clans["player_Clan"].cats[i], 'lives', 9)
    id = 1
    choices = []
    for i in clan.clans["player_Clan"].cats.copy():
      if clan.clans["player_Clan"].cats[i].rank == "warrior":
        print("[%d] %s" % (id, clan.clans["player_Clan"].cats[i].name))
        id += 1
        choices.append(i)
      print("There are no cats eligible for the deputy position!")
      print("As your Clan cannot function without a deputy or warriors to hunt or defend for it...")
      print("Your Clan has disbanded.")
      print("Sending you back to the main menu...")
      main_menu()
    else:
      correct_confirm = False
      cmd = "alfalfa"
      while correct_confirm == False:
        try:
          new_deputy = choices[int(cmd) - 1]
          clan.clans["player_Clan"].cats[new_deputy].rank = "deputy"
          correct_confirm = True
        except:
          cmd = input("""Who would you like to promote? Please enter the cat's ID.

          > """)

  # random recruit
  
  recruit_chance = 0
  recruit_chance += 5 * folder.folders["landmarks"].contents["Twolegplace"]
  rando = (random.randint(0, 100))
  if recruit_chance >= rando:

    print("")
    print("-- ! Special Event --")
    print("")
    
    if len(clan.clans["player_Clan"].cats) < (20 + ((len(clan.clans["player_Clan"].location) - 5) * 2)):
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

      cmd = input("""
      An outsider, a %s named %s, wants to join your Clan! Will you allow them? [Y/N]
      
      > """ % (description, prefix))

      if cmd == "N" or cmd == "n":
        print("You turned them away...")
      else:
        prefixes.remove(prefix)
        var_name = ""
        rando = (random.randint(5, 15))
        for i in range(rando):
          var_name = var_name + (random.choice(codebits))

        clan.clans["player_Clan"].cats[var_name] = cat(
    
        "", prefix, "", "",
        description, pronoun, coat, pattern, eye, size, build, 0, {"isqueen" : False, "pregnant" : 0}, [], [], [],
        "Neutral", [], "", 0, [], [], "", "",
        [], "", "unknown", "unknown",
        0, (random.randint(0, 3)), 0, {"Willpower" : 10, "Strength" : 1, "Toughness" : 1, "Speed" : 1, "Precision" : 1, "Charisma" : 1},
        [], "Neutral")

        stat_point = (clan.clans["player_Clan"].cats[var_name].lvl * 5)

        for i in range(stat_point):
          stat_add = (random.choice(list(clan.clans["player_Clan"].cats[var_name].stats)))

          if stat_add == "Willpower":
            clan.clans["player_Clan"].cats[var_name].stats["Willpower"] += 5
          else:
            clan.clans["player_Clan"].cats[var_name].stats[stat_add] += 1

        clan.clans["player_Clan"].cats[var_name].wp = clan.clans["player_Clan"].cats[var_name].stats["Willpower"]
      
        for i in range(random.randint(1, 3)):
          clan.clans["player_Clan"].cats[var_name].likes.append(random.choice(list(folder.folders["inventory"].contents)))
        clan.clans["player_Clan"].cats[var_name].favourite = (random.choice(list(folder.folders["inventory"].contents)))

        rando = (random.randint(1, 28))
        clan.clans["player_Clan"].cats[var_name].personality.append(personality_traits[rando - 1])
        if type(quotes[rando - 1]) is list:
          clan.clans["player_Clan"].cats[var_name].quote = (random.choice(quotes[rando - 1]))
        else:
          clan.clans["player_Clan"].cats[var_name].quote = quotes[rando - 1]
        if personality_traits[rando - 1] == "spiritual":
          rando = (random.randint(1, 2))
          if rando == 1:
            clan.clans["player_Clan"].cats[var_name].faith = "StarClan"
          elif rando == 2:
            clan.clans["player_Clan"].cats[var_name].faith = "The Dark Forest"

        rando = (random.randint(1, 4))
        clan.clans["player_Clan"].cats[var_name].rank = (random.choice(ranks))
        if clan.clans["player_Clan"].cats[var_name].rank == "medicine apprentice":
          rando = (random.randint(1, 2))
          if rando == 1:
            clan.clans["player_Clan"].cats[var_name].suffix = "paw"
            clan.clans["player_Clan"].cats[var_name].age = (random.randint(7, 18))
          else:
            clan.clans["player_Clan"].cats[var_name].suffix = (random.choice(suffixes))
            clan.clans["player_Clan"].cats[var_name].age = (random.randint(12, 36))
            for i in clan.clans["player_Clan"].cats.copy():
              if clan.clans["player_Clan"].cats[i].rank == "medicine cat":
                med_mentor = i
                break
            clan.clans["player_Clan"].cats[var_name].mentor = med_mentor
        elif clan.clans["player_Clan"].cats[var_name].rank == "apprentice":
          clan.clans["player_Clan"].cats[var_name].age = (random.randint(7, 18))
          clan.clans["player_Clan"].cats[var_name].suffix = "paw"
          clan.clans["player_Clan"].cats[var_name].mentor = (random.choice(list(clan.clans["player_Clan"].cats)))
          while (clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[var_name].mentor].rank == "medicine cat"
                 or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[var_name].mentor].rank == "medicine apprentice"
                 or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[var_name].mentor].rank == "kit"
                 or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[var_name].mentor].rank == "apprentice"):
            clan.clans["player_Clan"].cats[var_name].mentor = (random.choice(list(clan.clans["player_Clan"].cats)))
        elif clan.clans["player_Clan"].cats[var_name].rank == "elder":
          clan.clans["player_Clan"].cats[var_name].age = (random.randint(84, 120))
          if not rando == 1:
            clan.clans["player_Clan"].cats[var_name].suffix = input("What suffix would you like to give them? | ")
        elif clan.clans["player_Clan"].cats[var_name].rank == "kit":
          clan.clans["player_Clan"].cats[var_name].age = (random.randint(1, 6))
          clan.clans["player_Clan"].cats[var_name].suffix = "kit"
        else:
          clan.clans["player_Clan"].cats[var_name].age = (random.randint(12, 74))
          if not rando == 1:
            clan.clans["player_Clan"].cats[var_name].suffix = input("What suffix would you like to give them? | ")
        clan.clans["player_Clan"].cats[var_name].name = (clan.clans["player_Clan"].cats[var_name].prefix +
                                                              clan.clans["player_Clan"].cats[var_name].suffix)

        for i in mutations:
          rando = (random.randint(1, 40))
          if rando == 1:
            if i == "heterochromia":
              i = (random.choice(eyes)) + " heterochromia"
            clan.clans["player_Clan"].cats[var_name].mutations.append(i)

        for i in disabilities:
          rando = (random.randint(1, 40))
          if rando == 1:
            clan.clans["player_Clan"].cats[var_name].disabilities.append(i)
        
        if "blindness" in clan.clans["player_Clan"].cats[var_name].disabilities:
          clan.clans["player_Clan"].cats[var_name].stats["Toughness"] += 2
          clan.clans["player_Clan"].cats[var_name].stats["Precision"] -= 2
        if "spinal paralysis" in clan.clans["player_Clan"].cats[var_name].disabilities:
          clan.clans["player_Clan"].cats[var_name].stats["Willpower"] += 20
          clan.clans["player_Clan"].cats[var_name].stats["Speed"] -= 4
        if "facial paralysis" in clan.clans["player_Clan"].cats[var_name].disabilities:
          clan.clans["player_Clan"].cats[var_name].stats["Strength"] += 2
          clan.clans["player_Clan"].cats[var_name].stats["Precision"] -= 2

        print("%s has joined the Clan." % clan.clans["player_Clan"].cats[var_name].name)

  # random predator

  predator_chance = 0
  predator_chance += 5 * folder.folders["landmarks"].contents["Predator Territory"]
  rando = (random.randint(0, 100))
  if predator_chance >= rando:
    
    print("")
    print("-- ! Special Event --")
    print("")
    
    battle("predator", 0)

  # reset queen status
  
  for i in clan.clans["player_Clan"].cats.copy():
    if clan.clans["player_Clan"].cats[i].age_status["isqueen"] == True:
      stay_queen = False
      for a in clan.clans["player_Clan"].cats.copy():
        if ((clan.clans["player_Clan"].cats[a].Aparent == i or clan.clans["player_Clan"].cats[a].Bparent == i)
            and clan.clans["player_Clan"].cats[a].rank == "kit"):
          stay_queen = True
      if stay_queen == False:
        clan.clans["player_Clan"].cats[i].age_status["isqueen"] = False

  # death by exhaustion

  print("")
  print("--- %s REPORT ---" % clan.clans["player_Clan"].name)
  print("")

  for i in clan.clans["player_Clan"].cats.copy():

    print("")
    print("- %s -" % clan.clans["player_Clan"].cats[i].name)
    print("")
    
    if clan.clans["player_Clan"].cats[i].wp < 1:
      dead_guy = i
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

      # reputation events

      if abs(clan.clans["player_Clan"].cats[i].rep) > 20:
        max = 2
      elif abs(clan.clans["player_Clan"].cats[i].rep) > 15:
        max = 3
      elif abs(clan.clans["player_Clan"].cats[i].rep) > 10:
        max = 4
      elif abs(clan.clans["player_Clan"].cats[i].rep) > 5:
        max = 5
      else:
        max = 6

      rando = (1, max)

      if rando == 1:

        if clan.clans["player_Clan"].cats[i].rep < -10:
          print("%s has attacked the leader!" % clan.clans["player_Clan"].cats[i].name)
          
          battle("clanmate", i)

          if i in clan.clans["player_Clan"].cats:

            cmd = input("""Do you wish to exile %s? [Y]/[N]
            
            > """ % clan.clans["player_Clan"].cats[i].name)
            if cmd == "Y" or cmd == "y":
              
              print("%s has been exiled."  % clan.clans["player_Clan"].cats[i].name)
              if clan.clans["player_Clan"].cats[i].rank == "deputy":
                choices = []
                id = 1
                for i in clan.clans["player_Clan"].cats.copy():
                  if clan.clans["player_Clan"].cats[i].rank == "warrior":
                    print("[%d] %s" % (id, clan.clans["player_Clan"].cats[i].name))
                    id += 1
                    choices.append(i)
                if id == 1:
                  print("There are no cats eligible for the deputy position!")
                  print("As your Clan cannot function without a deputy or warriors to hunt or defend for it...")
                  print("Your Clan has disbanded.")
                  print("...")
                  print("Reload to start again!")
                  sys.exit(0)
                else:
                  correct_confirm = False
                  cmd = "alfalfa"
                  while correct_confirm == False:
                    try:
                      new_deputy = choices[int(cmd) - 1]
                      clan.clans["player_Clan"].cats[new_deputy].rank = "deputy"
                      correct_confirm = True
                    except:
                      cmd = input("""Who would you like to promote? Please enter the cat's ID.

                      > """)
                print("The new deputy is %s." % clan.clans["player_Clan"].cats[new_deputy].name)
              elif clan.clans["player_Clan"].cats[i].rank == "medicine cat":
                new_med = ""
                for i in clan.clans["player_Clan"].cats.copy():
                  if clan.clans["player_Clan"].cats[i].rank == "medicine apprentice":
                    new_med = i
                    break
                if new_med == "":
                  new_med = (random.choice(list(clan.clans["player_Clan"].cats)))
                  while (clan.clans["player_Clan"].cats[new_med].rank == "leader"
                         or clan.clans["player_Clan"].cats[new_med].rank == "deputy"
                         or clan.clans["player_Clan"].cats[new_med].rank == "kit"
                         or clan.clans["player_Clan"].cats[new_med].rank == "medicine cat"):
                    new_med = (random.choice(list(clan.clans["player_Clan"].cats)))    

                clan.clans["player_Clan"].cats[new_med].rank = "medicine cat"
                if clan.clans["player_Clan"].cats[new_med].suffix == "paw":
                  clan.clans["player_Clan"].cats[new_med].suffix = (random.choice(suffixes))
                  clan.clans["player_Clan"].cats[new_med].name = (clan.clans["player_Clan"].cats[new_med].prefix +
                                                                       clan.clans["player_Clan"].cats[new_med].suffix)
                  print("The new medicine cat is %s, who was just given their name by StarClan." % (clan.clans["player_Clan"].cats[new_med].name))
                else:
                  print("The new medicine cat is %s." % (clan.clans["player_Clan"].cats[new_med].name))

              for i in clan.clans["player_Clan"].cats.copy():
                if clan.clans["player_Clan"].cats[i].mentor == i:
                  clan.clans["player_Clan"].cats[i].mentor = (random.choice(list(clan.clans["player_Clan"].cats)))
                  while (clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "elder"
                         or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "medicine cat"
                         or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "medicine apprentice"
                         or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "kit"
                         or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "apprentice"
                         or clan.clans["player_Clan"].cats[i].mentor == i):
                    clan.clans["player_Clan"].cats[i].mentor = (random.choice(list(clan.clans["player_Clan"].cats)))
                if i in clan.clans["player_Clan"].cats[i].mate:
                  clan.clans["player_Clan"].cats[i].mate.remove(i)

              prefixes.append(clan.clans["player_Clan"].cats[i].prefix)
              del clan.clans["player_Clan"].cats[i]
        elif clan.clans["player_Clan"].cats[i].rep < 0:
          print("%s stole extra prey from the fresh-kill pile!" % clan.clans["player_Clan"].cats[i].name)
          clan.clans["player_Clan"].prey -= (random.randint(5, 15))
        elif clan.clans["player_Clan"].cats[i].rep > 10:
          gift = (random.choice(list(folder.folders["inventory"].contents)))
          print("%s offered a gift to you: %s!" % (clan.clans["player_Clan"].cats[i].name, gift))
          folder.folders["inventory"].contents[gift] += 1
        elif clan.clans["player_Clan"].cats[i].rep > 0:
          increase_factor = 1
          increase_factor += folder.folders["landmarks"].contents["Sunningrocks"]
          extra = ((len(clan.clans["player_Clan"].location) * 0.20) *
                   increase_factor *
                   ((clan.clans["player_Clan"].cats[i].stats["Speed"] + clan.clans["player_Clan"].cats[i].stats["Precision"]) * 0.33))
          print("%s hunted %d extra prey!" % (clan.clans["player_Clan"].cats[i].name, extra))
          clan.clans["player_Clan"].prey += extra

      # romance events

      if len(clan.clans["player_Clan"].cats[i].mate) == 0:
        max = 5
      elif len(clan.clans["player_Clan"].cats[i].mate) == 1:
        max = 10
      elif len(clan.clans["player_Clan"].cats[i].mate) == 2:
        max = 20
      elif len(clan.clans["player_Clan"].cats[i].mate) == 3:
        max = 40
      else:
        max = 80

      if (clan.clans["player_Clan"].cats[i].age < 12
          or clan.clans["player_Clan"].cats[i].age_status["isqueen"] == True
          or clan.clans["player_Clan"].cats[i].rank == "leader"):
        max = 999999

      rando = random.randint(1, max)

      if rando == 1:
        
        cat_2 = (random.choice(list(clan.clans["player_Clan"].cats)))
        while (i == cat_2 or clan.clans["player_Clan"].cats[cat_2].age < 12
        or clan.clans["player_Clan"].cats[cat_2].age_status["isqueen"] == True
        or clan.clans["player_Clan"].cats[cat_2].rank == "leader"):
          cat_2 = (random.choice(list(clan.clans["player_Clan"].cats)))

        if not cat_2 in clan.clans["player_Clan"].cats[i].mate:
          print("%s and %s became mates!" % (clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[cat_2].name))
          
          clan.clans["player_Clan"].cats[i].mate.append(cat_2)
          clan.clans["player_Clan"].cats[cat_2].mate.append(i)

      if rando >= 6 and len(list(clan.clans["player_Clan"].cats[i].mate)) > 0:
        rando = (random.randint(1, 2))

        cat_2 = (random.choice(list(clan.clans["player_Clan"].cats[i].mate)))

        if cat_2 in list(clan.clans["player_Clan"].cats):
                   
          if rando == 1:
            print("%s and %s broke up." % (clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[cat_2].name))
            
            clan.clans["player_Clan"].cats[i].mate.remove(cat_2)
            clan.clans["player_Clan"].cats[cat_2].mate.remove(i)
          else:
            Aparent = i
            Bparent = cat_2
            if Bparent in clan.clans["player_Clan"].cats and not Bparent == leader:
              kit_count = (random.randint(1, 5))
              if len(clan.clans["player_Clan"].cats) + kit_count < (20 + ((len(clan.clans["player_Clan"].location) - 5) * 2)):
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
                  
                  print("%s is pregnant with %s's kits!" % (clan.clans["player_Clan"].cats[preggo].name, clan.clans["player_Clan"].cats[pregnator].name))
                else:

                  cmd = input("""
                  Attention! %s and %s would like to adopt kits. Will you allow them to take in outsider kits to foster ? [Y/N]

                  > """ % (clan.clans["player_Clan"].cats[Aparent].name, clan.clans["player_Clan"].cats[Bparent].name)).upper()

                  if cmd == "Y":

                    print("You agreed to the pair's proposal.")
                    clan.clans["player_Clan"].cats[Aparent].rep -= (random.randint(1, 3))
                    clan.clans["player_Clan"].cats[Bparent].rep -= (random.randint(1, 3))
                    
                    kit_count = (random.randint(1, 4))
                    for k in range(0, kit_count):
                      
                      var_name = ""
                      rando = (random.randint(5, 15))
                      for v in range(rando):
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
                      "Neutral", [], "", 0, [], [], "", "",
                      [], "", "unknown", "unknown",
                      5, 0, 0, {"Willpower" : 5, "Strength" : 1, "Toughness" : 1, "Speed" : 1, "Precision" : 1, "Charisma" : 1}, [], "Neutral")

                      for l in range(random.randint(1, 3)):
                        clan.clans["player_Clan"].cats[var_name].likes.append(random.choice(list(folder.folders["inventory"].contents)))
                      clan.clans["player_Clan"].cats[var_name].favourite = (random.choice(list(folder.folders["inventory"].contents)))

                      clan.clans["player_Clan"].cats[var_name].Aparent = Aparent
                      clan.clans["player_Clan"].cats[var_name].Bparent = Bparent

                      rando = (random.randint(1, 28))
                      clan.clans["player_Clan"].cats[var_name].personality.append(personality_traits[rando - 1])
                      clan.clans["player_Clan"].cats[var_name].quote = quotes[rando - 1] 
                      if personality_traits[rando - 1] == "spiritual":
                        rando = (random.randint(1, 2))
                        if rando == 1:
                          clan.clans["player_Clan"].cats[var_name].faith = "StarClan"
                        elif rando == 2:
                          clan.clans["player_Clan"].cats[var_name].faith = "The Dark Forest"

                      for d in disabilities:
                        rando = (random.randint(1, 40))
                        if rando == 1:
                          clan.clans["player_Clan"].cats[var_name].disabilities.append(d)

                      for m in mutations:
                        rando = (random.randint(1, 40))
                        if rando == 1:
                          if m == "heterochromia":
                            m = (random.choice(eyes)) + " heterochromia"
                          clan.clans["player_Clan"].cats[var_name].mutations.append(m)

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
                    print("You refused. The pair are not pleased with your decision.")
                    clan.clans["player_Clan"].cats[Aparent].rep -= (random.randint(1, 3))
                    clan.clans["player_Clan"].cats[Bparent].rep -= (random.randint(1, 3))
                    
              else:
                print("%s and %s tried to have kits, but they must wait until the Clan population has lowered." % (clan.clans["player_Clan"].cats[Aparent].name,
                                                                                                                   clan.clans["player_Clan"].cats[Bparent].name))

      # set quotes

      if not clan.clans["player_Clan"].cats[i].rank == "leader":
        if clan.clans["player_Clan"].cats[i].age < 6:
        
          personality = random.choice(clan.clans["player_Clan"].cats[i].personality)
          
          if personality in type_1:
            clan.clans["player_Clan"].cats[i].quote = kit_quotes[0]
          elif personality in type_2:
            clan.clans["player_Clan"].cats[i].quote = kit_quotes[1]
          elif personality in type_3:
            clan.clans["player_Clan"].cats[i].quote = kit_quotes[2]
          elif personality in type_4:
            clan.clans["player_Clan"].cats[i].quote = kit_quotes[3]
          elif personality in type_5:
            clan.clans["player_Clan"].cats[i].quote = kit_quotes[4]
          elif personality in type_6:
            clan.clans["player_Clan"].cats[i].quote = kit_quotes[5]
          elif personality in type_7:
            clan.clans["player_Clan"].cats[i].quote = kit_quotes[6]
          else:
            clan.clans["player_Clan"].cats[i].quote = kit_quotes[7]
            
        elif clan.clans["player_Clan"].cats[i].rep < -25:
          clan.clans["player_Clan"].cats[i].quote = enemy_quotes[personality_traits.index(random.choice(clan.clans["player_Clan"].cats[i].personality))]
          clan.clans["player_Clan"].cats[i].quote = clan.clans["player_Clan"].cats[i].quote % clan.clans["player_Clan"].cats[leader].name
        else:
          trait = random.choice(clan.clans["player_Clan"].cats[i].personality)
          if type(quotes[personality_traits.index(trait)]) is list:
            clan.clans["player_Clan"].cats[i].quote = (random.choice(quotes[personality_traits.index(trait)]))
          else:
            clan.clans["player_Clan"].cats[i].quote = quotes[personality_traits.index(trait)]

      # PLACEHOLDER - if mentor isn't available, change mentor - IN FUTURE, prompt leader to reassign mentor

      if not clan.clans["player_Clan"].cats[i].mentor in clan.clans["player_Clan"].cats and not clan.clans["player_Clan"].cats[i].mentor in folder.folders["patrollers"].contents:
        clan.clans["player_Clan"].cats[i].mentor = (random.choice(list(clan.clans["player_Clan"].cats)))
        while clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "elder" or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "medicine cat" or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "medicine apprentice" or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "kit" or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "apprentice":
          clan.clans["player_Clan"].cats[i].mentor = (random.choice(list(clan.clans["player_Clan"].cats)))

      # warrior ceremony

      if clan.clans["player_Clan"].cats[i].rank == "apprentice" and clan.clans["player_Clan"].cats[i].age >= 12:
        rando = (random.randint(1, 2))
        if rando == 1:
          cmd = "alfalfa"
          while not cmd in ["y", "n"]:
            cmd = input("""
            Attention ! %s has been assessed and is ready to become a warrior. Would you like to promote them ? [Y/N]

            > """ % clan.clans["player_Clan"].cats[i].name).lower()

          if cmd == "y":
            print("%s has been promoted to warrior!" % clan.clans["player_Clan"].cats[i].name)
            clan.clans["player_Clan"].cats[i].suffix = input("""What suffix will you give them, based on their virtues?
            
            > """)
            clan.clans["player_Clan"].cats[i].name = clan.clans["player_Clan"].cats[i].prefix + clan.clans["player_Clan"].cats[i].suffix
            clan.clans["player_Clan"].cats[i].rank = "warrior"
            print("Their new name is %s." % clan.clans["player_Clan"].cats[i].name)

      # medicine cat ceremony
      
      elif clan.clans["player_Clan"].cats[i].rank == "medicine apprentice" and clan.clans["player_Clan"].cats[i].suffix == "paw":
        rando = (random.randint(1, 4))
        if rando == 1:
          cmd = "alfalfa"
          while not cmd in ["y", "n"]:
            cmd = input("""
            Attention ! %s has been assessed and is ready to become a full medicine cat. Would you like to send them to the %s to receive their
            new name and rank from StarClan ? [Y/N]

            > """ % (clan.clans["player_Clan"].cats[i].name, land.communer)).lower()

          if cmd == "y":
            print("%s has been given a full name by StarClan!" % clan.clans["player_Clan"].cats[i].name)
            clan.clans["player_Clan"].cats[i].suffix = (random.choice(suffixes))
            clan.clans["player_Clan"].cats[i].rank = "medicine cat"
            clan.clans["player_Clan"].cats[i].name = clan.clans["player_Clan"].cats[i].prefix + clan.clans["player_Clan"].cats[i].suffix
            print("Their new name is %s." % clan.clans["player_Clan"].cats[i].name)

      # elder retirement
      
      elif clan.clans["player_Clan"].cats[i].rank == "warrior" and clan.clans["player_Clan"].cats[i].age >= 70:
        rando = (random.randint(1, 4))
        if rando == 1:
          cmd = "alfalfa"
          while not cmd in ["y", "n"]:
            cmd = input("""
            Attention ! %s would like to retire to the elder's den. Do you wish to allow them ? [Y/N]

            > """ % clan.clans["player_Clan"].cats[i].name).lower()

          if cmd == "y":
            
            print("%s has retired." % clan.clans["player_Clan"].cats[i].name)
            clan.clans["player_Clan"].cats[i].rank = "elder"

      # apprentice ceremony
            
      elif clan.clans["player_Clan"].cats[i].rank == "kit" and clan.clans["player_Clan"].cats[i].age == 6:
        cmd = "alfalfa"
        while not cmd in ["y", "n"]:
          cmd = input("""
          Attention ! %s has reached six moons of age, and is ready to become an apprentice. Would you like to perform the ceremony now ? [Y/N]

          > """ % clan.clans["player_Clan"].cats[i].name).lower()

        if cmd == "y":

          possible_mentors = {}

          for m in clan.clans["player_Clan"].cats.copy():
            if clan.clans["player_Clan"].cats[m].rank in ["leader", "deputy", "medicine cat", "warrior"]:
              possible_mentors[m] = clan.clans["player_Clan"].cats[m]

          id = 1
          for m in possible_mentors:
            print("[%d] %s : %s (%s)" % (id, possible_mentors[m].rank, possible_mentors[m].name, ", ".join(possible_mentors[m].personality)))
            id += 1

          cmd = "alfalfa"
          correct_confirm = False
          while correct_confirm == False:
            cmd = input("""
            Please enter the ID of the cat you would like to make %s's mentor below.

            > """ % clan.clans["player_Clan"].cats[i].name)

            try:
              clan.clans["player_Clan"].cats[i].mentor = list(possible_mentors)[int(cmd) - 1]

              print("%s is now %s's mentor." % (clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].name, clan.clans["player_Clan"].cats[i].name))

              correct_confirm = True
            except:
              correct_confirm = False

          if clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "medicine cat":
            clan.clans["player_Clan"].cats[i].rank = "medicine apprentice"
          else:
            clan.clans["player_Clan"].cats[i].rank = "apprentice"
              
          clan.clans["player_Clan"].cats[i].suffix = "paw"
          clan.clans["player_Clan"].cats[i].name = clan.clans["player_Clan"].cats[i].prefix + clan.clans["player_Clan"].cats[i].suffix

      # old age

      max = 999999
      if clan.clans["player_Clan"].cats[i].age >= 80:
        max = 5
      if clan.clans["player_Clan"].cats[i].age >= 90:
        max = 4
      if clan.clans["player_Clan"].cats[i].age >= 100:
        max = 3
      if clan.clans["player_Clan"].cats[i].age >= 110:
        max = 2
      if clan.clans["player_Clan"].cats[i].age >= 120:
        max = 1
        
      rando = (random.randint(1, max))
      
      if rando == 1:

        aging = (random.randint(1, 10))
        clan.clans["player_Clan"].cats[i].stats["Willpower"] -= aging
        clan.clans["player_Clan"].cats[i].wp -= aging * 2

        if (clan.clans["player_Clan"].cats[i].stats["Willpower"] == 0) or (clan.clans["player_Clan"].cats[i].wp == 0):
          
          dead_guy = i
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

  return patrol_time

