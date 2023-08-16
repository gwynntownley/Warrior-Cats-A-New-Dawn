import random
from data.file import codebits
from entity.cat import cat
from entity.map import landmarks

class merchant(object):
  def __init__(self, name, inventory):
    self.name = name
    self.inventory = inventory
  merchants = {}
    
def genMer():

  var_name = ""
  for a in range((random.randint(5, 15))):
    var_name = var_name + (random.choice(codebits))

  invA = (random.choice(list(landmarks)))
  invB = (random.choice(list(landmarks)))
  invC = (random.choice(list(landmarks)))
  
  merchant.merchants[var_name] = merchant((random.choice(cat.rogueNames)), {

        (random.choice(landmarks[invA])) : {"price" : (random.randint(25, 75)),
                                                                       "stock" : (random.randint(5, 15))},
        
        (random.choice(landmarks[invB])) : {"price" : (random.randint(25, 75)),
                                                                       "stock" : (random.randint(5, 15))},

        (random.choice(landmarks[invC])) : {"price" : (random.randint(25, 75)),
                                                                       "stock" : (random.randint(5, 15))}
      })
