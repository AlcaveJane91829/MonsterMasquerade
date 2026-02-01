# GAMESCRIPT 2026 Saskint

# Variable to store the protaigonists name
default protag_name = "Gray"

# Characters used in the game
define p = Character("[protag_name]", color = "#ffffff", image = "protag") # Self-insert
define a = Character("Ambrosia", color = "#ffffff", image = "ambrosia") # Female vampire
define b = Character("Basalt", color = "#ffffff", image = "basalt") # Female Gargoyle
define nvb = Character("", color = "#ffffff", kind = nvl) # Novel-mode for Basalt's poetry
define r = Character("Razi", color = "#ffffff", image = "razi") # Non-Binary Creature thing
define m = Character("Maximus", color = "#ffffff", image = "maximus") # Male werewolf
define q = Character("???", color = "#ffffff") # Character labelled with question marks to mask their identity

# Backgrounds and CGs
image bg note = "note.png"
image bg blank = "#000000"
image bg ballroon = "Ballroom_Front_Final.png"

image cg ambrosia = 
image cg basalt = 
image cg maximus =
image cg razi = 

# Character portraits
image ambrosia = "AmbrosiaPH.png"
image basalt = "BasaltPH.png"
image maximus = "MaximusPH.png"
image razi = "RaziPH.png"

# If all characters are at max points (all at some number), poly ending?
# If all characters have negative point values, go_home?
# Otherwise, ending is character ending with most amount of points
# Ties are resolved based on the order of priority (given by how the order the dictionary is defined in below)
default character_points = {
    "Basalt":0,
    "Razi":0,
    "Maximus":0,
    "Ambrosia":0
}

# This is a python function to check the conditions used to go to the acquired ending. Hopefull, you're using a code editor that can collapse this for you to save space

# !!!!!! VERY IMPORTANT NOTE !!!!! 
# This function assumes the max number of points for each character is 25 (i.e., the sum of them all is 100). If that number changes, I need to edit this function -----Damarcelle
init python:
    def ending_conditional_calc():
        """
        Purpose: Calculate which ending the player receives at the end of the game
        Pre-conditions: The player has gone on all the dates and their final totals are tallied
        Post-conditions: N/A
        Return: String used to jump to the correct ending
        """
        global character_points

        ch_point = []
        sum_point = 0
        all_neg = True

        ch_point.append(character_points["Basalt"])
        ch_point.append(character_points["Razi"])
        ch_point.append(character_points["Maximus"])
        ch_point.append(character_points["Ambrosia"])

        for i in ch_point:
            sum_point += i
            if i >= 0:
                all_neg = False

        if sum_point == 100:
            return "poly"
        elif all_neg == True:
            return "home"
        elif max(ch_point) == ch_point[0]:
            return "basalt"
        elif max(ch_point) == ch_point[1]:
            return "razi"
        elif max(ch_point) == ch_point[2]:
            return "max"
        else:
            return "ambrosia"

# Boolean (True/False) variables denoting which charcters' dates have been seen
default seen_basalt = False
default seen_razi = False
default seen_maximus = False
default seen_ambrosia = False

# Variables that count up the dates seen and goes to an ending if applicable
default dates_seen = 0
default seen_all = False

# Dummy variable for the ending check, declared here to avoid bugs
default ending = ""


# The game starts here.
label start:
    ##### This is the label for the game's opening #####
    scene bg blank
    "You are arriving home when you find a mysterious red envelope with an intricate seal stuck onto your door."

    scene bg note 
    with pixellate

    q """
    You have been invited to the Bathory Estate for the 117th Annual Masquerade Ball.

    Come dressed in your finest attire for a reception that is to die for. We will be starting as the clock strikes
    midnight on overmorrow's eve.

    I expect you to not be late{p}{cps=2}---A{/cps}
    """

    """
    Who could have given you this invite!?{p}And why invite you!?

    It's not like you know someone who lives in this \"Bathory Estate\"

    Nonetheless, you are intrigued. The curiosity drives you to take up this mysterious yet alluring proposition.
    If anything, it would finally get you out of your drab and dreary home.

    Not to mention the dazzling outfit you have been dying to wear, yet haven't gotten the chance to.
    """

    scene bg blank
    with Dissolve(1.0)

    pause(1.0)

    jump introduction


label introduction:
    ##### This is where Ambrosia introduces us to all the other characters
    scene bg castle
    """
    You arrive at the estate shortly before midnight. The wind howls through the barren trees as
    pillars of moonlight cast upon the monolithic castle sitting atop the cliffs of the Bathory Estate.

    Something about this place causes the hair on the back of your neck to stand on end. Yet another part of you
    is allured to its irreverent beauty.
    """

    "You approach the towering entrance and knock."

    scene bg blank
    with Dissolve(0.5)

    "You approach the towering entrance and knock."

    # play audio "knock.mp3"
    # play audio "doorOpen.mp3"

    scene bg ballroom
    with dissolve

    show ambrosia neutral

    "Standing in front of you is a tall yet elegant woman."

    a "Greetings. It seems you have finally decided to join us."

    "She sniffs the air as she picks you apart with her obscured eyes."

    a "Well, don't you just smell {cps=15}delectable{/cps}. {w}You shall fit in just fine."
    a "Why don't you come and join us?"

    menu:
        "The woman reaches to grab your hand."

        "Certainly, please lead the way!":
            $ character_points["Ambrosia"] += 5
            "You demurely take the woman's hand. It is cold to the touch."
            a "Of course! The guests are going to adore you!"
        
        "Whoa, there! Slow down! Why am I even here!?":
            $ character_points["Ambrosia"] -= 5
            p "Whoa there, lady! Can I at least get some explanation!?"
            p "Why was I invited to this creepy castle!? I don't know anyone here!"
            show ambrosia shocked

            a "{i}sigh{/i}! Your insolent whining bores me. Join the party before I change my mind about you."

            "Well, isn't {i}she{/i} condescending..."
    
    hide ambrosia

    "The woman takes you into a large ball room filled with creatures of a all shapes and sizes."
    "Their inhuman forms hid behind intricate masks."

    "In this sea of ungodly vessels, four of these figures catch your eye in particular."

    show maximus neutral:
        xalign 0.0
        yalign 1.0
    with move
    show razi neutral:
        xalign 0.33
        yalign 1.0
    with move
    show basalt neutral:
        xalign 0.66
        yalign 1.0
    with move
    show ambrosia neutral:
        xalign 1.0
        yalign 1.0
    with move

    """
    A rugged man in a sheep mask,

    a sophisticated person in a strange chimeric mask,

    a woman with skin made of stone with devilish wings,

    and the hostess, a regal woman wearing a mask that resembles a mosquito.
    """

    hide maximus
    with moveoutleft

    hide razi
    with moveoutleft

    hide basalt
    with moveoutleft

    show ambrosia happy:
        xalign 0.5
        yalign 1.0
    with move

    a "Welcome everyone to the 117th Annual Masquerade Ball!"
    a "I am your enchanting hostess, Countess Ambrosia Bathory!"
    a "I hope you are all having a wonderful evening."

    show ambrosia neutral

    a """
    The Bathory family is always happy to make the acquaintance of and provide refuge to all the inhuman dregs
    pushed into the shadows by humanity.

    I am pleased to announce that the van Helsing family has finally been driven out of the area,
    so we shall not be seeing their ungentlemaly faces any time soon.
    """

    "The crowd gives an applause."

    a "I would also like to introduces our special guests for the night."
    show ambrosia happy:
        xalign 0.33
        yalign 1.0
    with move

    show maximus neutral:
        xalign 0.66
        yalign 1.0
    with moveinright

    a "This is Maximus Lupercus III, the Alpha of the Waning Crescent Pack. A very loyal ally to the Bathory family!"

    m "Pleased to make your acquaintance!"
    hide maximus with moveoutleft

    show razi:
        xalign 0.33
        yalign 1.0
    with moveinright

    a "Next is my good friend, Doctor Razi Frankenstein. One of the greatest minds... \"alive\""

    r """ 
    Thank you Madan Bathory. I do want to make a statement to the crowd.
    Do not bother coming up to me if you don't have anything interesting to say. I do not care for your hollow pleasantries.

    I do not need my time wasted---
    """

    hide razi
    with moveouttop

    a """
    Finally, we have my latest little pet project, Basalt von Slate. She was born from this very castle
    as part of the architecture. 
    
    Now she wanders the halls, spouting her . . . adequate . . . poetry.
    """

    show basalt:
        xalign 0.33
        yalign 1.0
    with moveinright
    b """
    Greetings, men, maidens, and monsters! I welcome you all to the dazzling spires for which I
    was spawned. Brought forth through the carved likeness of life and liveliness for which it was meant to
    represent. The very brick that lay above you also makes up my flesh...
    """

    "She continues with her poem for what feels like minutes"
    scene bg blank
    # After that introduction, we decide which date we want to start off with
    menu:
        "Visit Basalt...":
            $ seen_basalt = True
            $ dates_seen += 1
            jump basalt_date
            
        "Visit Razi...":
            $ seen_razi = True
            $ dates_seen += 1
            jump razi_date

        "Visit Maximus...":
            $ seen_maximus = True
            $ dates_seen += 1
            jump maximus_date
            
        "Visit Ambrosia...":
            $ seen_ambrosia = True
            $ dates_seen += 1
            jump ambrosia_date
    

label return_to_choice:
    ##### This is the "Hub" The player will go back to after each date until they've seen them all
    # All the dates jump back to here at the end
    scene bg blank
    if dates_seen == 4:
        $ seen_all = True

    p "Who do I see now..."

    menu:
        "Visit Basalt..." if seen_basalt == False:
            $ seen_basalt = True
            $ dates_seen += 1
            jump basalt_date
            
        "Visit Razi..." if seen_razi == False:
            $ seen_razi = True
            $ dates_seen += 1
            jump razi_date

        "Visit Maximus..." if seen_maximus == False:
            $ seen_maximus = True
            $ dates_seen += 1
            jump maximus_date
            
        "Visit Ambrosia..." if seen_ambrosia == False:
            $ seen_ambrosia = True
            $ dates_seen += 1
            jump ambrosia_date

        "Wait, there ISN'T anyone else to see..." if seen_all == True:
            $ ending = ending_conditional_calc()

            if ending == "poly":
                jump poly_ending
            elif ending == "home":
                jump go_home
            elif ending == "basalt":
                jump basalt_ending
            elif ending == "razi":
                jump razi_ending
            elif ending == "max":
                jump maximus_ending
            else:
                jump ambrosia_ending

label basalt_date:
    scene bg ballroom
    "You walk over to a corner of the room and see a woman made of stone."

    "You rack your brain to remember her name from when Ambrosia introduced her."

    "Basalt...{p}Basalt...{p}Basalt..."

    show basalt neutral
    p "You're Basalt, right?"

    b "Well, actually more of a granite..."
    b "OH! My name! You meant my name! Yes, I'm Basalt, hi!"
    b "Sorry, these associations..."
    b "They flow out of me like a river out into the sea..."

    menu:
        "Well, the skull's just a needle in a haystack of meaning, no?":
            $ character_points["Basalt"] += 5
            show basalt happy
            b "Er, well, yeah! And meaning's a very big haystack! Sometimes it makes me feel like an ant..."
        "Nice simile":
            show basalt happy
            b "Thank you! I try..."
        "Associations between what?":
            $ character_points["Basalt"] -= 5
            show basalt sad
            b "Well, I guess..."
            b "...between my name and my body..."

    show basalt happy
    b "At any rate it's nice to finally meet you properly, erm..."

    p "[protag_name]."

    b "Right, right, [protag_name]!"

    p "You, I'm surprised to see you this sociable, Basalt. You seemed pretty austere when Ambrosia was introducing you."
    
    show basalt neutral
    b "Well, I'm sort of a prize of the castle. I have to make a good impression on the guests, you know?"
    show basalt happy
    b "Speaking of --- what did you think of my poem!?"

    menu:
        "It was lovely! I really enjoyed it!":
            b "Thank you! You know, a lot of people don't seem to appreciate my poetry."
            show basalt sad
            b "Apparently, it can be a bit much..."
            p "Oh, hush, now! It was beutiful!"
            show basalt happy
            pause(1.0)
        "You know, you can't appreciate a poem on first read. Can I get it in writing?":
            $ character_points["Basalt"] += 5
            show basalt shocked
            b "REALLY!?"

            p "Mais, bien sur! What's the point of poetry if you don't engage!?"
            p "I'd be honoured to have a copy of your poem."

            bslow "W-wow, I..."
            b "...here. I'll give you the copy I used for the presentation."
            b "It's a little out of sorts, but the pages are numbered."

            p "Wow, that's so kind! Thank you so much!"
            p "I'm going to be honest..."
            p "...I didn't get all of it when you wrote it out."

            b "Well, that's understandable! It's a lot, I know, but it's nice to be taken seriously!"
            b "Sometimes, people don't..."
        "It was... Well, poetry's just...":
            show basalt sad
            b "Oh, I see. I guess poetry's not for everyone..."
    # end menu

    show basalt neutral
    b "Well, you know, maybe starting with long poetry was a bit of a long shot. Maybe we should start with something simpler."

    p "A haiku?"
    
    b "Oh, come on! That's a little basic! How about..."
    b "...a senryu?"

    p "Senryu?"

    b "It's like a Haiku, it's a type of originally Japanese poetry with a 5-7-5 syllable pattern."
    b "Except, in a senryu the topic is a humerous depiction of human folly and not nature."

    p "Wow. I thought the 5-7-5 thing is all a haiku was. I didn't know there were other kinds of poetry like it!"
    show basalt happy
    b "Well, {i}syllable{/i}, Japanese is actually a mora-timed language, well, you see, you should know vowel lenght is phonemic..."

    p "Okay, but this poem is in English, yes!"

    b "Yes, of course, sorry! Sometimes, I miss those shades of meaning you could say, haha!"

    p "Er..."

    show basalt sad
    b "Oh, right, you don't know I'm colourblind. Stone eyes have their disadvantages."
    b "Sorry. Sometimes I have a bad theory-of-other-minds. I forget others don't know everything."

    p "That's okay! Anyway, the poem..."
    
    show basalt happy
    b "Right, right, the poem here:"

    hide basalt
    nvl show dissolve
    nvb """
    I walk to the store

    To buy milk for Pekoe tea

    Drunk by my stuff'd cows
    """
    nvl hide dissolve

    show basalt happy
    b "So!? So!? Wha'djya think!?"

    menu:
        "What's the punchline...?":
            $ character_points["Basalt"] -= 5
            show basalt sad
            b "Oh, the punchline is that I'm buying milk for tea, but the tea is for stuffies, and the stuffies are cows,"
            b "and cows..."
            b "Sorry, I thought it was obvious..."
        "It was great! Love it!":
            b "Well, that's great! I'm glad you liked it!"
        "It was good, but the punchline could be smoother and the foible foib'ler":
            $ character_points["Basalt"] += 5
            b "You know, you're right!"
            b "I guess it's not really a \"foible\" to play with stuffies, is it?"
            b "And subtlety is..."
            b "...a subtle art I haven't mastered."
            b "Thank you!"

            p "For what?"

            b "Thank you for giving real feedback."
            b "Lots of people just call my poetry \"good\" without elaborating. It feels fake..."
    # end menu

    show basalt neutral
    b "Anyway, mind if I show you one last poem?"

    p "Sure, what kind is this one?"

    b "It's a sonnet, actually."

    p "A sonnet?"

    show basalt happy
    b "Yeah, like Shakespeare!"
    show basalt neutral
    b "Except the love this one's dedicated to isn't a person. It's nature."
    b "Here:"

    hide basalt
    nvl show dissolve
    nvb """
    Across the field, Prometheus gives fire,

    The fire of life to all the fields of grass,

    That takes their stasis'd states to active spire.

    Oh, lo! The wind! With Zephyr's unseen mass,

    Gives light to see the darken'd life of plants!

    And as I see that life, the life so hid,

    It grants the life within myself! It grants!

    I see that life, and all my fears are rid,

    All rid of fear my life is null and void!

    Oh, how, the wind it gives me strength to move!

    My too-pure disposition now alloy'd

    The strength to go unto the world and prove!

    My love, my laughter, all are made fulfilled

    As seen by wind, who made my stasis kill'd!
    """
    nvl hide dissolve

    show basalt sad
    b "I know it's not the greatest but..."

    menu:
        "Oh, nonsense it was great!":
            show basalt happy
            b "Oh, well, thank you..."
        "I could never keep that rhyme scheme up for a whole sonnet. Good work.":
            show basalt happy
            $ character_points["Ambrosia"] += 5
            b "Thanks! Yeah, it took me a while to right, but I think it's okay..."
            p "More than okay, it's great! Thank you for sharing!"
            b "Thank you..."
        "Well, it seemed a little old-hat":
            $ character_points["Ambrosia"] -= 5
            b "Yeah, well, I guess it's a sonnet..."

    b "Anyway, thank you so much for listening my poems! Again, I know I can be a lot..."

    p "Nonsense! That was great! Thank you!"

    b "No, thank {i}you{/i}! I'm going to see who else is here, but I'd like to see you again!"

    p "See you later, alligator!"

    b "See ya!"

    scene bg blank
    p "So that's basalt, huh. She's..."

    menu:
        "A great person. I hope she's right. I hope I'll see her again...":
            $ character_points["Basalt"] += 5
        "A bit much...":
            pass
        "A little hard to take seriously...":
            $ character_points["Basalt"] -= 5

    jump return_to_choice

label razi_date:
    ##### PLACEHOLDER
    jump return_to_choice

label maximus_date:
    scene bg ballroom
    
    show maximus neutral
    "You head over to a tall, well-built man with ample fur under his chin and beside his jaw. He's standing, wistfully, staring into the distance."

    show maximus happy
    "However, he beams as you approach."

    m "Why, hello there! My, you're looking rather swell this evening! May I inquire as to your name?"

    menu:
        "Oh, why, thank you! I'm [protag_name]!":
            $ character_points["Maximus"] += 5
            m "Exquisite! Let the rendez-vous commence, shall we?"
        "It's [protag_name]":
            m "Well, it's nice to meet you, [protag_name]!"
        "Hey, bub! It's a masquerade! Don't be nosy!":
            show maximus sad
            $ character_points["Maximus"] -= 5
            m "Oh, well, I suppose it is..."

    show maximus neutral

    p "So, what brings you to this place? You don't seem at all like the others I've met."

    m "So I look human to you, eh? Well, I..."

    p "...er, no, I didn't mean.."

    show maximus happy
    m "Oh, it's quite alright! I understand you're human; I can smell it. Being here would be quite the fish-out-of-water experience for you."
    show maximus shocked
    m "After all, I was one of you, once..."

    p "Wait, you can smell . . . {p} oh. You're a werewolf, aren't you?"

    show maximus neutral
    pause(0.125)
    show maximus happy
    m "Correctement!"

    p "Guess the tail shoul have clued me in..."

    m "Careful --- one can never be too astute in a place like this!"

    show maximus neutral
    m """
    As I said, I'm a werewolf, but I was born a human. I had a comfortable youth out in suburbia. White picket fence and all that. I never felt rich, but I was rich enough to never feel poor.

    I guess, for the bulk of it, I had the "typical North American life" they like to show you in old sitcoms. I went to school, and I did well in school and my exctracurriculars. I got a degree. I got a job. I got a wife.

    I loved my wife. Mathilda, her name was. We had two wonderful children together. I thought I'd get to give my children the quiet, comfortable life I had. I never thought of it as idyllic, but looking back, it seems quaint.

    Wife, two kids, our fence was even a picket fence and it was actually painted white...
    """

    show maximus sad
    m "..."
    m "Well, that was a long time ago. After a few years I..."

    menu:
        "Oh, I get it! That's when you became a werewolf!":
            m "Er, yes I . . . that's what I was getting to."
        "Yeah, yeah! You became a werewolf and was you're big and scary and you're sad!":
            $ character_points["Maximus"] -= 5
            m "Yes, yes, I suppose you're quite astute..."
        "Is . . . is that when you became a werewolf?":
            $ character_points["Maximus"] += 5
            m "{cps=2.0}. . .{/cps}"

    show maximus neutral
    m """
    It happened to me in the night. Someone else, some other werewolf, I guess he was hungry. I suppose, if you really think you're a were{i}wolf{/i} and you go out at night, that's a normal way to luncheon.

    I was there to visit my mother, my children's grandmother. The graveyard, that is. It was within walking distance of where we lived, the graveyard. And the fellow, the normal luncheon, I said...

    ...well, he wanted to eat, and I guess to him I was as good as a ham sandwich. 
    """
    
    mslow "It was a bloody thing, really.{nw}"
    show maximus sad
    extend "Through all the pain, my biggest fear was that my children would be forced to see me like that."

    show maximus neutral
    m """
    At any rate, my body reconstituted after a while, and I became the way you see me now. I turn at night, of course; when it's a full moon, I mean.

    But it's really not so bad. It turns out wolves are sleepy creatures, so I just take a warm glass of milk at night and hunker down in an oversized dog bed. 

    The bigger issue was what society thought of me after that.

    The tail . . . it was hard to explain to people that it was actually real, that it wasn't some strange fancy to wear a costume the whole day.
    """

    mslow "But Mathilda . . ."

    m """
    She wasn't cruel about it. She was strictly practical. She wanted the kids to be safe. So did I. We divorced and we agreed I'd leave.

    I do visit. I vist often. But only during the day, of course.

    For the most part I spend my time here --- Ambrosia found me, and agreed to keep me out of trouble by hiring me here. I help with the cleaning here.

    You'd think it'd be a cushy job, and Ambrosia does keep the pay and hours good, but I still have lots of time to read.
    """

    mslow "Lots of time to think..."

    menu:
        "Are you going to make {i}me{/i} a ham sandwich!?":
            m "Well, no, I'm not on the kitchen staff, I..."
            
            show maximus shocked
            m "...oh, you're asking if I'm going to eat you."
            m "No, I'm not going to eat you. It's not a full moon."

            show max neutral
            m "It's actually a new moon, in fact. Ambrosia's practical about these things. It's the safest time for everyone to come, and it's thematic in its own way, no?"

        "Well, that's one heck of a story!":
            $ character_points["Maximus"] -= 5
            show maximus sad
            m "Yeah, I..."
            m "Sorry, I know it's a lot to hear. I like to talk. Sorry."

        "Maximus...":
            $ character_points["Maximus"] += 5
            mslow ". . . "

    show maximus happy
    m "Well then, enough about me! How are you enjoying the ball?"

    menu:
        "I'm loving it! It's so amazing!":
            m "Lovely! I'm glad to hear it!"

        "Oh, {i}greeeeeeat{/i}, I {i}looooooooove{/i} being around monsters!":
            $ character_points["Maximus"] -= 5
            show maximus shocked
            m "Well, that's..."
            m "...that's nice..."

        "Truth be told, I'm a little overwhelmed. It's iteresting to meet you people, though!":
            $ character_points["Maximus"] += 5
            show maximus happy
            m "Well, I'm glad you find me interesting!"
            m "I know Ambrosia dragged you here without much context, but it was nice to meet you!"
    
    hide maximus
    
    a "OH, MAAAAAAAAXIMUUUUUUUUUUUS!!!!!!"

    show maximus happy at right
    m "Well, I guess I'm off! I hope to see you soon!"

    scene bg blank
    p "So that was Maximus, huh?"
    p "Quite a character. That story of his was quite sad."
    p "Of course, I've got to be carfeful about what people say about themselves..."

    menu:
        "Gotta get this sentimentality out of my head. They're monsters...":
            $ character_points["Maximus"] -= 5
        "Iteresting guy. Interestig talk.":
            pass
        "And yet, stil... Maximus... I hope he's okay...":
            $ character_points["Maximus"] += 5

    jump return_to_choice

label ambrosia_date:
    ##### PLACEHOLDER
    jump return_to_choice

label basalt_ending:
    scene bg ballroom

    "Well, you suppose, it's about time to head out."
    "It was certainly interesting to meet these people, but the {i}vibes{/i}, they're still freaking you out."
    "Besides, you don't want to stay out in the new moon too late, do you?"

    show basalt

    "As you go to leave, you see Basalt in the corner. She has a notepad and pen, clearly jotting down some poetic line or other."

    "You decide to give her a goodbye."

    p "Hey, er, Basalt..."

    show basalt happy
    b "Oh, hey [protag_name]! It was nice to meet you tonight!"

    show basalt neutral

    p "Yes, well..."

    b "OH! By the way, you own this castle!"

    p "Wait... WHAT!?"

    b "YEAH! Ambrosia wanted me to mention it! She's been managing the estate, but it's in your name."
    b "That's why she invited you out-of-the-blue --- she knew it wasn't strictly hers, so she tracked down the actual owner."
    b "I guess it came back to you. I don't know how, you'll have to ask her. Old politics, I think."

    p "Really? I can..."
    p "...stay here?"

    hide basalt

    """
    {i}STUPID, STUPID, STUPID!{/i} you think.

    You have a life! Things to do at home!

    What would you even have to {i}do{/i} here!?

    What does \"managing the estate\" even {i}mean{/i}!?
    """

    b "Hey..."

    scene cg basalt

    b "You know, it'll be nice..."
    b "...if you stayed, and I got to see you more often here..."

    """
    You look into her marble eyes and think...

    ...you can stay here.

    With her.

    You can see her every day and hear and read her poetry every day.

    You feel the expanse of meaning in her gaze, the haystack metaphor from earlier.

    If the skull really is a needle in a haystack of meaning...

    ...this place, the Bathory estate....

    ...it looks like a good place to get lost in, with her.

    With Basalt.
    """

    scene bg blank
    "You got Basalt's ending! Play again to try to see more!"
    jump credits

label razi_ending:
    ##### PLACEHOLDER
    show razi
    "You got Razi's ending! Play again to try to see more!"
    jump credits

label maximus_ending:
    scene bg ballroom

    "Well, you suppose, it's about time to head out."
    "It was certainly interesting to meet these people, but the {i}vibes{/i}, they're still freaking you out."
    "Besides, you don't want to stay out in the new moon too late, do you?"

    "As you go to do so, a hand with strange, paw-like fingers gently touches your shoulder."
    "You realize before even turning around --- it's Maximus."

    show maximus shocked
    m "Hey, erm, I..."

    "He seems..."
    "...upset? Sad? Hesitant? The expression is hard to place."

    m "I wanted to ask if you wanted stay here. At the castle."

    p "Maximus, I'm flattered, but I . . . I have a life back home. I can't just abandon that."

    show ambrosia at left
    with move
    a "About that..."
    a "The truth is, [protag_name], I invited you to the Bathory estate because {i}you{/i} were set to inherit it."
    a "The ball was so busy that I didn't have a chance to explain. I've been managing it, but properly it belongs to you."
    hide maximus
    a "I'll explain more about hows and wherefores about the circumstances if you do decide to stay."
    a "For now..."
    a "...I'll leave you two alone."
    hide ambrosia

    show maximus shocked
    p "Is this true? I technically..."
    p "...own, I own this place...?"

    show maximus sad
    m "Yes, you do. But, that's not what I wanted to ask..."

    p "What? What is it?"

    m "I want you to stay with me..."
    m "...{i}WITH{/i} me, [protag_name]!"
    m "I want to know what life with another is like..."
    m "...after Mathilda..."

    hide maximus

    """
    You stand there dumbfounded at the sudden proposal.

    Initially, you're hesitant. You only just met the guy, after all.

    But then...
    """

    scene cg maximus

    """
    He opens his arms into a big, wide hug, and you realize...

    You are completely safe with this man.

    In his big, loveable arms, you're safe.

    You actually...

    ...actually {i}want{/i} to take him up on his offer!

    Even in his condition, with his big, loveable smile...

    ...how bad could it be?
    """

    scene bg blank
    "You got Maximus' ending! Play again to try to see more!"
    jump credits

label ambrosia_ending:
    ##### PLACEHOLDER
    show ambrosia
    "You got Ambrosia's ending! Play again to try to see more!"
    jump credits

label poly_ending:
    ##### Placeholder? I don't know how serious of a suggestion this was ----Damarcelle
    "You got the poly ending! Play again to try to see more!"
    jump credits

label go_home:
    ##### YOU DIE!!!!!! (again, serious suggestion?) -----Damarcelle
    scene bg blank
    "Wow, what a jerk! You were mean to EVERYBODY! They ate you!"
    "You got the bad ending! Play again to try to see more!"
    jump credits

label credits:
    scene bg blank
    return

return