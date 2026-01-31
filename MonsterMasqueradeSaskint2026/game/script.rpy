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
    "You got Basalt's ending! Play again to try to see more!"
    return

label razi_ending:
    ##### PLACEHOLDER
    "You got Razi's ending! Play again to try to see more!"
    return

label maximus_ending:
    ##### PLACEHOLDER
    "You got Maximus' ending! Play again to try to see more!"
    return

label ambrosia_ending:
    ##### PLACEHOLDER
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