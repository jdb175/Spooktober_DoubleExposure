default heardSpeech = False
default heardSpirit = False

label day3Start:
    scene darkroom_workspace bright:
        matrixcolor BrightnessMatrix(-0.6)
    "It isn't until you reach the door to the darkroom and swing it open that you begin to feel afraid."
    "On the way you had sent a text to Bud, explaining the whole situation, but you don't know if they got it."
    "When you arrive, the darkroom is cloaked in shadow."
    "Just like in your dream"
    "And in the dimness, you can recognize that there is someone in here with you."
    show peter one:
        size(402, 540)
        xalign .44
        yalign .3
        ysize .3
        #crop(0, 0, 402, 540)
        fit("contain")
        matrixcolor TintMatrix("#171717")
    with dissolve
    "If they heard you come in, they don't react."
    "As your eyes adjust, your heart stops as you realize the figure is carrying a small knife."
    "With a slight flick of their wrist they make a cut on their arm."
    "The blood drips onto the desk, where you see several pieces of photo paper have been placed."
    "You can't help but gasp."
    "The figure turns around."
    hide peter one
    show peter one with dissolve
    Peter "You've come rather early."
    Peter "I suppose you were curious about who was leaving you your photo paper."
    Peter "I hope you don't find it too unseemly."
    Peter "I would have told you everything eventually."
    "Peter sighs."
    Peter "But if there's one thing I have learned, it is that people are impatient."
    Peter "And seem positively allergic to trusting others above their own desires."
    Peter "My name is Peter. Peter Carlson."
    Peter "I run the Darabondi Foundation."
    Peter "I personally selected you for this opportunity. Your work is... truly something. And I don't say that lightly."
    Peter "I am very excited to see what you've been working on."
    Peter "Or are we to answer questions first?"
    jump peterConvo

label peterConvo:
    menu:
        set menuset
        "What is the point of all this? Why give me this paper?":
            call thePoint
            $ heardSpeech = True
            jump peterConvo
        "Why am I having nightmares?":
            call thePorter
            $ heardSpirit = False
            jump peterConvo
        "What are you doing to that paper?":
            Peter "You surly have learned by know that this is no ordinary paper."
            Peter "I won't bore you with the details, but my blood is not ordinary blood."
            jump peterConvo
        "Porter, house, masks, robes - what the hell have you been up to?!":
            "A dark expression crosses Peter's face."
            Peter "I see you've been digging in places you shouldn't have been."
            Peter "Did you find some scribbling of Erin's? I thought I swept the place for that crap."
            Peter "Or maybe that little spirit has been whispering in your ear."
            Peter "Whatever you think you've learned, it isn't right."
            jump peterCalm
#        "I think you have a negative that I'd like to see.":
#            "A dark expression crosses Peter's face."
#            Peter "I see you've been digging in places you shouldn't have been."
#            Peter "Did you find some scribbling of Erin's? I thought I swept the place for that crap."
#            Peter "Or maybe that little spirit has been whispering in your ear."
#            Peter "Whatever you think you've learned, it isn't right."
#            jump peterAngry
        "(wait to see what else he has to say.)":
            jump peterCalm

label thePoint:
    Peter "If this seems all terribly complicated, I assure you it is not. I only seek to help you create."
    Peter "'Truth is everywhere. But art is the window through which truth may be seen.'"
    Peter "I always liked that quote. But why stop a window, when you could have a door?"
    Peter "There is a Brightness. It is both a thing and a place. It is both in the world and in the mind."
    Peter "Our world - and there are other worlds - is so far from it as to be a place of shadow."
    Peter "I want our world to be Bright."
    Peter "And while you may not fully understand it, you have begun to see the Bright."
    Peter "You are like a lantern now, an old lantern, nursing a sorry flame on a stub of a wick."
    Peter "Walk away now, do what you'd like, but that light cannot be snuffed out."
    Peter "Work with me, however, and I will provide that lantern oil, and that flame will grow."
    Peter "Grow and grow to a great blaze!"
    return

label thePorter:
    Peter "I do apologize for that."
    Peter "Suffice it to say that long ago I made an enemy of a spirit. And it considers my friends enemies as well."
    Peter "Rest assured that I will do what I can to protect you from it. I would be lying if I said that I could protect you fully."
    Peter "But as an artist, I'm sure you understand that a little bit of urgency, a little bit of risk, can be just the thing."
    Peter "'Nothing is more creative than death, since it is the whole secret of life.;"
    Peter "'It means that the past must be abandoned, that the unknown cannot be avoided, that 'I' cannot continue, and that nothing can be ultimately fixed.'"
    Peter "'When a man knows this, he lives for the first time in his life. By holding his breath, he loses it. By letting go he finds it'"
    "Peter's face, which so far has been hard to read, becomes gripped by an almost painful melancholy."
    Peter "Alan Watts. Such a way with words. If only I could express myself with such grace."
    Peter "The way you do."
    Peter "The way all of my artist children have..."
    Peter "If my contributions to art must be by the hands of another, so be it!"
    return


##CURRENTLY UNUSED!
label peterAngry:
    if heardSpeech == False:
        call thePoint
    elif heardSpirit == False:
        call thePorter
    else:
        "Whether you like it or not, we are bound together."
        "Anyone - or anything - who tells you there is a way out is lying."
    menu:
        "Lunge for Peter":
            temp "you'll get hurt by Peter, who escapes outside."
            temp "But bud is out there and beats 'em, and takes the negatives for you!"
        "Try to go back to playing along.":
            temp "Peter heads upstairs after some grandiose speechmaking"
            temp "But bud is out there and beats 'em, and takes the negatives for you!"
        "Give up on the negative. Maybe Peter has a point? Maybe he could help you become great?!" if corruption >= 15: #NOTE need to fix numbers.
            jump shitEnding

label peterCalm:
    if heardSpeech == False:
        call thePoint
    Peter "Now, if you have no more questions for me, I suppose I have one for you."
    Peter "Will you work with me?"
    "If your dream is right, Peter has a negative that you need."
    "Although should you trust a monster in a dream? Could Peter really bring you success? You *have* felt more alive these last two days than ever..."
    menu:
        "I need more than paper. Mr. Carlson. I need *imagery*. Something powerful.":
            jump peterCalmEnding
        "I know about the negative you carry. But don't worry, I don't want it. What I want is to *create*" if corruption >= 15: #NOTE need to fix numbers.
            jump shitEnding

label shitEnding:
    "Peter is surprised to hear you mention the negative. Afraid, even."
    "But you're done being a nobody."
    "Would you even know who Erin was if she hadn't taken Peter's offer, all those years ago?"
    "The nightmares continue. And Bud is a problem too, at first."
    "But they come around."
    "It is hard work, but the more you produce the brighter you see the world around you become."
    "You are able to take on students. Disciples. And show them how to make the world bright as well."
    "In your nightmares, the Porter becomes more frantic. You realize that, however weak or distant it may seem, this spirit is killing you."
    "You suspect you won't have long."
    "But as you watch your students work, watch your efforts change this sad, dim world, you can't help but laugh."
    "The sorry little lantern did indeed become a blazing flame. A flame that has caught the world."
    jump theEnd

label peterCalmEnding:
    #Previous line: I need more than paper. Mr. Carlson. I need *imagery*. Something powerful.
    you "Surely you can provide that?"
    "You see hesitation on Peter's face and feel like this bluff might just work."
    you "If you hold back, you can't expect me to give this my all."
    you "You promised me oil. Do you have it?"
    Peter "..."
    Peter "I've worked with... several other artists over the years."
    "He thumbs arkwardly at his pockets."
    Peter "Many of whom have worked with elements which themselves are... carry something of greater origin than this sorry world."
    Peter "I could arrange for some of them to be sent to you."
    you "The muse is striking now, though, Mr. Carlson. To discover all of this!? It's a rush. A creative opportunity that may never come again."
    Peter "I have a few things I could give you, I suppose. They weren't meant for... this."
    Peter "But I could see their artistic applications... yes. I suppose."
    "Peter removes from his pocket a small envelope and hands it to you."
    Peter "I imagine you want to get to work. I will return this afternoon to see what you create."
    hide peter with moveoutleft
    jump negativesReceived

label negativesReceived:
    "In the envelope, you discover several negatives and drawings."
    "Things Peter wanted to keep close... or keep secret for some reason."
    "Most of them you don't understand. But one thing you do recognize - a negative for a photo of the Porter itself."
    "A sorry looking thing, blind and mutilated. The same photo Erin had exposed her face over."
    scene darkroom_workspace red
    "You make your way over to the enlarger and begin to develop the photo"

label photoFinal_firstDev:
    "The spirit shudders to life. With no eyes to open, it simply tilts its head."
    #This is the porter IN the image. I think we'd rather not pull it out for this?
    porter "The image is old... but it will do."
    porter "It should be like so."
    temp "The porter's eyes fade back into its head"
    porter "Now, finish what was started."
    "You take the photo back to the enlarger for another exposure as quickly as possible."
    jump finalSiobhan

label finalSiobhan:
        menu:
            set menuset
            "Put SIOBHAN over the ARM":
                "This feels right."
                jump finalPeter
            "Put SIOBHAN over the HEART:":
                temp "This feels wrong! You gain some corruption. Maybe get a little bit of dialogue"
                jump finalSiobhan
            "Put SIOBHAN over the TONGUE":
                temp "This feels wrong! You gain some corruption. Maybe get a little bit of dialogue"
                jump finalSiobhan


label finalPeter:
    menu:
        set menuset
        "Put PETER over the ARM":
            temp "This feels wrong! You gain some corruption. Maybe get a little bit of dialogue"
            jump finalPeter
        "Put PETER over the HEART:":
            "This feels right."
            jump finalGunnar
        "Put PETER over the TONGUE":
            temp "This feels wrong! You gain some corruption. Maybe get a little bit of dialogue"
            jump finalPeter

label finalGunnar:
    menu:
        set menuset
        "Put GUNNAR over the ARM":
            temp "This feels wrong! You gain some corruption. Maybe get a little bit of dialogue"
            jump finalGunnar
        "Put GUNNAR over the HEART:":
            temp "This feels wrong! You gain some corruption. Maybe get a little bit of dialogue"
            jump finalGunnar
        "Put GUNNAR over the TONGUE":
            "This feels right."
            jump finalJudgement
    
label finalJudgement:
    "The bizarre composite now done, you bring it back to be exposed."
    porter "My power is returning."
    porter "My function may be served again."
    porter "You have done well."
    porter "The BRIGHT in this world will be culled, and things returned where they belong."
    porter "Humanity will regain my service again."
    porter "With perhaps more caution."
    #values broken
    if corruption <= 10:
        porter "I see little brightness in you."
        porter "Go. Live."
    elif corruption <= 20:
        porter "Now, for you, there will be pain."
        porter "As the brightness in you must be scraped out"
        temp "show corruption effects, then a screen flash"
        you "AAH"
        porter "You are lucky. Go. Live."
        porter "But leave your artistic ambitions behind... at least for a time."
        porter "Or you may reawake the danger."
    elif corruption >= 25:
        porter "..."
        porter "It is possible you have predicted what must come next."
        porter "You are a flame, little one. A flame that could catch the world."
        porter "Let your final thoughts be this: you have done something great. You have made right a wrong."
        "Your heart beats wildly as you step away from the photo. As if it could not hurt you if you were to look away."
        "But it can hurt you. And it does. It feels like cold, snaking from the back of your mind down your spine."
        "Coiling around your organs. The cold begins to burn and you pass out, and in your sudden sleep you see its face."
        "The cold is now touching every part of you, it is everywhere inside you."
        "You are gone."
        jump theEnd
    else:
        #This, mathematically, should never happen.
        porter "Go. Return to life."
    #only the corrupted ending skips this
    scene bg bedroom bright
    "The rest of the day passes without a single strange occurance."
    "Buddy arrived a few minutes after the exposure was done, exceedingly worried about you."
    "You worried about Peter's return."
    "But he never showed up."
    "And that night, when sleep finally comes"
    show bg bedroom sleep
    "It is empty. No dark dreams."
    if corruption >= 15:
        show bg bedroom sleep:
            matrixcolor BrightnessMatrix(1.1)
        "Only a little brightness in the corners"
    "Peter's death makes the papers the next day. 'Man found dead without heart. Psycho on the loose?"
    "But you know the truth."
    "Or, some of it anyway..."

label theEnd:
    scene thankyouforplaying
    ""