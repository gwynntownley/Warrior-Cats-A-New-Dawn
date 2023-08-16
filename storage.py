bird_species = {
    "pigeon" : {
        "colours" : ["slate-grey", "blue", "pink"],
        "chance" : 100,
        },
    "crow" : {
        "colours" : ["black", "hooded", "indigo"],
        "chance" : 100,
        },
    "starling" : {
        "colours" : ["speckled", "orange-bellied", "violet-backed"],
        "chance" : 100,
        },
    "chicken" : {
        "colours" : ["brown", "golden", "spotted white"],
        "chance" : 50,
        },
    "jay" : {
        "colours" : ["blue", "violet", "black"],
        "chance" : 50,
        },
    "magpie" : {
        "colours" : ["black and white", "blue", "brown and blue"],
        "chance" : 50,
        },
    "hoatzin" : {
        "colours" : ["red", "golden", "black"],
        "chance" : 25,
        },
    "cardinal" : {
        "colours" : ["red", "yellow", "white"],
        "chance" : 25,
        },
    }

class bird(object):
    def __init__(self, name, personality, species, colour, rarity, wp, stats):
        self.name = name
        self.personality = personality
        self.species = species
        self.colour = colour
        self.rarity = rarity
        self.wp = wp
        self.stats = stats

class disease(object):
  def __init__(self, name, infectivity, fatality):
    self.name = name
    self.infectivity = infectivity
    self.fatality = fatality
  diseases = {}

# garden folders

aviary = {}

# diseases

disease.diseases["greencough"] = disease("greencough", 2, 5)
disease.diseases["whitecough"] = disease("whitecough", 1, 2)
disease.diseases["redcough"] = disease("redcough", 3, 5)
disease.diseases["blackcough"] = disease("blackcough", 3, 10)
disease.diseases["yellowcough"] = disease("yellowcough", 2, 8)
                      
            
