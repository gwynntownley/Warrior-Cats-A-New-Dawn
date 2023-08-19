from entity.clan import clan

# WCND CALCULATOR

def parseOpt(oldopt):
  newopt = list(enumerate(oldopt, start=1))
  i = 0
  while i < len(newopt):
    if (len(newopt) <= 9):
      print("[%d] %s" % (newopt[i][0], newopt[i][1]))

      i += 1
    elif (len(newopt) <=19):
      try:
        print("[%d] %s    [%d] %s" % (newopt[i][0], newopt[i][1],
                                      newopt[i + 1][0], newopt[i + 1][1]))
        i += 2
      except:
        print("[%d] %s" % (newopt[i][0], newopt[i][1]))
        i += 1
    else:
      try:
        print("[%d] %s    [%d] %s    [%d] %s" % (newopt[i][0], newopt[i][1],
                                                 newopt[i + 1][0], newopt[i + 1][1],
                                                 newopt[i + 2][0], newopt[i + 2][1]))
        i += 3
      except:
        print("[%d] %s" % (newopt[i][0], newopt[i][1]))
        i += 1
        
def parseSel(selection, prompt):
  conf = False
  cmd = "alfalfa"
  while conf == False:
    try:
      choice = selection[int(cmd) - 1]
      conf = True
    except:
      cmd = input(prompt)
  return choice

def parseDesc(coat, pattern, pronoun, build, eye):
  if "-" in pattern:
    pelt_coat = coat.replace(" ", "-")
  else:
    pelt_coat = coat
    
  if "with" in pattern:
    pelt = "%s %s%s" % (pelt_coat, pronoun, pattern)
  else:
    pelt = "%s%s %s" % (pelt_coat, pattern, pronoun)

  if coat == "pale ginger" and pattern == "-and-black":
      pelt = "pale tortoiseshell %s" % pronoun
  elif (coat == "ginger" or coat == "flame-coloured") and pattern == "-and-black":
      pelt = "tortoiseshell %s"  % pronoun
  elif coat == "reddish-brown" and pattern == "-and-black":
      pelt = "dark tortoiseshell %s"  % pronoun
  if coat == "black" and pattern == "-and-black":
      pelt = "black %s" % pronoun
  elif coat == "black" and pattern == " with darker patches":
      new_pat = "black"
      while new_pat == "black":
        new_pat = (random.choice(coats))
      pattern = " with %s patches" % new_pat
      pelt = "%s %s%s" % (coat, pronoun, pattern)
  elif coat == "white" and pattern == "-and-white":
      pelt = "white %s" % pronoun
  elif coat == "white" and pattern == " with lighter patches":
      new_pat = "white %s" % pronoun
      while new_pat == "white":
        new_pat = (random.choice(coats))
      pattern = " with %s patches" % new_pat
      pelt = "%s %s%s" % (coat, pronoun, pattern)

  if "with" in pattern:
      description = ("%s %s and %s eyes" % (build, pelt, eye))
  else:
      description = ("%s %s with %s eyes" % (build, pelt, eye))

  return description

def findRel(tarclan, tarcat, rel):
  for r in list(clan.clans[tarclan].cats[tarcat].relationships):
    if clan.clans[tarclan].cats[tarcat].relationships[r][0] == rel:
      return r
      break

            
