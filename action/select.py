from bin.text import selectText
from data.clock import clock
from entity.clan import clan
from entity.map import seeMap
from entity.rank import rank
import random

# locate leader in faction roster
leader = None
for c in list(clan.clans["player_Clan"].cats):
  if clan.clans["player_Clan"].cats[c].rank == "leader":
    leader = c

def actionSelect(action):

  ### ASSIGN PATROL

  # is player still assigning cats to patrol ?
  done = False

  # has a captain been chosen for the patrol ?
  choseCap = False
  # will be set to chosen captain's CatID
  captain = None

  # cats to be put on patrol; CatID is appended to the list upon selection
  chosen = []

  # customises game text to be relavent to chosen patrol type
  keywords = []
  # turns taken to complete patrol action
  patrolTime = 0

  # training earns participants XP, sometimes at the expense of a little WP
  if action == "train":
    keywords = ["training session", "lesson", "off to strengthen their battle skills"]
    patrolTime = (random.randint(1, 2))
  # hunting earns prey for the faction and some XP for patrol members
  elif action == "hunt":
    keywords = ["hunting patrol", "hunt", "on a hunting mission"]
    patrolTime = (random.randint(2, 4))
  # expeditions earns territory for your faction, but take a long time and are risky
  elif action == "claim":
    keywords = ["exploratory patrol", "expedition", "on a quest to discover new territory"]
    patrolTime = (random.randint(20, 40))
  # border patrols have chances to earn a little of everything, such as prey, items, medicine, and/or recruits
  elif action == "patrol":
    keywords = ["border patrol", "patrol", "to patrol the border"]
    patrolTime = (random.randint(2, 4))
  else:
    keywords = ["patrol"]

  # ensures that if the selection process encounters an error, the process is aborted
  failed = False

  # checks whether or not the leader has been added to the patrol
  hasLeader = False

  # if patrol is a border patrol, the player may assign a "focus" to guide the results
  if action == "patrol":

    cmd = input(selectText["focus"])

    action = "patrol" + cmd

  # player will assign cats as long as !done
  while done == False:
    # cnt is used to "count" the number of cats eligible for patrol
    cnt = 1
    # possibles stores the CatIDs of eligible cats
    possibles = []
    for i in clan.clans["player_Clan"].cats.copy():
      # cats are eligible for the patrol if they meet the following conditions:
      # - the cats' rank permits them to
      # - the cat is currently idle (at camp)
      # - if the patrol is an expedition, the cat cannot be the leader
      if ((clan.clans["player_Clan"].ranks[clan.clans["player_Clan"].cats[i].rank].privs["can%s" % action.capitalize()]) and (("%s camp" % clan.clans["player_Clan"].name) in clan.clans["player_Clan"].cats[i].loc)
      and not (i == leader and action == "claim")):
        # display the cat's selection number, name, level, and WP; append to possibles list
        print(selectText["catInfo"] % (cnt, clan.clans["player_Clan"].cats[i].name, clan.clans["player_Clan"].cats[i].lvl, clan.clans["player_Clan"].cats[i].wp, clan.clans["player_Clan"].cats[i].stats["Willpower"]))
        possibles.append(i)
        cnt += 1

    # if no remaining cats are available...
    if cnt == 1:
      print(selectText["catsNone"] % keywords[0])
      done = True
      if choseCap == True:
        # if a captain has been selected, send patrol
        failed = False
      else:
        # if a captain has not been selected, abort process
        failed = True
      clock["turns"] += 1
    else:      
      conf = False
      cmd = "alfalfa"
      while conf == False:
        try:
          if str(cmd).lower() == "done":
            done = True
          else:
            target = possibles[int(cmd) - 1]
            confirmAddition = False
            if target == leader:

              confirmAddition = input(selectText["leaderAdd"] % (keywords[0], keywords[0])).lower()

              if confirmAddition == "y":
                confirmAddition = True
                hasLeader = True
              else:
                confirmAddition = False
            else:
              confirmAddition = True

            if confirmAddition == True:
                
              if choseCap == False:
                clan.clans["player_Clan"].cats[target].loc = "leading a(n) %s" % keywords[0]
                captain = target
                choseCap = True
              else:
                clan.clans["player_Clan"].cats[target].loc = "on a(n) %s with %s" % (keywords[0], clan.clans["player_Clan"].cats[captain].name)
                chosen.append(target)
          conf = True
        except Exception as e:
          if choseCap == False:
            cmd = input(selectText["capAdd"] % keywords[1])
          else:
            cmd = input(selectText["catAdd"] % (keywords[1], keywords[0]))

  if failed == False:
    y, target = seeMap("patrol")

    print(selectText["sent"] % keywords[2])

    print("Captain : %s" % captain)
    print("Action : %s" % action)

    confirm = False
    while confirm == False:
      try:

        clockCode = (action + "timer" + "-" + captain + "-" + str(y) +
                     "-" + target + "-" + str(hasLeader) + "-" + "-".join(chosen))

        clock[clockCode] = patrolTime

        print(hasLeader)
        confirm = True
      except:
        y, target = seeMap("patrol")
