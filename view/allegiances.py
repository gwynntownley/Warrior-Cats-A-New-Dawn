from entity.clan import clan
from entity.rank import rank

def allegiances(c):
  order = 0
  rankCheck = 0
  while rankCheck < len(list(clan.clans[c].ranks)):
    for i in clan.clans[c].ranks:
      if clan.clans[c].ranks[i].order == order:
        rankCheck += 1
        for m in clan.clans[c].cats.copy():
          if clan.clans[c].cats[m].rank == clan.clans[c].ranks[i].name:
            print("%s: %s- %s" % (clan.clans[c].cats[m].rank,
                                  clan.clans[c].cats[m].name,
                                  clan.clans[c].cats[m].description))
    order += 1
  
