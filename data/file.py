# save, load, and display data

# IMPORTS

import pickle
import traceback



# data

codebits = ["A", "B", "C", "D", "E",
            "F", "G", "H", "I", "J",
            "q", "w", "e", "r", "t",
            "y", "u", "i", "o", "p",
            "a", "s", "d", "f", "g",
            "h", "j", "k", "l", "z",
            "x", "c", "v", "b", "n",
            "m", "1", "2", "3", "4",
            "5", "6", "7", "8", "9",
            "10", "`", ":", "=", "[",
            "]", ",", ".", "/", "~",
            "!", "@", "#", "$", "%"]

# display save files

def filePreview(data):
  from entity.clan import clan, symbols
  from entity.cat import cat
  from storage import disease
  from entity.map import land
  from data.clock import clock
  from event.event import possibleCode, warriorCode
  for i in range(1, 10):
    try:
      with open("save_%d.dat" % i, 'rb') as file:
        (clan.clans, disease.diseases,
        land.communer, land.coordinates, clock,
        possibleCode,
        warriorCode, symbols) = pickle.load(file)
        print(clock)
        for c in clan.clans["player_Clan"].cats:
          if clan.clans["player_Clan"].cats[c].rank == "leader":
            leader = c
        print("[%d] - %s of %s, moon %d" % (i,
                                            clan.clans["player_Clan"].cats[leader].name,
                                            clan.clans["player_Clan"].name,
                                            clock["moon"]))
    except Exception:
      print("[%d] - BLANK" % i)
