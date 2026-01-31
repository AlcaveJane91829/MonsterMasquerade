# GAMESCRIPT 2026 Saskint

# Characters used in the game
define p = Character("Protaigonist", color = "#ffffff") # Self-insert
define v = Character("Ambrosia", color = "#ffffff") # Female vampire
define g = Character("Gargoyle", color = "#ffffff") # Female
define f = Character("Frankenstein", color = "#ffffff") # Non-Binary
define w = Character("Maximus", color = "#ffffff") # Male werewolf


# The game starts here.

label start:

    # "Scene" Represents a background sprite (see tutorial)

    scene bg room

    # This shows a character sprite. 

    show "eileen vhappy.png"

    # These display lines of dialogue.

    p "I am a protaigonist doing protaigonist-y things"

    p "(From boilerplate) Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
