# GAMESCRIPT 2026 Saskint

# Characters used in the game
define p = Character("Protaigonist", color = "#ffffff") # Self-insert
define v = Character("Ambrosia", color = "#ffffff") # Female vampire
define g = Character("Basalt", color = "#ffffff") # Female Gargoyle
define f = Character("Razi", color = "#ffffff") # Non-Binary Creature thing
define w = Character("Maximus", color = "#ffffff") # Male werewolf

# Images used in the game and showing image sample (commented out)
image cg example = "logo bw.png"
image bg blank = "#000000"
# scene bg black

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

# The game starts here.

label start:

    ##### THIS IS THE LABEL WE'LL USE FOR THE GAME OPENING #####

    # "Scene" Represents a background sprite (see tutorial)

    scene bg room

    # This shows a character sprite. 

    show eileen vhappy

    # These display lines of dialogue.

    p "I am a protaigonist doing protaigonist-y things"

    p "(From boilerplate) Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

label vampire_date:
    ##### PLACEHOLDER

label gargoyle_date:
    ##### PLACEHOLDER

label frank_date:
    ##### PLACEHOLDER

label wolf_date:
    ##### PLACEHOLDER

label vampire_ending:
    ##### PLACEHOLDER

label gargoyle_ending:
    ##### PLACEHOLDER

label frank_ending:
    ##### PLACEHOLDER

label wolf_ending:
    ##### PLACEHOLDER

label poly_ending:
    ##### Placeholder? I don't know how serious of a suggestion this was ----Damarcelle

label go_home:
    ##### YOU DIE!!!!!! (again, serious suggestion?) -----Damarcelle