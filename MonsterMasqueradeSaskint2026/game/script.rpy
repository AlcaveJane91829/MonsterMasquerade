# GAMESCRIPT 2026 Saskint

# Characters used in the game
define p = Character("Protaigonist", color = "#ffffff", image = "protag") # Self-insert
define a = Character("Ambrosia", color = "#ffffff", image = "ambrosia") # Female vampire
define b = Character("Basalt", color = "#ffffff", image = "basalt") # Female Gargoyle
define r = Character("Razi", color = "#ffffff", image = "razi") # Non-Binary Creature thing
define m = Character("Maximus", color = "#ffffff", image = "maximus") # Male werewolf

# Images used in the game and showing image sample (commented out)
image cg example = "logo bw.png"
image bg blank = "#000000"

# If all characters are at max points (all at some number), poly ending?
# If all characters have negative point values, go_home?
# Otherwise, ending is character ending with most amount of points
# Ties are resolved based on the order of priority (given by how the order the dictionary is defined in below)
$ character_points = {
    "Basalt":0,
    "Razi":0,
    "Maximus":0,
    "Ambrosia":0
}

# Boolean (True/False) variables denoting which charcters' dates have been seen
$ seen_basalt = False
$ seen_razi = False
$ seen_maximus = False
$ seen_ambrosia = False

# Variables that count up the dates seen and goes to an ending if applicable
$ dates_seen = 0
$ seen_all = False


# The game starts here.
label start:
    ##### This is the label for the game's opening #####

    p "Blah blah blah introductory dialogue"

    a "Let me introduce you to the gang..." # Placeholder to show structure; replace this with something more in-character ----Damarcelle
    jump introduction


label introduction:
    ##### This is where Ambrosia introduces us to all the other characters
    p "Who do I want to see first..."
    
    # After that introduction, we decide which date we want to start off with
    menu:
        "Visit Basalt...":
            $ seen_basalt = True
            jump basalt_date
            
        "Visit Razi...":
            $ seen_razi = True
            jump razi_date

        "Visit Maximus...":
            $ seen_maximus = True
            jump maximus_date
            
        "Visit Ambrosia...":
            $ seen_ambrosia = True
            jump ambrosia_date
    

label return_to_choice:
    ##### This is the "Hub" The player will go back to after each date until they've seen them all
    # All the dates jump back to here at the end
    $ if dates_seen == 4:
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
            # Go to poly ending if everyone has max points
            if (character_points["Basalt"] == 25) and (character_points["Razi"] == 25) and (character_points["Maximus"] == 25) and (character_points["Ambrosia"] == 25):
                jump poly_ending
            elif (character_points["Basalt"] < 0) and (character_points["Razi"] < 0) and (character_points["Maximus"] < 0) and (character_points["Ambrosia"] < 0):
                jump go_home
            # Set up conditionals for character endings

        

label basalt_date:
    ##### PLACEHOLDER
    jump return_to_choice

label razi_date:
    ##### PLACEHOLDER
    jump return_to_choice

label maximus_date:
    ##### PLACEHOLDER
    jump return_to_choice

label ambrosia_date:
    ##### PLACEHOLDER
    jump return_to_choice

label basalt_ending:
    ##### PLACEHOLDER

label razi_ending:
    ##### PLACEHOLDER

label maximus_ending:
    ##### PLACEHOLDER

label ambrosia_ending:
    ##### PLACEHOLDER

label poly_ending:
    ##### Placeholder? I don't know how serious of a suggestion this was ----Damarcelle

label go_home:
    ##### YOU DIE!!!!!! (again, serious suggestion?) -----Damarcelle

return