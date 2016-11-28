## Question objects for mad-libbing
# Designed to give the chillout.py game some added functionality
#20 adjectives
procList = [[("An irascible ", 1), ("A frenzied ", 1), ("A terrified ", -1), ("A flatulent ", 2), ("A defiantly grotesque ", -2),
              ("A shaky ", 0), ("A forlorn ", -1), ("An enchanted ", 1), ("A red-eyed ", 2), ("A pristine ", 2),
              ("An alarmingly large ", 0), ("A perplexingly small ", 1), ("A radical ", 0), ("A dangerously pink ", 1), ("A perverse ", -1),
              ("A furry ", 1), ("A three-toothed ", 1), ("A rapidly ballooning ", -1), ("A completely normal ", 0), ("An extremely racist ", -1)],
#20 entities
            [("skateboarder, ", 1),("parrot, ", 1),("telepathic swarm of bees, ", -1),("old miner, ", 0),("nurse, ", 0),
          ("version of your mother, ", -2),("time-traveler, ", 2),("hobo, ", -1),("talking car, ", -1),("plumber, ", 0),
          ("Snoop Dogg, ", 3),("clone of you, ", -1),("magical book, ", -1),("5th-grade chess club, ", 1),("series of increasingly absurd questions, ", -1),("wizard, ", 0),
          ("pancake with writing on it, ", 1),("possessed children's toy, ", -3),("instance of your spirit animal, ", 1),("Scientologist, ", -1),("mirror, ", 0)],
#16 compositions
                [("wearing ", 0), ("made of ", -1), ("covered in ", -1), ("throwing handfuls of ", 0), ("with a sack full of ", 1), ("whispering to their ", -1),
               ("chewing on ", 1),("delicately caressing some ", -2),("completely unrelated to ", 0),("shoveling a path through the ", 1),("festooned with ", 2),
               ("strangely lacking ", 1),("composed entirely out of ", 0),("lightly buttering some ", 1),("indecently eyeballing ", -1),("fresh out of ", 0),
                 ("with a phobia of ", -2), ("buried under a pile of ", -1),("in tights patterned with little ", 2), ("extruding ", -3)],
# 20 objects
            [("leather shoes, ", 0), ("gold bricks, ", 2), ("hamster wheels, ", 1), ("tinfoil-hats, ", -1), ("metallic glitter, ", 1),
           ("lewd skeleton parts, ", -2),("old newspapers, ", 0),("colorful beads, ", 0),("'legalize it' apparel, ", -1),("grape jelly, ", 2),
           ("plastic feathers, ", 1),("your self-esteem, ", -2),("golf pencils, ", 0),("playing cards, ", 0),("trumpets, ", 1),
           ("unlit candles, ", -1), ("wooden hammers, ", 0), ("cereal boxes, ", 0), ("used chewing gum, ", -1), ("404 errors, ", 0)],
# 20 actions
            [("offers you a handshake.", 5), ("pleads with you for their life.", 7), ("asks if you have change for a dollar.", 1), ("demands an end to Christmas.", -1),
          ("does a kickflip over your car.", 9), ("makes a mockery of everything you value.", -4),("accuses you of collaborating with banking conglomerates.", -3),
          ("offers you a hit.", 10), ("shows you a painting and asks your opinion.", 2), ("teaches you several new gestural vulgarities.", -1),
          ("stands motionless, saying nothing.", -2),("shoots paintballs at your knees.", -5), ("poses a difficult philosophical quandary.", 1),
          ("meets your eyes and mutters dejectedly, 'They know...' before exploding in a shower of gory bits.", -7), ("invites you to a party later", 6),
          ("hands you a coloring book.", 2), ("transforms into no less than 17 cats, which then scatter into the alleys.", -5),
          ("points at you while emitting a high-pitched keening noise to alert the others.", -9), ("wraps you in a big, bear-hug.", 4), ("just laughs.", 5)],
# 20 interrupts
            [("turns to you and ", 0), ("stops and ", 0), ("makes a silly face and ", 3),("undulates wildly and ", -1),("dusts their shoulders off and ", 0),
             ("looks up and ", 0), ("pauses and ", 0), ("thoughtfully sits and ", 1), ("does a quick double take and ", 0), ("jukes from side to side and ", 0),
             ("plays a jaunty tune on an imaginary flute and ", 4), ("slowly peels away its flesh and ", -4), ("emerges from a chrysalis and ", -1),
             ("pours a shot, downs it, and then ", 1), ("screeches loudly and ", -2), ("deploys a filthy meme and ", 2), ("plants an impressive garden and ", 3),
             ("levitates briefly and ", 1), ("mumbles in a dark-tongue and ", -1), ("removes their hat and ", 0)]
            ]
# 15 paranoid
para =  [("siphoning your thoughts for the mind-queen to feast upon", 0), ("being a Trump supporter", 0), ("being a paid shill for the industry", 0),
            ("only pretending to be human", 0), ("planting surveillance devices in your room", 0), ("boggarting", 0), ("secretly being a reptilian robot in disguise", 0),
            ("stealing your used tissues", 0), ("being a toilet-witch, fresh from India", 0), ("being a blackula", 0), ("working directly for Soros himself", 0),
            ("leaving you fatherless for all these years", 0), ("plotting to blow up your favorite coffee shop in a misguided attempt to point out systemic inequality", 0),
            ("actually being a skeleton in disguise", 0), ("making you forget what you were about to say", 0)]
            
# Command List
commands = ["chill", "run", "smoke"]


