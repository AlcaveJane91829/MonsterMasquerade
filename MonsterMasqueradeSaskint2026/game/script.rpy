# GAMESCRIPT 2026 Saskint

# Variable to store the protaigonists name
default protag_name = "Gray"

# Characters used in the game
define p = Character("[protag_name]", color = "#ffffff", image = "protag") # Self-insert
define a = Character("Ambrosia", color = "#ffffff", image = "ambrosia") # Female vampire
define b = Character("Basalt", color = "#ffffff", image = "basalt") # Female Gargoyle
define r = Character("Razi", color = "#ffffff", image = "razi") # Non-Binary Creature thing
define m = Character("Maximus", color = "#ffffff", image = "maximus") # Male werewolf
define q = Character("???", color = "#ffffff") # Character labelled with question marks to mask their identity

# Images used in the game and showing image sample (commented out)
image cg example = "logo bw.png"
# image note = "note.png" [Add this]
image bg blank = "#000000"

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

    scene note 
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

    show ambrosia

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

            a "{i}sigh{/i}! Your insolent whining bores me. Join the party before I change my mind about you."

            "Well, isn't {i}she{/i} condescending..."
    # end menu
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
    ##### PLACEHOLDER
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
            show basalt sad
            b "Well, I guess..."
            b "...between my name and my body..."

    show basalt happy
    b "At any rate it's nice to finally meet you properly, erm..."

    p "[protag_name]"

    b "Right, right, [protag_name]!"
        

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
    ##### PLACEHOLDER
    show basalt at right
    "You got Basalt's ending! Play again to try to see more!"
    return

label razi_ending:
    ##### PLACEHOLDER
    show razi
    "You got Razi's ending! Play again to try to see more!"
    return

label maximus_ending:
    ##### PLACEHOLDER
    show maximus
    "You got Maximus' ending! Play again to try to see more!"
    return

label ambrosia_ending:
    ##### PLACEHOLDER
    show ambrosia
    "You got Ambrosia's ending! Play again to try to see more!"
    return

label poly_ending:
    ##### Placeholder? I don't know how serious of a suggestion this was ----Damarcelle
    "You got the poly ending! Play again to try to see more!"
    return

label go_home:
    ##### YOU DIE!!!!!! (again, serious suggestion?) -----Damarcelle
    "You got the bad ending! Play again to try to see more!"
    return

return