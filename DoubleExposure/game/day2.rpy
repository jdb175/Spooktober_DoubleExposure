#all of day2 goes in here

##day 2 chars
define owl = Character("Owl") #Owl mask is Siobhan
define doubOwl = Character("Second Owl") #if we allow this, owl mask talking to owl mask
define flame = Character("Flame") #Flame mask is Peter
define doubFlame = Character("Second Flame") #if we allow this, flame mask talking to flame mask
define frog = Character("Frog") #Frog is Gunnar
define archer = Character("Archer") #Archer is Erin 
#I hate this archer mask, maybe it will change

##day 2 vars
default photoFirst = False
default paperFirst = False
default doneAPrint = False
default donePhoto2 = False
default donePhoto3 = False

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
    "As Bud leaves, you start to think about your next move."
    "As you gaze around the room, two things catch your eye."
    jump day2_darkroom

label day2_darkroomIntro:
    menu:
        set menuset
        "The desk":
            $ papersRemaining = 4
            "Sitting nearly on the corner of the desk is a small package, with a note on it."
            "'Forgot to drop these off yesterday. Some addit'l of Erin's items, in case they're of interest'"
            "Must be from the grant?"
            "You open the package and discover another small, hand-wrapped package of photo paper. The same paper you used last night."
            "And there's more of it this time - four whole sheets."
            if photoFirst == True:
                jump day2_printOne
            else:
                $ paperFirst = True
                jump day2_darkroomIntro
        "The photo on the wall":
            "In your dream you saw a photo hanging on the wall. You hadn't really taken note of it yesterday, but you see it today, just where it was in your dream."
            "You take it down and look at it for a little while. It is a print from one of Erin's last series - 'seen.'"
            temp "SHOW a mask photo here, not as a negative but a print"
            "The whole series was like this - various masks, shown in a presentational style. You never liked this one. Something about it felt unsettling."
            "You ponder the image for a minute before turning it over."
            "On a hunch, you pull off the back of the frame. Tucked inside are two strips of photo negatives."
            "One appears to be the original negatives from 'seen' itself - four masks in all."
            "For a moment, you forget the strange circumstances you are in - it's a rush seeing an original negative from Erin"
            "Most of the images are totally ruined, but it does look like there are a few near the end that are relatively untouched."
            if paperFirst == True:
                jump day2_printOne
            else:
                $ photoFirst = True
                jump day2_darkroomIntro

label day2_printOne:  #needs to be renamed like photo2_print or something
    $ curDevLevel = 0
    "You make your way to the enlarger."
    if doneAPrint == False:
        "You decide to start with the burnt negatives, since you have no idea what they are."
    elif papersRemaining > 1:
        "You have {papersRemaining} papers left"
    else:
        "This is your last piece of photo paper."
    temp "We'd let you click through these two as you'd like in the real interface"
    temp "NOTE: As of this writing, I'm not going to bother with 50/80/100% breakpoints for pulling the photo out of the developer.Waiting for the real interface to be done."
    menu:
        "PHOTO: Two robed figures, shot candidly from someone in hiding. One wears an owl mask.":
            $ papersRemaining -= 1
            $ doneAPrint = True
            jump photo2_firstDev
        "PHOTO: Two robed figures, standing before a doorway with a strange shimmer in it. One wears a mask that looks like flame":
            temp "Not yet written!"
            jump day2_printOne

label photo2_firstDev:
    "Something about the seemingly candid nature of this photo intrigues you."
    "You slide in a piece of photo paper and start to print the image."
    temp "SHOW development interface"
    "It begins to happen again..."
    if donePhoto2:
        "The conversation plays out as it did the first time. You know now that to see something new you will need to make a new exposure"
        jump photo2_double
    else:
        $ donePhoto2 = True
    temp "Zoom in as the photo comes to life"
    #This is GUNNAR in my headcannon
    show owl at right
    owl "Where your mask?"
    show blank at left
    unk "It's in my room. Where it ought to be."
    owl "So what you're saying is that you're not going through with me tonight?"
    owl "Or do you not believe Peter that we need our masks?"
    unk "I'm sorry, but I trust Peter more than you."
    unk "But more than that, I don't believe it pays to be reckless with these things."
    unk "He knows far more than us, and whatever you think you may have picked up these last few days, more than you too."
    owl "..."
    owl "It has only been days, hasn't it?"
    owl "It feels so much longer."
    unk "..."
    owl "So, are you going to turn me in?"
    #50% breakpoint!
    "You eye the clock. Photo's half developed. If you pull it out now, you'll get more time to double expose before it overdevelops"
    temp "currently you pull it out now or not at all, sorry player. will change w/real implementation"
    menu:
        "Pull it out":
            jump photo2_double
        "Keep watching":
            "Keeping one eye on the clock, you let the figures in the photo carry on."
    unk "Not a chance. I may even still come on one of your nighttime jaunts in the future, if you'll let me."
    unk "But not yet."
    owl "How indecisive of you."
    owl "You must know that, as an artist, indecision is a killer."
    owl "One of the few things that is truly deadly to us."
    owl "You must know that."
    owl "So keep stringing things along, if you'd like. Delaying every decision"
    owl "But the opportunity may not always be here."
    unk "..."
    unk "Wait here. I'll come."
    #100% exposeed
    hide blank
    owl "Soon we will transgress"
    owl "Soon, the bright will spill"
    owl "The guardian, the warden, the Porter will fall"
    owl "BUT HE SHALL RETURN"
    #using boilerplate language for now, will change this.
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    hide owl
    "You feel like SOMETHING TERRIBLE has happened."
    jump photo2_ruined

#bet this could be made generic?
label photo2_ruined:
    #FIX ME!!!
    "Well, you've ruined this photo, but that hardly matters."
    "Hopefully you learned something useful."
    jump day2_printOne #This will change in the real implementation

label photo2_double:
    "You pull out the photo."
    "The image stills, the voices quiet."
    "You take the now frozen scene to the enlarger"
    "You see an opportunity to use the negatives from Erin's mask series here."
    temp "here are the choices the interface will present to you, all options superimposed over the unmasked figure."
    menu:
        "Owl mask":
            jump photo2_addOwl
        "Flame mask":
            jump photo2_addFlame
        "Archer mask":
            jump photo2_addArcher
        "Frog mask":
            jump photo2_addFrog

#Siobhan, a double, we may decide to disallow this
label photo2_addOwl:
    "As your photo develops, you heart begins to quicken, almost uncontrollably."
    "The two robed figures, each wearing the same mask, begin to come to life"
    show owl at right
    show owl2 at left
    doubOwl "..."
    owl "Is this some kind of joke?"
    owl "Who are you?"
    owl "Why are you wearing my mask?"
    doubOwl "..."
    owl "I thought they were meant to be unique? Was that a lie?"
    doubOwl "..."
    owl "I'm not fucking around here, okay? Take off your mask! Who are you?"
    doubOwl "This corruption of the truth should not be possible."
    doubOwl "You have strayed beyond your limits, human."
    doubOwl "Given a gift, you were unsatisfied."
    doubOwl "Your hunger is your unmaking"
    hide owl2
    show porter at left
    temp "Fade/transition the second owl into the Porter!"
    porter "Your judgement was made long ago, transgressor."
    owl "This isn't... this isn't possible."
    owl "When is this? When is this happening?"
    owl "We haven't even killed you yet! The idea had not yet taken root in-"
    porter "This cannot be understood. And it will end."
    porter "NOW"
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    hide owl
    hide porter
    "What even was that?!"
    jump day2_printOne

label photo2_addFlame:
    show owl at right
    show flame at left
    "You watch with curiosity as the photo begins to move, the masked figures begin their speech"
    "This time, the figure in the owl mask does not seem to want to talk."
    "They hurry into the shadows, as if they do not want to be seen."
    hide owl
    flame "What are you doing sneaking around in the dark?"
    flame "I've already seen you, Siobhan." #this may be too much? But I think Peter would say it.
    show owl at right
    flame "Do you think I didn't notice someone has been going through my papers?"
    flame "I had very much hoped to catch you in the act."
    flame "But I didn't expect to catch you trying to sneak into the Bright House on your own."
    flame "Well? Speak."
    #leaving in this stub in case it is useful – this would be a great place to learn some magic if we go that route
    #hide owl
    #flame "You can't run."
    #flame "AIN'KA ARRAN"
    #the porter appears or some shit, idk. Just here as an example
    owl "I don't know what you think I'm doing, or what you think I've done."
    owl "But I do know you've been keeping a lot of secrets from us."
    flame "I've said many times that as we continue to explore together, I will share more of what I know."
    flame "That is entirely because I wanted to ensure I was working with people I could trust."
    flame "And here you are, living proof that I was right to be cautious."
    owl "I think you like holding all the power, stringing us along."
    owl "I think you want to keep the Bright House all to yourself."
    owl "You're only sharing it because of your own inability to understand it."
    flame "Don't be stupid! You had so much you could have gained from this!"
    flame "Your art, your insight, your abilities, in just a few days you have grown more than you might in months of toil!"
    flame "This is the light of creativity itself."
    flame "And now it will be shut to you forever."
    flame "I have summoned the Porter and told it that you summon it with stolen magic. That you intend to use to transgress its boundries"
    flame "It will open no more doors for you."
    "You look at the clock. The photo is fully developed. Leaving it in any further will ruin it."
    menu:
        "Pull it out":
            hide owl
            hide flame
            jump day2_printOne
    flame "Your time here is done, Siobhan. In this house, and the Other."
    owl "Blind in art, blind in all things but money."
    owl "BLIND TO THE DEPTHS OF MY TREACHERY"
    owl "THE HAND OF PORTER DRAWS THE DOORS"
    owl "THE DOORS ARE DRAWN BY THE HAND"
    owl "GIVE ME BACK MY HAND"
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    hide owl
    hide flame
    jump day2_printOne

label photo2_addArcher:
    "From the strange masked figures, you see faint movement and hear whispers, growing stronger, growing bolder."
    owl ""

label photo2_addFrog:
    "While it's clear that this photo wasn't taken to be a piece of art, there's an incredible energy you feel watching the masked figures shiver to life."
    "Like you are stealing a glimpse at some great secret."
    show frog at left
    show owl at right
    frog "Alright, I am ready."
    owl "You're making the right choice."
    frog "So, what comes now? Have you learned how to summon him, or..."
    owl "I have."
    frog "I see. I have to admit, I'm quite impressed. It's one thing to pick up a stray scrap of knowledge here or there, but-"
    owl "Can it. If you want to talk, let's talk in the Bright."
    frog "No offense, but the last thing I want to do there is hang around and *talk*"
    frog "I want to see something new. Something truly inspiring. Something that will finally spark that flame in me."
    frog "I envy you tremendously, you know. Sight, vision, comes so naturally to people that it is easy to pull meaning from what we see."
    frog "But words, there is this whole extra layer of processing that we have to do to understand words."
    "The figure in the owl mask doesn't seem to pay much mind. They move about, doing *something* in the dark."
    "Then, a bright light flashes briefly."
