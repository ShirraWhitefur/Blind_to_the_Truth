﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg background_01 = "images/background/background_01.jpg"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")


# The game starts here.
label start:
    scene bg background_01

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    return
