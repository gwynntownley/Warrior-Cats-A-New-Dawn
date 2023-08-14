import random

from entity.clan import clan

from data.file import codebits

biomes = {
'forest' : ['temperate forest', 'taiga', 'deep woodland', 'rainforest', 'rainforest canopy'],
'wetland' : ['moor', 'marsh', 'bog', 'swamp', 'deadland'],
'desert' : ['flatland', 'canyon', 'cactus forest', 'savannah', 'chaparral'],
'mountain' : ['mountain peak', 'mountain cliffside', 'mountain forest', 'mountain grassland', 'rocky ridge'],
'tundra' : ['cold desert', 'cold grassland', 'cold valley', 'glacier island', 'frozen forest'],
'coast' : ['smooth beach', 'rocky beach', 'ocean cliffside', 'palm forest', 'coastal grassland']
}

land_prefixes = ["Windover", "Druid's", "Devil's", "Chell", "Morgan's",
                  "Northern", "Southern", "Eastern", "Western", "Allerton",
                  "Chelford", "Littlepine", "Whitechurch", "Hare Hill", "Sailor"]
land_suffixes = ["Farm", "Moor", "Hollow", "Mineshaft", "Leap",
                  "River", "Campsite", "Lane", "Road", "Woods",
                  "Forest", "Mill", "Mountain", "Cliffs", "Lake"]

landmarks = {
    "Twolegplace" : ["Dog Bone", "Spiked Collar", "Shiny Trinket", "Medicinal Herb", "Rat Leftovers"],
    "Flower Fields" : ["Thorny Rose", "Violet Flower", "Cat Mint", "Medicinal Herb", "Songbird Leftovers"],
    "Sunningrocks" : ["Round Stone", "Vole Skull", "Clear Crystal", "Medicinal Herb", "Vole Leftovers"],
    "Ancient Tree" : ["Rainbow Beetle", "Dove Feather", "Fresh Moss", "Medicinal Herb", "Dove Leftovers"],
    "Predator Territory" : ["Huge Pelt", "Sharp Fang", "Viper Venom", "Medicinal Herb", "Hare Leftovers"]
}

# all plantlife in the game
plants = {
    'temperate forest' : ["oak trees", "birch trees", "sorrel", "bluebell flowers", "ferns"],
    'taiga' : ["spruce trees", "withering trees", "snowdrop flowers", "ferns", "tall grass"],
    'deep woodland' : ["oak trees", "birch trees", "bracken", "red roses", "ferns"],
    'rainforest' : ["kapok trees", "banana trees", "ferns", "tall grass", "hibiscus flowers"],
    'rainforest canopy' : ["kapok trees", "banana trees", "ferns", "tall grass", "hibiscus flowers"],
    'moor' : ["heather", "tall grass", "sorrel", "heath", "rosemary"],
    'marsh' : ["heather", "tall grass", "sorrel", "heath", "rosemary"],
    'bog' : ["heather", "tall grass", "sorrel", "heath", "rosemary"],
    'swamp' : ["mangrove trees", "heather", "tall grass", "sorrel", "heath"],
    'deadland' : ["mangrove trees", "heather", "tall grass", "sorrel", "heath"],
    'flatland' : ["cacti", "withering trees", "tall grass", "thornbushes", "shrubs"],
    'canyon' : ["cacti", "withering trees", "tall grass", "thornbushes", "shrubs"],
    'cactus forest' : ["cacti", "withering trees", "tall grass", "thornbushes", "shrubs"],
    'savannah' : ["cacti", "withering trees", "tall grass", "thornbushes", "baobab trees"],
    'chaparral' : ["cacti", "withering trees", "tall grass", "thornbushes", "baobab trees"],
    'mountain peak' : ["spruce trees", "ferns", "sorrel", "red roses", "tall grass"],
    'mountain cliffside' : ["spruce trees", "ferns", "sorrel", "red roses", "tall grass"],
    'mountain forest' : ["spruce trees", "ferns", "sorrel", "red roses", "tall grass"],
    'mountain grassland' : ["spruce trees", "ferns", "sorrel", "red roses", "tall grass"],
    'rocky ridge' : ["spruce trees", "ferns", "sorrel", "red roses", "tall grass"],
    'cold desert' : ["cacti", "withering trees", "tall grass", "thornbushes", "shrubs"],
    'cold grassland' : ["heather", "tall grass", "sorrel", "heath", "rosemary"],
    'cold valley' : ["heather", "tall grass", "sorrel", "heath", "rosemary"],
    'glacier island' : ["tall grass", "thornbushes", "shrubs", "withering trees", "snowdrop flowers"],
    'frozen forest' : ["tall grass", "thornbushes", "shrubs", "withering trees", "snowdrop flowers"],
    'smooth beach' : ["palm trees", "shrubs", "tall grass", "thornbushes", "cacti"],
    'rocky beach' : ["palm trees", "shrubs", "tall grass", "thornbushes", "cacti"],
    'ocean cliffside' : ["palm trees", "shrubs", "tall grass", "thornbushes", "cacti"],
    'palm forest' : ["palm trees", "shrubs", "tall grass", "thornbushes", "cacti"],
    'coastal grassland' : ["palm trees", "shrubs", "tall grass", "thornbushes", "cacti"]
    }

# all predators in the game
predators = {
    'temperate forest' : ['foxes', 'hawks', 'badgers', 'wolves', 'bears'],
    'taiga' : ['bears', 'wolves', 'tigers', 'foxes', 'lynxes'],
    'deep woodland' : ['foxes', 'hawks', 'badgers', 'wolves', 'bears'],
    'rainforest' : ['gorillas', 'jaguars', 'snakes', 'eagles', 'tigers'],
    'rainforest canopy' : ['gorillas', 'jaguars', 'snakes', 'eagles', 'tigers'],
    'moor' : ['hawks', 'eagles', 'dogs', 'snakes', 'foxes'],
    'marsh' : ['hawks', 'eagles', 'crocodiles', 'snakes', 'alligators'],
    'bog' : ['hawks', 'eagles', 'crocodiles', 'snakes', 'alligators'],
    'swamp' : ['hawks', 'eagles', 'crocodiles', 'snakes', 'alligators'],
    'deadland' : ['hawks', 'eagles', 'crocodiles', 'snakes', 'alligators'],
    'flatland' : ['bobcats', 'coyotes', 'hawks', 'snakes', 'owls'],
    'canyon' : ['bobcats', 'coyotes', 'hawks', 'snakes', 'owls'],
    'cactus forest' : ['bobcats', 'coyotes', 'hawks', 'snakes', 'owls'],
    'savannah' : ['lions', 'leopards', 'hyenas', 'eagles', 'dogs'],
    'chaparral' : ['bears', 'cougars', 'coyotes', 'foxes', 'bobcats'],
    'mountain peak' : ['cougars', 'snow leopards', 'bears', 'badgers', 'hawks'],
    'mountain cliffside' : ['cougars', 'snow leopards', 'bears', 'badgers', 'hawks'],
    'mountain forest' : ['cougars', 'snow leopards', 'bears', 'badgers', 'hawks'],
    'mountain grassland' : ['cougars', 'snow leopards', 'bears', 'badgers', 'hawks'],
    'rocky ridge' : ['cougars', 'snow leopards', 'bears', 'badgers', 'hawks'],
    'cold desert' : ['foxes', 'bears', 'owls', 'wolves', 'lynxes'],
    'cold grassland' : ['foxes', 'bears', 'owls', 'wolves', 'lynxes'],
    'cold valley' : ['foxes', 'bears', 'owls', 'wolves', 'lynxes'],
    'glacier island' : ['foxes', 'bears', 'owls', 'wolves', 'lynxes'],
    'frozen forest' : ['foxes', 'bears', 'owls', 'wolves', 'lynxes'],
    'smooth beach' : ['foxes', 'coyotes', 'hawks', 'eagles', 'dogs'],
    'rocky beach' : ['foxes', 'coyotes', 'hawks', 'eagles', 'dogs'],
    'ocean cliffside' : ['foxes', 'coyotes', 'hawks', 'eagles', 'dogs'],
    'palm forest' : ['foxes', 'coyotes', 'hawks', 'eagles', 'dogs'],
    'coastal grassland' : ['foxes', 'coyotes', 'hawks', 'eagles', 'dogs']
}
predators_ind = {
    'bears' : 'bear',
    'wolves' : 'wolf',
    'dogs' : 'dog',
    'foxes' : 'fox',
    'hawks' : 'hawk',
    'badgers' : 'badger',
    'tigers' : 'tiger',
    'lynxes' : 'lynx',
    'gorillas' : 'gorilla',
    'jaguars' : 'jaguar',
    'snakes' : 'snake',
    'eagles' : 'eagle',
    'crocodiles' : 'crocodile',
    'alligators' : 'alligator',
    'bobcats' : 'bobcat',
    'coyotes' : 'coyote',
    'owls' : 'owl',
    'lions' : 'lion',
    'leopards' : 'leopard',
    'hyenas' : 'hyena',
    'cougars' : 'cougar',
    'snow leopards' : 'snow leopard'
}

# all prey in the game
prey = {
    'temperate forest' : ['squirrel', 'skunk', 'rabbit', 'bird', 'mouse'],
    'taiga' : ['beaver', 'hare', 'lemming', 'frog', 'jay'],
    'deep woodland' : ['squirrel', 'frog', 'bird', 'mouse', 'rabbit'],
    'rainforest' : ['lemur', 'hornbill', 'macaw', 'frog', 'sloth'],
    'rainforest canopy' : ['lemur', 'hornbill', 'macaw', 'frog', 'sloth'],
    'moor' : ['rabbit', 'hare', 'bird', 'frog', 'vole'],
    'marsh' : ['bird', 'frog', 'mouse', 'vole', 'turtle'],
    'bog' : ['bird', 'frog', 'mouse', 'vole', 'turtle'],
    'swamp' : ['bird', 'frog', 'mouse', 'vole', 'turtle'],
    'deadland' : ['bird', 'frog', 'mouse', 'vole', 'turtle'],
    'flatland' : ['prairie dog', 'mouse', 'rabbit', 'hare', 'bird'],
    'canyon' : ["rabbit", "squirrel", "bat", "lizard", "bird"],
    'cactus forest' : ["rabbit", "squirrel", "bat", "lizard", "bird"],
    'savannah' : ['prairie dog', 'mouse', 'rabbit', 'hare', 'bird'],
    'chaparral' : ['prairie dog', 'mouse', 'rabbit', 'hare', 'bird'],
    'mountain peak' : ["rabbit", "beaver", "hyrax", "pika", "mouse"],
    'mountain cliffside' : ["rabbit", "beaver", "hyrax", "pika", "mouse"],
    'mountain forest' : ["rabbit", "beaver", "hyrax", "pika", "mouse"],
    'mountain grassland' : ["rabbit", "beaver", "hyrax", "pika", "mouse"],
    'rocky ridge' : ["rabbit", "beaver", "hyrax", "pika", "mouse"],
    'cold desert' : ['prairie dog', 'mouse', 'rabbit', 'hare', 'bird'],
    'cold grassland' : ['beaver', 'hare', 'lemming', 'frog', 'jay'],
    'cold valley' : ['beaver', 'hare', 'lemming', 'frog', 'jay'],
    'glacier island' : ['beaver', 'hare', 'lemming', 'frog', 'jay'],
    'frozen forest' : ['beaver', 'hare', 'lemming', 'frog', 'jay'],
    'smooth beach' : ["seagull", "bird", "turtle", "lizard", "hare"],
    'rocky beach' : ["seagull", "bird", "turtle", "lizard", "hare"],
    'ocean cliffside' : ["seagull", "bird", "turtle", "lizard", "hare"],
    'palm forest' : ["seagull", "bird", "turtle", "lizard", "hare"],
    'coastal grassland' : ["seagull", "bird", "turtle", "lizard", "hare"]
}

class land(object):
    def __init__(self, name, biome, predators, prey, plants, landmark, x, y, owner):
        self.name = name
        self.biome = biome
        self.predators = predators
        self.prey = prey
        self.plants = plants
        self.landmark = landmark
        self.x = x
        self.y = y
        self.owner = owner

    communer = ""

    coordinates = {
        0 : {},
        1 : {},
        2 : {},
        3 : {},
        4 : {},
        5 : {},
        6 : {},
        7 : {},
        8 : {},
        9 : {}
        }

def check():

    gencount = 200

    isGen = True

    for y in land.coordinates:
        for x in land.coordinates[y]:
            if land.coordinates[y][x].biome == "":
                isGen = False
            else:
                gencount -= 1

    return isGen, gencount

# Land claim
      
def autoClaim(c):

  # Find spawn
    
    spawn = (random.choice(clan.clans[c].location))

    spawn_y = spawn[0]

    spawn_x = list(land.coordinates[spawn_y]).index(spawn[1])

    claimed = False
    tries = 5

  # Claim land

    while claimed == False and tries > 0:

        inc_x = -1
        inc_y = -1

        while ((inc_x < 0 or inc_y < 0) or (inc_x == spawn_x and inc_y == spawn_y)) and tries > 0:

            inc_x = spawn_x + (random.randint(-1, 1))
            inc_y = spawn_y + (random.randint(-1, 1))

            tries -= 1
      
        try:

            inc = list(land.coordinates[inc_y])[inc_x]
            if land.coordinates[inc_y][inc].owner == None:
                land.coordinates[inc_y][inc].owner = c
                clan.clans[c].location.append([inc_y, inc])
                claimed = True

        except:

            claimed = False
            tries -= 1

def gen():

  # generate coordinate tokens

    for n in land.coordinates:
        for a in range(20):

            var_name = (random.choice(codebits))
            for i in range((random.randint(5, 15))):
                var_name = var_name + (random.choice(codebits))

            # create coordinate token

            land.coordinates[n][var_name] = land("",
                                        "", {}, {},
                                        {}, None, a, n, None)
  
    isGen = False

    while isGen == False:
        rando = (random.randint(1, 9))
        if rando == 1:

      # generate ocean/water

            spawn_y = random.choice(list(land.coordinates))
            spawn_x = random.randint(0, 19)

            spawn = list(land.coordinates[spawn_y])[spawn_x]

            while not land.coordinates[spawn_y][spawn].biome == "":

                spawn_y = random.choice(list(land.coordinates))
                spawn_x = random.randint(0, 19)

                spawn = list(land.coordinates[spawn_y])[spawn_x]  

            land.coordinates[spawn_y][spawn].owner = "ocean"
            land.coordinates[spawn_y][spawn].biome = "ocean"

            oceansize = (random.randint(5, 25))

            for n in range(oceansize):
        
                inc_x = -1
                inc_y = -1

                while (inc_x < 0 or inc_y < 0) or (inc_x > 19 or inc_y > 9) or (inc_x == spawn_x and inc_y == spawn_y):

                    inc_x = spawn_x + (random.randint(-1, 1))
                    inc_y = spawn_y + (random.randint(-1, 1))

                if inc_y in land.coordinates:
                    inc = list(land.coordinates[inc_y])[inc_x]
          
                if land.coordinates[inc_y][inc].owner == None:
                    land.coordinates[inc_y][inc].owner = "ocean"

                spawn_y = inc_y
                spawn_x = inc_x

        else:

            seed = (random.choice(list(biomes)))

            # generate biome

            spawn_y = random.choice(list(land.coordinates))
            spawn_x = random.randint(0, 19)

            spawn = list(land.coordinates[spawn_y])[spawn_x]

            while not land.coordinates[spawn_y][spawn].biome == "":

                spawn_y = random.choice(list(land.coordinates))
                spawn_x = random.randint(0, 19)

                spawn = list(land.coordinates[spawn_y])[spawn_x]

            land.coordinates[spawn_y][spawn].owner = None
            land.coordinates[spawn_y][spawn].biome = random.choice(biomes[seed])

            land.coordinates[spawn_y][spawn].name = (random.choice(land_prefixes)) + " " + (random.choice(land_suffixes))

          # populate land entity
            preyOpt = prey[land.coordinates[spawn_y][spawn].biome]
            rando = (random.randint(1, 3))
            for p in range(rando):
                newPrey = (random.choice(preyOpt))
                land.coordinates[spawn_y][spawn].prey[newPrey] = (random.randint(1, 12))
            rando = (random.randint(1, 3))
            plantOpt = plants[land.coordinates[spawn_y][spawn].biome]
            for p in range(rando):
                newPlant = (random.choice(plantOpt))
                land.coordinates[spawn_y][spawn].plants[newPlant] = (random.randint(1, 12))
            rando = (random.randint(1, 3))
            predOpt = predators[land.coordinates[spawn_y][spawn].biome]
            for p in range(rando):
                newPred = (random.choice(predOpt))
                land.coordinates[spawn_y][spawn].predators[newPred] = (random.randint(1, 12))

            biomesize = (random.randint(5, 25))

            for n in range(biomesize):

                inc_x = -1
                inc_y = -1

                while (inc_x < 0 or inc_y < 0) or (inc_x > 19 or inc_y > 9) or (inc_x == spawn_x and inc_y == spawn_y):

                    inc_x = spawn_x + (random.randint(-1, 1))
                    inc_y = spawn_y + (random.randint(-1, 1))

                if inc_y in land.coordinates:
                    inc = list(land.coordinates[inc_y])[inc_x]
              
                if land.coordinates[inc_y][inc].owner == None:
                    land.coordinates[inc_y][inc].biome = random.choice(biomes[seed])

                    land.coordinates[inc_y][inc].name = (random.choice(land_prefixes)) + " " + (random.choice(land_suffixes))
                    land.coordinates[inc_y][inc].prey = {}
                    land.coordinates[inc_y][inc].plants = {}
                    land.coordinates[inc_y][inc].predators = {}

                    # populate land entity
                    
                    rando = (random.randint(1, 3))
                    for p in range(rando):
                        newPrey = (random.choice(prey[land.coordinates[inc_y][inc].biome]))
                        land.coordinates[inc_y][inc].prey[newPrey] = (random.randint(1, 12))
                    rando = (random.randint(1, 3))
                    for p in range(rando):
                        newPlant = (random.choice(plants[land.coordinates[inc_y][inc].biome]))
                        land.coordinates[inc_y][inc].plants[newPlant] = (random.randint(1, 12))
                    rando = (random.randint(1, 3))
                    for p in range(rando):
                        newPred = (random.choice(predators[land.coordinates[inc_y][inc].biome]))
                        land.coordinates[inc_y][inc].predators[newPred] = (random.randint(1, 12))
                    spawn_y = inc_y
                    spawn_x = inc_x

        isGen, gencount = check()

  # populate map with landmarks

    for l in list(landmarks):

        count = 5
        while count > 1:
      
            spawn_y = (random.randint(0, 9))
            spawn_x = (random.randint(0, 19))

            markspawn = list(land.coordinates[spawn_y])[spawn_x]

            if land.coordinates[spawn_y][markspawn].landmark == None and land.coordinates[spawn_y][markspawn].owner == None:

                land.coordinates[spawn_y][markspawn].landmark = l
                
            count -= 1

  # spawn communer

    commhome = False

    while commhome == False:

        spawn_y = (random.randint(0, 9))
        spawn_x = (random.randint(0, 19))

        commspawn = list(land.coordinates[spawn_y])[spawn_x]

        if land.coordinates[spawn_y][commspawn].owner == None:
            land.communer = "Moon" + (random.choice([
            "pool", "stone", "tree", "glow", "cliff", "flower", "beast", "feather", "field", "cave", "watcher"
            ]))
            land.coordinates[spawn_y][commspawn].owner = "communer"
            commhome = True

  # spawn bazaar

    bbhome = False

    while bbhome == False:

        spawn_y = (random.randint(0, 9))
        spawn_x = (random.randint(0, 19))

        bbspawn = list(land.coordinates[spawn_y])[spawn_x]

        if land.coordinates[spawn_y][bbspawn].owner == None:
            land.coordinates[spawn_y][bbspawn].owner = "bazaar"
        bbhome = True

# Map generator

def seeMap(mode):

  # Map legend

    if mode == "patrol":
        print("=-= LEGEND=-=")
        print("[%s] = Claimed Territory" % (clan.clans["player_Clan"].symbol))
        print("{•} = discovered")

    else:

        print("=-= FACTIONS =-=")

        for i in clan.clans.copy():
            print("[%s] = %s" % (clan.clans[i].symbol, clan.clans[i].name))

        print("=-= FEATURES =-=")
        print("{○} = %s" % land.communer)
        print("{B} = Backway Bazaar")

        print("=-= OTHER =-=")
        print("{•} = discovered")
        print("{~} = water")

  # check for adjacent territories

    allies = ["player_Clan"]

    for c in clan.clans:
        if clan.clans[c].rep > 0:
            allies.append(c)

    adjacent = []

    for y in land.coordinates:
        for x in land.coordinates[y]:

          # for player Clan + allies

            for a in allies:

            # for each territory owned by ally

                for l in clan.clans[a].location:

              # find coord for location
                    ly = l[0]
                    lx = list(land.coordinates[ly]).index(l[1])

                    if (abs(list(land.coordinates[y]).index(x) - lx) < 2) and (abs(y - ly) < 2):
                        adjacent.append(x)  
                  
  # print map
              
    print("""
   0 0 0 0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 1 1
   0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9
  _________________________________________""")
    for y in land.coordinates:
        ystring = ["%s| " % codebits[int(y)]]
        for x in land.coordinates[y]:
            newy = ""
            if mode == "patrol":
                if land.coordinates[y][x].owner == "player_Clan":
                    newy = clan.clans["player_Clan"].symbol + " "
                elif land.coordinates[y][x].owner == None and x in adjacent:
                    newy = "• "
                else:
                    newy = "  "
            else:
                if land.coordinates[y][x].owner == "ocean":
                    newy = "~~"
                elif land.coordinates[y][x].owner == "communer":
                    newy = "○ "
                elif land.coordinates[y][x].owner == "bazaar":
                    newy = "B "
                elif land.coordinates[y][x].owner == None and x in adjacent:
                    newy = "• "
                elif land.coordinates[y][x].owner == None:
                    newy = "  "
                else:
                    newy = clan.clans[land.coordinates[y][x].owner].symbol + " "
            ystring.append(newy)
        ystring.append(" |")
        print("".join(ystring))
    print("  _________________________________________")


    if mode == "patrol":
        sortedLand = []
        for y in list(land.coordinates):
            for x in land.coordinates[y]:
                if land.coordinates[y][x].owner == "player_Clan":
                    sortedLand.append([y,x])
        toList = len(sortedLand)
        num = 0
        while toList > 0:
            if toList > 2:
                if list(land.coordinates[sortedLand[num][0]]).index(sortedLand[num][1]) < 10:
                    ind1 = str(0) + str(list(land.coordinates[sortedLand[num][0]]).index(sortedLand[num][1]))
                else:
                    ind1 = str(list(land.coordinates[sortedLand[num][0]]).index(sortedLand[num][1]))

                if list(land.coordinates[sortedLand[num + 1][0]]).index(sortedLand[num + 1][1]) < 10:
                    ind2 = str(0) + str(list(land.coordinates[sortedLand[num + 1][0]]).index(sortedLand[num + 1][1]))
                else:
                    ind2 = str(list(land.coordinates[sortedLand[num + 1][0]]).index(sortedLand[num + 1][1]))

                if list(land.coordinates[sortedLand[num + 2][0]]).index(sortedLand[num + 2][1]) < 10:
                    ind3 = str(0) + str(list(land.coordinates[sortedLand[num + 2][0]]).index(sortedLand[num + 2][1]))
                else:
                    ind3 = str(list(land.coordinates[sortedLand[num + 2][0]]).index(sortedLand[num + 2][1]))
                    
                print("[%s%s] %s - %s    [%s%s] %s - %s    [%s%s] %s - %s" %(
                codebits[sortedLand[num][0]], ind1,
                land.coordinates[sortedLand[num][0]][sortedLand[num][1]].name,
                land.coordinates[sortedLand[num][0]][sortedLand[num][1]].biome,
                codebits[sortedLand[num + 1][0]], ind2,
                land.coordinates[sortedLand[num + 1][0]][sortedLand[num + 1][1]].name,
                land.coordinates[sortedLand[num + 1][0]][sortedLand[num + 1][1]].biome,
                codebits[sortedLand[num + 2][0]], ind3,
                land.coordinates[sortedLand[num + 2][0]][sortedLand[num + 2][1]].name,
                land.coordinates[sortedLand[num + 2][0]][sortedLand[num + 2][1]].biome))
                num += 3
                toList -= 3
            elif toList > 1:

                if list(land.coordinates[sortedLand[num][0]]).index(sortedLand[num][1]) < 10:
                    ind1 = str(0) + str(list(land.coordinates[sortedLand[num][0]]).index(sortedLand[num][1]))
                else:
                    ind1 = str(list(land.coordinates[sortedLand[num][0]]).index(sortedLand[num][1]))

                if list(land.coordinates[sortedLand[num + 1][0]]).index(sortedLand[num + 1][1]) < 10:
                    ind2 = str(0) + str(list(land.coordinates[sortedLand[num + 1][0]]).index(sortedLand[num + 1][1]))
                else:
                    ind2 = str(list(land.coordinates[sortedLand[num + 1][0]]).index(sortedLand[num + 1][1]))
                    
                print("[%s%s] %s - %s    [%s%s] %s - %s" %(
                codebits[sortedLand[num][0]], ind1,
                land.coordinates[sortedLand[num][0]][sortedLand[num][1]].name,
                land.coordinates[sortedLand[num][0]][sortedLand[num][1]].biome,
                codebits[sortedLand[num + 1][0]], ind2,
                land.coordinates[sortedLand[num + 1][0]][sortedLand[num + 1][1]].name,
                land.coordinates[sortedLand[num + 1][0]][sortedLand[num + 1][1]].biome))
                num += 2
                toList -= 2
            else:

                if list(land.coordinates[sortedLand[num][0]]).index(sortedLand[num][1]) < 10:
                    ind1 = str(0) + str(list(land.coordinates[sortedLand[num][0]]).index(sortedLand[num][1]))
                else:
                    ind1 = str(list(land.coordinates[sortedLand[num][0]]).index(sortedLand[num][1]))
                
                print("[%s%s] %s - %s" %(
                codebits[sortedLand[num][0]], ind1,
                land.coordinates[sortedLand[num][0]][sortedLand[num][1]].name,
                land.coordinates[sortedLand[num][0]][sortedLand[num][1]].biome))
                num += 1
                toList -= 1

  # select coord
    target = None
    y = None
    x = None

    cmd = input("""
    Please enter the coordinate of the territory you would
    like to select below. Like so : YXX, i.e. A02, D14 ...

    If you would not like to select anything, just press ENTER.

    > """)

    try:
    
    # parse y
        if cmd[0].upper() in codebits:
            y = codebits.index(cmd[0].upper())
    
        # parse x
        if int(cmd[1]) == 1:
            x = 10
        else:
            x = 0

        x += int(cmd[2])

        # set target
        target = list(land.coordinates[y])[x]
        return y, target

    except:
        return None, None

def spawn(c):
    loc_y = random.choice(list(land.coordinates))

    location = random.choice(list(land.coordinates[loc_y]))
    while not land.coordinates[loc_y][location].owner == None:
        location = random.choice(list(land.coordinates[loc_y]))

    land.coordinates[loc_y][location].owner = c

    return (random.choice(["which is patrolled by %s." % random.choice(list(land.coordinates[loc_y][location].predators)),
    "notable for its %s." % random.choice(list(land.coordinates[loc_y][location].plants)),
    "rich in %s-prey." % random.choice(list(land.coordinates[loc_y][location].prey))])), loc_y, location

