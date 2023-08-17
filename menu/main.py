# user-navigable menu screen for WCND

## IMPORTS

import random
import traceback
import pickle

def menuMain():

  from bin.text import mainText
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
    print(mainText["title"])

    cmd = input(mainText["startCmd"]).upper()

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

    input(mainText["expoA"])

    input(mainText["expoB"])

    input(mainText["expoC"])

    input(mainText["expoD"])

    rando = (random.choice(list(clan.clans["player_Clan"].cats)))

    rando2 = (random.choice(list(clan.clans["player_Clan"].cats)))

    while rando2 == rando:
      rando2 = (random.choice(list(clan.clans["player_Clan"].cats)))

    input(mainText["expoE"] % (clan.clans["player_Clan"].cats[rando].name, clan.clans["player_Clan"].cats[rando].build, clan.clans["player_Clan"].cats[rando].pronoun))

    cmd = False

    while cmd == False:

      notable, loc_y, location = spawn("player_Clan")
    

      input(mainText["landFound"] % (clan.clans["player_Clan"].cats[rando].name, land.coordinates[loc_y][location].biome))

      cmd = input(mainText["landChoice"] % (land.coordinates[loc_y][location].biome, notable, clan.clans["player_Clan"].cats[rando2].name, clan.clans["player_Clan"].cats[rando2].coat,
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

        input(mainText["landVeto"] % clan.clans["player_Clan"].cats[rando].name)

        rando = (random.choice(list(clan.clans["player_Clan"].cats)))

        rando2 = (random.choice(list(clan.clans["player_Clan"].cats)))

        while rando2 == rando:
          rando2 = (random.choice(list(clan.clans["player_Clan"].cats)))

    input(mainText["guideA"])

    # Clan spawn

    print(mainText["landApprove"] % (land.coordinates[loc_y][location].biome, notable))

    if not land.coordinates[loc_y][location].landmark == None:
      print(mainText["landMark"] % land.coordinates[loc_y][location].landmark)

    #  Clan name
    clan.clans["player_Clan"].noun = input(mainText["factionType"])

    clan.clans["player_Clan"].name = input(mainText["factionName"] % clan.clans["player_Clan"].noun)
    
    land.coordinates[loc_y][location].name = "%s camp" % clan.clans["player_Clan"].name
    land.coordinates[loc_y][location].owner = "player_Clan"
    # Clan symbol

    parseOpt(symbols)

    clan.clans["player_Clan"].symbol = parseSel(symbols, mainText["factionIcon"] % (clan.clans["player_Clan"].name, clan.clans["player_Clan"].name))

    # Clan motto

    clan.clans["player_Clan"].motto = input(mainText["factionMotto"])

    # Cleanup

    for i in range(4):
      autoClaim("player_Clan")

    symbols.remove(clan.clans["player_Clan"].symbol)

    # Leader customization

    print(mainText["leaderIntroA"] % clan.clans["player_Clan"].name)
    print(mainText["leaderIntroB"])

    tried = False
    while tried == False:
      try:
        name = input(mainText["leaderName"])

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
      cmd = input(mainText["leaderGender"]).lower()

    if "t" in cmd:
      pronoun = "tom"
    elif "s" in cmd:
      pronoun = "she-cat"
    else:
      pronoun = "cat"
    
    print(mainText["leaderCoatA"])
    
    print("Coat Base : ")

    parseOpt(cat.coats)

    coat = parseSel(cat.coats, mainText["leaderCoatB"])
    
    print("Coat Pattern : ")

    parseOpt(cat.patterns)

    pattern = parseSel(cat.patterns, mainText["leaderPattern"])
  
    print("Eye Colours : ")

    parseOpt(cat.eyes)

    eye = parseSel(cat.eyes, mainText["leaderEyes"])

    print("Physical Traits : ")

    parseOpt(cat.builds)

    build = parseSel(cat.builds, mainText["leaderBuild"])

    print("Personality Traits : ")
    
    parseOpt(traits)

    trait_a = parseSel(traits, mainText["leaderTrait"])
    
    quote = input(mainText["leaderQuote"])
    
    description = parseDesc(coat, pattern, pronoun, build, eye)

    # Add leader to Clan

    clan.clans["player_Clan"].cats["leader"] = cat(
    fullName, prefix, root, suffix, "leader",
    description, pronoun, coat, pattern, eye, build, 36, {"isqueen" : False, "pregnant" : 0}, [], [], [],
    "Player", [trait_a], quote, 0, [], [], "", "",
    {},
    10, 1, 0, {"Willpower" : 10, "Strength" : 2, "Toughness" : 2, "Speed" : 2, "Precision" : 2, "Charisma" : 2}, [],
    clan.clans["player_Clan"].name, "Neutral", "%s camp" % clan.clans["player_Clan"].name)

    print(mainText["welcome"] %
          (clan.clans["player_Clan"].cats["leader"].name, clan.clans["player_Clan"].name))

    for c in list(clan.clans["player_Clan"].cats).copy():
      clan.clans["player_Clan"].cats[c].loc = "%s camp" % clan.clans["player_Clan"].name

    # Part Two: Generate the other Factions

    input(mainText["othersA"])
    input(mainText["othersB"])

    for i in range((random.randint(1, 5))):
      genClan()

    if len(list(clan.clans)) == 1:
      input(mainText["genError"])
      mainMenu()

    for i in range(3):
      genMer()

    print(mainText["lifeScene"] % land.communer)

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

      print(mainText["lifeGift"] % (name, relation, virtue))

    print("")
    print(mainText["lifeEnd"])

    menuPlay(clock, symbols)

  elif cmd == "L":

    print(mainText["load"])

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

    input(mainText["cont"])
    
    menuPlay(clock, symbols)


