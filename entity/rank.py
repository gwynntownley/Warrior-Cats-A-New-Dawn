# rank data notes

# name (ex. warrior, kit, medicine cat)
# order (order in the allegiance, ex. leader 0, deputy 1, elder 6)
# privs (a dictionary containing several iterable priveleges - a cat can have up to 5 priv points, making healing/inheriting ranks more exclusive)
  # canFight (1pt)
  # canHeal (3pt)
  # canHunt (1pt)
  # canMate (1pt)
  # canInherit (3pt)
  # canPatrol (1pt)
  # canTrain (1pt)
# autoAge (cat is automatically assigned rank at a certain age - true/false)
  # sourceRank (cat must be from sourceRank to be promoted)
  # ageMin (minimum age cat is promoted at)
# prefix (if rank has a set prefix, it goes here ex. chief, general, rookie)
# suffix (if rank has a set suffix, it goes here ex. kit, paw, star)

class rank(object):
  def __init__(self, name, order, privs, autoAge, prefix, suffix):
    self.name = name
    self.order = order
    self.privs = privs
    self.autoAge = autoAge
    self.prefix = prefix
    self.suffix = suffix

rankTemplates = {
  "leader" : rank("leader", 0, {
  "canFight" : True,
  "canHeal" : False,
  "canHunt" : True,
  "canPatrol" : True,
  "canTrain" : True,
  "canClaim" : False,
  "canMate" : True,
  "canInherit" : False,
  "isUnique" : True}, {
    "autoAge" : False,
    "sourceRank" : None,
    "ageMin" : None
    }, "", ""),
  
  "cat" : rank("cat", 3, {
  "canFight" : True,
  "canHeal" : False,
  "canHunt" : True,
  "canPatrol" : True,
  "canTrain" : True,
  "canClaim" : True,
  "canMate" : True,
  "canInherit" : False,
  "isUnique" : False}, {
    "autoAge" : True,
    "sourceRank" : "kit",
    "ageMin" : 12
    }, "", ""),
  
  "kit" : rank("kit", 5, {
  "canFight" : False,
  "canHeal" : False,
  "canHunt" : False,
  "canPatrol" : False,
  "canTrain" : False,
  "canClaim" : False,
  "canMate" : False,
  "canInherit" : False,
  "isUnique" : False}, {
    "autoAge" : False,
    "sourceRank" : None,
    "ageMin" : None
    }, "", ""),
  
  "warrior" : rank("warrior", 3, {
  "canFight" : True,
  "canHeal" : False,
  "canHunt" : True,
  "canPatrol" : True,
  "canTrain" : True,
  "canClaim" : True,
  "canMate" : True,
  "canInherit" : False,
  "isUnique" : False}, {
    "autoAge" : False,
    "sourceRank" : None,
    "ageMin" : None
    }, "", ""),
  
  "elder" : rank("elder", 6, {
  "canFight" : False,
  "canHeal" : False,
  "canHunt" : False,
  "canMate" : False,
  "canInherit" : False,
  "canPatrol" : False,
  "canTrain" : False,
  "canClaim" : False,
  "isUnique" : False}, {
    "autoAge" : True,
    "sourceRank" : None,
    "ageMin" : 70
    }, "", ""),
  
  "deputy" : rank("deputy", 1, {
  "canFight" : True,
  "canHeal" : False,
  "canHunt" : True,
  "canMate" : False,
  "canInherit" : True,
  "canPatrol" : True,
  "canTrain" : True,
  "canClaim" : False,
  "isUnique" : True}, {
    "autoAge" : False,
    "sourceRank" : None,
    "ageMin" : None
    }, "", ""),
  
  "apprentice" : rank("apprentice", 4, {
  "canFight" : True,
  "canHeal" : False,
  "canHunt" : True,
  "canMate" : False,
  "canInherit" : False,
  "canPatrol" : True,
  "canTrain" : True,
  "canClaim" : True,
  "isUnique" : False}, {
    "autoAge" : True,
    "sourceRank" : "kit",
    "ageMin" : 6
    }, "", ""),
  
  "medicine cat" : rank("medicine cat", 2, {
  "canFight" : False,
  "canHeal" : True,
  "canHunt" : False,
  "canMate" : False,
  "canInherit" : False,
  "canPatrol" : True,
  "canTrain" : True,
  "canClaim" : False,
  "isUnique" : False}, {
    "autoAge" : False,
    "sourceRank" : None,
    "ageMin" : None
    }, "", ""),

  "prey-hunter" : rank("hunter", 3, {
  "canFight" : False,
  "canHeal" : False,
  "canHunt" : True,
  "canMate" : True,
  "canInherit" : False,
  "canPatrol" : True,
  "canTrain" : True,
  "canClaim" : False,
  "isUnique" : False}, {
    "autoAge" : False,
    "sourceRank" : None,
    "ageMin" : None
    }, "", ""),
  }
