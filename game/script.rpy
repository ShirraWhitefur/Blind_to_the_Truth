# You can place the script of your game in this file.
init:
    $ renpy.music.register_channel("Ambient_Hospital_Machine","sfx",True,tight=True)

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
image bg Background_01 = "images/background/background_01.jpg"
image Doctor NPH = "images/NPH.jpg"

# Declare characters used by this game.
define You = Character('You', color="#c8ffc8")
define Doc = Character('Doctor', color="#c8ffc8")

# The game starts here.
label start:
    scene bg Background_01
    You "Forewarning.  The audio is a proof of concept thing.  It'll turn off at the first choice.  Because argh.  And lets not talk about test images.  Nope.  Same turn off."
    jump Beginning_01

label Beginning_01:
    You "{i}Darkness. I'd been scared to death of it as a child; of everything it could hide. Now it was everywhere.{/i}{w=1} \n{i}I can't remember when it started, really I don't remember much at all. Just… the feeling when I seemed to settle back into myself.{/i}"
    ## Shirra - PUT THE AUDIO IN! - {Ambient hospital noises, muffled talking}
    $ renpy.music.play('sounds/Ambient_Hospital_Machine.ogg',channel='Ambient_Hospital_Machine',loop=True,fadein=5)
    ## Jeff - GET THE REAL AUDIO - {Ambient hospital noises, muffled talking}
    You "{i}Where am I?{w=1} What’s going on?{w=1} Is someone there?{/i}"
    Doc "The patient is coming around."
    ## Shirra - SCENE CHANGE - [Doctor is at best a vague outline. Nothing else is really visible, backgrounds are black]
    ## Shirra - Tentatively, try to put the first blink transition filter thing in here?
    show Doctor NPH at topright
    ## Shirra - REMOVE THE TEST IMAGE!
    You "Wh{w=0.5}.. what happened?{w=1} Where am I?"
    Doc "Try not to move. There was an… accident. We got you out in time but there were complications."
    You "Complications?{w=1} What kind of complications?"
    Doc "It’s best not to dwell too much. We are still running tests.{w=1} For the moment, I just need you to cooperate with me. Can you do that?"
    $ renpy.music.stop(channel='Ambient_Hospital_Machine', fadeout=5)
    hide Doctor NPH
    menu:
        Doc "It’s best not to dwell too much. We are still running tests. For the moment, I just need you to cooperate with me. Can you do that?{fast}"
        "Alright":
            jump Beginning_01_Choice_01_Alright
        "Tell me what happened first.":
            jump Beginning_01_Choice_01_Tell_me
        "No! What's going on?":
            jump Beginning_01_Choice_01_No

label Beginning_01_Choice_01_Alright:
    You "I… guess so. What do you need me to do?"
    Doc "I’m just going to ask you a few questions, see how you are feeling and then we’ll move forward from there.{w=1} Let me know if you’re experiencing anything strange or uncomfortable."
    You "Okay. I can do that."
    jump Beginning_02

label Beginning_01_Choice_01_Tell_me:
    You "Wait, tell me why I’m here. What happened to me?"
    Doc "… you were in a car accident.{w=1} The safety features deployed but you suffered a substantial blow to the head.{w=1} You have been unconscious for about a week and you only started to respond to us a few moments ago."
    You "I don’t remember being in an accident."
    Doc "Memory loss is common in these cases.{w=1} We’re just trying to determine the extent of the damage.{w=1} I just need to ask you a few questions and then we’ll be able to start treatment."
    You "I think I can do that."
    jump Beginning_02

label Beginning_01_Choice_01_No:
    You "I don’t want any tests! I want to know what’s going on here right now!"
    Doc "Please, calm down.{w=1} You lost quite a bit of blood in the accident and the last thing you need is to put additional stress on your heart.{w=1} I assure you, we are just here to help."
    You "What accident? I don’t remember an accident!"
    Doc "Short term memory loss is common with head trauma. If you let us treat you, it’s likely you’ll get your memories back in time.{w=1} If you stay agitated, however, it’s just going to risk further damage."
    You "{i}Something about all this still bothered me. I felt ill at ease. Still, maybe I should play along.{/i}"
    jump Beginning_02

label Beginning_02:
    Doc "Just relax and answer the questions as accurately as possible."
    You "{i}I nodded, still more than a little shaken. Everything was confusing and my head began to ache every time I tried to think too hard.{/i}"
    Doc "Alright, what is your name?"
    ## Shirra - PUT THE NAME ENTRY FIELD IN!
    You "I'm _YOU_ Because the fox is too lazy to set up the name entry field at the moment!"
    ## Shirra - PUT THE NAME ENTRY FIELD IN!
    jump Beginning_02_Choice_01

label Beginning_02_Choice_01:
    Doc "Excellent! Now, I’m going to play some tones. Let me know if you can hear them."
    menu:
        Doc "Excellent! Now, I’m going to play some tones. Let me know if you can hear them.{fast}"
    ## Shirra - PUT THE AUDIO IN! - {One high tone.}
        "Yes":
            jump Beginning_02_Choice_01_Yes
        "No":
            jump Beginning_02_Choice_01_No

label Beginning_02_Choice_01_Yes:
    Doc "Good, good…"
    ## Shirra - PUT THE AUDIO IN! - {One middle tone.}
    menu:
        Doc "Good, good…{fast}"
        "Yes":
            jump Beginning_02_Choice_02_Yes
        "No":
            jump Beginning_02_Choice_02_No

label Beginning_02_Choice_01_No:
    ## Jeff - WRITE THIS.
    You "Yeah, that ain't a properly written moment.  Sorry!"
    jump Beginning_02_Choice_01

label Beginning_02_Choice_02_Yes:
    Doc "Good, good…"
    ## Shirra - PUT THE AUDIO IN! - {Distorted whisper saying “They won’t tell you.”}
    menu:
        Doc "Good, good…{fast}"
        "Wait… what?":
            jump Beginning_02_Choice_03_What
        "Uh, yes?":
            jump Beginning_02_Choice_03_Yes

label Beginning_02_Choice_02_No:
    ## Jeff - WRITE THIS.
    You "Yeah, that ain't a properly written moment.  Sorry!"
    jump Beginning_02_Choice_01_Yes
    

label Beginning_02_Choice_03_What:
    You "Wait. What was that last one?"
    Doc "The last one was a low tone.{w=1} Did you hear something different?"
    menu:
        Doc "The last one was a low tone. Did you hear something different?{fast}"
        "No… I guess not.":
            jump Beginning_02_Choice_03_01_Guess_Not
        "Play it again.":
            jump Beginning_02_Choice_03_01_Play_it_Again

label Beginning_02_Choice_03_01_Guess_Not:
    You "{i}Maybe I was just hearing things. That was probably all it was.{/i}"
    You "No. No, I heard it alright."
    You "{i}I could hear the doctor scribbling something down onto his chart, his pencil tapping on the page for a moment before he spoke again.{/i}"
    Doc "Alright, let’s move onto the next test."

label Beginning_02_Choice_03_01_Play_it_Again:
    You "{i}I could have sworn I heard something. I wasn’t hallucinating.{/i}"
    You "Would you play the tone again?"
    Doc "Certainly."
    ## Shirra - PUT THE AUDIO IN! - {One low tone.}
    You "{i}That wasn’t what I heard the first time. What’s going on here?{/i}"
    Doc "Did you hear it alright that time?"
    menu:
        Doc "Did you hear it alright that time?{fast}"
        "Yes.":
            jump Beginning_02_Choice_03_02_Yes
        "It was different!":
            jump Beginning_02_Choice_03_02_Different

label Beginning_02_Choice_03_02_Yes:
    You "{i}Guess it really was just me hearing things. I must be more out of it than I thought.{/i}"
    You "Yes. I guess I’m just a little disorientated."
    Doc "Alright. Let me know if it gets worse or better. We’ll want to check on that."
    ## Shirra - PUT IN PROPER JUMP!
    jump end
    
label Beginning_02_Choice_03_02_Different:
    You "{i}I don’t get it! That wasn’t the same noise! What’s going on here?{/i}"
    You "Can you play it again?"
    Doc "Are you sure?{w=1} We’re just trying to diagnose the extent of the damage."
    You "{i}I needed to hear it one more time, just to be sure.{/i}"
    You "Yes, if you could."
    Doc "Alright."
    ## Shirra - PUT THE AUDIO IN! - {One low tone.}
    You "{i}… it didn’t make sense. Still, it was unmistakable now. I guess I was just hearing things.{/i}"
    ## Shirra - PUT IN PROPER JUMP!
    jump end

label Beginning_02_Choice_03_Yes:
    ## Shirra - PUT IN PROPER JUMP!
    jump end

label End:
    You "Nevermind, end of test!"
    return

