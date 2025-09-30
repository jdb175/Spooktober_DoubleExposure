#all of day2 goes in here

##day 2 chars
define owl = Character("Owl", color="#f42f2f") #Owl mask is Siobhan
define doubOwl = Character("Second Owl", color="#c98484") #if we allow this, owl mask talking to owl mask
define flame = Character("Flame", color="#d68408") #Flame mask is Peter
define doubFlame = Character("Second Flame", color="#847257") #if we allow this, flame mask talking to flame mask
define frog = Character("Frog", color="#42aa32") #Frog is Gunnar
define archer = Character("Sage", color="#1e9eb2" ) #Archer is Erin 

##day 2 vars
default photoFirst = False
default paperFirst = False
default doneAPrint = False
default donePhoto2 = False
default donePhoto3 = False

transform magic_strike:
    parallel:
        matrixcolor BrightnessMatrix(2.0)
        pause 0.1
        matrixcolor BrightnessMatrix(1.0)
        pause 0.1
        matrixcolor BrightnessMatrix(2.0)
        easein 1 matrixcolor BrightnessMatrix(0)

transform collapse:
    yoffset 0
    xoffset 0
    parallel:
        ease_back 1 yoffset 80
    parallel:
        linear 1 xoffset 25

#I have no idea why I need this multiplier the one place I use it...
transform collapsed(m = 1):
    yoffset 80*m
    xoffset 24 + m

label day2PostPrintDialogue:
    if photoRuined == True:
        "You're left holding a wrecked photograph."
        "You suspect that you heard many useful things which were meant to be kept secret..."
    else:
        "You're left holding a bizarre photo you suspect no one was meant to see."
        "A conversation which, certainly, no one was meant to hear."
    return

#region start of day 2
label day2Start:
    stop music fadeout 2.0 
    stop ambiance_1 fadeout 2.0
    stop ambiance_2 fadeout 2.0
    stop ambiance_3 fadeout 2.0
    #Note: I have no idea what BG this should be. We probably just have to make it the darkroom.
    "You feel like you've hardly slept at all."
    play sound "text-vibrate.mp3" volume 0.4
    "Grabbing your phone, you see a text from Bud."
    window hide
    scene bg bedroom morning
    $ reset_phone_data()
    $ phone_start()
    $ switch_channel_view("bud_dm")
    show screen phone_ui with dissolve
    $ lock_phone_screen()
    if budLevel == 0:
        $ send_phone_message("Bud", "yo sorry to bother you", "bud_dm")
        $ send_phone_message("Bud", "but could i come by the darkroom today?", "bud_dm")
    else:
        $ send_phone_message("Bud", "Hey can  come by the darkroom?", "bud_dm")
    window hide
    $ send_phone_message("Bud", "had a weird day yesterday and learned some wild stuff you might be interested in", "bud_dm")
    $ send_phone_message("Bud", "also got some cool ideas.", "bud_dm")
    $ send_phone_message("Bud", "ever heard of an artist called siohan kent?", "bud_dm")
    $ send_phone_message("Bud", "siobhan*", "bud_dm")
    hide screen phone_ui
    $ phone_end()
    window show
    play sound ["text-type.mp3"]
    queue sound "text-send.mp3" volume 0.2
    "You throw on some clothes and tell Bud to meet you in an hour."
    #we move to the studio
    stop sound
    scene darkroom_workspace bright with Fade(0.8, 0.4, 0.8)
    pause .5
    show buddy determination with moveinleft
    play music "lil-guitar-loop.mp3" volume 0.5 fadein 4
    bud "So I kept thinking about like, my piece, what I was going to do."
    show buddy talkhand
    bud "As you know, I was thinking of doing something about her disappearance, like, exploring that."
    show buddy disgust
    bud "But then I decided that would probably be seen as kinda trashy."
    show buddy question
    bud "So I was looking at her life as a whole, maybe something about that."
    show buddy amused
    bud "And discovered she'd dedicated one of her pieces to this artist I'd never heard of: {i}Siobhan Kent{/i}."
    show buddy question
    bud "Mixed media artist. A lot of similar themes."
    show buddy confused
    bud "But there was not really any record of them interacting or anything, you know?"
    bud "Like, they never did a showing together."
    show buddy talkhand
    bud "Here's the crazy part. Siobhan? {i}Disappeared.{/i} A few months before Erin did." #same day? What's better for us?
    show buddy confused
    bud "So... it begs the question, how did they know each other?"

label day2BudConvo:
    show buddy listen
    menu:
        set menuset
        "I thought you said you weren't going to do something on her disappearance.":
            show buddy question
            bud "I wasn't! I swear! I was looking for just, you know, generic inspiration!"
            jump day2BudConvo
        "I think I know how they knew each other.":
            show buddy question
            bud "Oh shit, really?"
    show buddy listen
    you "They were both in some sort of... magical organization? Cult?" #Ugh I hate how this scene makes over-explaining hard to avoid
    show buddy sus
    if peterKnown == True:
        you "Run by this guy Peter Carlson." #keep double checking what info is given at this point
    else:
        you "Run by some guy named Peter."
    if porterKnown == True:
        you "Working with, or using, or calling upon, some sort of spirit called the Porter."
    if houseKnown == True:
        you "They had plans to go {i}through{/i} something or {i}to{/i} something. Some other place."
    else:
        you "They were planning to {i}do{/i} something together. I don't really know what."
    show buddy sus
    bud "..."
    if budLevel <= 5:
        show buddy sad
        bud "... ..."
        show buddy angry
        bud "Okay, fine, I get it. You think I'm crazy."
        bud "You're just here to work on your art. I get it."
        show buddy sad
        you "I am being completely serious."
        show buddy question
    else:
        bud "... ..."
        show buddy laughs
        bud "Are you serious? That's... absolutely wild!"
        show buddy clever
        bud "I knew it had to be something freaky!"
        show buddy amused
    bud "How the hell do you know all of that?"
    #Stretch goal is make this a choice, create a second route.
    show buddy smile
    "This is way too much to keep all to yourself. You decide to tell Bud everything."
    show buddy talkhand
    "Any fear you had that the story would be too strange to believe evaporates instantly."
    show buddy disgust
    "They're hanging on to your every word."
    show buddy talkhand
    bud "You have to show me."
    #FIX: this doesn't work 100%, you need to make the choice to try other photo paper earlier mandatory
    show buddy listen
    you "I would, but there's no more photo paper."
    if corruption >= 10:
        you "Besides, I... think it might be dangerous."
        "Bud's eyes go wide, but they don't say anything."
    if peterKnown == True:
        show buddy question
        bud "Okay, well, I guess in the meantime I should look up this, uh, Peter Carlson."
    else:
        show buddy question
        bud "Okay, well, I guess in the meantime I should look up this, uh, Peter guy."
    if porterKnown == True:
        show buddy talkhand
        bud "And some sort of spirit called a Porter?"
    if gunnarKnown:
        show buddy listen
        you "Look up someone named Gunnar too. I think they're famous. Possibly a writer?"
    show buddy question
    bud "Okay, yeah, I'll try."
    bud "If you get a chance to learn more, you should take it."
    show buddy sad
    bud "I feel like this isn't going away and I think we need to learn more."
    "..."
    show buddy tricky
    bud "This is fucking crazy, though, isn't it!"
    show buddy talkhand
    bud "I'll come by later? Or call you if anything super interesting comes up."
    if corruption >= 10:
        show buddy sad
        bud "... be careful."
    hide buddy with moveoutleft
    "As Bud leaves, you start to think about your next move."
    stop music fadeout 4
    "Gazing around the room, two things catch your eye."
    jump day2_darkroom
#endregion

image owlmask = "masks/owl mask.png"
image sagemask = "masks/face mask.png"
image flamemask = "masks/flame mask.png"
image frogmask = "masks/frog mask.png"

image sneakphoto = "photos/night populated.png"
image portalphoto = "photos/portal populated.png"

#region darkroom
label day2_darkroom:
    scene darkroom_workspace bright
    menu:
        set menuset
        "The desk":
            scene parcel
            "Sitting neatly on the corner of the desk is a small package, with a note on it."
            "{font=NothingYouCouldDo-Regular.ttf}'Forgot to drop these off yesterday. Some more of Erin's items, in case they're of interest'" #handwriting
            "Must be from the foundation?"
            play sfx_1 "slides/remove-2.mp3"
            "You peek inside the package and discover another small, hand-wrapped package of photo paper. The same paper you used last night."
            "And there's more of it this time - five whole sheets." #NOTE: this being hardcoded is a challenge if we change it.
            if photoFirst == True:
                jump day2_print
            else:
                $ paperFirst = True
                jump day2_darkroom
        "The photo on the wall":          
            "In your dream you saw a photo hanging on the wall."
            show bg painting with Dissolve(1)
            "You hadn't really clocked it yesterday, but there it is, just where it was in your dream."
            play sfx_1 "slides/remove-1.mp3"
            "You take it down and look at it for a little while. It is a print from one of Erin's last series - 'seen.'"
            play sfx_3 "brass-hit.mp3" volume 0.1
            play sfx_2 "low-thud-single.mp3" volume 0.2
            show mask double exposure with Dissolve(1)
            "The whole series was like this - various masks, shown in a presentational style."
            "You never liked this one. Something about it felt unsettling."
            hide mask double exposure with dissolve
            "You ponder the image for a minute before turning it over."
            show bg painting back with dissolve
            "On a hunch, you pull off the back of the frame. Tucked inside is a strip of photo negatives."
            "Most of the images appear to be the original negatives from 'seen' itself - four masks in all."
            show owlmask  with dissolve:
                zoom 0.7
                xalign 0.5
                matrixcolor SaturationMatrix(0) * InvertMatrix()            
            "{font=ReenieBeanie-Regular.ttf}{size=+26}The Owl"
            hide owlmask with dissolve
            show flamemask with dissolve:
                zoom 0.7
                xalign 0.5
                matrixcolor SaturationMatrix(0) * InvertMatrix()         
            "{font=ReenieBeanie-Regular.ttf}{size=+26}The Flame"
            hide flamemask with dissolve
            show sagemask with dissolve:
                zoom 0.7
                xalign 0.5
                matrixcolor SaturationMatrix(0) * InvertMatrix()         
            "{font=ReenieBeanie-Regular.ttf}{size=+26}The Sage"
            hide sagemask with dissolve
            show frogmask with dissolve:
                zoom 0.7
                xalign 0.5
                matrixcolor SaturationMatrix(0) * InvertMatrix()         
            "{font=ReenieBeanie-Regular.ttf}{size=+26}The Frog"
            hide frogmask with dissolve
            "For a moment, you forget the strange circumstances you are in."
            "It's a rush seeing an original negative from Erin!"
            "Two of the images, however, hardly look like works of art at all."
            show sneakphoto with dissolve:
                zoom 0.4
                xanchor 0.5
                yanchor 0.5
                rotate 1
                xalign 0.1
                yalign 0.4
                matrixcolor  SaturationMatrix(0) * InvertMatrix() * BrightnessMatrix(.2) 
            show portalphoto with dissolve:
                zoom 0.4
                xanchor 0.5
                yanchor 0.5
                rotate -2
                xalign 0.9
                yalign 0.37
                matrixcolor SaturationMatrix(0) * InvertMatrix()      
            "Candid photographs of strange figures in robes."
            show portalphoto with dissolve
            hide sneakphoto with dissolve
            hide portalphoto with dissolve
            #"Most of the images are totally ruined, but it does look like there are a few near the end that are relatively untouched."
            if paperFirst == True:
                jump day2_print
            else:
                $ photoFirst = True
                jump day2_darkroom
#endregion

#region projector basics
label day2_print:
    window hide
    $ begin_day(Days.DAY_TWO)
    $ onFirstBase = True #changes dialogue in select double
    scene darkroom_workspace bright
    "With these negatives, and more paper, you realize you have a chance to learn more about what is really going on."
    "You, of course, have some doubts. After all, you know that you don't {i}really{/i} know what's going on."
    "And this package with fresh paper suddenly arriving is... suspicious..."
    show darkroom_workspace red
    $ play_darkroom_light()
    if corruption >= 15:
        "But you find your heart quickening at the thought of seeing these photos come to life again."
    else:
        "But you know this might be the best path to understanding."
    jump projector_select_base_daytwo

label projector_select_base_daytwo:
    scene black_background with flash
    $ start_enlarger()
    window hide
    $ target_label = renpy.call_screen("enlarger_select_photo")
    show bg tray red
    "With an image chosen, you take your new print to the developing bath."
    show photopaper tray at developingImageWave with Dissolve(0.5):
        matrixcolor TintMatrix("#975555") 
    show fakeClock:
        zoom .3
        xanchor 0.5
        yanchor 0.575
        xalign 0.5
        yalign 0.4
    show clock pointer aligned:
        zoom .3
        xanchor 0.5
        yanchor 0.575
        xalign 0.5
        yalign 0.5
    with dissolve
    "Once again you set out your watch. {b}30 seconds{/b} to maximize the double exposure, {b}60 seconds{/b} until it's done."
    jump expression target_label

    label projector_select_double_daytwo:
    scene darkroom_workspace red
    "You grab your tongs and pull out the photo."
    $ complete_label = get_tag_if_finished()
    if(complete_label):
        jump expression complete_label
    if onFirstBase == True:
        "Then, you make your way to the enlarger."
        "You're eager to see what you might be able to learn from these negatives you found."
        $ onFirstBase = False
    else:
        if corruption <= 15:
            "Then it's back to the enlarger, ready to see what the next negative might reveal..."
        else:
            "Then it's back to the enlarger. You're already thinking of the next negative, what kind of beautiful imagery it could create..."
            "No, wait, this is about learning, not creating... Right?"  
    window hide
    $ start_enlarger()
    $ target_label = renpy.call_screen("enlarger_select_photo")        
    jump expression target_label

label post_image_completion_daytwo:
    scene darkroom_workspace red
    $ photoRuined = False
    $ reachedEnd = False
    if(current_photo_paper > 0):
        if(current_photo_paper == 1):
            "You have a single piece of photo paper left."
            if corruption >= 25:
                "You feel a strange pang of sorrow in your chest. You don't want this to end."
                "You want to make more photos..."
                "Then you remember what it is you're really trying to do."
                "Figure out what's going on. Nothing more."
            else:
                "You think carefully about what you still need to learn..."
        else:
            "You have [current_photo_paper] pieces of photo paper left."
            "Which is good, because you still have so many questions to answer."
        jump projector_select_base_daytwo
    jump endOfDay2
#endregion

#region sneaky (secret meeting)
label develop_sneaky:
    scene black_background with fade
    $ start_developing(BASE_IMAGE_SNEAKY)
    "Something about the seemingly candid nature of this photo intrigues you."
    "You slide in a piece of photo paper and start to print the image."
    $ develop(5)
    $ audio_sneaky()
    "'It' begins to happen again..."
    #NOTE: Add "if seen this photo already" code in once we standardize how it works.
    if donePhoto2:
        "You could watch it all play out once more, or you could just pull it out as soon as possible."
        menu:
            "Watch it all again":
                $ donePhoto2 = False
            "Pull it out":
                $ develop (30)
                "The robed figures argue as before, but your eyes are on the clock."
                $ stop_developing_instant()
    #This is GUNNAR, officially
    $ zoom_development = True
    pause 3
    show owl argue at dcp, xflip, left with Dissolve(1)
    show robes crossed at dcp, right with dissolve
    $ zoom_development = True
    owl "Took you long enough!"
    show owl open at xflip, dcp
    owl "Where's your mask?"
    $ develop(10)
    show robes crossed at dcp
    show owl open at xflip,dcp
    unk "It's in my room. Where it ought to be."
    show owl argue at xflip, dcp
    owl "So what you're saying is that you're not going through with me tonight?"
    show owl show at xflip, dcp
    owl "Or do you not believe Peter that we need our masks?"
    $ develop(15)
    show robes open at dcp
    show owl hips at xflip, dcp
    unk "I'm sorry, but I trust Peter more than you."
    show robes crossed at dcp
    unk "Don't get me wrong. I've... seriously been considering it."
    unk "I may even come with you on one of your future jaunts..."
    $ develop(20)
    show robes crossed at dcp
    show owl hips at xflip, dcp
    unk "But if I may speak frankly, I don't believe it pays to be reckless with these things."
    show robes open at dcp
    unk "Peter knows far more than me, and whatever you think you may have picked up these last few days, he knows more than you, too."
    show robes crossed at dcp
    owl "..."
    show owl scared at dcp
    owl "It has only been days, hasn't it?"
    show owl hips at dcp
    owl "It feels so much longer."
    $ develop(25)
    show owl hips at dcp
    show robes crossed at dcp
    unk "..."
    $ develop(30)
    show owl argue at xflip, dcp
    show robes crossed at dcp
    owl "So, are you going to turn me in?"
    if(development_end_signalled == False):
        "You eye the clock. Photo's half developed. If you pull it out now, you'll get more time to double expose before it overdevelops"
    $ develop(35)
    show robes open at dcp
    show owl hips at xflip, dcp
    unk "Not a chance. As I said, I may change my mind and go through with you one of these evenings."
    unk "But not yet."
    show robes crossed at dcp
    show owl show at xflip, dcp
    owl "How indecisive of you."
    $ develop(40)
    show robes crossed at dcp
    show owl argue at xflip, dcp
    owl "You must know that indecision is one of the few things that is truly deadly to an artist."
    owl "So keep stringing things along, if you'd like. Delaying every decision."
    show owl hips at xflip, dcp
    owl "But the opportunity may not always be here."
    $ develop(45)
    show robes crossed at dcp
    show owl hips at xflip, dcp
    unk "..."
    $ develop(50)
    show robes open at dcp
    show owl hips at xflip, dcp
    unk "Wait here. I'll come."
    $ develop(55)
    show robes crossed at dcp
    show owl argue at xflip, dcp
    owl "Good. Be quick. He's a heavy sleeper but wakes early."
    hide robes crossed with moveoutright
    $ develop(60)
    show owl crossed at xflip, dcp
    owl "He better not turn me in..."
    "The image is getting brighter now, becoming overdeveloped"

label develop_sneaky_overexposed:
    $ renpy.block_rollback()
    $ develop_overexposed(5)
    $ corruption += 5
    $ audio_sneaky_overexpose()
    show owl crossed at xflip, dcp, dc_overexpose
    owl "soon we will transgress"
    $ audio_escalate(1)
    owl "soon The Bright will spill"
    $ develop_overexposed(10)
    $ audio_escalate(2)
    show owl crossed at xflip, dcp, dc_overexpose
    owl "The guardian, the warden, the Porter will fall"
    $ develop_overexposed(15)
    $ audio_escalate(3)
    show owl magic at xflip, dcp, dc_overexpose
    owl "BUT HE SHALL RETURN"
    $ develop_overexposed(20)
    show owl magic at xflip, dcp, dc_overexpose
    jump complete_sneaky

label complete_sneaky:  
    $ finish_development()
    $ donePhoto2 = True
    call corruptionDialogue
    "As you pull out the image, it ceases to move."
    "Your heart, however, continues to beat quickly."
    if corruption >= 15:
        "Should you be more careful with these forces?"
    jump post_image_completion_daytwo

#region sneaky siobhan/owl
label develop_sneaky_owl:
    $ start_double_exposing(OBJECT_IMAGE_OWL)
    $ audio_sneaky()
    "As your photo develops, you heart begins to quicken, almost uncontrollably."
    $ zoom_development = True
    pause 3
    show owl crossed at dcp, xflip, left with Dissolve(.4)
    show owl2 hips at dcs, right with Dissolve(.8)
    $ audio_sneaky_melody("siobhan")
    "The two robed figures, each wearing the same mask, begin to speak."
    $ develop_double(5)
    show owl crossed at xflip, dcp
    show owl2 hips at dcs
    doubOwl "..."
    owl "Is this some kind of joke?"
    show owl point at xflip, dcp
    owl "Who are you?"
    show owl argue at xflip, dcp
    owl "Why are you wearing my mask?"
    $ develop_double(10)
    show owl crossed at xflip, dcp
    show owl2 hips at dcs
    doubOwl "..."
    doubOwl ".........."
    $ develop_double(15)
    show owl crossed at xflip, dcp
    show owl2 hips at dcs
    owl "I'm not fucking around here, okay? Take off your mask! Who are you?"
    show owl scared at xflip, dcp
    owl "Or is this another one of those nightmares??"
    show owl2 point:
        dcs
        WhiteNoise
    doubOwl "{sc=1}This corruption of the truth should not be possible{/sc}."
    show owl2 argue
    doubOwl "You have strayed beyond your limits, human."
    $ develop_double(20)
    show owl scared at xflip, dcp
    show owl2 explain at dcs
    doubOwl "Given a gift, you were unsatisfied."
    show owl2 point at dcs
    doubOwl "Your hunger is your unmaking."
    hide owl2 at dcs with Dissolve(.4)
    show porter dead:
        dcs
        yalign .01
        xalign .9
        WhiteNoise
    with Dissolve(.6)
    $ develop_double(25)
    show owl scared at xflip, dcp
    show porter dead at dcs
    porter "{sc=2}Your judgement was made long ago, transgressor.{/sc}"
    owl "This isn't... this isn't possible."
    $ develop_double(30)
    show porter dead at dcs
    show owl show at xflip, dcp
    owl "When is this? When is this happening?"
    show owl point at xflip, dcp
    owl "{size=+4}We haven't even killed you yet!"
    show owl open at xflip, dcp
    owl "{size=+4}I have no hand to give you!!"
    $ reachedEnd = True

label develop_sneaky_owl_overexposed:
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out at the perfect time."
    else:
        "You know that if you keep this photo in any longer, you will overexpose it"
    $ audio_escalate(1)
    $ develop_overexposed(10)
    show owl open at dcp, dc_overexpose
    show porter dead:
        dcs
        yalign .01
        xalign .9
        WhiteNoise
    $ corruption += 5
    $ audio_sneaky_overexpose()
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    porter "{sc=2}This cannot be understood. And it will end.{/sc}"
    $ develop_overexposed(20)
    $ audio_escalate(2)
    show owl open at dcp, dc_overexpose
    show porter dead at dcp, dc_overexpose
    porter "{sc=2}NOW{/sc}"
    $ develop_overexposed(30)
    $ audio_escalate(3)
    show owl open at dcp, dc_overexpose
    show porter dead at dcp, dc_overexpose
    call corruptionDialogue
    hide owl
    hide porter
    jump complete_sneaky_owl

label complete_sneaky_owl:  
    $ finish_development()
    $ donePhoto2 = True
    "As you pull out the image, it ceases to move."
    "What even was that?!"
    jump post_image_completion_daytwo
#endregion

#region sneaky peter/flame
label develop_sneaky_flame:
    $ start_double_exposing(OBJECT_IMAGE_FLAME)
    $ audio_sneaky()
    "You watch with curiosity as the photo begins to move, the masked figures begin their speech."
    $ zoom_development = True
    pause 3
    show owl crossed at dcp, xflip, left with Dissolve(.4)
    show fire hips at dcs, right with Dissolve(.8)
    "This time, the figure in the owl mask does not seem to want to talk."
    show owl crossed at dcp
    pause .1
    hide owl with moveoutleft
    "They hurry into the shadows, as if they do not want to be seen."
    $ develop_double(5)
    show fire point at dcs
    $ audio_sneaky_melody("peter")
    flame "What are you doing sneaking around in the dark?"
    flame "I've already seen you, Siobhan." #this may be too much? But I think Peter would say it.
    $ develop_double(10)
    show fire argue at dcs
    show owl scared at dcp, xflip, left with moveinleft
    flame "Do you think I didn't notice someone has been going through my papers?"
    show fire explain at dcs
    show owl crossed at xflip, dcp
    flame "I had very much hoped to catch you in the act."
    show fire hips at dcs
    flame "But I didn't expect to catch you trying to sneak into the Bright House on your own."
    show fire point at dcs
    flame "Well? Speak."
    show owl open at xflip, dcp
    show fire hips at dcs
    owl "I don't know what you think I'm doing, or what you think I've done."
    show owl point at xflip, dcp
    owl "But I do know you've been keeping a lot of secrets from us."
    $ develop_double(15)
    show fire explain at dcs
    show owl crossed at xflip, dcp
    flame "I've said many times that as we continue to explore together, I will share more of what I know."
    flame "That is entirely because I wanted to ensure I was working with people I could trust."
    show fire argue at dcs 
    flame "And here you are, living proof that I was right to be cautious."
    show fire hips at dcs
    owl "I think you like holding all the power, stringing us along."
    show owl explain at xflip, dcp
    owl "I think you want to keep the Bright House all to yourself."
    $ develop_double(20)
    show fire hips at dcs
    show owl point at xflip, dcp
    owl "You're only sharing it because of your own inability to understand it."
    show owl crossed at xflip, dcp
    show fire argue at dcs
    flame "Don't be stupid! You had so much you could have gained from this!"
    flame "Your art, your insight, your abilities..."
    flame "In just a few days, you have grown more than you would have in years of toil!"
    show fire open at dcs
    flame "This is the light of {b}creativity itself{/b}."
    flame "And now it will be shut to you forever."
    $ develop_double(25)
    show fire argue at dcs
    show owl crossed at xflip, dcp
    flame "I have already summoned the Porter and told it that you've been calling it with stolen magic."
    show fire point at dcs
    flame "That you intend to transgress the limits it has set for us."
    show fire hips at dcs
    flame "It will open no more doors for you."
    $ develop_double(30)
    show fire show at dcs
    show owl crossed at xflip, dcp
    flame "Now, get your things and leave my home."
    $ reachedEnd = True

label develop_sneaky_flame_overexposed:
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out at the perfect time."
    else:
        "You know that if you keep this photo in any longer, you will overexpose it."
    $ develop_overexposed(10)
    show fire point at dcs, dc_overexpose
    show owl show at dcp, xflip, dc_overexpose
    $ corruption += 5
    $ audio_sneaky_overexpose()
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    flame "Your time here is done, Siobhan. In this house, and the Other."
    $ develop_overexposed(15)
    $ audio_escalate(1)
    show fire show at dcs, dc_overexpose
    show owl crossed at dcp, xflip, dc_overexpose
    owl "Blind in art, blind in all things but money."
    owl "BLIND TO THE DEPTHS OF MY TREACHERY"
    $ develop_overexposed(20)
    $ audio_escalate(2)
    show fire show at dcs
    show owl crossed at dcp, xflip, dc_overexpose
    owl "THE {sc=4}HAND{/sc} OF THE PORTER DRAWS THE DOORS"
    owl "THE DOORS ARE DRAWN BY THE {sc=4}HAND{/sc}"
    $ develop_overexposed(25)
    $ audio_escalate(3)
    show fire show at dcs:
        WhiteNoise
    show owl crossed at dcp, xflip, dc_overexpose
    owl "{sc=4}GIVE ME BACK MY HAND{/sc}!"
    call corruptionDialogue
    hide owl
    hide flame
    jump complete_sneaky_flame

label complete_sneaky_flame:  
    $ finish_development()
    $ donePhoto2 = True
    call day2PostPrintDialogue
    jump post_image_completion_daytwo
#endregion

#region sneaky erin/archer
label develop_sneaky_archer:
    #This scene needs more information
    $ start_double_exposing(OBJECT_IMAGE_ARCHER)
    $ audio_sneaky()
    "From the strange masked figures, you see faint movement and hear whispers, growing stronger, growing bolder."
    $ zoom_development = True
    pause 3
    $ develop_double(5)
    show owl hips at dcp, left with Dissolve(.4)
    show sage crossed at dcs, right with Dissolve(.8)
    owl "Oh!"
    show owl hips at xflip, dcp
    owl "It's... it's you."
    owl "What are you doing here?"
    $ audio_sneaky_melody("erin")
    show sage explain at dcs
    archer "I could ask you the same question."
    show owl show at xflip, dcp
    show sage hips at dcs
    owl "I've been taking walks at night. Trying to basically process everything we've seen in the Bright House."
    show owl crossed at xflip, dcp
    owl "I find wearing the costume helps me remember. Stupid as they are."
    owl "Because it's like..."
    show owl scared at xflip, dcp
    owl "The first time I went through the portal... that first day It all made so much sense."
    show owl show at xflip, dcp
    owl "I could see the threads connecting {i}there{/i} to {i}here{/i}."
    show owl open at xflip, dcp
    owl "I felt like I'd just taken a tour backstage at a play I'd seen a thousand times."
    show owl crossed at xflip, dcp
    owl "But it fades so fast, doesn't it?"
    $ develop_double(10)
    show owl crossed at xflip, dcp
    show sage open at dcs
    archer "It does."
    show sage show at dcs
    archer "I think it's meant to fade, though."
    archer "I think we're not meant to understand."
    show sage hips at dcs
    archer "Not really."
    show owl open at xflip, dcp
    owl "Oh, that's definitely what {i}they{/i} think."
    show owl explain at xflip, dcp
    owl "Peter and his freaky little spirit gremlin. Keeping tabs on us."
    owl "Telling us where we can and can't go."
    show owl crossed at xflip, dcp
    show sage explain at dcs
    archer "I don't know. I think there's a reason for that."
    show sage open at dcs
    archer "Although what the hell do I know."
    show sage hips at dcs
    archer "Actually... I envy you."
    archer "Your recent work has been... incredible. I don't know how to describe it."
    show sage open at dcs
    archer "But it feels like I can see a bit of that place when I look at it."
    show sage hips at dcs
    show owl scared at xflip, dcp
    owl "Who knows if anyone else will. Every piece I make just immediately feels like it's shit."
    show owl crossed at xflip, dcp
    owl "Like it's so far from what I meant to say."
    $ develop_double(15)
    show owl explain at xflip, dcp
    show sage hips at dcs
    owl "But don't you think if you could just get a little further in the House you could figure it out?"
    owl "Like there's answers just waiting for you if you could go deeper?"
    show owl crossed at xflip, dcp
    owl "At least for us. Maybe not for poor Gunnar."
    show owl show at xflip, dcp
    owl "I looked in his notebook. It's like The Shining, writing the same sentence over and over again."
    show owl explain at xflip, dcp
    owl "Not literally, like, he's not crazy. I don't think. But it's just first sentence, second sentence, cross it out."
    show sage argue at dcs
    show owl crossed at xflip, dcp
    archer "He's actually successful though."
    show sage hips at dcs
    show owl show at xflip, dcp
    owl "And you will be too! I think you're better at this than you think."
    owl "Your idea of using the masks is cool. Not sure what Peter will think, but it's cool."
    show owl explain at xflip, dcp
    owl "I think he'll do anything you ask, though, if you just say it's 'for your art.'"
    show owl crossed at xflip, dcp
    show sage open at dcs
    archer "See? This is what I mean. I think my art sucks, you think your art sucks, but to the outside world it's good."
    show owl scared at xflip, dcp
    show sage hips at dcs
    owl "Maybe..."
    $ develop_double(20)
    show owl crossed at xflip, dcp
    show sage hips at dcs
    owl "..."
    owl "Do you really trust Peter and that... creature?"
    show sage show at dcs
    archer "I don't know. I trust him not to get us killed or anything."
    archer "But I still don't feel like I understand what he's trying to do. Or why that spirit helps him."
    show sage point at dcs
    archer "I'm debating doing what you did..."
    show sage explain at dcs
    archer "Trying to read some of Peter's notes and stuff."
    $ develop_double(25)
    show owl crossed at xflip, dcp
    show sage hips at dcs
    owl "Yeah. Me too."
    owl "..."
    show owl explain at xflip, dcp
    owl "I wonder where he keeps his... you know, his spells and stuff."
    owl "I wonder if we could find those too."
    show owl crossed at xflip, dcp
    archer "I think that's a bad idea."
    owl "Yeah, you're probably right."
    $ develop_double(30)
    $ reachedEnd = True

label develop_sneaky_archer_overexposed:
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out at the perfect time."
    else:
        "You know that if you keep this photo in any longer, you will overexpose it."
    $ develop_overexposed(10)
    show owl crossed at left, dcp, xflip, dc_overexpose
    show sage hips at dcs, right, dc_overexpose
    $ corruption += 5
    $ audio_sneaky_overexpose()
    $ photo_ruined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    #This is crappy because it gives you no clues and maybe even throws you down an incorrect path.
    owl "... Wait, you never answered me. What {i}are{/i} you doing out here? Dressed in your portal robes??"
    archer "Oh."
    archer "I... I don't know."
    $ audio_escalate(1)
    archer "Wait, how could I possibly {i}not know{/i}?"
    $ develop_overexposed(15)
    show owl crossed at dcp, xflip, dc_overexpose
    show sage hips at dcs, dc_overexpose
    archer "I was walking at night, but I don't remember putting on my mask. My robes."
    $ audio_escalate(2)
    archer "{size=+2}Did I really do that?"
    $ develop_overexposed(20)
    show owl crossed at dcp, xflip, dc_overexpose
    show sage hips at dcs, dc_overexpose
    archer "{size=+5}HOW MUCH OF THIS IS REAL?"
    $ develop_overexposed(25)
    $ audio_escalate(3)
    show owl crossed at dcp, xflip, dc_overexpose
    show sage hips at dcs, dc_overexpose
    archer "{size=+10}IS ANY OF THIS REAL??"
    jump complete_sneaky_archer

label complete_sneaky_archer:
    $ finish_development()
    $ donePhoto2 = True
    call day2PostPrintDialogue
    jump post_image_completion_daytwo
#endregion

#region sneaky gunnar/frog
label develop_sneaky_frog: #This scene is hella long but needs to be...
    $ start_double_exposing(OBJECT_IMAGE_FROG)
    $ audio_sneaky()
    "While it's clear that this photo wasn't taken to be a piece of art, there's an incredible energy you feel watching the masked figures shiver to life."
    "Like you are stealing a glimpse at some great secret."
    $ zoom_development = True
    pause 3
    $ develop_double(5)
    show owl crossed at dcp, left with Dissolve(.4)
    show frog hips at dcs, right with Dissolve(.8)
    $ audio_sneaky_melody("gunnar")
    frog "You're still here!"
    show frog open at dcs
    frog "Didn't Peter tell you to clear out?"
    show frog hips at dcs
    owl "I will. Tomorrow."
    show owl crossed at dcp, xflip
    owl "Thought I'd come one last time to our usual 'meeting.'"
    frog "That's thoughtful of you, but you know that the Porter won't let you in anymore."
    show frog show at dcs
    frog "And if you can't get in, I can't get in, so I'm afraid our midnight jaunts have come to a close."
    show frog hips at dcs
    show owl argue at dcp, xflip
    owl "What makes you think the Porter will let you in?"
    show owl explain at dcp, xflip
    owl "I'm sure Peter instructed it to prevent {i}any{/i} of us from getting in alone."
    show owl crossed at dcp, xflip
    show frog show at dcs
    frog "No harm in trying, is there?"
    show frog hips at dcs
    frog "But not with you here. That definitely won't fly."
    $ develop_double(10)
    show owl explain at dcp, xflip
    show frog hips at dcs
    owl "You know if you get the ritual wrong there can be consequences. If you attempt it without my help, it could go bad for you."
    owl "Are you really sure you've got it down?"
    show owl crossed at dcp, xflip
    frog "I'm a keen observer. I'll be alright."
    show owl show at dcp, xflip
    owl "So you know what to keep hidden in your left hand and what to trace on your right?"
    show frog scared at dcs
    frog "..."
    show frog crossed at dcs
    frog "You're making things up."
    show owl open at dcp, xflip
    owl "I'm trying to help you."
    show owl show at dcp, xflip
    owl "Let me show you. And then I'll get out of your way."
    "The figure in the owl mask presses something small and black into the other's left palm."
    "They then grab the other's right hand and gently uncurl their fingers before tracing a shape on the palm."
    show owl explain at dcp, xflip
    owl "Keep learning about this place. You and I have come to understand how {b}important{/b} it is. What's hidden within."
    show owl hips at dcp, xflip
    show frog open at dcs
    frog "I will."
    show frog crossed at dcs
    frog "..."
    frog "Thank you."
    show owl hips:
        dcp
        xzoom 1
    owl "Good luck."
    hide owl with moveoutleft
    show frog magic at dcs
    "The frog-masked figure stands alone now. They raise their hands in purposeful, almost artful gestures."
    show frog explain at dcs
    "They remain completely, eerily silent. The only sound is the swooshing of their robes and the creaking of old floorboards."
    show frog magic at dcs
    "Then..."
    #NOTE: effects here!
    play drone_1 "bass-drone-1.mp3" fadein 1.0 volume 0.5
    play sfx_1 "low-thud-single.mp3" volume 0.5
    play sfx_2 "guitar-Ab.mp3" volume 0.6
    show porter speak at dcs, left, xflip, DramaticRevealPorter
    with flash
    pause 3.56
    porter "You."
    $ develop_double(15)
    show porter swear at dcs, xflip, EmergencyReset
    show frog hips at dcs
    porter "Peter has told me that you wander where you are not meant to wander."
    porter "Beyond the walls of the House and into the Gardens. That you have even gazed into the Well."
    porter "You will not ent-"
    play drone_2 "bass-drone-2.mp3" volume 0.3
    show porter swear at dcs, magic_strike, xflip, Regicide
    porter "wh.."
    porter "what is that"
    show porter swear at dcs, xflip, DoubleRegicide
    frog "What is... what? This?"
    show frog open at dcs
    "They open their left palm and reveal the odd stone pressed within."
    play sfx_2 "gong-1.mp3"
    play drone_3 "piano-underscore-spook-2.mp3"
    porter "WHAT HAVE YOU DONE?"
    show porter swear at dcs, collapse, xflip, UltimateRegicide
    "The spirit's thin legs seem to collapse under it. It begins to shake."
    show porter swear at dcs, magic_strike, xflip, ArmGlow
    play sfx_3 "eerie-1.mp3"
    "Its arm begins to glow, consumed by a sickly yellow light."
    "The light travels through the air and into the darkness, traveling towards the hand of another."
    $ develop_double(20)
    show frog crossed at dcs
    show porter swear at dcs, magic_strike, xflip, ArmGlow
    show owl magic at dcp, center, ArmGlowOwlHand with moveinbottom
    owl "Apologies to use you like that, but I wasn't going to let anyone freeze me out."
    owl "Not after all I've seen and learned."
    play audio "gore/porter-death.mp3"
    stop drone_1 fadeout 1
    stop drone_2 fadeout 1
    stop drone_3 fadeout 1
    stop sfx_1 fadeout 1
    stop sfx_2 fadeout 1
    stop sfx_3 fadeout 1
    pause 0.5
    hide porter
    show porter dead at dcs, magic_strike, xflip, collapsed(1):
        shader None
    stop photo_1 fadeout 1
    frog "What have you done?! What did you do to it?!"
    owl "Go. Your part is done here."
    frog "{size=+7}{sc=1}Aaaahh!"
    show frog crossed at xflip, dcs
    hide frog with moveoutright
    $ develop_double(25)
    show owl point at center, dcp
    "Their hand now glowing with the same sickly light, the figure in the owl mask places their hand on the floor."
    "Slowly, they trace a circle around the writhing spirit."
    play sfx_1 "guitar-Ab.mp3" volume 0.5
    play sfx_2 "low-thud-single.mp3" volume 0.5
    hide porter with flash
    "As they close the loop, a gate opens in the floor and the Porter is gone."
    $ develop_double(30)
    $ reachedEnd = True

label develop_sneaky_frog_overexposed:
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out just in time."
    else:
        "You look at the clock. The photo is fully developed. Leaving it in any further will ruin it."
    $ develop_overexposed(10)
    $ corruption += 5
    $ audio_sneaky_overexpose()
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    show owl at center, dcs, dc_overexpose
    hide owl with moveoutleft
    "The figure in the owl mask walks into the shadows, leaving the image eerily quiet."
    "In the silence you are able to hear something behind you. Breathing?{nw=1}"
    show porter dead:
        dcp
        center
        zoom 1.5
        xalign .5
        yalign .1
        linear 100 zoom 3
    play sfx_1 "low-thud-single.mp3"
    $ audio_escalate(1)
    porter "{sc=3}{size=+10}GIVE IT BACK"
    hide porter with dissolve
    "Gasping for breath, you look around the room. It's just you."
    $ audio_escalate(2)
    "You hear some kind of noise coming from the photo in the tray."
    "Full of dread, you turn back to the image, keeping one eye on the rest of the room."
    show owl scared at center, dcs, dc_overexpose
    $ develop_overexposed(15)
    $ audio_escalate(3)
    show owl scared at center, dcs, dc_overexpose
    "They are weeping."
    $ develop_overexposed(20)
    show owl scared at center, dcs, dc_overexpose
    call corruptionDialogue
    hide owl
    jump complete_sneaky_frog

label complete_sneaky_frog:
    $ finish_development()
    $ donePhoto2 = True
    call day2PostPrintDialogue
    jump post_image_completion_daytwo
#endregion
#endregion

#region portal (portal opens)
#may have to use porter name variable
label develop_portal:
    scene black_background with fade
    $ start_developing(BASE_IMAGE_PORTAL)
    #NOTE: Add "if seen this photo already" code in once we standardize how it works.
    if donePhoto3 == False:
        "It's hard not to be intrigued by the strange, surreal glow in this image. Was this really an undoctored photo?"
    else:
        "Surely there is more to learn from this strange gateway..."
    "You slide in a piece of photo paper and start to print the image."
    $ develop(5)
    "It begins to happen again..."
    $ audio_portal()
    #play photo_1 "creaking-underscore.mp3"
    #play photo_2 "low-thudding.mp3"
    if donePhoto3:
        "You could watch it all play out once more, or you could just pull it out as soon as possible"
        menu:
            "Watch it all again":
                $ donePhoto3 = False
            "Pull it out":
                $ develop (30)
                "The same little pageant plays out, but your eyes are on the clock."
                $ stop_developing_instant()
    $ zoom_development = True
    pause 3
    show fire point at dcp, right with Dissolve(1)
    show robes crossed at dcp, xflip, left with dissolve
    flame "THE DOOR IS OPEN. Step through, quickly!"
    show robes reach at dcp, xflip, UltimateRegicide
    unk "I can see it! The House!"
    flame "Hurry!"
    hide robes reach with Dissolve(1)
    pause .2
    unk2 "Is it your will that I follow them?"
    show porter speak at dcp, xflip with moveinleft
    porter "Or would you rather accompany them today?"
    $ develop(10)
    show porter listen at dcp, xflip
    show fire explain at dcp
    flame "You go. I'll wait here."
    show fire hips at dcp
    show porter speak at dcp, xflip
    porter "As you wish."
    $ develop(15)
    show porter listen at dcp, xflip
    show fire open at dcp
    flame "I think you can take them to the Vestibule today."
    show fire show at dcp
    flame "I wonder if they will find the statuary there as inspiring as I do." #deliberate reference to Piranisi here, hope it's not seen as copying.
    $ develop(20)
    show porter swear at dcp, xflip
    show fire hips at dcp
    porter "The Vestibule sits near the Windows of the Garden. I would not take them somewhere so bright."
    show porter sad at dcp, xflip
    porter "They have stepped through so many times so quickly already."
    $ develop(25)
    show fire crossed at dcp
    show porter swear at dcp, xflip
    porter "You know there are risks."
    porter "Even the service I owe to you to you cannot override my purpose."
    $ develop(30)
    show fire crossed at dcp
    show porter speak at dcp, xflip
    porter "They must rest soon or they will begin to overflow. You will see to it that it is so."
    if(development_end_signalled == False):
        $ audio_warn_clock()
        "You eye the clock. Photo's half developed. If you pull it out now, you'll get more time to double expose before it overdevelops."
    $ develop(35)
    show fire hips at dcp
    show porter listen at dcp, xflip
    flame "Yes, of course, of course. They need to actually start producing some art at some point anyway."
    show fire open at dcp
    flame "Not that I blame them. What could be more dull than sitting around {i}working{/i} when you could be in another world?"
    show fire hips at dcp
    porter "..."
    show fire show at dcp
    flame "Go. Take them to the Vestibule. Show them the Corridor of Statues."
    $ develop(40)
    show fire hips at dcp
    show porter listen at dcp, DoubleRegicide
    "The Porter turns to face the strange glow at the end of the hallway. It steps into it and begins to disappear."
    show porter swear at dcp, UltimateRegicide
    "Then, the spirit raises a trembling, withered hand. It traces some kind of shape in the air."
    hide porter with dissolve
    "The spirit then disappears into the bright light."
    $ develop(45)
    show fire hips at dcp
    "The figure in the flame mask sighs deeply."
    flame "Now the waiting."
    $ develop(50)
    show fire crossed at dcp
    flame "..."
    $ develop(55)
    show fire crossed at dcp
    flame "Loyal little spirit, is it not?"
    $ develop(60)
    show fire scared at dcp
    flame "I wonder what the Porter would do if it caught me entering now..."
    show fire crossed at dcp
    flame "Best to trust its guidance, I suppose."

label develop_portal_overexposed:
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out just in time."
    else:
        "If you don't pull the photo out now, it will be overexposed."
    $ audio_portal_overexpose()
    $ develop_overexposed(5)
    show fire crossed at right, dcp, dc_overexpose
    $ corruption += 5
    $ audio_escalate(1)
    flame "Foolish little thing. {sc=1}Blind{/sc} little thing."
    $ develop_overexposed(10)
    show fire crossed at dcp, dc_overexpose
    flame "{sc=1}Mute{/sc} little thing. {sc=2}Bloodless{/sc} little thing."
    $ develop_overexposed(15)
    $ audio_escalate(2)
    show fire crossed at dcp, dc_overexpose
    flame "{sc=2}TRAPPED{/sc} little thing. {sc=4}BETRAYED{/sc} little thing."
    $ develop_overexposed(20)
    show fire crossed at dcp, dc_overexpose
    flame "{sc=4}BUT IT WILL BE MADE WHOLE."
    $ audio_escalate(3)
    flame "{sc=4}AND {sc=4}BRIGHT THINGS WILL BE CONTAINED{/sc}!"
    $ develop_overexposed(25)
    show fire crossed at dcp, dc_overexpose
    call corruptionDialogue
    jump complete_portal

label complete_portal:  
    $ finish_development()
    $ donePhoto3 = True
    "As you pull out the image, it ceases to move."
    "Your heart, however, continues to beat quickly."
    if corruption >= 15:
        "Should you be more careful with these forces?"
    jump post_image_completion_daytwo

#region portal siobhan/owl
label develop_portal_owl:
    $ start_double_exposing(OBJECT_IMAGE_OWL)
    $ audio_portal()
    "As the owl mask begins to fade into view, you feel like the whole character of the light has shifted."
    $ develop_double(5)
    $ zoom_development = True
    pause 3
    show fire explain at dcp, right with Dissolve(.4)
    show owl hips at dcs, xflip, left with Dissolve(.8)    
    flame "Wait. Something is wrong."
    $ audio_portal_melody("siobhan")
    "Shimmering into view on the other side of portal is the figure from your dreams." #the portal language is a hot mess, maybe needs a variable or hardcoded use of the term before optional scenes.
    show porter swear at dcp, center, DoubleRegicide with dissolve
    show fire crossed at dcp
    porter "I am sorry, but she carries too much Brightness. This one remains today."
    show porter listen at dcp
    flame "I see. Of course."
    $ develop_double(10)
    show owl crossed at xflip, dcs
    show fire hips at dcp
    show porter swear at dcp
    "The lumbering thing moves its hand in a strange, purposeful motion."
    show porter listen at dcp
    "As it does so, it's hard to shake the momentary feeling that the spirit is looking at you."
    hide porter listen with dissolve
    "The light flickers and the portal vanishes, along with the spirit."
    show fire show at dcp
    flame "I'm sorry."
    show fire hips at dcp
    show owl scared at xflip, dcs
    owl "..."
    show owl crossed at xflip, dcs
    show fire open at dcp
    flame "Say, how about we go look at some of your recent work?"
    show fire point at dcp
    flame "I was so enchanted with your collage concept from last night."
    show fire explain at dcp
    flame "It's the first thing anyone here has made that feels like it tells the story of THAT world, you know?"
    $ develop_double(15)
    show owl crossed at xflip, dcs
    show fire open at dcp
    flame "It made me think about how both worlds are, really, cousin worlds."
    show fire magic at dcp
    flame "Or, twins, in a way."
    show fire hips at dcp
    show owl scared at xflip, dcs
    owl "I don't think that deeply about it, to be honest. I just go with my gut."
    show owl crossed at xflip, dcs
    show fire show at dcp
    flame "Of course. That's what makes you a great artist."
    show fire hips at dcp
    flame "... Maybe you can help Gunnar with that while you're at it."
    owl "'Too Bright...'"
    show owl open at xflip, dcs
    owl "What does that {i}really{/i} mean?"
    $ develop_double(20)
    show owl crossed at xflip, dcs
    show fire argue at dcp
    flame "I imagine it's because you're simply more open to the truth of that place. Because of your artistic temperament."
    show fire explain at dcp
    flame "It's a good thing."
    show fire hips at dcp
    show owl argue at xflip, dcs
    owl "Is it? Your little butler doesn't seem to think so."
    show owl crossed at xflip, dcs
    show fire open at dcp
    flame "Now that's just uncalled for. No need to be rude."
    show fire hips at dcp
    show owl show at xflip, dcs
    owl "Does that mean you don't know the answer?"
    show owl crossed at xflip, dcs
    show fire explain at dcp
    flame "Why do think I chose the flame as my mask?"
    show fire hips at dcp
    show owl show at xflip, dcs
    owl "Because it's an obvious metaphor?"
    $ develop_double(25)
    show owl crossed at xflip, dcs
    show fire explain at dcp
    flame "Because it's an accurate metaphor."
    flame "Many good things become harmful if you get too close."
    show fire hips at dcp
    owl "Of course."
    show owl open at xflip, dcs
    owl "Sorry for the commentary. It just sucks not going in."
    $ develop_double(30)
    show owl hips at xflip, dcs
    show fire show at dcp
    flame "Let's get some food. Maybe you can tell me more about your thoughts about the Orrery and its Door?"
    show owl hips at dcs
    hide owl point with moveoutleft
    hide fire show with moveoutleft
    "With that, you are left staring at an empty hallway."
    $ reachedEnd = True

label develop_portal_owl_overexposed:
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo right as the stopwatch hits 60 seconds."
    else:
        "If you don't pull the photo out now, it will be overexposed."
    hide owl with moveoutleft
    hide fire with moveoutleft
    $ develop_overexposed(10)
    $ corruption += 5
    $ audio_portal_overexpose()
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the motion in the frame {b}jolt forwards{/b}, as if skipping time."
    "With the frame now empty, only the subtle shifting of the light tells you this photograph is still animate."
    $ develop_overexposed(15)
    $ audio_escalate(1)
    "The colors burn into nothing, slowly making the photo unrecognizable."
    $ develop_overexposed(20)
    "Then, something strange starts to happen."
    $ audio_escalate(2)
    "You start to perceive that in the brightness of the photograph there is a {size=+6}pattern"
    $ develop_overexposed(25)
    $ audio_escalate(3)
    "That your {size=+2}{i}mistake{/i}{/size} has been not making your previous exposures {size=+8}BRIGHT{/size} enough."
    $ develop_overexposed(30)
    "You are struck with the urge to laugh and before you can exert any will in the matter an oddly flat chuckle escapes your lips."
    play sfx_1 "solo-laugh-2.mp3" volume 0.5
    pause 0.2
    $ audio_hard_stop_all()
    "The sound in the empty darkroom is jarring and jolts you back to your senses."
    "You pull out the photo, feeling suddenly uncomfortable."
    jump complete_portal_owl

label complete_portal_owl:  
    $ finish_development()
    $ donePhoto3 = True
    call day2PostPrintDialogue
    jump post_image_completion_daytwo
#endregion

#region photo3 peter/flame
label develop_portal_flame:
    $ start_double_exposing(OBJECT_IMAGE_FLAME)
    $ audio_portal()
    "As your photo develops, the light of the portal flickers and dims."
    "The two robed figures, each wearing the same mask, begin to come to life."
    $ develop_double(5)
    $ zoom_development = True
    pause 3
    show fire point at dcp, right with Dissolve(.4)
    show fire2 hips at dcs, xflip, left with Dissolve(.8)
    $ audio_portal_melody("peter")
    flame "Where did you get that mask?"
    show fire argue at dcp
    flame "Is this some kind of joke?"
    show fire crossed at dcp
    doubFlame "..."
    show fire point at dcp
    flame "Or have I finally gone too far? Unmask, and show me your face!"
    show fire2 open at xflip, dcs
    doubFlame "It's me. You."
    $ develop_double(10)
    show fire crossed at dcp
    show fire2 open at xflip, dcs
    doubFlame "Not as you are, but as you will be."
    show fire2 explain at xflip, dcs
    doubFlame "I'm the one who lives in your house. I am in your skin and your thoughts are my thoughts."
    show fire scared at dcp
    show fire2 hips at xflip, dcs
    flame "Is this another one of those fucking nightmares?"
    $ develop_double(15)
    show fire scared at dcp
    show fire2 hips at xflip, dcs
    flame "Or... are you really here?"
    show fire2 explain at xflip, dcs
    doubFlame "I am not here."
    doubFlame "It will be many years until I am here. Decades."
    show fire2 open at xflip, dcs
    doubFlame "But when the time comes and I am here, it will be by the magic you are about to discover here. This week."
    $ develop_double(20)
    show fire argue at dcp
    show fire2 open at xflip, dcs
    flame "Cut the cryptic bullcrap."
    show fire point at dcp
    flame "Show me who you really are."
    show fire2 point at xflip, dcs
    doubFlame "You change, Peter. You betray your friend, you betray yourself, and you betray your flesh."
    show fire2 point at WhiteNoise, xflip, dcs
    doubFlame "You traded your heart for power, Peter."
    $ develop_double(25)
    show fire scared at dcp
    show fire2 point at WhiteNoise, xflip, dcs
    doubFlame "And now what beats in your chest is a vacancy. A hole."
    doubFlame "And then you begin to hollow out others, trying to fill this hole you have created."
    $ develop_double(30)
    show fire crossed at dcp
    show fire2 point at WhiteNoise, xflip, dcs
    flame "So... so... so what is this, like some kind of warning?"
    $ reachedEnd = True

label develop_portal_flame_overexposed:
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out just as the stopwatch hits 60 seconds."
    else:
        "If you don't pull the photo out now, it will be overexposed."
    $ develop_overexposed(10)
    show fire scared at dcp, dc_overexpose
    show fire2 argue at xflip, dcs, WhiteNoise
    $ corruption += 5
    $ audio_portal_overexpose()
    $ audio_escalate(1)
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    doubFlame "Yes, but not for you."
    $ develop_overexposed(20)
    show fire scared at dcp, dc_overexpose
    show fire2 argue at xflip, dcs, WhiteNoise
    $ audio_escalate(2)
    doubFlame "For the one who watches us."
    if corruption >= 15:
        doubFlame "The one who is {sc=3}Bright"
    else:
        doubFlame "The one who is {sc=2}not yet too Bright."
    $ audio_escalate(3)
    #I want to put more of an ending clue here but need to write that first.
    call corruptionDialogue
    hide flame2
    hide flame
    jump complete_portal_flame

label complete_portal_flame:  
    $ finish_development()
    $ donePhoto3 = True
    "As you pull out the image, it ceases to move."
    "What even was that?!"
    jump post_image_completion_daytwo
#endregion

#region photo3 erin/archer
label develop_portal_archer:
    $ start_double_exposing(OBJECT_IMAGE_ARCHER)
    #This slot gives a HELL of a lot away, almost feels like it should be saved for day3 somehow.
    #This is also set way in the future, I'm leaving it that way for now but it may make more sense to make it happen later
    "You take a deep breath and prepare yourself, focusing intently on the image fading into view."
    $ develop_double(5)
    $ audio_portal()
    $ zoom_development = True
    pause 3
    show fire open at dcp, right with Dissolve(.4)
    show sage crossed at dcs, xflip, left with Dissolve(.8)
    $ audio_portal_melody("erin")
    flame "I'm glad you changed your mind."
    show fire show at dcp
    flame "I'd like to ask why, but I'm afraid it'll only make you run away again."
    show fire hips at dcp
    archer "..."
    flame "Of course, you don't have to say anything."
    show fire explain at dcp
    flame "I have to be honest."
    show fire show at dcp
    flame "When I pulled this little group together, I had no idea what was going to happen."
    flame "Once it all started to go wrong, I felt like I had made a terrible mistake."
    $ develop_double(10)
    show sage crossed at xflip, dcs  
    show fire open at dcp
    flame "Now I see that everything that happened was all in service of something greater."
    flame "So. Here is my guess. After all this time, you've come around to the same conclusion."
    show sage explain at xflip, dcs
    show fire hips at dcp
    archer "That's not it."
    show sage crossed at xflip, dcs
    archer "I wanted nothing to do with what you two had done. Honestly, I still don't."
    show sage scared at xflip, dcs
    archer "But I started having these... terrible, realistic nightmares. About the Porter."
    archer "Started seeing it in real life, started feeling this icy pain that would grip my heart at random times."
    $ develop_double(15)
    show sage explain at xflip, dcs
    show fire hips at dcp
    archer "I spoke to Siobhan. Before she died. She wasn't easy to find, always with one foot in some other world."
    archer "I wanted her to undo what'd she'd done. She didn't listen. She wasn't afraid of the Porter."
    show sage show at xflip, dcs
    archer "I spoke to Gunnar. He was easy enough to find. He doesn't leave his apartment at all anymore, the nurse said."
    show sage open at xflip, dcs
    archer "The walls, the floors, every square inch covered in mad writings. I could read enough to know the dreams were coming for him too."
    $ develop_double(20)
    show sage open at xflip, dcs
    show fire hips at dcp
    archer "So if I'm going to be hounded by some nightmare thing for all the shit you lot got up to..."
    show sage crossed at xflip, dcs
    archer "...I'd like to at least get something out of it."
    flame "I understand that logic. I'm a bit disappointed that an artist such as yourself has such a... selfish perspective."
    show fire open at dcp
    flame "We all meet out end eventually. What matters is what we {b}create{/b} along the way."
    flame "But, that doesn't matter. All that matters is that you are here now."
    show fire magic at dcp
    "The figure in the flame mask makes a gesture and something is drawn through the portal."
    show porter dead weyes at center, dcp, DoubleRegicide with Dissolve(1)
    flame "So..."
    flame "What will you take into yourself?"
    $ develop_double(25)
    show sage crossed at xflip, dcs
    show fire hips at dcp
    show porter dead weyes at center, dcp, DoubleRegicide
    archer "..."
    archer "I want its eyes."
    flame "Done."
    show fire magic at dcp
    "The flame-masked figure makes a gesture."
    show porter dead weyes at center, dcp, magic_strike, EyeGlow
    "Yellow light begins to form around the Porter's eyes."
    "The flame-masked figure snaps their fingers."
    $ play_crunch()
    show porter dead at center, dcp, magic_strike, DoubleRegicide
    flame "Done."
    $ develop_double(30)
    show sage open at dcs, EyeGlowSage
    show fire magic at dcp
    show porter dead at center, dcp, DoubleRegicide
    "Then, the eyes of the sage mask begin to glow."
    "The brightness lingers for a moment. Then it begins to disappear."
    show sage crossed at xflip, EmergencyReset
    "Almost as if it is being sucked into the mask..."
    $ reachedEnd = True

label develop_portal_archer_overexposed:    
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out just in time - perfectly exposed."
    else:
        "If you don't pull the photo out now, it will be overexposed."
    $ develop_overexposed(10)
    show sage crossed at dcs, dc_overexpose
    show fire magic at dcp, dc_overexpose
    show porter dead at center, dcp, DoubleRegicide, dc_overexpose
    $ corruption += 5
    $ audio_portal_overexpose()
    $ audio_escalate(1)
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    flame "What do you see?"
    archer "bright"
    $ develop_overexposed(15)
    show sage crossed at dcs, dc_overexpose
    show fire magic at dcp, dc_overexpose
    show porter dead at center, dcp, DoubleRegicide, dc_overexpose
    $ audio_escalate(2)
    archer "BRIGHT"
    archer "And I see..."
    $ develop_overexposed(20)
    show sage crossed at dcs, dc_overexpose
    show fire magic at dcp, dc_overexpose
    show porter dead at center, dcp, DoubleRegicide, dc_overexpose
    $ audio_escalate(3)
    archer "I see a way out."
    call corruptionDialogue
    jump complete_portal_archer

label complete_portal_archer:  
    $ finish_development()
    $ donePhoto3 = True
    call day2PostPrintDialogue
    jump post_image_completion_daytwo
#endregion

#region photo3 gunnar/Frog
label develop_portal_frog:
    $ start_double_exposing(OBJECT_IMAGE_FROG)
    "You stare intently, aware of the eerie quiet of the darkroom. A quiet you know will soon be filled with voices."
    $ develop_double(5)
    $ zoom_development = True
    $ audio_portal()
    pause 3
    show fire crossed at dcp, right with Dissolve(.4)
    show frog explain at dcs, xflip, left with Dissolve(.8)
    $ audio_portal_melody("gunnar")
    "As expected, the two robed figures begin to move and speak."
    "But there is another figure, visible faintly through the portal."
    show porter dead weyes at dcp, center, DoubleRegicide with Dissolve(1)
    frog "I can't believe that worked!"
    show frog open at dcs, xhack
    frog "That was incredible, Peter. You're a genius, a true genius!"
    "Peter, if that who it is, stares blankly at the Porter."
    $ develop_double(10)
    show porter dead weyes at dcp
    show frog hips at dcs, xhack
    show fire crossed at dcp
    flame "Can you hear me?"
    porter "..."
    show fire scared at dcp
    flame "What did she do to you?"
    show frog explain at dcs, xhack
    frog "I told you, she took its power. I would have stopped her if I had known what she was doing."
    show fire crossed at dcp
    frog "I don't understand this stuff the way you do, or the way she did."
    flame "Quiet."
    show frog open at dcs, xhack
    frog "If we're going to do this, Peter..."
    show frog hips at dcs, xhack
    show fire scared at dcp
    flame "I wish we knew where she went."
    $ develop_double(15)
    show porter dead weyes at dcp
    show frog open at dcs, xhack
    show fire crossed at dcp
    frog "You think she's even in this world? Even in the Bright House? She could be anywhere."
    show frog show at dcs, xhack
    frog "A few simple gestures not just from the Bright House, but from the Garden, from..."
    frog "Hell, Peter, I wonder if you even know what else could be out there."
    show frog hips at dcs, xhack
    show fire explain at dcp
    flame "This feels wrong."
    show fire crossed at dcp
    show frog explain at dcs, xhack
    frog "If you want to find her, you won't find her without {sc=2}power{/sc} of your own."
    show frog open at dcs, xhack
    frog "As for me, I just want to write."
    frog "I was so close to something great, Peter. Isn't that all you wanted to come out of this? Something truly great for humanity?"
    show frog show at dcs, xhack
    flame "..."
    $ develop_double(20)
    show porter dead weyes at dcp
    show frog hips at dcs, xhack
    show fire open at dcp
    flame "Alright. Hand me the stone."
    show frog explain at dcs, xhack
    "The frog passes a small, dark object to Peter, who grips it in his left palm."
    show frog hips at dcs, xhack
    show fire magic at dcp
    "He then traces some kind of design over his chest."
    show porter dead weyes at dcp, magic_strike, HeartGlow
    "Holding out both hands, a yellow glow appears in the chest of the spirit."
    show fire magic at dcp, HeartGlowPeter
    "The light forms an almost imperceptible thread connecting Peter's chest with the Porter's."
    $ develop_double(25)
    $ play_crunch()
    show porter dead weyes at dcp, magic_strike, EmergencyReset
    show frog hips at dcs, xhack
    show fire magic at dcp
    flame "Ah."
    flame "It burns."
    show frog scared at dcs, xhack
    frog "Holy hell..."
    show frog show at dcs, xhack
    show fire crossed at dcp
    frog "Are you alright?"
    show fire scared at dcp
    "The figure with the flame mask does not move, for a moment."
    flame "Yes."
    show fire open at dcp, magic_strike, EmergencyReset
    flame "It is done."
    flame "Your turn."
    show frog hips at dcs, xhack
    flame "Take what you will from this husk."
    $ develop_double(30)
    $ reachedEnd = True

label develop_portal_frog_overexposed:
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out just in time."
    else:
        "If you don't pull the photo out now, it will be overexposed."
    $ develop_overexposed(10)
    $ corruption += 5
    $ audio_portal_overexpose()
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    show porter dead weyes at center, dcp, dc_overexpose
    show frog hips at left, dcs, dc_overexpose
    show fire open at right, dcp, dc_overexpose
    $ audio_escalate(1)
    frog "How... how does it feel?"
    flame "I can feel its power."
    $ develop_overexposed(15)
    show porter dead weyes at center, dcp, dc_overexpose
    show frog hips at left, dcs, dc_overexpose
    show fire open at right, dcp, dc_overexpose
    frog "What should it be?"
    $ develop_overexposed(20)
    show porter dead weyes at center, dcp, dc_overexpose
    show frog hips at left, dcs, dc_overexpose
    show fire open at right, dcp, dc_overexpose
    frog "Do words live in the tongue? Or the mind? Do I want to see what is in that mind? Could I even comprehend it?"
    $ audio_escalate(2)
    flame "{size=+10}FOOL{/size}."
    $ develop_overexposed(25)
    show porter dead weyes at center, dcp, dc_overexpose
    show frog hips at left, dcs, dc_overexpose
    show fire open at right, dcp, dc_overexpose
    flame "{size=+7}IT MATTERS NOT{/size}."
    $ audio_escalate(3)
    flame "{size=+7}ALL WILL BE RETURNED{/size}."
    $ develop_overexposed(30)
    show porter dead weyes at center, dcp, dc_overexpose
    show frog hips at left, dcs, dc_overexpose
    show fire open at right, dcp, dc_overexpose
    flame "{size=+15}ALL MUST BE RETURNED{/size}"
    call corruptionDialogue
    jump complete_portal_frog

label complete_portal_frog:  
    $ finish_development()
    $ donePhoto3 = True
    call day2PostPrintDialogue
    jump post_image_completion_daytwo
#endregion
#endregion

#region end of day 2

label endOfDay2:
    "That's it. You're out of paper."
    if corruption >= 20:
        "You feel a twinge of sadness. You weren't ready to be done with this..."
    "You collapse in Erin's chair, thoughts swirling."
    "Trying to make sense of the events you've seen. To piece together the timeline."
    "You can't be sure that everything you've seen is real, or {i}was{/i} real, but at the same time it almost adds up."
    play sound "text-vibrate.mp3" volume 0.6
    "Your phone buzzes. It's Bud. They're outside."
    show darkroom_workspace bright
    $ play_darkroom_light_off()
    show buddy question with moveinleft
    play photo_1 '<loop 20>piano-underscore-spook-1.mp3' volume 0.1
    bud "So I looked into Peter Carlson..."
    show buddy angry
    bud "Um, it got weird."
    show buddy question
    bud "So he's the guy who runs this foundation."
    show buddy confused
    bud "Turns out he's been involved with a few other art organizations as well."
    show buddy sad
    bud "The former 'Siobhan Kent Young Artist Grant,' for example."
    show buddy sus
    bud "That one's shut down now. A lot of the recipients, uh, seem to have died or disappeared.."
    show buddy question
    bud "Same for the  'Gunnar Olsen Young Poet Award' winners."
    if porterKnown == True:
        show buddy talkhand
        bud "I didn't have a lot of luck looking up any kind of a spirit called the Porter."
        show buddy think
        bud "That's probably just because like, where the hell do you even start with something like that?"
        show buddy talkhand
        bud "But it did come up in some of Gunnar's unfinished works. And the works of the poet award winners."
        show buddy confused
        bud "It's either some sort of like, vengeful killer or some sort of guardian angel."
        show buddy sus
        you "That's super helpful..."
        show buddy laughs
        bud "Right?"
    show buddy listen
    you "Bud... did you have any nightmares last night?"
    show buddy question
    bud "Kinda, yeah, actually."
    show buddy disgust
    bud "I kept dreaming of these chopped up body parts and like, all these different creatures pecking at them."
    bud "This owl was eating someone's hand and then there was this mustached guy just like, watching it all from the woods." #NOTE: ARCHER REFERENCE
    show buddy angry
    bud "Oh god, then mustache man ate the heart!? Damn, I almost forgot how messed up it was."
    show buddy confused
    bud "How did you know?"
    show buddy listen
    you "I had one too. About the Porter."
    you "I don't know what Peter's game is here, but I think we need to get out of all of this."
    show buddy question
    bud "So we just quit?"
    show buddy sad
    bud "..."
    show buddy disgust
    bud "It's too late for that, isn't it?"
    "You fill Bud in on everything you've seen."
    show buddy sad
    "Bud sighs."
    show buddy question
    bud "I feel crazy."
    show buddy talkhand
    bud "Like, this is starting to make sense, but where the hell do we fit in?"
    show buddy sad
    you "I think the spirit wants something from us."
    show buddy listen
    you "In my dream, it showed me where to find some photos. Photos that Erin, or someone, had hidden."
    show buddy question
    bud "Yeah but like, it showed me all these random body parts getting ripped apart."
    show buddy listen
    you "It talked to me about body parts as well..."
    show buddy sus
    you "A heart, a hand, a tongue, and eyes."
    bud "..."
    show buddy think
    bud "Can I see that photo you found again?"
    play audio "slides/remove-2.mp3"
    show porter photo erin:
        zoom .9
        xalign 0.0
        yalign 0.5
        rotate 1.5
    bud "Look at the exposure. Erin's face over the Porter's face."
    bud "Why would Erin do that?"
    bud "Her eyes over its eyes."
    bud "This isn't a coincidence."
    hide porter photo erin
    #show buddy amused
    #bud "Oh. Now {i}that{/i} is interesting."
    #show buddy question
    #bud "In the negative here, the spirit has no eyes..."
    #bud "But in your dream, it did, right?"
    #show buddy listen
    #you "Yeah."
    #bud "..."
    #show buddy talkhand
    show buddy question
    bud "I think we need to find the original negative of this photograph."
    show buddy sus
    bud "Do you think it could be hidden somewhere here?"
    show buddy listen
    you "We should look!"
    play photo_2 'piano-underscore-spook-2.mp3' volume 0.5
    "Your search the other day was quick. As the photos hidden behind the picture frame made clear, you hadn't done a truly deep search."
    stop ambiance_1 fadeout 2.0
    stop ambiance_2 fadeout 2.0
    stop ambiance_3 fadeout 2.0
    scene darkroom_workspace bright with Fade(.7, .5, .4)
    "The hours go by. The sun sets. There's so much stuff - not just in the studio, but in the rest of the house - that you realize this could take all night."
    show buddy question
    bud "Hey, I gotta get some sleep. I'm going to be totally dead tomorrow otherwise."
    show buddy amused
    bud "But I'll come by first thing in the morning?"
    show buddy listen
    "You nod and thank Bud for their help."
    hide buddy with dissolve
    "You're pretty tired as well."
    play sfx_1 "slides/remove-2.mp3"
    "Before you go, you grab all the prints you took today and shove them in your bag."
    jump night2
#endregion

#region night2
label night2:
    scene bg bedroom light with Dissolve(1)
    pause .3
    stop photo_1 fadeout 4
    stop photo_2 fadeout 4
    "The fear of the dreams keeps you up for a while..."
    $_window_show()
    show bg bedroom sleep with dissolve
    call night_crickets
    "But sometime around two in the morning, sleep finds you."
    call nightmare_start
    show bg nightmare:
        RaveLights
    with Dissolve(2.0)
    "And so do the dreams."
    call nightmare_porter_appear
    pause 1.2
    show porter dead:
        yalign .03
        xalign .5
    with moveinbottom
    stop ambiance_3 fadeout 4.0
    play nightmare_2 ["porter-drums-1.mp3"] fadein 6 volume 1
    if corruption >= 25: #high
        porter "..."
        porter "i see now you are already {sc=4}BRIGHT{/sc}"
        porter "but that does not mean it is too late to RIGHT what is {sc=4}WRONG"
        porter "like the {sc=4}SAGE DID{/sc}. she returned my eyes, and was so freed"
    elif corruption >=15:
        porter "you are {sc=4}SO BRIGHT{/sc} that I fear you are {sc=4}NEARLY LOST"
        porter "you have little time before it is too late"
        porter "like the {sc=4}SAGE{/sc} was. she undid her wrong and returned my eyes, but it was too late for her"
    else:
        porter "you are not yet {sc=4}SO BRIGHT{/sc} as to be {sc=4}LOST{/sc}"
        porter "but if you are not quick, you will be soon"
        porter "like the {sc=4}SAGE{/sc} was. she undid her wrong, but it was too late for her"
    porter "now you know their {sc=4}TRANSGRESSION{/sc}"
    porter "until it is {sc=2}UNDONE{/sc}..."
    porter "undone in {sc=3}FULL{/sc}..."
    porter "you will not rest"
    $_window_hide()
    play audio "porter-single-voice-higher.mp3" volume 0.2
    show porter dead at ZoomInto:
        WhiteNoise
    pause 1.1
    play sfx_1 "low-thud-single.mp3"
    scene darkroom_workspace bright:
        WhiteNoise
        matrixcolor BrightnessMatrix(-0.7)
    show peter old speak:
        size(402, 540)
        xalign .44
        yalign .3
        ysize .3
        #crop(0, 0, 402, 540)
        fit("contain")
        matrixcolor TintMatrix("#171717")
    with Fade(0.1,0.0,0.5,color="#cdc4c4ff")
    pause .6
    play nightmare_3 ["<sync nightmare_2>porter-drums-2.mp3", "porter-drums-2.mp3"] fadein 2 volume 0.8
    play drone_3 "bass-drone-2.mp3" volume 1 fadein 2
    porter "{sc=4}HE{/sc} has the final piece"
    porter "{sc=4}HE{/sc} is there now"
    show bg nightmare
    play ambiance_1 "heartbeat.mp3" volume 1 fadein 2
    porter "You must GO NOW"
    play sfx_1 "guitar-Ab.mp3"
    play sfx_2 "gong-1.mp3"
    play audio "porter-wail.mp3"
    play ambiance_3 "crickets-1.mp3" volume 0.05 fadein 2 loop
    pause 1.3
    show bg nightmare:
        size(1920, 1080) crop (0, 0, 1920, 1080)
        linear .8 crop(1130, 310, 360, 240)
    porter "{size=+20}NOW!!{nw=.6}"    
    scene bg bedroom light with flash
    call nightmare_stop
    "You wake up and your body is already halfway out of bed."
    "You throw on clothes, send a quick text to Bud, and rush out the door."
    call night_crickets_stop
    jump day3Start
#endregion
