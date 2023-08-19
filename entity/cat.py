import random

# import clan class from clan script
from bin.text import catText
from entity.clan import clan
from entity.map import landmarks
from entity.rank import rank, rankTemplates
from data.file import codebits
from data.parse import findRel

# Cat objects

class cat(object):
  def __init__(self, name, prefix, root, suffix, rank, 
   description, pronoun, coat, pattern, eyes, build, age, age_status, scars, mutations, disabilities,
   title, personality, quote, rep, likes, found_likes, favourite, found_favourite,
   relationships, 
   wp, lvl, xp, stats, moves, allegiance,
   faith, loc):

    # identity
      self.name = name
      self.prefix = prefix
      self.root = root
      self.suffix = suffix
      self.rank = rank
    # description
      self.description = description
      self.pronoun = pronoun
      self.coat = coat
      self.pattern = pattern
      self.eyes = eyes
      self.build = build
      self.age = age
      self.age_status = age_status
      self.scars = scars
      self.mutations = mutations
      self.disabilities = disabilities
    # social
      self.title = title
      self.personality = personality
      self.quote = quote
      self.rep = rep
      self.likes = likes
      self.found_likes = found_likes
      self.favourite = favourite
      self.found_favourite = found_favourite
    # relationships
      self.relationships = relationships
    # stats
      self.wp = wp
      self.lvl = lvl
      self.xp = xp
      self.stats = stats
      self.moves = moves
    # alignment
      self.allegiance = allegiance
      self.faith = faith
    # locale
      self.loc = loc

  # customization features

  # names

  rogueNames = ["Varjak", "Oliver", "Liz", "Snowball", "Napoleon", "Boo", "Autumn",
                 "Ninja", "Sassy", "Charlie", "Finley", "Kimi", "Xochi", "Katara",
                 "Butterbug", "Fleckie", "Nyx", "Wednesday", "Snuggles", "Teddy", "William",
                 "Queenie", "Pablo", "Jerusalem", "Olaf", "Cookie", "Bowie", "Lucy", "DJ",
                 "Clay", "Rainbow", "Joey", "Zooey", "Freckles", "Sandy", "Waffle Master",
                 "Star", "Petunia", "Lily", "Dink", "Mango", "Diez", "Bart", "Litchi", "Lulu",
                 "Smokey", "Smudge", "Zig", "Zag"]

  roots = [
      "Acorn", "Adder", "Air", "Alder", "Amber", "Ant", "Apple", "Arch", "Ash", "Aspen",
      "Badger", "Bark", "Bay", "Bee", "Beech", "Beetle", "Berry", "Birch", "Bird", "Black", "Blaze", "Blizzard", "Bloom", "Blossom", "Blue", "Boulder", "Bounce", "Bracken", "Bramble", "Breeze", "Briar", "Bright", "Brindle", "Bristle", "Broken", "Brown", "Bumble", "Buzzard",
      "Cedar", "Cherry", "Chive", "Cinder", "Cinnamon", "Claw", "Cloud", "Clover", "Coal", "Cone", "Copper", "Cricket", "Crooked", "Crouch", "Crow", "Curl", "Cypress",
      "Daisy", "Dapple", "Dark", "Dauber", "Dawn", "Dead", "Deer", "Dew", "Doe", "Dove", "Down", "Drift", "Duck", "Dusk", "Dust",
      "Eagle", "Ebony", "Echo", "Eel", "Eclipse", "Edge", "Egret", "Elder", "Ember",
      "Fallen", "Fallow", "Fawn", "Feather", "Fennel", "Fern", "Ferret", "Fidget", "Fin", "Finch",  "Fire", "Flail", "Flame", "Flash", "Flax", "Fleet", "Flicker", "Flint", "Flip", "Flower", "Flutter", "Fly", "Fog", "Fox", "Freckle", "Fringe", "Frog", "Frond", "Frost", "Furze", "Fuzzy",
      "Goat", "Golden", "Goose", "Gorse", "Grass", "Grape", "Gravel", "Grey", "Green", "Gull",
      "Hail", "Half", "Hare", "Hatch", "Haven", "Hawk", "Hay", "Hazel", "Heather", "Heavy", "Heron", "Hickory", "Hill", "Hollow", "Holly", "Honey", "Hoot", "Hop", "Hope", "Horse", "Hound",
      "Ibex", "Ibis", "Ice", "Icy", "Indigo", "Inferno", "Ivy",
      "Jackal", "Jade", "Jagged", "Jay", "Jitter", "Jump", "Jumping", "Juniper", "Jute",
      "Keen", "Kestrel", "Kindle", "Kink", "Kite", "Kudu",
      "Lake", "Larch", "Lark", "Lavender", "Leaf", "Leopard", "Lichen", "Light", "Lightning", "Lily", "Lion", "Little", "Lizard", "Log", "Long", "Lost", "Loud", "Lynx",
      "Maggot", "Mallow", "Maple", "Marigold", "Marsh", "Meadow", "Midge", "Milk", "Minnow", "Mint", "Mist", "Misty", "Mole", "Moon", "Morning", "Moss", "Mossy", "Moth", "Mottle", "Mouse", "Mud", "Mumble", "Myrtle",
      "Nectar", "Needle", "Nettle", "Newt", "Night", "Noble", "Noodle", "Nut",
      "Oak", "Oat", "Odd", "Olive", "One", "Onion", "Orange", "Otter", "Owl",
      "Pale", "Parsley", "Patch", "Pear", "Pebble", "Perch", "Petal", "Plum", "Pod", "Pool", "Poppy", "Pounce", "Prickle", "Primrose", "Puddle",
      "Quail", "Quartz", "Quick", "Quiet", "Quill", "Quiver", "Quokka",
      "Rabbit", "Ragged", "Rain", "Rat", "Raven", "Red", "Reed", "Ripple", "River", "Robin", "Rock", "Rook", "Root", "Rose", "Rowan", "Rubble", "Running", "Rush", "Russet", "Rye",
      "Sage", "Sand", "Sandy", "Scorch", "Sedge", "Seed", "Shade", "Shadow", "Sharp", "Sheep", "Shell", "Shimmer", "Shining", "Short", "Shred", "Shrew", "Shy", "Silver", "Sky", "Slate", "Sleek", "Slight", "Sloe", "Small", "Smoke", "Snail", "Snake", "Snap", "Sneeze", "Snip", "Snook", "Snow", "Soft", "Song", "Soot", "Sorrel", "Spark", "Sparrow", "Speckle", "Spider", "Spike", "Spire", "Splash", "Spot", "Spotted", "Squirrel", "Stag", "Starling", "Stem", "Stoat", "Stone", "Stork", "Storm", "Strike", "Stumpy", "Sun", "Sunny", "Swallow", "Swamp", "Swan", "Sweet", "Swift",
      "Tall", "Talon", "Tangle", "Tansy", "Tawny", "Terror", "Thistle", "Thorn", "Thrift", "Thrush", "Thunder", "Tiger", "Timber", "Tiny", "Toad", "Torn", "Trout", "Tulip", "Tumble", "Turtle", "Twig",
      "Ugly", "Umber",
      "Valley", "Velvet", "Verdant", "Vine", "Violet", "Vixen", "Vole",
      "Wasp", "Wave", "Weasel", "Web", "Weed", "Wet", "Whisker", "White", "Whorl", "Wild", "Willow", "Wind", "Wish", "Wolf", "Wood", "Wooly", "Wren",
      "Yarrow", "Yawn", "Yellow", "Yerba", "Yonder", "Yucca"
      ]

  suffixes = [
      "bark", "beam", "bee", "belly", "berry", "bird", "blaze", "branch", "breeze", "briar", "bright", "brook", "burr", "bush",
      "claw", "cloud", "crawl", "creek",
      "dapple", "dawn", "drop", "dusk", "dust",
      "ear", "eye", "eyes",
      "face", "fall", "fang", "feather", "fern", "fire", "fish", "flake", "flame", "flight", "flower", "foot", "frost", "fur",
      "gorse",
      "hawk", "haze", "heart",
      "jaw", "jump",
      "leaf", "leap", "leg", "light",
      "mask", "mist", "moon", "mouse",
      "nose",
      "pad", "pelt", "petal", "pool", "poppy", "pounce", "puddle", 
      "runner",
      "scar", "scratch", "seed", "shade", "shine", "sight", "skip", "sky", "slip", "snout", "snow", "song", "speck", "speckle", "spirit", "splash", "spot", "spots", "spring", "stalk", "stem", "step", "stone", "storm", "stream", "strike", "stripe", "swoop",
      "tail", "talon", "thistle", "thorn", "throat", "toe", "tooth", "tuft",
      "watcher", "water", "whisker", "whisper", "willow", "wind", "wing", "wish",
      ]

  # coats

  coats = [
  "black",
  "white",
  "dark grey",
  "heather-grey",
  "light grey",
  "dark brown",
  "reddish-brown",
  "light brown",
  "ginger",
  "flame-coloured",
  "pale ginger"
  ]

  eyes = [
  "red",
  "amber",
  "yellow",
  "olive",
  "green",
  "teal",
  "icy blue",
  "blue",
  "indigo",
  "violet",
  "pink",
  ]

  # builds
  
  builds = [
    "broad-shouldered",
    "fluffy",
    "hairless",
    "huge",
    "large",
    "lithe",
    "muscular",
    "plump",
    "small",
    "short",
    "stocky",
    "tall",
    "thin",
    "tiny",
  ]

  disabilities = [
    "blindness",
    "deafness",
    "muteness",
    "spinal paralysis",
    "facial paralysis"
  ]

  scars = [
    "torn ear",
    "torn tail",
    "shoulder scar",
    "muzzle scar",
    "back scar",
    "chest scar",
    "belly scar",
    "face scar",
    "nose scar",
    "eye scar",
    "tail scar",
    "throat scar",
    "missing leg",
    "missing tail",
    "missing eye"
  ]

  mutations = [
  "bobtail",
  "folded ears",
  "fluffy tail",
  "large paws",
  "polydactyl",  "extra ears",
  "polycoria",
  "sloped head",
  "heterochromia",
  "munchkin"
  ]

  patterns = [
  " spotted",
  " with darker patches",
  "-and-black",
  " with lighter patches",
  "-and-white",
  " pointed",
  " tabby",
  "",
  "",
  ""
  ]

  # character

  dialogue = {
      1 : [
    ["I hate you! I wish somecat else was leader, somecat who isn't so mean !", "When I get bigger, I'm gonna try my hardest to be nothing like you !"],
    ["Oi, shut your mouth! You don't have the right to speak to me like that !", "You're real lucky you're the authority 'round here, or I'd make you pay for your words !"],
    ["Hey, that really hurts! A leader's meant to care about us, not push us around... you're just a big bully !", "You're cruel."],
    ["Shut your fucking mouth.", "Next time you say that to me, I'll rip your tongue out."],
    ["What was that for? You can't just go around being rude like that!", "Why in StarClan's name would you say that ?! Maybe the rumours about your villainy are true."],
    ["You're such an idiot! Talk to me when you learn to think before you speak.", "I've just about had it with your drivel. You're not that clever, you know."],
    ["How dare you insult our ancestors that way! The dead are always with us, and your words will surely anger them.", "If you refuse to change your ways, I fear what lies along your path."],
    ["I hate you! You're boring and lame and I would make an infinitely better leader than you!", "What, you tryna start something, bub ? I don't care if you're the leader, I'll beat your ass anytime."],
    ["No! Stay away! D-don't hurt me, please!", "Y-you're the thing that terrifies me most. I hope you're proud of that."]
          ],
      2 : [
    ["You're a mean, mean cat!", "Grrr !!!!!!!! Go away !!"],
    ["Oi, you better leave, pal... before I make you!", "Hah ! You know, that'd be funny if it weren't so damn pathetic."],
    ["Why did you feel the need to say that? I think... I think I need to go.", "You can be mean to me all you like, but it's not gonna make you look any tougher."],
    ["This is stupid. I'm leaving.", "This conversation is a waste of time."],
    ["Ugh. If you're going to be like this, I'm leaving.", "Hey, who gave you the right to push me around like that ? At least I'm putting in solid effort."],
    ["Hmph. I don't have time for morons like you.", "I prize the time I have, which is why I'm ending this pointless conversation."],
    ["Speaking is a gift. Don't waste it on foolish nonsense such as this.", "Be mindful of your words. Use them poorly and it will be your folly."],
    ["Don't call me shallow! You're shallow. And your face looks stupid, too.", "You know, I'm way too cool for this conversation. I'm getting out of here !"],
    ["When you say t-things like that, it worries me... why do you have to b-be so mean?", "Ack ! I didn't r-realize you came here just to scare me ..."]
          ],
      3 : [
    ["You're no fun ... you never play with us!", "My grown-up friend said you're a 'nincompoop' !"],
    ["Hmph ... I wouldn't go around saying that if I were you. You know it's bad when I won't even say it !", "Eyy, eyy, woah, woah. That's a bit too far with the laughs, mate. Reel it in before you say something you regret !"],
    ["That's pretty mean. I hope you don't talk this way to the more sensitive of our Clanmates.", "I'm sorry if you think I'm wasting your time. I'll ... I'll go if you need me to."],
    ["... I have to go.", "That's not funny."],
    ["Wow. Um, okay. I have no idea how to respond to that.", "I get you're the leader, but you don't need to boss me around. I can handle myself, thanks."],
    ["You don't often think before you speak, do you ?", "Are you sure you know what you're talking about ?"],
    ["When you say something like that, I find it difficult to believe you have our best interests at heart.", "Hmph ... Try not to use that language in the company of our ancestors."],
    ["Aww. You're booooring.", "I'd prank you, but you're no fun even when you're humiliated !"],
    ["Yikes. You know, you scare me sometimes.", "... yikes ! I don't like the sound of that !"]
          ],
      4 : [
    ["Do you want to play moss-ball with me?", "When I grow up, I'm gonna be the bestest warrior ever !"],
    ["Hmph! Serves that guy right.", "I'm itchin' for a fight. You know any sucker I can punch ?"],
    ["Oh no! I hope everyone in that situation turned out okay.", "Well, that sounds like a swell time you had !"],
    ["...", "... what ? Are you talking to me ?"],
    ["It's a beautiful day, isn't it ?", "I'm gonna work extra hard today !"],
    ["What am I doing? Observing... same as every day.", "I wish there were an intellectual equivalent to moss-ball. Moss-puzzle ... mind-ball ... something like that."],
    ["I have advice for you. Talk less... smile more.", "I have advice for you. Don't take advice from an odd fool like me."],
    ["I'm so amazing, don't you agree ?", "Hey ! Want me to say something fourth-wall-breaking ? Hope the answer is yes, because I just did ;)"],
    ["Aaaaah! You startled me !", "... eep ! I mean, w-what's up, big scary leader guy ?"]
          ],
      5 : [
    ["I like playing with you.", "I wanna play again !"],
    ["Ha! You're hilarious.", "Congrats ... you've impressed me."],
    ["Oh, thank you! That's kind of you to say.", "Has anycat told you you look radiant today ?"],
    ["... ha.", "... thanks."],
    ["Thank you. I worked extra hard today and I'm glad to hear it made a difference.", "I can see how you became the leader."],
    ["That's a very clever idea. I'll have to remember that one.", "I can tell by your words that you're no fool. That's respectable."],
    ["These are hard times, but I'm glad you're choosing to do what is right.", "That was a nice story. You have a way with words."],
    ["I think you're pretty cool, for a stuffy ol' leader at least.", "Yeah ! Let's go commit crimes together, bucko !"],
    ["T-thank you, for being so kind and patient with me...", "Oh ! You scared me, but I'm happy it's you."]
          ],
      6 : [
    ["You're nice for a grown-up. You're more fun than the others!", "Yay ! I love when you come to visit me !"],
    ["Say, mate, we should hang out more often! You're pretty fun when you ain't orderin' me around.", "Ey, if anyone tries to throw ya shade, let me at 'em ! No one messes with our leader !"],
    ["I really appreciate that. Even a few kind words go a long way.", "Oh, you're sweet."],
    ["Hm. Thank you... for your company.", "... I like that you're not scared by my silence."],
    ["We should go hunting together sometime! Hanging out with you is always fun.", "We're buds, right ? Prime-time buddies ?"],
    ["Wow, I didn't even notice that. I can appreciate a cat who knows how to read between the lines.", "At last, someone with sense around here. Thank you."],
    ["Our ancestors have their eyes on you. And I know they are proud.", "Great things lie on your path. I can feel it."],
    ["Oh man, that's a riot! Did you hear the one about the medicine cat who married a weasel ?", "Hey, wanna go prank the next poor bloke who pads through the entrance with me ? You seem like the type to appreciate a good practical joke."],
    ["When I'm around you, I don't f-feel so skittish... I wonder why that is?", "Y-you're so warm, and pleasant ... I don't think I could ever be scared by you."],
          ],
      7 : [
    ["You're so awesome ! I wanna be leader too, someday !", "I'm gonna be just like you when I grow up ! You're the coolest cat I know !"],
    ["Oi, mate, don't worry 'bout what they say ! If you ask me, you're a mighty fine leader.", "Ugh. I want to be mean to you so badly, but it's damn near impossible. Why are you the only cat I can't bully ?"],
    ["Thank you so much. I feel proud knowing our Clan is led by such a caring and selfless cat.", "I wish I could be in this moment forever, with you and with this fuzzy feeling in my heart ..."],
    ["I ... appreciate what you've done for the Clan. You're a good leader ... and a good friend.", "... I wish I could tell you how much that means to me. But I can't find ... the words."],
    ["Just know I'll back you up no matter what, got it? I'm proud to have you for a leader.", "I'll die for you ! I know that sounds crazy, but it's true. I'm loyal to you to the end."],
    ["It's rare I meet another cat on my intellectual level. Well done.", "I'm supposed to be the rational one. So why do my thoughts always turn to mush whenever I'm around you ..?"],
    ["You are a wise and well-spoken cat. I'm glad that it is you leading our Clan to greatness.", "I believe our paths have been intertwined from the start. Do you believe it too ?"],
    ["Even though I would obviously make the better leader, I suppose you're a good second best !", "I love you ! I mean, as a joke, of course ... ha-ha, so funny ... funny ... joke ..."],
    ["I wish I was brave, like you! I suppose that's why you're the leader, huh?", "I'm terrified of everything, even of myself, but you ... you make me feel safe. And that's the best feeling in the world."],
          ]

      }

traits = ["calm", "careful", "caring",
                      "cold", "determined", "devoted",
                      "durable", "expressive", "feisty",
                      "hardworking", "impulsive", "intelligent",
                      "kind", "loving", "loyal",
                      "moral", "nervous", "observant",
                      "passionate", "peaceful",  "proud",
                      "resolute", "scrappy", "sharp",
                      "spiritual", "thoughtful", "wise"]


kit_quotes = [
  "When my friends get sad, I get sad. It makes me... want to do whatever I can to make them feel better.",
  "I wish grown-ups wouldn't call me lonely just 'cuz I like being by myself.",
  "I'm gonna be the best warrior ever someday! That's my dream!",
  "The other kits say I'm boring because I'd rather listen to stories rather than run around chasing butterflies... but they're wrong, aren't they?",
  "StarClan will protect me, when nothing else will.",
  "Why do all the grown-ups have to be so boring?",
  "I get scared a lot, but being around braver friends helps me feel brave, too!"
]

quotes = [
  ["I treat my Clanmates not just as comrades, but as family.", "I like to see the beauty in all things."],
  ["A day spent idle is a day wasted.", "My duty is everything to me. I will not rest until it is fulfilled."],
  ["Sometimes I wish my Clanmates would laugh a little more.", "Don't let the world get you down ! Grin through the pain and prove your demons wrong !"],
  ["To be a Clan cat, more than anything, you must have your wits about you at all times.", "We are all a whisker away from death. That is the thrill, is it not ?"],
  ["Persevereance- the ability to overcome any and all obstacles- will serve you much better than foolish courage ever will.", "Surviving is enough."],
  ["Just because I notice things other cats don't, does that make me special ?", "It is true that I see everything, but sometimes I feel like I know nothing."],
  ["You may have the sharper claws, my friend, but in a battle of mind I would surely come out on top.", "I choose to wage war with my words."],
  ["Where would the Clans be without unity ? Without comaraderie ? Without love ?", "They call me weak. But they are the ones who forget that love is the strongest force of all."],
  ["Am I the only one who constantly feels as if they are being watched ?", "I think I'm paranoid ... and complicated."],
  ["When I joined the Clans, I joined knowing I would one day die for my Clan. And I am perfectly content with that.", "In this world, unity is power. And solitude is death."],
  ["Kindness is a preferable battle tactic to violence. Ever heard of 'kill 'em with kindness'?", "The best we can do is be good, right ?"],
  ["Pride is the ultimate virtue, for it is pride in me, my Clan, and the Warrior Code that drives me to bring good to the world.", "It's good to know your own greatness."],
  ["When I set my mind to something, I'm not letting it go. That's just how I am.", "Don't underestimate me ! I'll fight to the death to protect what's mine !"],
  ["I would rather be a weakling with wits than a powerful fool.", "True power is the wisdom to know that there is no true power."],
  ["Patience will get you much farther than a quick wit.", "I will wait for my chance to shine. Forever, if necessary."],
  "What's the point in feeling at all ? Just to end up getting hurt ?", 
  "StarClan works in mysterious ways.", 
  "I think thoughtfulness is a skill, like hunting or fighting. You need to hone it.", 
  "If you ask me, the Clans fight far too often. We all share the same culture and all worship StarClan- what's the point in throwing spittle over nothing?", 
  "Not even the leader can stop me from getting my way!", 
  "'Caring too much' isn't a fault, not really. If you ask me, cats nowadays care too little.",
  "Whatever comes my way, rest assured I will survive.", 
  "When I'm happy, I laugh. When I'm sad, I weep. It's disingenuous to hide your feelings.",
  "Call me stubborn, but being firm in your beliefs is not a flaw. To be sure of yourself is a grand thing to be.", 
  "It's important to put care into every pawstep you take. You never know when you may trip and fall.", 
  "I have zero sympathy for the unfaithful. When I grab ahold of something, I remain devoted to it, simple as that.", 
  "My paws are guided not by law, but by virtue, as all cats' paws should be"]


def genKit(c, Aparent, Bparent, kit_count):

  # Start
  
  for i in range(0, kit_count):

    for a in clan.clans[c].cats.copy():
      if clan.clans[c].cats[a].rank == "leader":
        leader = a
                  
    var_name = ""
    for i in range(8):
      var_name = var_name + (random.choice(codebits))

    # Gender assignment

    pronoun = (random.choice(["cat", "tom", "she-cat"]))

    # Physical properties

    rando = (random.randint(0, 1))
    if rando == 0:
      build = clan.clans[c].cats[Aparent].build
    else:
      build = clan.clans[c].cats[Aparent].age_status[Bparent].build

    rando = (random.randint(0, 1))
    if rando == 0:
      coat = clan.clans[c].cats[Aparent].coat
    else:
      coat = clan.clans[c].cats[Aparent].age_status[Bparent].coat

    rando = (random.randint(0, 1))
    if rando == 0:
      pattern = clan.clans[c].cats[Aparent].pattern
    else:
      pattern = clan.clans[c].cats[Aparent].age_status[Bparent].pattern

    rando = (random.randint(0, 1))
    if rando == 0:
      eye = clan.clans[c].cats[Aparent].eyes
    else:
      eye = clan.clans[c].cats[Aparent].age_status[Bparent].eyes

    
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
    elif coat == "white" and pattern in [" with lighter patches", " with white patches", "-and-white"]:           
        pelt = "white %s" % pronoun
        new_pat = "white %s" % pronoun
        while "white" in new_pat:
          new_pat = (random.choice(coats))
        pattern = " with %s patches" % new_pat
        pelt = "%s %s%s" % (coat, pronoun, pattern)

    if "with" in pattern:
        description = ("%s %s and %s eyes" % (build, pelt, eye))
    else:
        description = ("%s %s with %s eyes" % (build, pelt, eye))

    clan.clans[c].cats[var_name] = cat(

    "", "", "", "kit", "kit",
    description, pronoun, coat, pattern, eye, build, 0, {"isqueen" : False, "pregnant" : 0}, [], [], [],
    "Neutral", [], "", 0, [], [], "", "",
    "", "", "unknown", "unknown",
    5, 0, 0, {"Willpower" : 5, "Strength" : 1, "Toughness" : 1, "Speed" : 1, "Precision" : 1, "Charisma" : 1}, [],
    clan.clans[c].name, "Neutral", "")

    # Disabilities and mutations

    for i in clan.clans[c].cats[Aparent].mutations:
      if i in clan.clans[c].cats[Aparent].age_status[Bparent].mutations:
        odds = 1
      else:
        odds = 2
      rando = (random.randint(1, 3))
      if rando > odds:
        clan.clans[c].cats[var_name].mutations.append(i)

    for i in cat.disabilities:
      rando = (random.randint(1, 40))
      if rando == 1:
        clan.clans[c].cats[var_name].disabilities.append(i)

    if "blindness" in clan.clans[c].cats[var_name].disabilities:
      clan.clans[c].cats[var_name].stats["Toughness"] += 2
      clan.clans[c].cats[var_name].stats["Precision"] -= 2
    if "spinal paralysis" in clan.clans[c].cats[var_name].disabilities:
      clan.clans[c].cats[var_name].stats["Willpower"] += 20
      clan.clans[c].cats[var_name].stats["Speed"] -= 4
    if "facial paralysis" in clan.clans[c].cats[var_name].disabilities:
      clan.clans[c].cats[var_name].stats["Strength"] += 2
      clan.clans[c].cats[var_name].stats["Precision"] -= 2

    # Liked items

    for i in range(random.randint(3, 5)):
      like = random.choice(list(landmarks))
      clan.clans[c].cats[var_name].likes.append(random.choice(landmarks[like]))
    like = random.choice(list(landmarks))
    clan.clans[c].cats[var_name].likes.append(random.choice(landmarks[like]))
    clan.clans[c].cats[var_name].favourite = (random.choice(landmarks[like]))

    if clan.clans[c].cats[Aparent].pronoun == "tom":
      titleA = "father"
    elif clan.clans[c].cats[Aparent].pronoun == "she-cat":
      titleA = "mother"
    else:
      titleA = "parent"

    if clan.clans[c].cats[Aparent].age_status[Bparent].pronoun == "tom":
      titleB = "father"
    elif clan.clans[c].cats[Aparent].age_status[Bparent].pronoun == "she-cat":
      titleB = "mother"
    else:
      titleB = "parent"
      

    clan.clans[c].cats[var_name].relationships[Aparent] = [titleA, (random.randint(1, 10))]
    clan.clans[c].cats[var_name].relationships[Bparent] = [titleB, (random.randint(1, 10))]

    # Personality

    clan.clans[c].cats[var_name].personality.append((random.choice(traits)))
    
    personality = (random.choice(clan.clans[c].cats[var_name].personality))
    if clan.clans[c].cats[var_name].age < 6:
  
      if personality in ["proud", "impulsive", "passionate"]:
        clan.clans[c].cats[var_name].quote = kit_quotes[0]
      elif personality in ["caring", "kind", "loving", "peaceful"]:
        clan.clans[c].cats[var_name].quote = kit_quotes[1]
      elif personality in ["cold", "calm", "resolute", "durable"]:
        clan.clans[c].cats[var_name].quote = kit_quotes[2]
      elif personality in ["determined", "devoted", "loyal", "hardworking"]:
        clan.clans[c].cats[var_name].quote = kit_quotes[3]
      elif personality in ["intelligent", "observant", "sharp"]:
        clan.clans[c].cats[var_name].quote = kit_quotes[4]
      elif personality in ["moral", "spiritual", "wise"]:
        clan.clans[c].cats[var_name].quote = kit_quotes[5]
      elif personality in ["expressive", "feisty", "scrappy"]:
        clan.clans[c].cats[var_name].quote = kit_quotes[6]
      else:
        clan.clans[c].cats[var_name].quote = kit_quotes[(random.randint(0,6))]
    else:
      trait = random.choice(clan.clans[c].cats[var_name].personality)
      if type(quotes[traits.index(personality)]) is list:
        clan.clans[c].cats[var_name].quote = (random.choice(quotes[traits.index(personality)]))
      else:
        clan.clans[c].cats[var_name].quote = quotes[traits.index(personality)]        
    if personality == "spiritual":
      rando = (random.randint(1, 2))
      if rando == 1:
        clan.clans[c].cats[var_name].faith = "StarClan"
      elif rando == 2:
        clan.clans[c].cats[var_name].faith = "The Dark Forest"

    # Name kit

    if Aparent == leader or Bparent == leader:
      rando = (random.randint(1, 2))
      if rando == 1 and ((Aparent == leader and Bparent in clan.clans[c].cats) or (Bparent == leader and Aparent in clan.clans[c].cats)):
        root = (random.choice(cat.roots))
        if Aparent == leader:
          temp = Bparent
        else:
          temp = Aparent
        print("%s has named a %s kit %s." % (clan.clans[c].cats[Aparent].age_status[temp].name,
                                             clan.clans[c].cats[var_name].description, root))
      else :
        root = input(catText["nameKit"] % clan.clans[c].cats[var_name].description)
        
      clan.clans[c].cats[var_name].root = root

      clan.clans[c].cats[var_name].title = "Kit"
    else:
      root = (random.choice(cat.roots))
      clan.clans[c].cats[var_name].root = root

    clan.clans[c].cats[var_name].name = clan.clans[c].cats[var_name].root

    clan.clans[c].cats[var_name].loc = clan.clans[c].name + " camp"

    print("%s was born!" % clan.clans[c].cats[var_name].name)

# generate pre-existing cats

def genCat(c, assign):

  # Define globals

  global folder

  # Start

  var_name = ""
  for i in range(8):
    var_name = var_name + (random.choice(codebits))

  root = (random.choice(cat.roots))

  pronoun = (random.choice(["cat", "tom", "she-cat"]))

  build = (random.choice(cat.builds))

  coat = (random.choice(cat.coats))

  pattern = (random.choice(cat.patterns))

  eye = (random.choice(cat.eyes))
  
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
        new_pat = (random.choice(cat.coats))
      pattern = " with %s patches" % new_pat
      pelt = "%s %s%s" % (coat, pronoun, pattern)
  elif coat == "white" and pattern == "-and-white":
      pelt = "white %s" % pronoun
  elif coat == "white" and pattern == " with lighter patches":
      new_pat = "white %s" % pronoun
      while new_pat == "white":
        new_pat = (random.choice(cat.coats))
      pattern = " with %s patches" % new_pat
      pelt = "%s %s%s" % (coat, pronoun, pattern)

  if "with" in pattern:
      description = ("%s %s and %s eyes" % (build, pelt, eye))
  else:
      description = ("%s %s with %s eyes" % (build, pelt, eye))

  if not assign == "recruit":

      clan.clans[c].cats[var_name] = cat(

      "", "", root, "", "",
      description, pronoun, coat, pattern, eye, build, (random.randint(12, 72)), {"isqueen" : False, "pregnant" : 0}, [], [], [],
      "Neutral", [], "", 0, [], [], "", "",
      {},
      5, (random.randint(1, 7)), 0, {"Willpower" : 5, "Strength" : 1, "Toughness" : 1, "Speed" : 1, "Precision" : 1, "Charisma" : 1}, [],
      clan.clans[c].name, "Neutral", "")

      if not assign == None:
        clan.clans[c].cats[var_name].rank = assign
      else:
        clan.clans[c].cats[var_name].rank = (random.choice(list(clan.clans[c].ranks)))
        while clan.clans[c].cats[var_name].rank == "leader":
          clan.clans[c].cats[var_name].rank = (random.choice(list(clan.clans[c].ranks)))

      if clan.clans[c].cats[var_name].rank == "apprentice":
        clan.clans[c].cats[var_name].lvl = (random.randint(1, 3))
        clan.clans[c].cats[var_name].age = (random.randint(6, 12))
        tries = 5
        gotMentor = False
        while not gotMentor and tries > 0:
          for i in clan.clans[c].cats.copy():
            found_cat = True
            if (rankTemplates[clan.clans[c].cats[i].rank].privs["canPatrol"]):
              possible_mentor = i
              for i in clan.clans[c].cats.copy():
                currMent = findRel(c, i, "mentor")
                if clan.clans[c].cats[i].rank == "apprentice" and currMent == possible_mentor:
                  found_cat = False
              if found_cat == True:
                if possible_mentor in clan.clans[c].cats[var_name].relationships:
                  clan.clans[c].cats[var_name].relationships[possible_mentor][0] = "mentor"
                else:
                  clan.clans[c].cats[var_name].relationships[possible_mentor] = ["mentor", 0]
          if found_cat == False:
            possible_mentor = random.choice(list(clan.clans[c].cats))
            while (not rankTemplates[clan.clans[c].cats[i].rank].privs["canPatrol"]):
              possible_mentor = random.choice(list(clan.clans[c].cats))
            if possible_mentor in clan.clans[c].cats[var_name].relationships:
              clan.clans[c].cats[var_name].relationships[possible_mentor][0] = "mentor"
            else:
              clan.clans[c].cats[var_name].relationships[possible_mentor] = ["mentor", 0]
          tries -= 1
        try:
          findRel(c, var_name, "mentor")
        except:
          clan.clans[c].cats[var_name].rank = (random.choice(list(clan.clans[c].ranks)))
          while clan.clans[c].cats[var_name].rank == "leader":
            clan.clans[c].cats[var_name].rank = (random.choice(list(clan.clans[c].ranks)))
      elif clan.clans[c].cats[var_name].rank == "kit":
        clan.clans[c].cats[var_name].lvl = 0
        clan.clans[c].cats[var_name].age = (random.randint(0, 5))
      elif clan.clans[c].cats[var_name].rank == "elder":
        clan.clans[c].cats[var_name].lvl = (random.randint(1, 5))
        clan.clans[c].cats[var_name].age = (random.randint(70, 120))
      elif clan.clans[c].cats[var_name].rank == "leader":
        clan.clans[c].cats[var_name].lvl = (random.randint(1, 5))
        clan.clans[c].cats[var_name].age = (random.randint(12, 70))
        setattr(clan.clans[c].cats[var_name], 'lives', 9)
      else:
        clan.clans[c].cats[var_name].lvl = (random.randint(1, 5))
        clan.clans[c].cats[var_name].age = (random.randint(12, 70))
        
      clan.clans[c].cats[var_name].name = clan.clans[c].cats[var_name].root

      stat_point = (clan.clans[c].cats[var_name].lvl * 5)

      for i in range(stat_point):
        stat_add = (random.choice(list(clan.clans[c].cats[var_name].stats)))

        if stat_add == "Willpower":
          clan.clans[c].cats[var_name].stats["Willpower"] += 5
        else:
          clan.clans[c].cats[var_name].stats[stat_add] += 1
      
      clan.clans[c].cats[var_name].wp = clan.clans[c].cats[var_name].stats["Willpower"]

      rando = (random.randint(1, 27))
      clan.clans[c].cats[var_name].personality.append(traits[rando - 1])

      if clan.clans[c].cats[var_name].age < 6:
    
        if traits[rando - 1] in ["proud", "impulsive", "passionate"]:
          clan.clans[c].cats[var_name].quote = kit_quotes[0]
        elif traits[rando - 1] in ["caring", "kind", "loving", "peaceful"]:
          clan.clans[c].cats[var_name].quote = kit_quotes[1]
        elif traits[rando - 1] in ["cold", "calm", "resolute", "durable"]:
          clan.clans[c].cats[var_name].quote = kit_quotes[2]
        elif traits[rando - 1] in ["determined", "devoted", "loyal", "hardworking"]:
          clan.clans[c].cats[var_name].quote = kit_quotes[3]
        elif traits[rando - 1] in ["intelligent", "observant", "sharp"]:
          clan.clans[c].cats[var_name].quote = kit_quotes[4]
        elif traits[rando - 1] in ["moral", "spiritual", "wise"]:
          clan.clans[c].cats[var_name].quote = kit_quotes[5]
        elif traits[rando - 1] in ["expressive", "feisty", "scrappy"]:
          clan.clans[c].cats[var_name].quote = kit_quotes[6]
        else:
          clan.clans[c].cats[var_name].quote = kit_quotes[(random.randint(0,6))]
      else:
        if type(quotes[rando - 1]) is list:
          clan.clans[c].cats[var_name].quote = (random.choice(quotes[rando - 1]))
        else:
          clan.clans[c].cats[var_name].quote = quotes[rando - 1]
      if traits[rando - 1] == "spiritual":
        rando = (random.randint(1, 2))
        if rando == 1:
          clan.clans[c].cats[var_name].faith = "StarClan"
        elif rando == 2:
          clan.clans[c].cats[var_name].faith = "The Dark Forest"

      clan.clans[c].cats[var_name].name = clan.clans[c].cats[var_name].root

      for i in range(random.randint(3, 5)):
        like = random.choice(list(landmarks))
        clan.clans[c].cats[var_name].likes.append(random.choice(landmarks[like]))
      like = random.choice(list(landmarks))
      clan.clans[c].cats[var_name].likes.append(random.choice(landmarks[like]))
      clan.clans[c].cats[var_name].favourite = (random.choice(landmarks[like]))
      
      for i in cat.mutations:
        rando = (random.randint(1, 100))
        if rando == 1:
          if i == "heterochromia":
              i = (random.choice(cat.eyes)) + " heterochromia"
          clan.clans[c].cats[var_name].mutations.append(i)
          

      for i in cat.disabilities:
        rando = (random.randint(1, 50))
        if rando == 1:
          clan.clans[c].cats[var_name].disabilities.append(i)
        
      if "blindness" in clan.clans[c].cats[var_name].disabilities:
        clan.clans[c].cats[var_name].stats["Toughness"] += 2
        clan.clans[c].cats[var_name].stats["Precision"] -= 2
      if "spinal paralysis" in clan.clans[c].cats[var_name].disabilities:
        clan.clans[c].cats[var_name].stats["Willpower"] += 20
        clan.clans[c].cats[var_name].stats["Speed"] -= 4
      if "facial paralysis" in clan.clans[c].cats[var_name].disabilities:
        clan.clans[c].cats[var_name].stats["Strength"] += 2
        clan.clans[c].cats[var_name].stats["Precision"] -= 2

      clan.clans[c].cats[var_name].loc = clan.clans[c].name + " camp"
      
  else:
      clan.clans["player_Clan"].cats[var_name] = cat(

      "", "", root, "", "",
      description, pronoun, coat, pattern, eye, build, 0, {"isqueen" : False, "pregnant" : 0}, [], [], [],
      "Neutral", [], "", 0, [], [], "", "",
      {},
      0, (random.randint(0, 3)), 0, {"Willpower" : 10, "Strength" : 1, "Toughness" : 1, "Speed" : 1, "Precision" : 1, "Charisma" : 1}, [],
      clan.clans[c].name, "Neutral", "")

      stat_point = (clan.clans["player_Clan"].cats[var_name].lvl * 5)

      for i in range(stat_point):
        stat_add = (random.choice(list(clan.clans["player_Clan"].cats[var_name].stats)))

        if stat_add == "Willpower":
          clan.clans["player_Clan"].cats[var_name].stats["Willpower"] += 5
        else:
          clan.clans["player_Clan"].cats[var_name].stats[stat_add] += 1

      clan.clans["player_Clan"].cats[var_name].wp = clan.clans["player_Clan"].cats[var_name].stats["Willpower"]

      print(catText["recruitIntro"] % (clan.clans["player_Clan"].cats[var_name].description, clan.clans["player_Clan"].cats[var_name].root, clan.clans["player_Clan"].name))

      accepted = input(catText["recruitAccept"] % clan.clans["player_Clan"].name).lower()

      if accepted == "y":
        accepted = True
        
        clan.clans["player_Clan"].cats[var_name].wp = 5 + (clan.clans["player_Clan"].cats[var_name].lvl * 5)

        clan.clans["player_Clan"].cats[var_name].stats["Willpower"] = clan.clans["player_Clan"].cats[var_name].wp

        for i in range(random.randint(3, 5)):
          like = random.choice(list(landmarks))
          clan.clans[c].cats[var_name].likes.append(random.choice(landmarks[like]))
        like = random.choice(list(landmarks))
        clan.clans[c].cats[var_name].likes.append(random.choice(landmarks[like]))
        clan.clans[c].cats[var_name].favourite = (random.choice(landmarks[like]))

        rando = (random.randint(1, 27))
        clan.clans["player_Clan"].cats[var_name].personality.append(traits[rando - 1])
        if clan.clans[c].cats[var_name].age < 6:
      
          if traits[rando - 1] in ["proud", "impulsive", "passionate"]:
            clan.clans[c].cats[var_name].quote = kit_quotes[0]
          elif traits[rando - 1] in ["caring", "kind", "loving", "peaceful"]:
            clan.clans[c].cats[var_name].quote = kit_quotes[1]
          elif traits[rando - 1] in ["cold", "calm", "resolute", "durable"]:
            clan.clans[c].cats[var_name].quote = kit_quotes[2]
          elif traits[rando - 1] in ["determined", "devoted", "loyal", "hardworking"]:
            clan.clans[c].cats[var_name].quote = kit_quotes[3]
          elif traits[rando - 1] in ["intelligent", "observant", "sharp"]:
            clan.clans[c].cats[var_name].quote = kit_quotes[4]
          elif traits[rando - 1] in ["moral", "spiritual", "wise"]:
            clan.clans[c].cats[var_name].quote = kit_quotes[5]
          elif traits[rando - 1] in ["expressive", "feisty", "scrappy"]:
            clan.clans[c].cats[var_name].quote = kit_quotes[6]
          else:
            clan.clans[c].cats[var_name].quote = kit_quotes[(random.randint(0,6))]
        else:
          trait = random.choice(clan.clans[c].cats[var_name].personality)
          if type(quotes[rando - 1]) is list:
            clan.clans[c].cats[var_name].quote = (random.choice(quotes[rando - 1]))
          else:
            clan.clans[c].cats[var_name].quote = quotes[rando - 1]
        if traits[rando - 1] == "spiritual":
          rando = (random.randint(1, 2))
          if rando == 1:
            clan.clans["player_Clan"].cats[var_name].faith = "StarClan"
          elif rando == 2:
            clan.clans["player_Clan"].cats[var_name].faith = "The Dark Forest"


        rando = (random.randint(1, 4))
        clan.clans["player_Clan"].cats[var_name].rank = (random.choice(list(clan.clans[c].ranks)))

        while clan.clans["player_Clan"].cats[var_name].rank == "leader":
          clan.clans["player_Clan"].cats[var_name].rank = (random.choice(list(clan.clans[c].ranks)))
        
        if clan.clans["player_Clan"].cats[var_name].rank in ["apprentice", "medicine apprentice"]:
          clan.clans["player_Clan"].cats[var_name].age = (random.randint(7, 12))
          possible_mentors = {}

          for m in clan.clans["player_Clan"].cats.copy():
            if clan.clans["player_Clan"].cats[m].rank in ["leader", "deputy", "medicine cat", "warrior"]:
              possible_mentors[m] = clan.clans["player_Clan"].cats[m]

          id = 1
          for m in possible_mentors:
            print("[%d] %s : %s (%s)" % (id, possible_mentors[m].rank, possible_mentors[m].name, ", ".join(possible_mentors[m].personality)))
            id += 1

          cmd = "alfalfa"
          conf = False
          while conf == False:
            cmd = input(catText["mentorAssign"] % clan.clans["player_Clan"].cats[var_name].root)

            try:
              if list(possible_mentors)[int(cmd) - 1] in clan.clans[c].cats[var_name].relationships:
                clan.clans[c].cats[var_name].relationships[list(possible_mentors)[int(cmd) - 1]][0] = "mentor"
              else:
                clan.clans[c].cats[var_name].relationships[list(possible_mentors)[int(cmd) - 1]] = ["mentor", 0]

              print(catText["mentorConf"] % (clan.clans["player_Clan"].cats[list(possible_mentors)[int(cmd) - 1]].name, clan.clans["player_Clan"].cats[var_name].root))

              conf = True
            except:
              conf = False

          if clan.clans["player_Clan"].cats[list(possible_mentors)[int(cmd) - 1]].rank == "medicine cat":
            clan.clans["player_Clan"].cats[var_name].rank = "medicine apprentice"
          else:
            clan.clans["player_Clan"].cats[var_name].rank = "apprentice"
              
        elif clan.clans["player_Clan"].cats[var_name].rank == "elder":
          clan.clans["player_Clan"].cats[var_name].age = (random.randint(84, 120))
        elif clan.clans["player_Clan"].cats[var_name].rank == "kit":
          clan.clans["player_Clan"].cats[var_name].age = (random.randint(1, 6))
        else:
          clan.clans["player_Clan"].cats[var_name].age = (random.randint(12, 72))
          
        clan.clans["player_Clan"].cats[var_name].name = clan.clans["player_Clan"].cats[var_name].root

        for i in cat.mutations:
          rando = (random.randint(1, 100))
          if rando == 1:
            if i == "heterochromia":
                i = (random.choice(cat.eyes)) + " heterochromia"
            clan.clans["player_Clan"].cats[var_name].mutations.append(i)

        for i in cat.disabilities:
          rando = (random.randint(1, 40))
          if rando == 1:
            clan.clans["player_Clan"].cats[var_name].disabilities.append(i)

        if "blindness" in clan.clans["player_Clan"].cats[var_name].disabilities:
          clan.clans["player_Clan"].cats[var_name].stats["Toughness"] += 2
          clan.clans["player_Clan"].cats[var_name].stats["Precision"] -= 2
        if "spinal paralysis" in clan.clans["player_Clan"].cats[var_name].disabilities:
          clan.clans["player_Clan"].cats[var_name].stats["Willpower"] += 20
          clan.clans["player_Clan"].cats[var_name].stats["Speed"] -= 4
        if "facial paralysis" in clan.clans["player_Clan"].cats[var_name].disabilities:
          clan.clans["player_Clan"].cats[var_name].stats["Strength"] += 2
          clan.clans["player_Clan"].cats[var_name].stats["Precision"] -= 2

        print(catText["recruitConf"] % (clan.clans["player_Clan"].cats[var_name].name, clan.clans["player_Clan"].noun))
        
        clan.clans[c].cats[var_name].loc = clan.clans[c].name + " camp"
      else:
        accepted = False

      return var_name, accepted



