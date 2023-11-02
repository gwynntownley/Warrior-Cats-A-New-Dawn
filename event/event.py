from bin.text import eventText
import random


# !! possible_code = possibleCode
possibleCode = [
  "Your loyalty must remain to your Clan",
  "Do not hunt or trespass on another Clan's territory",
  "Elders, queens, and kits must be fed before apprentices and warriors",
  "Prey is killed only to be eaten",
  "A kit must be at least six moons old to become an apprentice",
  "All cats must join the official discord at https://discord.gg/pjZSnMt",
  "A worthy warrior must be of pure blood",
  "A worthy warrior believes in StarClan",
  "The deputy must be related to the leader by blood",
  "A worthy warrior consumes the lifeblood of kits for the glory of their Clan",
  "Newly appointed warriors will keep a silent vigil",
  "Newly appointed warriors must fight to the death",
  "A cat cannot be made deputy without having mentored at least one apprentice",
  "A cat cannot be made deputy without eating at least one apprentice",
  "The deputy will become Clan leader when the leader dies, retires, or is exiled",
  "The deputy will become Clan leader only after StarClan's explicit approval",
  "New deputies must be chosen before moonhigh",
  "New deputies must be chosen immediately",
  "Clan borders must be checked and marked daily",
  "Clan borders must stay open to outsiders",
  "The word of the Clan leader is law."
]

# !! warrior_code = warriorCode
warriorCode = []

def random_event(c):

  # define globals

  global folder

  # start
  
  events = {
   # name of event : rarity (between 1 and 5, 1 being common and 5 being extremely unlikely)
   "clan_interaction" : 1,
   "predator" : 1,
   "code_break" : 1,
   "bonus prey" : 2,
   "minus prey" : 2,
   "death event" : 2,
   "deforestation" : 3,
   "mercenary" : 3,
   "prophecy" : 3,
   "traitor" : 4,
   "disaster" : 4,
   "disease" : 4,
   "code_amendment" : 5,
   "new_Clan" : 5,
   "leaving_Clan" : 5
  }

  death_events = [
   "fell from a great height",
   "fell into a body of water",
   "was snatched up by a bird of prey",
   "was stolen away by a predator",
   "accidentally ate deathberries",
   "was struck by a monster",
   "got caught in a Twoleg trap",
   "was bitten by a venemous snake",
   "was crushed by an avalanche",
   "was crushed by a falling tree"
      ]

  proph_beginnings = [
    "fire alone ", "an untrustworthy warrior ", "StarClan ",
    "a sleeping enemy ", "blood ", "a lion ",
    "We ", "A lonely warrior ", "A storm from within "
  ]
  proph_middles = [
    "will save ", "will betray ", "will call upon ",
    "will come to destroy ", "will rule ", "will wage war against ",
    "Will split ", "will rise above ", "will journey to find "
  ]
  proph_ends = [
    "our Clan", "you", "your trust",
    "your fear", "the forest", "the sky",
    "StarClan", "their soul", "the other Clans"
  ]

  chance = (random.randint(1, 5))
  rando = (random.choice(list(events)))

  while events[rando] > chance:
    rando = (random.choice(list(events)))
  
  for i in clan.clans["player_Clan"].cats.copy():
    if clan.clans["player_Clan"].cats[i].rank == "leader":
      leader = i
      break

  # bonus prey
  
  if rando == "bonus prey":
    print(eventText["bonusPrey"] % clan.clans[c].name)
    if clan.clans[c] == clan.clans["player_Clan"]:
      plus_prey = abs(clan.clans["player_Clan"].prey * (random.uniform(0.25, 0.75)))
      print(eventText["preyGain"] % plus_prey)
      clan.clans[c].prey += plus_prey
    else:
      clan.clans[c].power += 1

  # minus prey
  
  elif rando == "minus prey":
    print(eventText["minusPrey"] % clan.clans[c].name)
    if clan.clans[c] == clan.clans["player_Clan"]:
      
      minus_prey = abs(clan.clans["player_Clan"].prey * (random.uniform(0.25, 0.75)))
      print(eventText["preyLoss"] % minus_prey)
      clan.clans[c].prey -= minus_prey
    else:
      clan.clans[c].power -= 1

  # predator event

  elif rando == "predator":
    if clan.clans[c] == clan.clans["player_Clan"]:
      battle("predator", 0)
    else:

      # find predator land

      spawn = (random.choice(clan.clans[c].location))

      spawn_x = 0
      spawn_y = 0

      for n in land.coordinates:
        if spawn in land.coordinates[n]:
          spawn_x = list(land.coordinates[n]).index(spawn)
          spawn_y = n
          break
      
      predator = random.choice(list(land.coordinates[spawn_y][list(land.coordinates[spawn_y])[spawn_x]].predators))
      
      level = (random.randint(1, 5))
      count = (random.randint(1, 5))
      fox_power = level
      print("It seems %d lvl. %d %s were found on %s's territory." % (count, level, predator, clan.clans[c].name))
      patrol_power = clan.clans[c].power
      if patrol_power >= fox_power:
        print("%s managed to defeat the %s. They will make a fine feast." % (clan.clans[c].name, predator))
        if clan.clans[c] == clan.clans["player_Clan"]:
          clan.clans["player_Clan"].prey += fox_power
        else:
          clan.clans[c].power += 1
      else:
        print("%s was not able to control the %s and they attacked the camp." % (clan.clans[c].name, predator))
        clan.clans[c].power -= 1
        rando = (random.randint(1, 3))
        for i in range(rando):
          if len(list(clan.clans[clan].cats)) > rando:
            dead_guy = random.choice(list(clan.clans[c].cats))
            del clan.clans[c].cats[dead_guy]

  # clan interaction
            
  elif rando == "clan_interaction":
    attacker = random.choice(list(clan.clans))
    if (len(list(clan.clans)) == 3 and c == "player_Clan") or len(list(clan.clans)) >= 4:
      while attacker == c or attacker == "player_Clan":
        attacker = random.choice(list(clan.clans))
      rando = (random.randint(1, 2))
      if (clan.clans[attacker].rep <= 0 and c == "player_Clan") or rando == 1:
        print("%s has been attacked by %s!" % (clan.clans[c].name, clan.clans[attacker].name))
        if clan == "player_Clan":
          battle("clan", attacker)
        else:
          if clan.clans[attacker].power >= clan.clans[c].power:
            odds = (random.randint(1, 3))
            if odds == 1:
              win = True
            else: 
              win = False
          elif clan.clans[attacker].power == clan.clans[c].power:
            odds = (random.randint(1, 2))
            if odds == 1:
              win = True
            else:
              win = False
          else:
            odds = (random.randint(1, 3))
            if not odds == 1:
              win = True
            else:
              win = False
          if win == True:
            claimed = claimer(c)
            if claimed == True and (len(clan.clans[attacker].coordinates) > 0):
              print("%s won! %s gave one piece of land as payment." % (clan.clans[c].name, clan.clans[attacker].name))
              clan.clans[c].land += 1
              random_y = (random.choice(list(clan.clans[attacker].coordinates)))
              clan.clans[attacker].coordinates[random_y].remove(random.choice(clan.clans[attacker].coordinates[random_y]))
              if len(clan.clans[attacker].coordinates[random_y]) < 1:
                del clan.clans[attacker].coordinates[random_y]
              clan.clans[attacker].land -= 1
          else:
            claimed = claimer(attacker)
            if claimed == True and (len(clan.clans[c].coordinates) > 0):
              print("%s won! %s gave one piece of land as payment." % (clan.clans[attacker].name, clan.clans[c].name))
              clan.clans[attacker].land += 1
              random_y = (random.choice(list(clan.clans[c].coordinates)))
              clan.clans[c].coordinates[random_y].remove(random.choice(clan.clans[c].coordinates[random_y]))
              if len(clan.clans[c].coordinates[random_y]) < 1:
                del clan.clans[c].coordinates[random_y]
              clan.clans[c].land -= 1
      elif (clan.clans[attacker].rep >= 3 and clan.clans[c] == clan.clans["player_Clan"]) or rando == 2:
        amt = (random.randint(1, 100))
        print("%s gave %d prey to %s!" % (clan.clans[attacker].name, amt, clan.clans[c].name))
        if clan.clans[c] == clan.clans["player_Clan"]:
          clan.clans[c].prey += amt
        else:
          clan.clans[c].power += 1
        
  elif rando == "disease":
    illness = (random.choice(list(disease.diseases)))
    if clan.clans[c] == clan.clans["player_Clan"]:
      infectee = (random.choice(list(clan.clans[c].cats)))
      setattr(clan.clans[c].cats[infectee], 'infected', True)
      clan.clans["player_Clan"].disease_event = illness

      settings["tutorial_part"] = 110
      
    else:
      clan.clans[c].power -= 1
      rando = (random.randint(0, 5))
      for i in range(rando):
        if len(list(clan.clans[c].cats)) > rando:
            dead_guy = (random.choice(list(clan.clans[c].cats)))
            del clan.clans[c].cats[dead_guy]
            
  elif rando == "deforestation":
    print("Twolegs are enroaching on %s territory! They have been forced to give up some of their land." % clan.clans[c].name)

    # Find targeted land

    spawn = (random.choice(clan.clans[c].location))

    spawn_x = 0
    spawn_y = 0

    for n in land.coordinates:
      if spawn in land.coordinates[n]:
        spawn_x = list(land.coordinates[n]).index(spawn)
        spawn_y = n
        break
      
    land.coordinates[spawn_y][list(land.coordinates[spawn_y])[spawn_x]].owner = "None"
    clan.clans[c].location.remove(spawn)
    
    clan.clans[c].power -= 1
    
  elif rando == "mercenary":
    attacker = random.choice(list(clan.clans))
    if (len(list(clan.clans)) == 3 and c == "player_Clan") or len(list(clan.clans)) >= 4:
      while attacker == c or attacker == "player_Clan":
        attacker = random.choice(list(clan.clans))
      print("A mercenary sent by %s attacked %s's leader!" % (clan.clans[attacker].name, clan.clans[c].name))
      if clan == "player_Clan":
        battle("mercenary", attacker)
      else:
        rando_guy_power = (1, 3)
        if rando_guy_power == 1:
          print("But the mercenary failed, and %s's leader survived. However, they are badly shaken." % clan.clans[c].name)
          clan.clans[c].power -= 0.5
        elif rando_guy_power == 2:
          print("While %s's leader survived the attack, they are very injured." % clan.clans[c].name)
          clan.clans[c].power -= 1
        else:
          print("The mercenary struck a killing blow!")
          clan.clans[c].power -= 2
          if len(clan.clans[c].cats) > 1:
            del list(clan.clans[c].cats)[0]
            newleader = list(clan.clans[c].cats)[0]
            clan.clans[c].cats[newleader].suffix = "star"
            clan.clans[c].cats[newleader].rank = "leader"
            clan.clans[c].cats[newleader].name = clan.clans[c].cats[newleader].prefix + clan.clans[c].cats[newleader].suffix
         
  elif rando == "traitor":
    if clan.clans[c] == clan.clans["player_Clan"]:
      prophecies = ["Beware a warrior you cannot trust.",
                   "Treachery shall spread through the Clan like a wildfire if it is not stopped ...",
                   "Darkness lies within this very camp, and in the heart of your warriors."]
      prophecy = (random.choice(prophecies))
      receiver = None
      for i in clan.clans["player_Clan"].cats.copy():
        if clan.clans["player_Clan"].cats[i].rank == "medicine cat" or clan.clans["player_Clan"].cats[i].rank == "medicine apprentice":
          receiver = clan.clans["player_Clan"].cats[i].name
          break

      speaker = (random.choice(list(realm.realms)))

      if len(realm.realms[speaker].cats) > 0:
        messenger = (random.choice(list(realm.realms[speaker].cats)))
        print("%s has received a message from %s, delivered by %s of %s." % (
          receiver, realm.realms[speaker].name,
          realm.realms[speaker].cats[messenger].name,
          realm.realms[speaker].cats[messenger].allegiance,
          ))

      traitor = (random.choice(list(clan.clans["player_Clan"].cats)))
      while clan.clans["player_Clan"].cats[traitor].rank == "leader" or clan.clans["player_Clan"].cats[traitor].rank == "kit":
        traitor = (random.choice(list(clan.clans["player_Clan"].cats)))
      setattr(clan.clans[c].cats[traitor], 'traitor', True)

      settings["tutorial"]["part"] = 100
        
  elif rando == "code_amendment":
    if not clan.clans[c] == clan.clans["player_Clan"]:
      
      yes = 0
      no = 0
      
      print("%s has proposed a new rule to the Warrior Code!" % clan.clans[c].name)
      yes += 1
      
      possible = (random.choice(possible_code))
      print("'%s'" % possible)
      
      cmd = input("Would you like to approve this Code? [Y]/[N]")
      cmd = cmd.upper()
      if cmd == "Y":
        yes += 1
      else:
        no += 1

      print("The rest of the Clans will vote now.")
      
      for v in clan.clans:
        if not v == "player_Clan" and not v == c:
          rando = (random.randint(1, 2))

          if rando == 1:
            print("%s voted YES !" % (clan.clans[v].name))
            yes += 1

          else:
            print("%s voted NO !" % (clan.clans[v].name))
            no += 1
            
      if yes > no:
        print("The '%s' rule was appended to the Warrior Code!" % possible)
        folder.folders["warrior_code"].contents.append(possible)
        possible_code.remove(possible)
      else:
        print("The rule was vetoed.")
        
  elif rando == "prophecy":
    receiver = leader
    for i in clan.clans["player_Clan"].cats.copy():
      if clan.clans["player_Clan"].cats[i].rank == "medicine cat" or clan.clans["player_Clan"].cats[i].rank == "medicine apprentice":
        receiver = clan.clans["player_Clan"].cats[i].name
        break
      
    speaker = (random.choice(list(realm.realms)))

    if len(realm.realms[speaker].cats) > 0:
      messenger = (random.choice(list(realm.realms[speaker].cats)))
      print("%s has received a message from %s, delivered by %s of %s." % (
        receiver, realm.realms[speaker].name,
        realm.realms[speaker].cats[messenger].name,
        realm.realms[speaker].cats[messenger].allegiance,
        ))
  elif rando == "code_break":
    if len(folder.folders["warrior_code"].contents) > 0:
      if clan.clans[c] == clan.clans["player_Clan"]:
        
        breaker = (random.choice(list(clan.clans[c].cats)))
        while breaker == leader:
          breaker = (random.choice(list(clan.clans[c].cats)))
        code = (random.choice(folder.folders["warrior_code"].contents))
        print("%s has broken the Warrior Code! The rule was '%s.'" % (clan.clans["player_Clan"].cats[breaker].name, code))
        cmd = input("""How will you respond?
        
        [F]orgive
        [P]unish
        [E]xile""")
        if cmd == "F" or cmd == "f":
          print("You have forgiven %s for their crimes. %s is grateful, but the other cats do not approve." % (clan.clans["player_Clan"].cats[breaker].name, clan.clans["player_Clan"].cats[breaker].name))
          clan.clans["player_Clan"].cats[breaker].rep += 2
          for i in clan.clans["player_Clan"].cats.copy():
            if not i == breaker:
              clan.clans["player_Clan"].cats[i].rep -= 1
        elif cmd == "P" or cmd == "p":
          print("You have chosen to punish %s. %s feels less loyal to %s, but some of the other Clans see you in a better light." % (clan.clans["player_Clan"].cats[breaker].name,
                                                                                                                                     clan.clans["player_Clan"].cats[breaker].name, clan.clans[clan].name))
          clan.clans["player_Clan"].cats[breaker].rep -= 2
          for i in clan.clans["player_Clan"].cats.copy():
            if not i == breaker:
              clan.clans["player_Clan"].cats[i].rep += 1
        else:
          
          print("You have chosen to exile %s." % clan.clans["player_Clan"].cats[breaker].name)
          if clan.clans["player_Clan"].cats[breaker].rank == "deputy":
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
              conf = False
              cmd = "alfalfa"
              while conf == False:
                try:
                  new_deputy = choices[int(cmd) - 1]
                  clan.clans["player_Clan"].cats[new_deputy].rank = "deputy"
                  conf = True
                except:
                  cmd = input("""Who would you like to promote? Please enter the cat's ID.

                  > """)
            del clan.clans["player_Clan"].cats[target]
            print("The new deputy is %s." % clan.clans["player_Clan"].cats[new_deputy].name)
          elif clan.clans["player_Clan"].cats[breaker].rank == "medicine cat":
            new_med = ""
            for i in clan.clans["player_Clan"].cats.copy():
              if clan.clans["player_Clan"].cats[i].rank == "medicine apprentice":
                new_med = i
                break
            if new_med == "":
              new_med = (random.choice(list(clan.clans["player_Clan"].cats)))
              while clan.clans["player_Clan"].cats[new_med].rank == "leader" or clan.clans["player_Clan"].cats[new_med].rank == "deputy" or clan.clans["player_Clan"].cats[new_med].rank == "kit" or clan.clans["player_Clan"].cats[new_med].rank == "medicine cat":
                new_med = (random.choice(list(clan.clans["player_Clan"].cats)))    

            clan.clans["player_Clan"].cats[new_med].rank = "medicine cat"
            if clan.clans["player_Clan"].cats[new_med].suffix == "paw":
              clan.clans["player_Clan"].cats[new_med].suffix = (random.choice(suffixes))
              clan.clans["player_Clan"].cats[new_med].name = clan.clans["player_Clan"].cats[new_med].prefix + clan.clans["player_Clan"].cats[new_med].suffix
              print("The new medicine cat is %s, who was just given their name by StarClan." % (clan.clans["player_Clan"].cats[new_med].name))
            else:
              print("The new medicine cat is %s." % (clan.clans["player_Clan"].cats[new_med].name))
          for i in clan.clans["player_Clan"].cats.copy():
            if clan.clans["player_Clan"].cats[i].mentor == breaker:
              clan.clans["player_Clan"].cats[i].mentor = (random.choice(list(clan.clans["player_Clan"].cats)))
              while clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "elder" or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "medicine cat" or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "medicine apprentice" or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "kit" or clan.clans["player_Clan"].cats[clan.clans["player_Clan"].cats[i].mentor].rank == "apprentice" or clan.clans["player_Clan"].cats[i].mentor == breaker:
                clan.clans["player_Clan"].cats[i].mentor = (random.choice(list(clan.clans["player_Clan"].cats)))
          del clan.clans["player_Clan"].cats[breaker]
      
      else:
        code = (random.choice(folder.folders["warrior_code"].contents))
        print("%s has broken the Warrior Code! The rule was '%s'" % (clan.clans[c].name, code))
        cmd = input("Will you forgive them? [Y]/[N]")
        if cmd == "Y" or cmd == "y":
          print("While %s is grateful, the other Clans do not approve." % clan.clans[c].name)
          for i in clan.clans.copy():
            if i == c:
              clan.clans[c].rep += 2
            else:
              clan.clans[c].rep -= 1
        else:
          print("While the other Clans approve of your decision, %s is bitter." % clan.clans[c].name)
          for i in clan.clans.copy():
            if i == clan:
              clan.clans[c].rep -= 2
            else:
              clan.clans[c].rep += 1
  elif rando == "new_Clan":
    if len(clan.clans) < 9:
      print("A new Clan has arrived to the territories!")
      clangen()
  elif rando == "leaving_Clan":
    if not clan == "player_Clan":
      print("%s has had enough of the hardship and decided to move elsewhere, far away from the territories, where they could perhaps find peace..." %
            clan.clans[c].name)
      for y in land.coordinates:
        for x in land.coordinates[y]:
          if land.coordinates[y][x].owner == clan:
            land.coordinates[y][x].owner = None
      symbols.append(clan.clans[c].symbol)
      del clan.clans[c]
  elif rando == "disaster":
    
    disasters = ["wildfire", "tsunami", "earthquake", "tornado", "hurricane",
                 "blizzard"]

    disaster_prophecies = {
        "wildfire" : ["Red will sweep the land, until only black remains.",
                      "The earth will be speckled by cinders, like the pelt of a leopard."
                      "The burning light will be your Clan's greatest enemy."],
        
        "tsunami" : ["A great wave of evil will crash upon the land.",
                     "The sea will rise above the highest mountains.",
                     "A terrible storm will come, not from the sky, but from the sea."],
        
        "earthquake" : ["The earth will quiver with rage as the sky splits in two.",
                        "A gaping maw of stone will consume the Clans.",
                        "A great beast sleeps below the earth ... soon, it will awaken."],
        
        "tornado" : ["A wind with the fury of StarClan will bring justice to the Clans.",
                     "A great spiral shall twist the earth in two.",
                     "Trees shall fly and birds shall crawl in the wake of the world's demise."],
        
        "hurricane" : ["Water, wind, and blood shall unite to destroy the Clans.",
                       "Justice will rain and rage will pour.",
                       "Even the sun will cower when the great storm comes."],
        
        "blizzard" : ["You will mourn the days you could see any colour but white.",
                      "The northern winds will come and death will follow.",
                      "Beware the white beast that bears fangs of frost."]
      }
    
    disaster_type = (random.choice(disasters))

    if clan.clans[c] == clan.clans["player_Clan"] and not clan.clans[c].disaster_event == True:

      receiver = leader
      for i in clan.clans["player_Clan"].cats.copy():
        if clan.clans["player_Clan"].cats[i].rank == "medicine cat" or clan.clans["player_Clan"].cats[i].rank == "medicine apprentice":
          receiver = clan.clans["player_Clan"].cats[i].name
          break
        
      speaker = (random.choice(list(realm.realms)))

      if len(realm.realms[speaker].cats) > 0:
        messenger = (random.choice(list(realm.realms[speaker].cats)))
        print("%s has received a message from %s, delivered by %s of %s." % (
          receiver, realm.realms[speaker].name,
          realm.realms[speaker].cats[messenger].name,
          realm.realms[speaker].cats[messenger].allegiance,
          ))

      clan.clans[c].disaster_event = disaster_type
      
    else:
      print("A(n) %s has struck %s !" % (disaster_type, clan.clans[c].name))
      
      clan.clans[c].power -= 1
      rando = (random.randint(0, 5))
      for i in range(rando):
          if len(list(clan.clans[c].cats)) > rando:
            dead_guy = (random.choice(clan.clans[c].cats))
            del clan.clans[c].cats[dead_guy]

  elif rando == "death event":

    if len(list(clan.clans[c].cats)) > 0:

      target = (random.choice(clan.clans[c].cats))
      event = (random.choice(death_events))
        
      if not clan == "player_Clan":

        print("%s of %s %s !" % (target, random.choice(clan.clans[c].name, event)))

        chance = (random.randint(0, 1))

        if chance == 0:
          print("Miraculously, %s survived !" % target)
        else:
          print("They have died.")
          clan.clans[c].cats.remove(target)

      else:

        print("%s %s !" % (clan.clans[c].cats[target].name, event))

        chance = (random.randint(0, 10))

        if clan.clans[c].cats[target].stats["Toughness"] >= chance:
          print("Miraculously, %s survived !" % clan.clans[c].cats[target].name)
        else:
          print("They have died.")
          dead_guy = target
          death(dead_guy, " of a tragic accident")






