bank = {
  "bank_level" : 1,
  "Prey" : 0,
  "Herbs" : 0,
  "Dog Bone" : 0,
  "Spiked Collar": 0,
  "Shiny Trinket": 0,
  "Thorny Rose": 0,
  "Violet Flower": 0,
  "Cat Mint": 0,
  "Round Stone": 0,
  "Vole Skull": 0,
  "Clear Crystal": 0,
  "Rainbow Beetle": 0,
  "Dove Feather": 0,
  "Fresh Moss": 0,
  "Huge Pelt": 0,
  "Sharp Fang": 0,
  "Viper Venom": 0
}

def menuBazaar():
  cmd = "alfalfa"
  while not cmd in ["J", "L", "M"]:
    cmd = input("""Welcome to the Backway Bazaar, an alleyway hidden from prying eyes that is bustling with activity!
                   Here you can barter for herbs and items in the Merchant Hall, or peruse the other "specialty shops".
                   New stores pop up and old ones are upgraded all the time, so be sure to check back frequently!

    [EDDIE'S SHOP UNDER CONSTRUCTION]

    [J]ay the Healer
    
    [L]iz the Banker

    [M]erchant Hall
    
    """).upper()

  # Jay
  
  elif cmd == "J": 
    price = (random.randint(1, 10))
    while not cmd == "Y" and not cmd == "N":
      cmd = input("""
      [Jay] : "Oi, Clan cat. I sell all kinds'a medicinal stuff here ... well,
      that's a lie, I just sell herbs. But in the future there might be more ... so
      keep an eye open if you got prey to fork over.
      
      That said, the current price per herb is %d prey. Do you wanna buy?"

      [Y/N]
      
      > """ % price)
      cmd = cmd.upper()
    if cmd == "Y":
      amt = "alfalfa"
      conf = False
      while conf == False:
        try:
          if (price * int(amt)) > clan.clans["player_Clan"].prey:
            print("""
            [Jay] : "Oi, what is it yer tryna pull? You can't afford these herbs! You tryna rip me off or somethin- think I'm stupid?!" """)
          else:
            clan.clans["player_Clan"].prey -= (price * int(amt))
            clan.clans["player_Clan"].herbs += int(amt)
            print("""
            [Jay] : "Here ya go. Have a day." """)
          conf = True
        except:
          amt = input("""
          [Jay] : "How many herbs we talkin' here? Don't worry about stock, I can get more in a flash if you order more than I got on me." 
          
          > """)
    else:
      print("""
      [Jay] : "Suuuure, dude. Just hold up the line for everyone else and *not* buy anything. You %s cats are all the same... come back when you're going to actually buy something." """ % (clan.clans["player_Clan"].noun))
      purchased = True

  # Liz

  elif cmd == "L":
    cmd = "alfalfa"

    purchased = False

    while purchased == False:

      while not cmd in ["W", "D", "E"]:

        print("""

        [Liz] : "... huh? Oh, hi, customer! Welcome to the Backway Bank.
        We keep your prey, herbs, and items all safe in case of emergency.
        What would you like to do?"

        -- Contents --
        
        """)

        id = 1
        for i in folder.folders["bank"].contents.copy():
          if not i == "bank_level":
            print("[%d] %s: %d" % (id, i, folder.folders["bank"].contents[i]))
            id += 1

        cmd = input("""

        [W]ithdraw

        [D]eposit

        [E]xit

        > """).upper()

      # Set action

      if cmd == "E":
        conf = True
        action = "exit"
      elif cmd == "W":
        action = "withdraw"
      else:
        action = "deposit"
          
      cmd = "alfalfa"
      conf = False

      # Select

      while conf == False:
        try:
          target = list(folder.folders["bank"].contents)[int(cmd)]
          conf = True
        except:
          cmd = input("""

        [Liz] : Enter the ID of the item you'd like to %s.

        > """ % action)

      # Withdraw
      
      if action == "withdraw":
        if folder.folders["bank"].contents[target] > 0:
          amt = "alfalfa"
          conf = False
          while conf == False:
            try: 
              if int(amt) > folder.folders["bank"].contents[target]:
                amt = folder.folders["bank"].contents[target]

              if target == "Prey":
                clan.clans["player_Clan"].prey += amt
                folder.folders["bank"].contents[target] -= amt

                print("""[Liz] : "...enjoy your %d prey... have a good day." """ % amt)
              elif target == "Herbs":
                clan.clans["player_Clan"].herbs += amt
                folder.folders["bank"].contents[target] -= amt

                print("""[Liz] : "...enjoy your %d herbs... have a good day." """ % amt)
              else:
                folder.folders["inventory"].contents[target] += amt
                folder.folders["bank"].contents[target] -= amt

                print("""[Liz] : "...enjoy your %d %s... have a good day." """ % (amt, target))
              
              conf = True
              purchased = True

            except:
              amt = input("""
              [Liz] "Sure... how much are you taking out? You have %d %s."
              
              > """ % (folder.folders["bank"].contents[target], target))

          
        else:
          print("""[Liz] : "Oh... it looks like you don't have any %s to withdraw." """ % target)

      # Deposit

      elif action == "deposit":
        if folder.folders["bank"].contents[target] == limit:
          amt = "alfalfa"
          conf = False
          while conf == False:
            try: 
              if int(amt) > limit:
                amt = folder.folders["bank"].contents[target]
                print("""[Liz] : "Uh, it doesn't look like we have enough room for %d %s, so I rounded down to %d..." """)

              if target == "Prey":
                clan.clans["player_Clan"].prey += amt
                folder.folders["bank"].contents[target] -= amt

                print("""[Liz] : "...%d prey has been deposited... have a good day." """ % amt)
              elif target == "Herbs":
                clan.clans["player_Clan"].herbs += amt
                folder.folders["bank"].contents[target] -= amt

                print("""[Liz] : "...%s herbs has been deposited... have a good day." """ % amt)
              else:
                folder.folders["inventory"].contents[target] += amt
                folder.folders["bank"].contents[target] -= amt

                print("""[Liz] : "...%d %s has been deposited... have a good day." """ % (amt, target))
              
              conf = True
              purchased = True

            except:
              amt = input("""
              [Liz] "Sure... how much are you taking out? You have %d %s."
              
              > """ % (folder.folders["bank"].contents[target], target))

          
        else:
          print("""[Liz] : "Oh... it looks like you have reached the %s cap, which is %d." """ % (target, limit))

      # Exit

      else:
        print("""[Liz] : "Come again!" """)

  # Merchant Hall

  elif cmd == "M":
    id = 1
    for i in folder.folders["merchants"].contents.copy():
      print("[%d] %s (wares: %s)" % (id, folder.folders["merchants"].contents[i].name,
                                     ", ".join(list(folder.folders["merchants"].contents[i].inventory))))
      id += 1
    cmd = "alfalfa"
    conf = False
    while conf == False:
      try:
        target = list(folder.folders["merchants"].contents)[int(cmd) - 1]
        conf = True
      except:
        cmd = input("""
        Which merchant would you like to visit? Please enter their ID.
        
        > """)

    purchased = False
    while purchased == False:
      print("""
      [%s] : "Hello, hello! Please examine my wares, and tell me what you'd like to purchase by entering the item's ID! If you don't wish to buy anything, just say 'no' or 'bye'!"
      """ % folder.folders["merchants"].contents[target].name)

      id = 1

      for i in folder.folders["merchants"].contents[target].inventory:
        print("""[%d] %s (price : %d prey) (stock : %s)
              """ % (id, i, folder.folders["merchants"].contents[target].inventory[i]["price"],
                                                          folder.folders["merchants"].contents[target].inventory[i]["stock"]))

      cmd = input("> ")

      try:
        cmd = int(cmd)
        item = list(folder.folders["merchants"].contents[target].inventory)[cmd]
        
        if folder.folders["merchants"].contents[target].inventory[item]["stock"] < 1:
          print("""
          [%s] : "Oops, looks like we're fresh out of stock." """ % folder.folders["merchants"].contents[target].name)
        else:
          amt = "alfalfa"
          try:
            if int(amt) > folder.folders["merchants"].contents[target].stock_1:
              print("""
              [%s] : "I don't have enough of that item, I'm afraid." """ % folder.folders["merchants"].contents[target].name)
            elif folder.folders["merchants"].contents[target].inventory[item]["price"] * int(amt) > clan.clans["player_Clan"].prey:
              print("""
              [%s] : "It seems you can't afford this item. Come back when you can." """ % folder.folders["merchants"].contents[target].name)
            else:
              folder.folders["merchants"].contents[target].inventory[item]["stock"] -= int(amt)
              folder.folders["inventory"].contents[item] += int(amt)
              clan.clans["player_Clan"].prey -= folder.folders["merchants"].contents[target].inventory[item]["price"] * int(amt)
              print("""
              [%s] : "Thank you so very much for your purchase!" """ % folder.folders["merchants"].contents[target].name)
              purchased = True
          except:
            amt = input("""
            [%s] : "How many do you wish to purchase?"
            
            > """ % folder.folders["merchants"].contents[target].name)
      except:
        print("""
        [%s] : "Have a wonderful day!" """ % folder.folders["merchants"].contents[target].name)
        purchased = True
