#all of day2 goes in here
##day 2 vars
default budWatching = False

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
    show buddy
    bud "So I kept thinking about like, my piece, what I was going to do."
    bud "I think I told you I was thinking of doing something like, on her disappearance, like what happened to her."
    bud "But then I decided that would probably be seen as kinda trashy."
    bud "So I was looking at her life as a whole, maybe something about that."
    bud "And discovered she'd dedicated one of her pieces to this artist I'd never heard of. Siobhan Kent"
    bud "Mixed media artist. A lot of similar themes."
    bud "But there was not really any record of them interacting or anything, you know? Like, they never did a showing together."
    bud "Here's the crazy part. Siobhan? *Disappeared.* A few months before Erin did." #same day? What's better for us?
    bud "So... it begs the question, how did they know each other?"

label day2BudConvo:
    #menu:
    #    set menuset
    #    "I thought you said you weren't going to do something on her disappearance":
    #        bud "I wasn't! I swear! I was looking for just, you know, generic inspiration!"
    #        jump day2BudConvo
    #    "I think I know how they knew each other":
    you "I think I know how they knew each other"
    bud "Oh shit, really?"
    you "They were both in some sort of... magical organization? Cult?" #Ugh I hate how this scene makes overexplaining hard to avoid
    if peterKnown == True:
        you "Run by this guy Peter Carlson" #keep double checking what info is given at this point
    else:
        you "Run by some guy named Peter."
    if porterKnown == True:
        you "Working with, or using, or calling upon, some sort of spirit called the Porter."
    if houseKnnown == True:
        you "They had plans to go *through* something or *to* something. Some other place."
    else:
        you "They were planning to *do* something together. I don't really know what."
    bud "..."
    if budLevel <= 5:
        bud "..."
        bud "Okay, fine, I get it. You think I'm crazy."
    else:
        bud "..."
        bud "Are you serious? That sounds crazy."
    you "I am being completely serious."
    bud "How could you know all of that?"
    #Stretch goal is make this a choice, create a second route.
    "This is way too much to keep all to yourself. You decide to tell Bud everything."
    "Any fear you had that the story would be too strange to believe evaporates instantly."
    "They're hanging on to your every word."
    bud "You have to show me."
    #FIX: this doesn't work 100%, you need to make the choice to try other photo paper earlier manditory
    you "I would, but there's no more photo paper."
    if corruption >= 10:
        you "Besides, I... think it might be dangerous."
        "Bud's eyes go wide, but they don't say anything."
    if peterKnown == True:
        bud "Okay, well, I guess in the meantime I should look up this uh, Peter Carlson"
    else:
        bud "Okay, well, I guess in the meantime I should look up this, uh, Peter guy"
    if porterKnown == True:
        bud "And some sort of spirit called a Porter?"
    if gunnarKnown:
        you "Look up someone named Gunnar too. I think they're famous. Possibly a writer?"
    bud "Okay, yeah, I'll try."
    bud "This is fucking crazy"
    bud "I'll come by later? Or call you if anything super interesting comes up."
    if corruption >= 10:
        bud "... be careful."
    hide buddy
    "As the words leave your mouth, you instintively glance towards the devlopment trays"
    "Sitting nearly on the corner of the desk is a small package."
    "Bud watches as you pick it up and read the note."
    #stretch goal this is an art asset but we can just describe it if necessary. 
    #We could also have Bud say in the phone call that they met with someone from the foundation yestereay who asked them to bring paper.
    you "'Forgot to drop these off yesterday. Some addit'l of Erin's items, in case they're of interest'"
    bud "Must be from the grant?"
    you "You open the package and discover a small strip of negatives..."
    you "And another small, hand-wrapped package of photo paper. The same paper you used last night."
    #How TF do I get bud OUT of this scene lol. Or just own them being present.
        
    jump day2_darkroom

label day2_darkroom:
    scene bg darkroom1
    "The room is much as you left it yesterday."
    "The photos you developed yesterday lay on the desk, motionless, quiet. You know, like a photograph ought to be."
    "Then, something catches your eye - sitting by the photo trays."
    "Another package of photo paper. Wrapped neatly. Ready for you to use"