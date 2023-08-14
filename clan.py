import random

# clan objects

class clan(object):
  def __init__(self, name, motto, noun, location, landmark,
               inv, prey, herbs, rep,
               cats, symbol, ranks, events):

    self.name = name
    self.motto = motto
    self.noun = noun
    self.location = location
    self.landmark = landmark
    self.inv = inv
    self.prey = prey
    self.herbs = herbs
    self.rep = rep
    self.cats = cats
    self.symbol = symbol
    self.ranks = ranks
    self.events = events

  clans = {}

symbols = ["♠",
           "♣",
           "♥",
           "♦",
           "■",
           "Ω",
           "☼",
           "☻",
           "▲"]

virtues = [
  "Adventure",
  "Certainty", "Courage", "Compassion", "Confidence", "Curiosity",
  "Determination", "Duty",
  "Endurance", "Energy", "Equality",
  "Faith", "Family", "Fate", "Forgiveness", "Friendship",
  "Grace",
  "Happiness", "Home", "Honour", "Hope", "Humility", "Humour",
  "Independence", "Instinct",
  "Judgement", "Justice", 
  "Kithood",
  "Lawfulness", "Love", "Loyalty", 
  "Mentorship", "Mercy",
  "Nobility",
  "Patience", "Peace", "Perception", "Pride", "Progress", "Protection", 
  "Resilience", "Respect",
  "Strength", "Survival",
  "Toughness", "Tradition", "Trust", 
  "Warfare", "Willpower", "Wisdom"
]

# group names

clanNames = ["Forest", "Moor", "Cliff", "Ice", "Bay",
             "Wind", "North", "Fjord", "Pine", "Hollow",
             "Oak", "Heather", "Berry", "Pine", "Root"]

tribeNames = ["Falling Leaves", "Dancing Wind", "Soaring Hawks", "Lasting Snow", "Rolling Tides",
              "Winding Paths", "Leaping Trout", "Roaming Flame", "Withering Trees", "Crying Night",
              "Rising Dawn", "Running Stoats", "Diving Gulls", "Thawing Ice", "Pounding Paws"]

otherNames = ["Wanderers", "Survivors", "Seekers", "Guardians", "Marauders",
              "Seers", "Hunters", "Rangers", "Jokers", "Icewalkers",
              "Burrowers", "Runners", "Treehoppers", "Firebringers"]

# generate group structures

def genClan():

  # Define globals

  global clan

  from entity.map import land, autoClaim
  from entity.cat import genCat, cat
  from entity.rank import rankTemplates
  from data.file import codebits

  # Start

  foundland = False
  tries = 5
  while tries > 0:

    loc_y = random.choice(list(land.coordinates))
    
    location = random.choice(list(land.coordinates[loc_y]))
    while not land.coordinates[loc_y][location].owner == None and tries > 0:
      location = random.choice(list(land.coordinates[loc_y]))
      tries -= 1
    
    if land.coordinates[loc_y][location].owner == None:
      foundland = True
      tries = 0
    else:
      tries -= 1
  
  if foundland == True:
    
    clan_name = (random.randint(1, 3))
    if clan_name == 1:
      clan_name = (random.choice(clanNames)) + "Clan"
      noun = "Clan"
    elif clan_name == 2:
      clan_name = "The Tribe of " + (random.choice(tribeNames))
      noun = "Tribe"
    else:
      clan_name = "The " + (random.choice(otherNames))
      noun = (random.choice(["Group", "Guild", "Band", "Troupe", "Faction"]))
    for a in clan.clans:
      while clan.clans[a].name == clan_name:
        clan_name = (random.randint(1, 3))
        if clan_name == 1:
          clan_name = (random.choice(clanNames)) + "Clan"
        elif clan_name == 2:
          clan_name = "Tribe of " + (random.choice(tribeNames))
        else:
          clan_name = "The " + (random.choice(otherNames))
        
    clan_var = ""
    for a in range(random.randint(5, 15)):
      clan_var = clan_var + (random.choice(codebits))

    land.coordinates[loc_y][location].owner = clan_var
    land.coordinates[loc_y][location].name = "%s camp" % clan_name
      
    clan.clans[clan_var] = clan(clan_name, "%s and %s" % ((random.choice(virtues)), (random.choice(virtues))), noun, [[loc_y, location]],
                                {}, {}, 0,
                                0, (random.randint(-5, 5)), {},
                                (random.choice(symbols)), {}, {
                                  "traitor" : [False, []],
                                  "disease" : [False, ""],
                                  "disaster" : [False, "", 0]})
    
    symbols.remove(clan.clans[clan_var].symbol)

    for i in range(4):
      autoClaim(clan_var)

    numofRanks = (random.randint(3, len(rankTemplates)))

    for r in range(numofRanks):
      if not "leader" in list(clan.clans[clan_var].ranks):
        clan.clans[clan_var].ranks["leader"] = rankTemplates["leader"]
      elif not "kit" in list(clan.clans[clan_var].ranks):
        clan.clans[clan_var].ranks["kit"] = rankTemplates["kit"]
      else:
        selected = random.choice(list(rankTemplates))
        tries = 5
        while selected in list(clan.clans[clan_var].ranks) and tries > 0:
          selected = random.choice(list(rankTemplates))
          tries -= 1
        clan.clans[clan_var].ranks[selected] = rankTemplates[selected]
    

    # Generate leader

    var_name = genCat(clan_var, "leader")

    # Generate other Clanmates

    rando = (random.randint(3, 9))

    for i in range(rando):

      genCat(clan_var, None)

    notable = (random.choice(["which is patrolled by %s." % random.choice(list(land.coordinates[loc_y][location].predators)),
                            "notable for its %s." % random.choice(list(land.coordinates[loc_y][location].plants)),
                            "rich in %s-prey." % random.choice(list(land.coordinates[loc_y][location].prey))]))
    
    print("%s's home is a/n %s, %s" % (clan.clans[clan_var].name, land.coordinates[loc_y][location].biome, notable))

    if not land.coordinates[loc_y][location].landmark == None:
      print("Their camp is adjacent to a(n) %s." % land.coordinates[loc_y][location].landmark)  
