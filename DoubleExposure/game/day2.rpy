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
    if houseKnown == True:
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

#region darkroom
label day2_darkroom:
    menu:
        set menuset
        "The desk":
            $ papersRemaining = 5 #not actually used anymore
            "Sitting nearly on the corner of the desk is a small package, with a note on it."
            "'Forgot to drop these off yesterday. Some addit'l of Erin's items, in case they're of interest'"
            "Must be from the grant?"
            "You open the package and discover another small, hand-wrapped package of photo paper. The same paper you used last night."
            "And there's more of it this time - four whole sheets."
            if photoFirst == True:
                jump day2_printOne
            else:
                $ paperFirst = True
                jump day2_darkroom
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
                jump day2_darkroom

label day2_printOne:  #needs to be renamed like photo2_print or something
    $ curDevLevel = 0
    if papersRemaining == 0:
        "That's it for photos today. You're out of paper."
        jump endOfDay2
    "You make your way to the enlarger."
    if doneAPrint == False:
        "You decide to start with the burnt negatives, since you have no idea what they are."
    elif papersRemaining > 1:
        "You have {papersRemaining} papers left"
    else:
        "This is your last piece of photo paper."
    temp "We'd let you click through these two as you'd like in the real interface"
    temp "NOTE: As of this writing, I'm not going to bother with 50/80/100 percent breakpoints for pulling the photo out of the developer.Waiting for the real interface to be done."
    menu:
        "PHOTO: Two robed figures, shot candidly from someone in hiding. One wears an owl mask.":
            $ papersRemaining -= 1
            $ doneAPrint = True
            jump photo2_firstDev
        "PHOTO: Two robed figures, standing before a doorway with a strange shimmer in it. One wears a mask that looks like flame":
            $ papersRemaining -= 1
            $ doneAPrint = True
            jump photo3_firstDev
#endregion

#region photo2 (secret meeting)
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

#region photo2 siobhan/owl
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
    doubOwl "..."
    owl "I'm not fucking around here, okay? Take off your mask! Who are you?"
    owl "Or is this another one of those nightmares??"
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
    owl "We haven't even killed you yet! I've got no hand to give you yet!"
    porter "This cannot be understood. And it will end."
    porter "NOW"
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    hide owl
    hide porter
    "What even was that?!"
    jump day2_printOne
#endregion

#region photo2 peter/flame
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
    flame "Collect your things and go."
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
#endregion

#region photo2 erin/archer
label photo2_addArcher:
    #This scene needs more information
    "From the strange masked figures, you see faint movement and hear whispers, growing stronger, growing bolder."
    show archer at left
    show owl at right
    owl "Oh!"
    owl "It's... what are you doing here?"
    archer "I could ask you the same question."
    owl "I've been taking walks at night. Trying to, basically process everything we've seen in the Bright House."
    owl "I find wearing the costume helps me remember. Stupid as they are."
    owl "Because it's like, after that first day. When I came back through. It all made so much sense."
    owl "I could see the threads connecting *there* to *here*. I felt like I'd just taken a tour backstage at a play I'd seen a thousand times."
    owl "But it fades so fast, doesn't it?"
    archer "It does."
    archer "I think it's meant to. Or, I think we're not meant to understand."
    owl "Oh, that's definitely what *they* think. Peter and his freaky little dog. Keeping tabs on us. Telling us where we can and can't go."
    archer "I don't know. I think there's a reason for that."
    archer "Although what do I know. I envy you. Your recent work has been... incredible. I don't know how to describe it."
    archer "But it feels like I can see a bit of that place when I look at it."
    owl "Who knows if anyone else will. Every piece I make just immediately feels like it's shit. Like it's so far from what I meant."
    owl "But don't you think if you could just get a little further you could figure it out? If you feel stuck too, well, there's answers deeper for you, aren't there?"
    owl "Maybe not for poor Gunnar. I looked in his notebook. It's like the shining, writing the same sentence over and over again."
    owl "Not literally, like, he's not crazy. I don't think. But it's just first sentence, second sentence, cross it out."
    owl "I liked your kitchen thing. I think you're better at this than you think. The idea of using the masks is cool too. Not sure what Peter will think."
    archer "See? This is what I mean. I think my art sucks, you think your art sucks, but to the outside world it's good."
    owl "Maybe..."
    owl "..."
    owl "Do you really trust Peter and that... creature?"
    archer "I don't know. I trust him not to get us killed or anything."
    archer "But I still don't feel like I understand what he's trying to do. Or why that spirit helps him."
    archer "I'm debating doing what you did..."
    archer "Trying to read some of Peter's notes and stuff."
    owl "Yeah. Me too."
    owl "..."
    owl "I wonder where he keeps his... you know, his spells and stuff."
    owl "I wonder if we could find those too."
    archer "I think that's a bad idea."
    owl "Yeah, you're probably right."
    menu:
        "Pull it out, it's at 100 percent":
            hide owl
            hide archer
            jump day2_printOne
    #This is crappy because it gives you no clues and maybe even throws you down an incorrect path.
    owl "... wait, you never answered me. What *are* you doing out here? Dressed like you're going through."
    archer "Oh."
    archer "I... I don't know."
    archer "Wait, why is that I don't know?"
    archer "I was walking at night, but I don't remember putting on my mask. My robes."
    archer "Did I really DO THAT?"
    archer "HOW MUCH OF THIS IS REAL?"
    archer "IS ANY OF THIS REAL??"
    jump day2_printOne
    
#endregion

#region photo2 gunnar/frog
label photo2_addFrog: #This scene is hella long but needs to be...
    "While it's clear that this photo wasn't taken to be a piece of art, there's an incredible energy you feel watching the masked figures shiver to life."
    "Like you are stealing a glimpse at some great secret."
    show frog at left
    show owl at right
    frog "You're still here. I wasn't expecting to see you. Didn't Peter tell you to clear out?"
    owl "I will. Tomorrow. Thought I'd come one last time to our usual meeting."
    frog "That's thoughtful of you, but you know that the Porter won't let you in anymore."
    frog "And if you can't get in, I can't get in, so I'm afraid our midnight jaunts have come to a close."
    owl "What makes you think the Poter will let you in? I'm sure Peter instructed it to prevent *any* of us from getting in alone."
    frog "No harm in trying, is there?"
    frog "But not with you here. That definitely won't fly"
    owl "You know if you get the ritual wrong there can be consequences. If you attempt it without my help, it could go bad for you."
    owl "Are you really sure you've got it down?"
    frog "I'm a keen observer. I'll be alright."
    owl "So you know what to keep hidden in your left hand and what to trace on your right?"
    frog "..."
    frog "You're making things up."
    owl "I'm trying to help you."
    owl "Let me show you. And then I'll get out of your way."
    owl "Keep learning about this place. You and I have come to understand how *important* it is. What's hidden within."
    "The figure in the owl mask presses something small and black into the other's left palm."
    "They then grab the other's right hand and gently uncurl their fingers before tracing a shape on the palm."
    frog "Good luck."
    hide owl
    "The frog masked figure stands alone now. They raise their hands in purposeful, almost artful gestures."
    "They remain completely, eerily silent. The only sound is the swooshing of their robes and the creaking of old floorboards."
    "Then, something happens."
    temp "FLASH! Maybe superimpose a the portal image from the other base photo?" #If we can make it animated that would be so cool.
    show porter at left
    porter "You."
    porter "Peter has told me that you wander where you are not meant to wander"
    porter "Beyond the walls of the House and into the Gardens. That you have even gazed into the Well."
    porter "You will not ent-"
    porter "wh"
    porter "what is that"
    frog "What is... what? This"
    "They open their left palm and reveal the object pressed within."
    porter "WHAT HAVE YOU DONE?"
    "The spirit's thin legs seem to collapse under it. It begins to shake."
    "Its arm begins to glow, consumed by a sickly yellow light."
    "The light travels through the air and into the darkness, travelling towards the hand of another."
    show owl at center
    owl "Apologizes to use you like that, but I wasn't going to let anyone freeze me out."
    owl "Not after all I've seen and learned."
    frog "What have you done?! What did you do to it?!"
    owl "Go. Your part is done here."
    frog "Aaaahh!"
    hide frog
    "Their hand now glowing with the same sickly light, the figure in the owl shuts the portal with a gesture."
    "Then, carefully, they place their hand on the floor and begin to trace a circle around the Porter"
    "As they close the loop, a gate opens in the floor and the now-convulsing spirit falls in."
    "You look at the clock. The photo is fully developed. Leaving it in any further will ruin it."
    menu:
        "Pull it out, it's at 100 percent":
            hide owl
            hide flame
            jump day2_printOne
    "The figure in the owl mask walks into the shadows, leaving the image eerily quiet."
    "In the silence you are able to hear something behind you. Breathing?"
    "You turn around"
    show bg darkroom_workspace #hopefully this works with Jason's implementation, we'll have to see.
    show porter at center #this should be a jump scare
    porter "GIVE IT BACK"
    hide porter with dissolve
    "Gasping for breath, you look around the room. It's just you."
    "You hear some kind of noise coming from the photo in the tray."
    "Full of dread, you turn back to the image, careful not to fully take your eye off the rest of the room."
    hide bg darkroom_workspace
    show owl at center
    "They are weeping."
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    hide owl
    jump day2_printOne
#endregion
#endregion

#region photo 3 (portal opens)
#may have to use porter name variable
label photo3_firstDev:
    "It's hard not to be intrigued by the strange, surreal glow in this image. Was this really an undoctored photo?"
    "You slide in a piece of photo paper and start to print the image."
    temp "SHOW development interface"
    "It begins to happen again..."
    if donePhoto3:
        "The conversation plays out as it did the first time. You know now that to see something new you will need to make a new exposure"
        jump photo3_double
    else:
        $ donePhoto3 = True
    temp "Zoom in as the photo comes to life"
    show flame at right
    show generic_robed at left
    flame "THE DOOR IS OPEN. Step through, quickly!"
    hide generic_robed with moveoutleft
    unk "Will you follow them?"
    show porter with moveinleft
    porter "Or shall I?"
    flame "You should follow. I will wait here."
    porter "As you wish."
    flame "I think you can take them to the Vestibule today."
    flame "I wonder if they will find the statuary there as inspiring as I do." #deliberate reference to Piranisi here, hope it's not seen as copying.
    porter "The Vestibule sits near the Windows of the Garden. I would not take them somewhere so bright."
    porter "They have stepped through so many times so quickly already."
    porter "Even the service I owe to you to you cannot override my purpose."
    porter "They must rest soon or they will begin to overflow. You will see to it that it is so."
    #50% breakpoint!
    "You eye the clock. Photo's half developed. If you pull it out now, you'll get more time to double expose before it overdevelops"
    temp "currently you pull it out now or not at all, sorry player. will change w/real implementation"
    menu:
        "Pull it out":
            jump photo2_double
        "Keep watching":
            "Keeping one eye on the clock, you let the figures in the photo carry on."
    flame "Yes, of course, of course. They need to actually start producing some art at some point anyway."
    flame "Not that I blame them. What could be more dull than sitting around *working* when you could be in another world."
    porter "..."
    flame "Go. Take them to the vestibule. Show them the statue garden."
    hide porter with moveoutleft
    "From the other side of the portal - for that is what it must be - the Porter steps through"
    "Then, the spirit raises a trembling, withered hand. It traces some kind of shape in the air."
    temp "The portal disappears"
    "The figure in the flame mask sighs deeply."
    flame "Now the waiting."
    flame "..."
    flame "Loyal little spirit, is it not."
    #100% exposeed
    flame "Foolish little thing. Blind little thing."
    flame "Mute little thing. Bloodless little thing."
    flame "TRAPPED little thing. BETRAYED little thing."
    flame "BUT IT WILL BE MADE WHOLE."
    flame "AND BRIGHT THINGS WILL BE CONTAINED."
    #using boilerplate language for now, will change this.
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    jump photo3_ruined

#bet this could be made generic?
label photo3_ruined:
    #FIX ME!!!
    "Well, you've ruined this photo, but that hardly matters."
    "Hopefully you learned something useful."
    jump day2_printOne #This will change in the real implementation

label photo3_double:
    "You pull out the photo."
    "The image stills, the voices quiet."
    "You take the now frozen scene to the enlarger"
    "You see an opportunity to use the negatives from Erin's mask series here."
    temp "here are the choices the interface will present to you, all options superimposed over the unmasked figure."
    menu:
        "Owl mask":
            jump photo3_addOwl
        "Flame mask":
            jump photo3_addFlame
        "Archer mask":
            temp "not yet written"
            jump photo3_double
            #jump photo3_addArcher
        "Frog mask":
            jump photo3_addFrog

#region photo3 siobhan/owl
label photo3_addOwl:
    "As the owl mask begins to fade into view, you feel like the whole character of the light has shifted."
    #Siobhan is denied entry by the porter
    show owl at left
    show flame at right
    flame "Wait. Something is wrong."
    "Shimmering into view on the other side of portal is the figure from your dreams" #the portal language is a hot mess, maybe needs a variable or hardcoded use of the term before optional scenes.
    show porter at center
    porter "She carries too much brightness. This one remains today."
    flame "I see. Of course."
    "The lumbering thing moves its hand in a strange, purposeful motion. The light flickers and the portal vanishes."
    "It's hard to shake the momentary feeling that the spirit was looking at you."
    flame "I'm sorry."
    flame "Maybe we can look at some of your work. I was so enchanted with your collage concept from last night."
    flame "It's the first thing anyone here has made that feels like it tells the story of THAT world as the story of THIS world"
    flame "Or, that both worlds are cousin worlds. Or, twins, in a way."
    owl "I don't think that deeply about it, to be honest. I just go with my gut."
    flame "Of course. That's what makes you great."
    flame "... maybe you can help Gunnar with that while you're at it."
    owl "Too bright.."
    flame "I imagine it's because you're simply more open to the truth of that place. Because of your artistic temperment."
    flame "It's a good thing."
    owl "Is it? Your little butler doesn't seem to think so."
    flame "Now that's just uncalled for. No need to be rude."
    owl "Does that mean you don't know the answer?"
    flame "Why do think I chose the flame as my mask?"
    owl "Because it's an obvious metaphor?"
    flame "Because it's an accurate metaphor."
    flame "Many good things become harmful if you get too close."
    owl "Of course."
    owl "Sorry for the commentary. It just sucks not going in."
    flame "Let's get some food. Maybe you can tell me more about your thoughts about the Orrery and it's Door?"
    menu:
        "Pull it out, it's at 100 percent":
            hide owl
            hide flame
            jump day2_printOne
    hide owl with moveoutleft
    hide flame with moveoutleft
    "Only the subtle shifting of the light tells you this photograph is still animate."
    "The colors burn into nothing, slowly making the photo unrecognizable."
    "Then, something strange starts to happen."
    "You start to percieve that in the brightness of the photograph there is a pattern"
    "That your MISTAKE has been not making your previous exposures BRIGHT ENOUGH."
    "You are struck with the urge to laugh and before you can exert any will in the matter an oddly flat mirthless chuckle escapes your lips" #-_-
    "The sound in the empty darkroom is jarring and jolts you back to your senses."
    "You pull out the photo, feeling suddenly uncomfortable."
#endregion

#region photo3 peter/flame
label photo3_addFlame:
    "As your photo develops, the light of the portal flickers and dims."
    "The two robed figures, each wearing the same mask, begin to come to life."
    #Peter reckons with his own ambition and folly in agreeing to split the spirit
    show flame at left
    show flame2 at right
    flame "Where did you get that mask?"
    flame "Is this some kind of joke?"
    doubFlame "..."
    flame "Or have I finally gone too far? Unmask, and show me your face!"
    doubFlame "It's me. You."
    doubFlame "Not as you are, but as you will be."
    doubFlame "I'm the one who lives in your house. I am in your skin and your thoughts are my thoughts."
    flame "Is this another one of those fucking nightmares?"
    flame "Or... are you really here?"
    doubFlame "I am not here."
    doubFlame "It will be many years until I am here. Decades."
    doubFlame "But when the time comes and I am here, it will be by the magic you are about to discover here. This week."
    flame "This is some cryptic bullcrap. You don't sound like me at all. Do your homework before trying to impersonate me."
    doubFlame "You change, Peter. You betray your friend, you betray yourself, and you betray your flesh."
    doubFlame "You traded your heart for power, Peter."
    doubFlame "And now what beats in your chest is a vacancy. A hole."
    doubFlame "And then you begin to hollow out others, trying to fill this hole you have created."
    flame "So... so... so what is this, like some kind of warning?"
    menu:
        "Pull it out, it's at 100 percent":
            hide flame
            hide flame2
            jump day2_printOne
    doubFlame "Yes, but not for you."
    doubFlame "For the one who is watching us."
    if corruption >= 10:
        doubFlame "The one who is bright"
    else:
        doubFlame "The one who is not yet too bright."
    #I want to put more of an ending clue here but need to write that first.
    hide flame2
    hide flame
#endregion

#region photo3 erin/archer
label photo3_addArcher:
    #This slot gives a HELL of a lot away, almost feels like it should be saved for day3 somehow.
    #This is also set way in the future, I'm leaving it that way for now but it may make more sense to make it happen later
    "You take a deep breath and prepare yourself, focusing intently on the image fading into view."
    "The two robed figures begin to come to life."
    #Scene possibilities for this slot:
    #Flame convinces Erin to join in the plot to take the eyes
    #Flame and Erin discuss the nightmares they've been having and how to stop them
    show archer at left
    show flame at right
    flame "I'm glad you changed your mind."
    flame "I'd like to ask why, but I'm afraid it'll only make you run away again."
    archer "..."
    flame "Of course, you don't have to say anything."
    flame "I have to be honest. When I pulled this little group together I had no idea what was going to happen."
    flame "When it all started to go wrong, I felt like I had made a terrible mistake."
    flame "Now I see that everything that happened was all in service of something greater."
    flame "So. Here is my guess. You've come to see that too."
    archer "That's not it."
    archer "I wanted nothing to do with what you two had done. Honestly, I still don't."
    archer "But I started having these... terrible, realistic nightmares. About the Porter."
    archer "Started seeing it in real life, started feeling this icy pain that would grip my heart at random times."
    archer "I spoke to Siobhan. Before she died. She wasn't easy to find, always with one foot in some other world."
    archer "I wanted her to undo what'd she'd done. She didn't listen. She wasn't afraid of the Porter."
    archer "I spoke to Gunnar. He was easy enough to find. He doesn't leave his apartment at all anymore, the nurse said."
    archer "The walls, the floors, every square inch covered in mad writings. I could read enough to know the dreams were coming for him too."
    archer "So if I'm going to be hounded by some nightmare thing for all the shit you lot got up to..."
    archer "...I'd like to at least get something out of it."
    flame "I understand that logic. I'm a bit disappointed that an artist such as yourself has such a... selfish perspective."
    flame "We all burn out sometime. What matters is what we produce, what we *do*."
    flame "So, what will you take into yourself?"
    show porter wounded at center
    "The figure in the flame mask makes a gesture and the portal darkens."
    "In it can be seen the figure of the Porter, laying still and motionless."
    archer "... I want its eyes."
    flame "Done."
    "Yellow light begins to form around the Porter's eyes."
    "The eyes of the archer mask, too, begin to glow."
    #100 percent dev
    menu:
        "Pull it out, it's at 100 percent":
            hide frog
            hide porter wounded
            hide flame
            jump day2_printOne
    flame "What do you see?"
    archer "bright."
    archer "BRIGHT"
    archer "And I see..."
    archer "I see a way out."
#endregion

#region photo3 gunnar/Frog
label photo3_addFrog:
    "You stare intently, aware of the eerie quiet of the darkroom. A quiet you know will soon be filled with voices."
    #Gunnar suggests the entire plot.
    show frog at left
    show flame at right
    frog "I can't believe that worked."
    frog "That was incredible, Peter. You're a genius, a true genius."
    "Peter, if that who it is, stares blankely at the open portal."
    "Instead of the brightness we see shadow. And in it, the strange figure from our dreams." #Yes, this does mean another asset for dark portal. Hopefully just an easy palette swap:(
    "The porter."
    show porter wounded at center
    flame "Can you hear me?"
    porter "..."
    flame "What did she do to you?"
    frog "I told you, she took its power. I would have stopped her if I had known what she was doing."
    frog "I don't understand this stuff the way you do, or the way she did."
    flame "Quiet."
    frog "If we're going to do this, Peter..."
    flame "I wish we knew where she went."
    frog "You think she's even in this world? Even in the Bright House? She could be anywhere."
    frog "A few simple gestures not just from the Bright House, but from the Garden, from... Hell, Peter, I wonder if you even know what else could be out there."
    flame "This feels wrong."
    frog "Do what you think is right. If you want to find her, you won't find her without power of your own."
    frog "As for me, I just want to write."
    frog "I was so close to something great, Peter. Isn't that all you wanted to come out of this? Something truly great for humanity?"
    flame "..."
    flame "Alright. Hand me the stone."
    "The frog passes a small, dark object to Peter, who grips it in his left palm."
    "He then traces some kind of design over his chest."
    "Holding out both hands, a yellow glow appears in the chest of the spirit."
    "The light forms a thin thread, connecting Peter's chest with the spirit's"
    flame "Good god..."
    "The figure with the flame mask sits motionless."
    flame "It is done."
    flame "Your turn."
    flame "Take what you will from this husk."
    menu:
        "Pull it out, it's at 100 percent":
            hide frog
            hide porter wounded
            hide flame
            jump day2_printOne
    frog "How... how does it feel?"
    flame "I can feel its power."
    frog "What should it be?"
    frog "Do words live in the tongue? Or the mind? Do I want to see what is in that mind? Could I even comprehend it?"
    flame "FOOL"
    flame "IT MATTERS NOT"
    flame "ALL WILL BE RETURNED"
    flame "ALL MUST BE RETURNED"
#endregion
#endregion

#region end of day 2
label endOfDay2:
    "You wipe the sweat from your brow and sit in Erin's chair, thought swirling."
    "Trying to make sense of the events you've seen. To piece together the timeline."
    "You can't be sure that everything you've seen is real, or was real, but at the same time it almost adds up."
    "Your phone buzzes. It's Bud. They're outside."
    #Okay, so there are two ending possibilities I see here:
    #First ending, Erin created the foundation to put an end to this. Strongly hinted by the fact that she has been trying to cure the Porter
    #Second ending, Erin was trying to do good, but Peter runs the foundation. We are offered a second photo from Peter, and choose whether to use his or Erin's
    bud "So I looked into Peter Carlson..."
    bud "Um, it got weird."
    bud "So he's the guy who runs this foundation."
    bud "Also, there used to be a Siobhan Kent young artists grant. A lot of the recipients, uh, seem to have died."
    bud "Same for the, uh Gunnar Olsen young poet award award winners."
    if porterKnown == true:
        bud "I didn't have a lot of luck looking up any kind of a spirit called the Porter."
        bud "That's probably just because like, where the hell do you even start with something like that."
        bud "But it did come up in some of Gunnar's unfinished works. And the works of the poet award winners."
        bud "It's either some sort of like, vengeful killer or some sort of guardian angel."
        you "That's super helpful..."
        bud "Right?"
    you "Bud... did you have any nightmares last night?"
    bud "Kinda, yeah, actually. I kept dreaming of these chopped up body parts and like, all these different creatures pecking at them."
    bud "This owl was eating someone's hand and then there was this moustached guy just like, watching it all from the woods."
    bud "Oh god then he ate his own eyes."
    bud "How did you know?"
    you "I had one too. About the porter."
    you "I don't know what Peter's game is here but I think we need to get out of all of this."
    bud "So we just quit?"
    bud "..."
    bud "It's too late for that, isn't it?"
    "You fill Bud in on everything you've seen."
#endregion