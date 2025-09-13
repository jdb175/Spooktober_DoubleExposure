#all of day2 goes in here

label day2Start:
    #Note: I have no idea what BG this should be. We probably just have to make it the darkroom.
    "You wake up feeling like you've hardly slept at all."
    "Grabbing your phone, you see a text from Bud."
    if budLevel == 0:
        bud "yo sorry to bother you"
        bud "but could i come by the darkroom today?"
    else:
        bud "Hey can i come by the darkroom"
    bud "had a weird day yesterday and learned some weird stuff you might be interested in"
    bud "also got some cool ideas."
    bud "ever heard of an artist called siohan kent?"
    bud "siobhan*"
    "You throw on some clothes and tell Bud to meet you in an hour."
    #we move to the studio
    show darkroom_workspace
    show bud
    bud "So I kept thinking about like, my piece, what I was going to do."
    bud "I think I told you I was thinking of doing something like, on her disappearance, like what happened to her."
    bud "But then I decided that would probably be seen as kinda trashy."
    bud "So I was looking at her life as a whole, maybe something about that."
    bud "And discovered she'd dedicated one of her pieces to this artist I'd never heard of. Siobhan Kent"
    bud "Mixed media artist. A lot of similar themes."
    bud "But there was not really any record of them interacting or anything, you know? Like, they never did a showing together."
    bud "Here's the crazy part. Siobhan? *Disappeared.* A few months before Erin did." #same day? What's better for us?
    bud "So... I ask you, how did they know each other?"

label day2BudConvo:
    menu:
        set menuset
        "I thought you said you weren't going to do something on her disappearance":
            bud "I wasn't! I swear! I was looking for just, you know, generic inspiration!"
            jump day2BudConvo
        "I think I know how they knew each other":
            bud "Oh shit, really?"
            menu:
                "I think they were in some kind of cult":
                "I think they"
        
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
