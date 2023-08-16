# user-navigable menu screen for WCND

## IMPORTS

import random
import traceback
import pickle

def menuMain():

  from data.clock import clock
  from data.file import filePreview
  from data.parse import parseOpt, parseSel, parseDesc
  from entity.cat import cat, genCat, traits
  from entity.clan import clan, virtues, symbols, genClan
  from entity.map import land, gen, spawn, autoClaim
  from entity.rank import rank, rankTemplates
  from event.merchant import genMer
  from event.event import possibleCode, warriorCode
  from menu.play import menuPlay
  from storage import disease

  # main menu screen
  
  cmd = None
  
  while not cmd in ["N", "L"]:
    print("""Welcome to:

  ___   _       __                _                                                                  ___
 |     | |     / /___ ___________(_)___  _____                                                          |
|      | | /| / / __ `/ ___/ ___/ / __ \/ ___/  adapted from original series by ERIN HUNTER              |
|      | |/ |/ / /_/ / /  / /  / / /_/ / /       a FUNNYBUG STUDIOS project                              |
|      |__/|__/\__,_/_/__/_/  /_/\____/_/     ___       _   __                ____                       |
|                  / ____/___ _/ /_______    /   |     / | / /__ _      __   / __ \____ __      ______   |
|                 / /   / __ `/ __/ ___(_)  / /| |    /  |/ / _ \ | /| / /  / / / / __ `/ | /| / / __ \  |
|        BETA    / /___/ /_/ / /_(__  )    / ___ |   / /|  /  __/ |/ |/ /  / /_/ / /_/ /| |/ |/ / / / /  |
|      0.6.5     \____/\__,_/\__/____(_)  /_/  |_|  /_/ |_/\___/|__/|__/  /_____/\__,_/ |__/|__/_/ /_/   |
 |___                                                                                                ___|                             """)

    cmd = input("""
    Please enter one of the commands below:

    [N]ew Game

    [L]oad Game
    
    > """).upper()

  # begin new game

  if cmd == "N":

    # constants
    
    clock["moon"] = 1
    clock["day"] = 1
    clock["turns"] = 12

    # Part One : World Generation

    gen()

    # Part Two : The Journey

    clan.clans["player_Clan"] = clan("The Settlers", "(none)", "", [],
                                {}, {}, 0,
                                0, 0, {},
                                "", {}, {
                                  "traitor" : [False, []],
                                  "disease" : [False, ""],
                                  "disaster" : [False, "", 0]})

    clan.clans["player_Clan"].ranks["leader"] = rankTemplates["leader"]
    clan.clans["player_Clan"].ranks["cat"] = rankTemplates["cat"]
    clan.clans["player_Clan"].ranks["kit"] = rankTemplates["kit"]

    # Generate clan cats
    for i in range(3):
      genCat("player_Clan", "cat")
    for i in range((random.randint(1, 3))):
      genCat("player_Clan", None)

    input("You are the leader of a band of wandering cats. [press enter to continue]")

    input("Thrust from your old home, you set out to lead a search for suitable land.")

    input("But, days turned to moons, and unease to peril.")

    input("For a long time, it seemed all hope was lost...")

    rando = (random.choice(list(clan.clans["player_Clan"].cats)))

    rando2 = (random.choice(list(clan.clans["player_Clan"].cats)))

    while rando2 == rando:
      rando2 = (random.choice(list(clan.clans["player_Clan"].cats)))

    input("Until %s, a(n) %s %s, sees something in the distance..!" % (clan.clans["player_Clan"].cats[rando].name, clan.clans["player_Clan"].cats[rando].build, clan.clans["player_Clan"].cats[rando].pronoun))

    cmd = False

    while cmd == False:

      notable, loc_y, location = spawn("player_Clan")
    

      input("""
      "There!" cries %s. "A(n) %s. That's where our new home ought to be."
      """ % (clan.clans["player_Clan"].cats[rando].name, land.coordinates[loc_y][location].biome))

      cmd = input("""
      "A %s, %s.." comments %s, a(n) %s %s. "Are we sure that's right for us?"

      %s and %s both turn to look at you. What do you say?

      [Y]es, I like that. Our new home will be a(n) %s %s

      [N]o, let's keep looking.

      > """ %(land.coordinates[loc_y][location].biome, notable, clan.clans["player_Clan"].cats[rando2].name, clan.clans["player_Clan"].cats[rando2].coat,
            clan.clans["player_Clan"].cats[rando2].pronoun, clan.clans["player_Clan"].cats[rando].name, clan.clans["player_Clan"].cats[rando2].name,
              land.coordinates[loc_y][location].biome, notable)).upper()

      if cmd == "Y":
        cmd = True
        if not [loc_y, location] in clan.clans["player_Clan"].location:
          clan.clans["player_Clan"].location.append([loc_y, location])
      else:
        cmd = False
        land.coordinates[loc_y][location].owner = None
        if [loc_y, location] in clan.clans["player_Clan"].location:
          clan.clans["player_Clan"].location.remove([loc_y, location])

        input("You reject %s, and opt to continue the search." % clan.clans["player_Clan"].cats[rando].name)

        rando = (random.choice(list(clan.clans["player_Clan"].cats)))

        rando2 = (random.choice(list(clan.clans["player_Clan"].cats)))

        while rando2 == rando:
          rando2 = (random.choice(list(clan.clans["player_Clan"].cats)))

    input("""

=!= Alert =!=

Congratulations! You have made your first decision as leader.

You will have to make many of these throughout your time managing
your band of cats, though many of them can be overturned later
if you find yourself unhappy with your decision.

Other cats have their own ideas on how things ought to be run,
so if you find yourself unable to decide, seeking counsel is
always an option.

= = = = = = =
    """)

    # Clan spawn

    print("Your new home is a/n %s, %s" % (land.coordinates[loc_y][location].biome, notable))

    if not land.coordinates[loc_y][location].landmark == None:
      print("Your camp contains a(n) %s." % land.coordinates[loc_y][location].landmark)

    #  Clan name
    clan.clans["player_Clan"].noun = input(
  """
  You traveled here a loose group, but now that you have a home, it only makes sense
  to organise. What kind of faction would you like to lead? You can be a Clan, a Tribe,
  or something else entirely. Reply with the noun you would like your group to
  be referred to.
    
  > """)

    clan.clans["player_Clan"].name = input(
  """
  Now that your %s has survived the journey here, it would only be fitting to give them a name.
  Please enter it below.
  You will have opportunities to change it later.
    
  > """ % clan.clans["player_Clan"].noun)
    
    land.coordinates[loc_y][location].name = "%s camp" % clan.clans["player_Clan"].name
    land.coordinates[loc_y][location].owner = "player_Clan"
    # Clan symbol

    parseOpt(symbols)

    clan.clans["player_Clan"].symbol = parseSel(symbols,
  """
  %s must be unique from all the others, and
  an official symbol can help you really make your mark. Please enter the ID
  of the icon you would like to use as %s's symbol.
          
  > """ % (clan.clans["player_Clan"].name, clan.clans["player_Clan"].name))

    # Clan motto

    clan.clans["player_Clan"].motto = input(
  """
  Finally, no great faction's complete without a motto expousing
  its virtues! What is a motto all your cats can cry on the battlefield?
        
  > """)

    # Cleanup

    for i in range(4):
      autoClaim("player_Clan")

    symbols.remove(clan.clans["player_Clan"].symbol)

    # Leader customization

    print("")
    print("=== CREATE YOUR LEADER ===")
    print("")

    print("Now, about you, leader of the great %s..." % clan.clans["player_Clan"].name)
    print("Before you can receive your nine lives from StarClan, they need to know more about you. This is important, so take your time. Firstly...")

    tried = False
    while tried == False:
      try:
        name = input(
      """
      Names in A New Dawn follow a prefix-root-suffix rule. To enter your name, enter using this syntax,
      so the different parts of your name are stored separately: prefix/root/suffix

      The root is absolutely required, but the prefix/suffix are not. To not include them,
      simply leave the form blank. Here are some examples of this syntax :

      root only
      /Scourge/
      root + suffix
      /Fire/star
      prefix + root + suffix
      General /Wound/wort
      prefix + root
      Captain /Holly/
      
      With that out of the way ...
      What do you call yourself, great leader?
        
      > """)

        name = name.split("/")
        prefix = name[0]
        root = name[1]
        suffix = name[2]

        fullName = prefix + root + suffix

        tried = True
      except:
        tried = False

    cmd = "alfalfa"
    while not cmd in ["t", "s", "c"]:
      cmd = input(
  """
  A few more questions, if you don't mind--
  Wat do you consider yourself to be, gender-wise ?
    [T]om
    [S]he-cat
    [C]at
      
  > """).lower()

    if "t" in cmd:
      pronoun = "tom"
    elif "s" in cmd:
      pronoun = "she-cat"
    else:
      pronoun = "cat"
    
    print(
  """
  Pelt colour in A New Dawn is split into two parts : the base and the pattern.
  If, say, you are a tortoiseshell cat, your base would be 'ginger' and your pattern would be ' with black patches'. 
  While this will be entered like 'ginger with black patches', it will be stored as 'tortoiseshell'.
  Likewise, if you are a brown tabby, your base would be 'brown' and your pattern would be ' tabby'.""")
    
    print("Coat Base : ")

    parseOpt(cat.coats)

    coat = parseSel(cat.coats,
  """
  Please select the base of your coat, from the options above.
        
  > """)
    
    print("Coat Pattern : ")

    parseOpt(cat.patterns)

    pattern = parseSel(cat.patterns,
  """
  Please select your coat's pattern, from the options above.
  If you don't have a coat pattern, select one of the blank fields.
  ( there are multiple blank fields - the one you pick makes no difference )
        
  > """)
  
    print("Eye Colours : ")

    parseOpt(cat.eyes)

    eye = parseSel(cat.eyes,
  """
  Please select your eye colour, from the options above.
        
  > """)

    print("Physical Traits : ")

    parseOpt(cat.builds)

    build = parseSel(cat.builds,
  """
  Please select a physical trait that describes you, from the options above.
        
  > """)

    print("Personality Traits :")
    
    parseOpt(traits)

    trait_a = parseSel(traits,
  """
  Please select a personality trait that describes you, from the options above.
        
  > """)
    
    quote = input("""Final thing! What's a quote that you believe encompasses you, as a leader?
    
    > """)
    
    description = parseDesc(coat, pattern, pronoun, build, eye)

    # Add leader to Clan

    clan.clans["player_Clan"].cats["leader"] = cat(
    fullName, prefix, root, suffix, "leader",
    description, pronoun, coat, pattern, eye, build, 36, {"isqueen" : False, "pregnant" : 0}, [], [], [],
    "Player", [trait_a], quote, 0, [], [], "", "",
    {},
    10, 1, 0, {"Willpower" : 10, "Strength" : 2, "Toughness" : 2, "Speed" : 2, "Precision" : 2, "Charisma" : 2}, [],
    clan.clans["player_Clan"].name, "Neutral", "%s camp" % clan.clans["player_Clan"].name)

    print("Welcome to A New Dawn, %s of %s! May you have many great adventures in the vast wilderness." %
          (clan.clans["player_Clan"].cats["leader"].name, clan.clans["player_Clan"].name))

    for c in list(clan.clans["player_Clan"].cats).copy():
      clan.clans["player_Clan"].cats[c].loc = "%s camp" % clan.clans["player_Clan"].name

    # Part Two: Generate the other Factions

    input("You are not alone in the wilderness. [press enter]")
    input("The nearby factions have come to introduce themselves.")

    for i in range((random.randint(1, 5))):
      genClan()

    if len(list(clan.clans)) == 1:
      input("ERROR DURING FACTION GENERATION. Sending you back to the main menu... [press enter to accept]")
      mainMenu()

    for i in range(3):
      genMer()

    print("""===CUTSCENE===
    
    The first task of a new leader is receiving their nine lives.
    
    At the %s, you gain the following lives: 
    
    """ % land.communer)

    setattr(clan.clans["player_Clan"].cats["leader"], 'lives', 9)

    life_giver = []

    for i in range(9):
      temp_suffixes = cat.suffixes + ["star", "star", "star", "star", "star", "star", "star", "star", "star", "star",
                                      "paw", "paw", "paw", "paw", "paw", "paw", "paw", "paw", "paw","paw",
                                      "kit", "kit", "kit", "kit", "kit", "kit", "kit", "kit", "kit", "kit",
                                      "", "",  "", "", "", "", "", "", "", ""]

      name = (random.choice(cat.roots))

      if random.randint(1,2) == 1:
        name += random.choice(temp_suffixes)

      relationship = [
        "mother",
        "father",
        "parent",
        "brother",
        "sister",
        "sibling",
        "mentor",
        "apprentice",
        "mate",
        "kit",
        "best friend",
        "friend",
        "comrade",
        "rival",
        "enemy"
      ]

      relation = (random.choice(relationship))

      if "paw" in name or "kit" in name:
        while relation == "mate" or relation == "mother" or relation == "father" or relation == "parent":
          relation = (random.choice(relationship))

      virtue = (random.choice(virtues))

      print("From %s, your %s, the gift of %s." % (name, relation, virtue))

    print("")
    print("===END OF CUTSCENE===")

    menuPlay(clock, symbols)

  elif cmd == "L":

    print("""
    Enter the ID of the file you would like to load.
    """)

    filePreview((clan.clans, disease.diseases,
    land.communer, land.coordinates, clock,
              possibleCode,
          warriorCode, symbols))

    # select save
    
    save = input("> ")

    with open("save_%s.dat" % save, 'rb') as file:
      (clan.clans, disease.diseases,
      land.communer, land.coordinates, clock,
      possibleCode,
      warriorCode, symbols) = pickle.load(file)

    input("Press enter when you're ready.")
    
    menuPlay(clock, symbols)


