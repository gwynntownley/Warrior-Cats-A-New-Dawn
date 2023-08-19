### ACTION/SELECT

selectText = {

  "focus" : """
    What should the focus of this patrol be?

    [1] Surveying the area and keeping an eye on things. (no change)

    [2] Finding potential recruits. (increased chance of finding recruits)

    [3] Gathering herbs. (increased chance of discovering herbs--only works if territory includes "Flower Field")

    [4] Collecting odd trinkets and den-building material. (increased chance of finding new items--only works if territory includes at least one landmark)

    [5] Securing the borders and keeping neighbouring enemies out. (increased chance of enemy encounter)

    > """,

  "catInfo" : "%d: %s (LVL %d, %d/%d WP)",

  "catsNone" : "You have no more cats eligible for a(n) %s!",

  "leaderAdd" : """
              Attention! You are trying to add yourself to this %s. Because you will be away,
              your turns for the duration of the %s will automatically be skipped. Would you still
              like to go? [Y/N]

              > """,

  "capAdd" : """First, you must assign a patrol CAPTAIN to lead the %s. Enter their ID below.
            
            > """,

  "catAdd" : """To assign a cat to this %s, enter their ID. To send the %s as is, say DONE.
            
            > """,

  "sent" : "You sent some of your cats %s! Wish them well!",

  
  
}

### DATA/CLOCK

clockText = {

  "invadeCat" : "Cats from %s have invaded your camp!",

  "invadePred" : "Predators have discovered your camp!",

  "return" : "%s and their patrol have returned!",

  "xpGain" : "%s gained %d xp.",

  "landClaim" : "They have claimed new land for %s! Now you will catch more prey when you hunt, and you can recruit more cats.",

  "landType" : "This land is a %s.",

  "landMark" : "This new land also included a landmark: %s!",

  "landFail" : "Unfortunately, the mission was unsuccessful - they found themselves unable to claim the chosen territory for their own.",

  "huntReturn" : "The hunting patrol led by %s has returned!",

  "huntCatch" : "%s has caught a(n) %s for %d feedings and gained %d xp.",

  "huntWP" : "%s lost %d WP in the process.",

  "huntFail" : "Your cats couldn't find anything to catch. The prey might have gone somewhere else...",

  "trainReturn" : "The training session taught by %s has finished!",

  "trainXP" : "%s gained %d fighting xp from training.",

  "trainWP" : "%s lost %d WP in the process.",

  "borderReturn" : "The border patrol led by %s has returned!",

  "borderPrey" : "%s came back with a(n) %s worth %d feedings.",

  "borderItem" : "%s found a(n) %s while exploring. It has been added to the Clan's inventory.",

  "borderHurt" : "%s got injured during the patrol.",

  "borderWP" : "%s lost %d WP.",

  "borderXP" : "%s has earned %d experience points from this patrol.",

  "preyGreat" : "The patrol noticed that prey was running especially well here.",

  "preyGood" : "The patrol found plenty of good hunting spots in that part of the territory.",

  "preyPoor" : "The patrol found hunting in the area to be poor, though there were still some prey about.",

  "preyBare" : "The patrol noticed this territory was almost completely bare of prey. Hunting there would be a waste of time.",

  "famine" : "They also found signs of famine in the area--the hunting here may begin to suffer.",

  "growth" : "This part of the territory is showing signs of growth and prosperity. If it continues to thrive like this, the hunting conditions may improve."

}

### ENTITY/CAT

catText = {

  "nameKit" : """What would you like to name your kit, a(n) %s ? root only please.
        
        > """,

  "recruitIntro" : "Your patrol has brought back a(n) %s named %s. They would like to join %s.",

  "recruitAccept" : """Do you accept them into %s? [Y/N]

      > """,

  "mentorAssign" : """
            Please enter the ID of the cat you would like to make %spaw's mentor below.

            > """,

  "mentorConf" : "%s is now %spaw's mentor.",

  "recruitConf" : "%s has joined the %s.",
}

### MENU/MAIN

mainText = {
  
  "title" : """Welcome to:

  ___   _       __                _                                                                  ___
 |     | |     / /___ ___________(_)___  _____                                                          |
|      | | /| / / __ `/ ___/ ___/ / __ \/ ___/  adapted from original series by ERIN HUNTER              |
|      | |/ |/ / /_/ / /  / /  / / /_/ / /       a FUNNYBUG STUDIOS project                              |
|      |__/|__/\__,_/_/__/_/  /_/\____/_/     ___       _   __                ____                       |
|                  / ____/___ _/ /_______    /   |     / | / /__ _      __   / __ \____ __      ______   |
|                 / /   / __ `/ __/ ___(_)  / /| |    /  |/ / _ \ | /| / /  / / / / __ `/ | /| / / __ \  |
|        BETA    / /___/ /_/ / /_(__  )    / ___ |   / /|  /  __/ |/ |/ /  / /_/ / /_/ /| |/ |/ / / / /  |
|      0.6.5     \____/\__,_/\__/____(_)  /_/  |_|  /_/ |_/\___/|__/|__/  /_____/\__,_/ |__/|__/_/ /_/   |
 |___                                                                                                ___|""",
  
  "startCmd" : """
    Please enter one of the commands below:

    [N]ew Game

    [L]oad Game
    
    > """,

  "expoA" : "You are the leader of a band of wandering cats. [press enter to continue]",

  "expoB" : "Thrust from your old home, you set out to lead a search for suitable land.",

  "expoC" : "But, days turned to moons, and unease to peril.",

  "expoD" : "For a long time, it seemed all hope was lost...",

  "expoE" : "Until %s, a(n) %s %s, sees something in the distance..!",

  "landFound" : """
      "There!" cries %s. "A(n) %s. That's where our new home ought to be."
      """,

  "landChoice" : """
      "A %s, %s.." comments %s, a(n) %s %s. "Are we sure that's right for us?"

      %s and %s both turn to look at you. What do you say?

      [Y]es, I like that. Our new home will be a(n) %s %s

      [N]o, let's keep looking.

      > """,

  "landVeto" : "You reject %s, and opt to continue the search.",

  "guideA" : """

=!= Alert =!=

Congratulations! You have made your first decision as leader.

You will have to make many of these throughout your time managing
your band of cats, though many of them can be overturned later
if you find yourself unhappy with your decision.

Other cats have their own ideas on how things ought to be run,
so if you find yourself unable to decide, seeking counsel is
always an option.

= = = = = = =
    """,

  "landApprove" : "Your new home is a/n %s, %s",

  "landMark" : "Your camp contains a(n) %s.",

  "factionType" : """
  You traveled here a loose group, but now that you have a home, it only makes sense
  to organise. What kind of faction would you like to lead? You can be a Clan, a Tribe,
  or something else entirely. Reply with the noun you would like your group to
  be referred to.
    
  > """,

  "factionName" : """
  Now that your %s has survived the journey here, it would only be fitting to give them a name.
  Please enter it below.
  You will have opportunities to change it later.
    
  > """,

  "factionIcon" : """
  %s must be unique from all the others, and
  an official symbol can help you really make your mark. Please enter the ID
  of the icon you would like to use as %s's symbol.
          
  > """,

  "factionMotto" : """
  Finally, no great faction's complete without a motto expousing
  its virtues! What is a motto all your cats can cry on the battlefield?
        
  > """,

  "leaderIntroA" : "Now, about you, leader of the great %s...",

  "leaderIntroB" : "Before you can receive your nine lives from StarClan, they need to know more about you. This is important, so take your time. Firstly...",

  "leaderName" : """
      Names in A New Dawn follow a prefix-root-suffix rule. To enter your name, enter using this syntax,
      so the different parts of your name are stored separately: prefix/root/suffix

      The root is absolutely required, but the prefix/suffix are not. To not include them,
      simply leave the form blank. Here are some examples of this syntax :

      root only
      /Scourge/
      root + suffix
      /Fire/star
      prefix + root + suffix
      General /Wound/wort
      prefix + root
      Captain /Holly/
      
      With that out of the way ...
      What do you call yourself, great leader?
        
      > """,

  "leaderGender" : """
  A few more questions, if you don't mind--
  Wat do you consider yourself to be, gender-wise ?
    [T]om
    [S]he-cat
    [C]at
      
  > """

  "leaderCoatA" : """
  Pelt colour in A New Dawn is split into two parts : the base and the pattern.
  If, say, you are a tortoiseshell cat, your base would be 'ginger' and your pattern would be ' with black patches'. 
  While this will be entered like 'ginger with black patches', it will be stored as 'tortoiseshell'.
  Likewise, if you are a brown tabby, your base would be 'brown' and your pattern would be ' tabby'. """,

  "leaderCoatB" : """
  Please select the base of your coat, from the options above.
        
  > """,

  "leaderPattern" : """
  Please select your coat's pattern, from the options above.
  If you don't have a coat pattern, select one of the blank fields.
  ( there are multiple blank fields - the one you pick makes no difference )
        
  > """,

  "leaderEyes" : """
  Please select your eye colour, from the options above.
        
  > """,

  "leaderBuild" : """
  Please select a physical trait that describes you, from the options above.
        
  > """,

  "leaderTrait" : """
  Please select a personality trait that describes you, from the options above.
        
  > """,

  "leaderQuote" : """Final thing! What's a quote that you believe encompasses you, as a leader?
    
  > """,

  "welcome" : "Welcome to A New Dawn, %s of %s! May you have many great adventures in the vast wilderness.",

  "othersA" : "You are not alone in the wilderness. [press enter]",

  "othersB" : "The nearby factions have come to introduce themselves.",

  "genError" : "ERROR DURING FACTION GENERATION. Sending you back to the main menu... [press enter to accept]"

  "lifeScene" : """
  
    =!= CUTSCENE =!=
    
    The first task of a new leader is receiving their nine lives.
    
    At the %s, you gain the following lives: 
    
    """,

  "lifeGift" : "From %s, your %s, the gift of %s.",

  "lifeEnd" : "=!= END OF CUTSCENE =!=",

  "load" : """
    Enter the ID of the file you would like to load.
    """,

  "cont" : "Press enter when you're ready."


}
