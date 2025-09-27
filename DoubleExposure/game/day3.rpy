default heardSpeech = False
default heardSpirit = False

label day3Start:
    show black_background
    pause 1
    "It isn't until you reach the door to the darkroom and swing it open that you begin to feel afraid."
    scene darkroom_workspace bright:
        matrixcolor BrightnessMatrix(-0.6)
    "The room is cloaked in shadow."
    "Just like in your dream"
    "And in the dimness, you can recognize that there is someone in here with you."
    show peter old speak:
        size(402, 540)
        xalign .44
        yalign .3
        ysize .3
        #crop(0, 0, 402, 540)
        fit("contain")
        matrixcolor TintMatrix("#3c3c3c")
    with dissolve
    pause 1
    "If they heard you come in, they don't react."
    "As your eyes adjust, your heart stops as you realize the figure is carrying a small knife."
    show peter old arm
    "With a slight flick of their wrist they make a cut on their arm."
    "The blood drips onto the desk, where you see several pieces of photo paper have been placed."
    "You can't help but gasp."
    show peter old speak
    "The figure turns around."
    hide peter
    show peter old focus with dissolve
    Peter "You've come rather early."
    show peter old explain
    Peter "I suppose you were curious about who was leaving you your photo paper."
    Peter "I hope you don't find it too unseemly."
    show peter old show
    Peter "I would have told you everything eventually."
    show peter old tense
    "Peter sighs."
    show peter old snark
    Peter "But if there's one thing I have learned, it is that people are impatient."
    show peter old paranoid
    Peter "And seem positively allergic to trusting others above their own desires."
    show peter old explain
    Peter "My name is Peter. Peter Carlson."
    Peter "I run the Darabondi Foundation."
    show peter old show
    Peter "I personally selected you for this opportunity. Your work is... truly something. And I don't say that lightly."
    show peter old explain
    Peter "I am very excited to see what you've been working on."
    show peter old snark
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
            show peter old explain
            Peter "You surly have learned by know that this is no ordinary paper."
            show peter old show
            Peter "I won't bore you with the details, but my blood is not ordinary blood."
            jump peterConvo
        "Porter, house, masks, robes - what the hell have you been up to?!":
            show peter old focus
            "A dark expression crosses Peter's face."
            Peter "I see you've been digging in places you shouldn't have been."
            show peter old angry
            Peter "Did you find some scribbling of Erin's? I thought I swept the place for that crap."
            show peter old focus
            Peter "Or maybe that little spirit has been whispering in your ear."
            show peter old explain
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
    show peter old snark
    Peter "If this seems all terribly complicated, I assure you it is not. I only seek to help you create."
    show peter old explain
    Peter "'Truth is everywhere. But art is the window through which truth may be seen.'"
    Peter "I always liked that quote."
    show peter old focus
    Peter "But why stop a window, when you could have a door?"
    show peter old explain
    Peter "There is a Brightness. It is both a thing and a place. It is both in the world and in the mind."
    show peter old show
    Peter "Our world - and there are other worlds - is so far from it as to be a place of shadow."
    Peter "I want our world to be Bright."
    show peter old angry
    Peter "And while you may not fully understand it, you have begun to see the Bright."
    show peter old explain
    Peter "You are like a lantern now, an old lantern, nursing a sorry flame on a stub of a wick."
    show peter old focus
    Peter "Walk away now, do what you'd like, but that light cannot be snuffed out."
    show peter old explain
    Peter "Work with me, however, and I will provide that lantern oil, and that flame will grow."
    show peter old show
    Peter "Grow and grow to a great blaze!"
    return

label thePorter:
    show peter old show
    Peter "I do apologize for that."
    show peter old explain
    Peter "Suffice it to say that long ago I made an enemy of a spirit. And it considers my friends enemies as well."
    Peter "Rest assured that I will do what I can to protect you from it. I would be lying if I said that I could protect you fully."
    show peter old show
    Peter "But as an artist, I'm sure you understand that a little bit of urgency, a little bit of risk, can be just the thing."
    Peter "'Nothing is more creative than death, since it is the whole secret of life.;"
    show peter old explain
    Peter "'It means that the past must be abandoned, that the unknown cannot be avoided, that 'I' cannot continue, and that nothing can be ultimately fixed.'"
    Peter "'When a man knows this, he lives for the first time in his life. By holding his breath, he loses it. By letting go he finds it'"
    show peter old paranoid
    "Peter's face, which so far has been hard to read, becomes gripped by an almost painful melancholy."
    Peter "Alan Watts. Such a way with words. If only I could express myself with such grace."
    show peter old explain
    Peter "The way you do."
    show peter focus
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
        show peter old open
        "Whether you like it or not, we are bound together."
        show peter old angry
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
    show peter old explain
    Peter "Now, if you have no more questions for me, I suppose I have one for you."
    show peter old show
    Peter "Will you work with me?"
    "If your dream is to be trusted, Peter has a negative that you need."
    "Although should you trust a monster in a dream? Could Peter really bring you success? You {i}have{/i} felt more alive these last two days than ever..."
    menu:
        "I need more than paper. Mr. Carlson. I need {i}imagery{/i}. Something powerful to work with.":
            jump peterCalmEnding
        "I know about the negative you carry. But don't worry, I don't want it. What I want is to {i}create{/i}" if corruption >= 25: #NOTE need to fix numbers.
            jump shitEnding

label shitEnding:
    "Peter is surprised to hear you mention the negative. Afraid, even."
    show peter old tense
    "But you're done being a nobody."
    "Would you even know who Erin was if she hadn't taken Peter's offer, all those years ago?"
    show peter old arm
    "You shake Peter's bloody hand, and in doing so seal your fate."
    hide peter with dissolve
    "You begin to create new work."
    show darkroom_workspace red
    "Not playing with Erin's old toys, no."
    show darkroom_workspace red:
        matrixcolor BrightnessMatrix(.05)
    "Creating {sc=5}ART{/sc}!"
    "The nightmares continue. And Bud is a problem too, at first."
    show darkroom_workspace red:
        matrixcolor BrightnessMatrix(.2)
    "But they come around."
    "It is hard work, but the more you produce the brighter you see the world around you become."
    show darkroom_workspace red:
        matrixcolor BrightnessMatrix(.3)
    "You are able to take on students. Disciples. And show them how to make the world bright as well."
    show darkroom_workspace red:
        matrixcolor BrightnessMatrix(.4)
    "In your nightmares, the Porter becomes more frantic."
    "You realize that, however weak or distant it may seem, this spirit is killing you."
    show darkroom_workspace red:
        matrixcolor BrightnessMatrix(.5)
    "You suspect you won't have long."
    "But as you watch your students work, watch your efforts change this sad, dim world, you can't help but laugh."
    show darkroom_workspace red:
        matrixcolor BrightnessMatrix(.6)
    "The sorry little lantern did indeed become a blazing flame. A flame that has caught the world."
    jump theEnd

label peterCalmEnding:
    #Previous line: I need more than paper. Mr. Carlson. I need *imagery*. Something powerful.
    show peter old tense
    you "Surely you can provide that?"
    show peter old paranoid
    "You see hesitation on Peter's face and feel like this bluff might just work."
    you "If you hold back, you can't expect me to give this my all."
    show peter old tense
    you "You promised me oil. Do you have it?"
    show peter old focus
    Peter "..."
    show peter old explain
    Peter "I've worked with... several other artists over the years."
    show peter old paranoid
    "He thumbs arkwardly at his pockets."
    show peter old explain
    Peter "Many of whom have worked with elements which themselves are... carry something of greater origin than this sorry world."
    show peter old paranoid
    Peter "I could... potentially... arrange for some of them to be sent to you."
    show peter old tense
    you "The muse is striking now, though, Mr. Carlson. To discover all of this!? It's a rush. A creative opportunity that may never come again."
    show peter old worry
    Peter "I have a few things I could give you, I suppose. They weren't meant for... this."
    show peter old focus
    Peter "But I could see their artistic applications... yes. I suppose."
    show peter old arm
    "Peter removes from his pocket a small envelope and hands it to you."
    show peter old worry
    Peter "I imagine you want to get to work. I will return this afternoon to see what you create."
    hide peter with moveoutleft
    jump negativesReceived

label negativesReceived:
    "In the envelope, you discover several negatives and drawings."
    "Things Peter wanted to keep close... or keep secret for some reason."
    "Most of them you don't understand. But one thing you do recognize - a negative for a photo of the Porter itself."
    "A sorry looking thing, blind and mutilated. The same photo Erin had exposed her face over."
    scene darkroom_workspace red
    "You make your way over to the enlarger and begin to expose the photo"

label photoFinal_firstDev:
    show screen projector_porter_intro
    "The spirit shudders to life. With no eyes to open, it simply tilts its head."
    #This is the porter IN the image. I think we'd rather not pull it out for this?
    porter "The image is old... but it will do."
    porter "It should be like so."
    $ porter_eyes = True
    porter "Now, finish what was started."
    "You take the photo back to the enlarger for another exposure as quickly as possible."
    jump finalSiobhan

label finalSiobhan:
    call screen projector_porter_final("Siobhan", "arm") with Fade(1,1,1)
    $ arm_added = True
    "This feels right."

label finalPeter:
    call screen projector_porter_final("Peter", "heart")
    $ heart_added = True
    "This feels right."

label finalGunnar:
    call screen projector_porter_final("Gunnar", "tongue")
    $ tongue_added = True
    "This feels right."
    
label finalJudgement:
    show screen projector_porter_healed with Fade(1,1,1)
    hide screen projector_porter_healing
    "The bizarre composite now done, you bring it back to be developed."
    $ zooming_porter = True
    porter "My power is returning."
    $ zoomed_porter = True
    porter "My function may be served again."
    $ ascend_porter = True
    porter "You have done well."
    scene darkroom_workspace red:
        WhiteNoise
        matrixcolor BrightnessMatrix(-.5)
    hide screen projector_porter_healed with Fade(1,1,1)
    show porter talk at center with Dissolve(.4)
    porter "The BRIGHT in this world will be culled, and things returned where they belong."
    show porter swear
    porter "Humanity will regain my service again."
    show porter talk
    porter "With perhaps more caution."
    porter "..."
    #values broken
    if corruption <= 15:
        porter "I see little brightness in you."
        show porter swear
        porter "Go. Live."
    elif corruption <= 30:
        show porter swear
        porter "Now, for you, there will be {sc=2}some pain{/sc}."
        show porter talk
        porter "The brightness in you must be scraped out"
        show porter swear with Fade(.2, 0.1, .5, color="#fefefe")
        you "{fast}{sc=4}AAAAAHHHH{/sc}{w=.4}{nw}"
        # window auto False
        # window show
        while corruption > 0:
            $ corruption -= 5
            extend "{fast}{sc=4}HHHH{w=.4}{nw}"
        #window auto True
        show porter talk with Fade(.2, 0.1, .5, color="#fefefe")
        "The pain, which felt like hot knives carving at your insides, quickly starts to fade."
        "You feel... better?"
        porter "You are lucky. Go. Live."
        porter "But leave your artistic ambitions behind... at least for a time."
        porter "Or you may reawake the danger."
    else:
        show porter swear
        porter "It is possible you have predicted what {sc=2}must come next{/sc}."
        show porter talk
        porter "You have become {sc=4}too bright{/sc}"
        porter "You are a flame, little one. A flame that could catch the world."
        "You feel an anger, or maybe a fear, rise in your chest."
        "But alongside it, you feel... frenzy, a strangeness inside you."
        "Could the spirit be right??"
        porter "It was not your fault."
        porter "You were tricked... and had none to truly guide you."
        show porter swear
        porter "Let your final thoughts be this: you have done something great. You have made right a wrong."
        show darkroom_workspace red:
            matrixcolor BrightnessMatrix(-0.55)
        show porter swear at center:
            matrixcolor BrightnessMatrix(-.1)
        "Your heart beats wildly as the porter begins to make some sort of magical gesture..."
        show darkroom_workspace red:
            matrixcolor BrightnessMatrix(-0.65)
        show porter swear:
            matrixcolor BrightnessMatrix(-.2)
        "You wonder if this is truly happening. If any of this can truly hurt you."
        "But it can hurt you."
        show darkroom_workspace red:
            matrixcolor BrightnessMatrix(-0.7)
        show porter swear:
            matrixcolor BrightnessMatrix(-.3)
        "And it does."
        show darkroom_workspace red:
            matrixcolor BrightnessMatrix(-0.75)
        show porter swear:
            matrixcolor BrightnessMatrix(-.4)
        "It feels like cold, snaking from the back of your mind down your spine."
        show darkroom_workspace red:
            matrixcolor BrightnessMatrix(-0.8)
        show porter swear:
            matrixcolor BrightnessMatrix(-.5)
        "Coiling around your organs. The cold begins to burn and you pass out, and in your sudden sleep you see its face."
        show darkroom_workspace red:
            matrixcolor BrightnessMatrix(-0.9)
        show porter swear:
            matrixcolor BrightnessMatrix(-.7)
        "The cold is now touching every part of you, it is everywhere inside you."
        show darkroom_workspace red:
            matrixcolor BrightnessMatrix(-1)
        show porter swear:
            matrixcolor BrightnessMatrix(-.9)
        "You are gone."
        hide porter
        show black_background
        jump theEnd
    #only the corrupted ending skips this
    scene darkroom_workspace red with Fade(1, 0.4, .5, color="#000000")
    "The rest of the day passes without a single strange occurance."
    show buddy question at center:
        matrixcolor TintMatrix(color="#e22b2b")
    with moveinleft
    "Buddy arrived a few minutes after the exposure was done, exceedingly worried about you."
    show darkroom_workspace bright
    show buddy question at center:
        matrixcolor None
    "You thought they'd want to hear all about what happened with the porter"
    show buddy smile
    "But mostly they seemed happy to see that you were alright."
    "You both worried about Peter's return."
    "But he never showed up."
    "Peter's death would make the papers the next day."
    "'{font=CastoroTitling-Regular.ttf}Man found dead with heart missing. Psycho on the loose?{/font}'"
    show bg bedroom light with Dissolve(1)
    "But that would come later. It was late. What you needed was sleep."
    show bg bedroom sleep
    "Sleep comes quickly. And when it does, it is peaceful."
    "No dark dreams."
    if corruption >= 15:
        show bg bedroom sleep:
            matrixcolor BrightnessMatrix(.1)
        "Only a little brightness in the corners"
    "But you know the truth."
    "Or, some of it anyway..."

label theEnd:
    $_window_hide()
    show thankyouforplaying with Fade(1.1, 0.5, .5, color="#ffffff")
    pause 2.2
    pause 2.2