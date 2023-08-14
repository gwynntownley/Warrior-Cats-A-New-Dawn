## executible python script to boot WARRIOR CATS : A NEW DAWN

## IMPORTS

from menu.main import menuMain
import traceback

# contain game within an unbreakable while loop

on = True

while on == True:
  
  try:
    
    # launch main menu
    
    menuMain()
    
    # if user fails, print and continue loop
    
    print("Unfortunately, despite your best efforts...")
    print("Your cats could not withstand the fierce wilderness...")
    print("And disbanded.")
    print("...")
    print("Sending you back to the main menu...")
    
  except Exception:
    
    # if system crashes, print traceback and continue loop
    
    print("Oops! Seems the game has run into an error. Here's the traceback, if you're curious: ")
    traceback.print_exc()
    input("Press enter when you're ready to be sent to the main menu.")

"""
DEVNOTES

Agenda
- add "gathering" (just have it spout out events for now, like it used to be-- add interactions later)
-- start with disease to test
- develop mentorship system
-- appoint mentors to cats, apprentices by default are prompted to assign mentor
-- when mentors and apprentices are on the same patrol, xp for both are boosted
- if invaders attack the camp (predators or rivals), and it is not defended successfully, they will inflict damage on the faction
-- kill cats, take prey, herbs, and/or inventory items, and in the future when camp building is added your dens will be damaged

- new item system
Rarity *: can be found in any territory. base material used for a lot of things.
Rarity **: can be found in some territory types. used to fortify higher-level dens and unique structures (such as an aviary).
Rarity ***: can be found in exclusive landmarks. used in gifts and trading among other cats and the Bazaar.
Rarity ****: cannot be found naturally. used for equipment or augmenting spiritual power.

* Items
Stone
Twig
Mud
Fur
Feather
Twoleg Junk

- to heal a sick or injured cat, a cat must be assigned to "heal" them, taking an amount of turns comparable to a hunting patrol, making that cat unusable
-- odds of healing success are based on healing skill, which can be increased with special training sessions that cost herbs. this is so players can't
just make every rank a healer rank and assign random cats to instantly cure whoever

"""
