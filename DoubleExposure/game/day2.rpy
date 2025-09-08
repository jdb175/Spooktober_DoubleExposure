#all of day2 goes in here

label day2:
    "Soon, it is morning."
    "You spend some time going through Erin's art books, trying to see if that FACE shows up."
    "You find a few works from Siobhan as well in one of your art books."
    "It mentions her as a brief collaborator of Erin's. She died tragically. Fell off a cliff. Not too far off from when Erin disappeared."
    if corruption <= 5:
        "You feel like if there's anything to be learned, it's back at Erin's place."
    else:
        "You feel drawn back to Erin's studio. As if the answers you seek will surely be found there."
    jump day2_budConvo

label day2_budConvo:
    show bud
    bud "Oh, hey!"
    temp "I think Bud will help you with some important info here, but I'm not going to write this scene just yet."
    jump day2_darkroom

label day2_darkroom:
    scene bg darkroom1
    "The room is much as you left it yesterday."
    "The photos you developed yesterday lay on the desk, motionless, quiet. You know, like a photograph ought to be."
    "Then, something catches your eye - sitting by the photo trays."
    "Another package of photo paper. Wrapped neatly. Ready for you to use"
    menu:
        "'Hey, Bud - has anyone else been down here?'":
            ""
        "Open it":
            ""
