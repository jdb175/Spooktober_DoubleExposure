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

#region start of day 2
label day2Start:
    stop music fadeout 2.0 
    stop ambiance_1 fadeout 2.0
    stop ambiance_2 fadeout 2.0
    stop ambiance_3 fadeout 2.0
    #Note: I have no idea what BG this should be. We probably just have to make it the darkroom.
    "You wake up feeling like you've hardly slept at all."
    play sound "text-vibrate.mp3" volume 0.4
    "Grabbing your phone, you see a text from Bud."
    window hide
    scene bg bedroom light
    $ reset_phone_data()
    $ phone_start()
    show screen phone_ui with dissolve
    $ switch_channel_view("bud_dm")
    $ lock_phone_screen()
    if budLevel == 0:
        $ send_phone_message("Bud", "yo sorry to bother you", "bud_dm")
        $ send_phone_message("Bud", "but could i come by the darkroom today?", "bud_dm")
    else:
        $ send_phone_message("Bud", "Hey can  come by the darkroom?", "bud_dm")
    window hide
    $ send_phone_message("Bud", "had a weird day yesterday and learned some weird stuff you might be interested in", "bud_dm")
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
    show buddy question with moveinleft
    bud "So I kept thinking about like, my piece, what I was going to do."
    show buddy talkhand
    bud "I think I told you I was thinking of doing something like, on her disappearance, like what happened to her."
    show buddy sad
    bud "But then I decided that would probably be seen as kinda trashy."
    show buddy question
    bud "So I was looking at her life as a whole, maybe something about that."
    show buddy amused
    bud "And discovered she'd dedicated one of her pieces to this artist I'd never heard of. Siobhan Kent"
    show buddy question
    bud "Mixed media artist. A lot of similar themes."
    show buddy talkhand
    bud "But there was not really any record of them interacting or anything, you know? Like, they never did a showing together."
    show buddy sad
    bud "Here's the crazy part. Siobhan? {i}Disappeared.{/i} A few months before Erin did." #same day? What's better for us?
    show buddy talkhand
    bud "So... it begs the question, how did they know each other?"

label day2BudConvo:
    show buddy listen
    menu:
        set menuset
        "I thought you said you weren't going to do something on her disappearance":
            show buddy question
            bud "I wasn't! I swear! I was looking for just, you know, generic inspiration!"
            jump day2BudConvo
        "I think I know how they knew each other":
            show buddy question
            bud "Oh shit, really?"
    show buddy listen
    you "They were both in some sort of... magical organization? Cult?" #Ugh I hate how this scene makes overexplaining hard to avoid
    if peterKnown == True:
        you "Run by this guy Peter Carlson" #keep double checking what info is given at this point
    else:
        you "Run by some guy named Peter."
    if porterKnown == True:
        you "Working with, or using, or calling upon, some sort of spirit called the Porter."
    if houseKnown == True:
        you "They had plans to go {i}through{/i} something or {i}to{/i} something. Some other place."
    else:
        you "They were planning to {i}do{/i} something together. I don't really know what."
    show buddy sad
    bud "..."
    if budLevel <= 5:
        bud "..."
        show buddy question
        bud "Okay, fine, I get it. You think I'm crazy."
    else:
        bud "..."
        show buddy laughs
        bud "Are you serious? That's... absolutely wild!"
    you "I am being completely serious."
    show buddy question
    bud "How could you know all of that?"
    #Stretch goal is make this a choice, create a second route.
    show buddy listen
    "This is way too much to keep all to yourself. You decide to tell Bud everything."
    "Any fear you had that the story would be too strange to believe evaporates instantly."
    show buddy talkhand
    "They're hanging on to your every word."
    bud "You have to show me."
    #FIX: this doesn't work 100%, you need to make the choice to try other photo paper earlier manditory
    show buddy listen
    you "I would, but there's no more photo paper."
    if corruption >= 10:
        you "Besides, I... think it might be dangerous."
        "Bud's eyes go wide, but they don't say anything."
    if peterKnown == True:
        show buddy question
        bud "Okay, well, I guess in the meantime I should look up this uh, Peter Carlson"
    else:
        show buddy question
        bud "Okay, well, I guess in the meantime I should look up this, uh, Peter guy"
    if porterKnown == True:
        show buddy talkhand
        bud "And some sort of spirit called a Porter?"
    if gunnarKnown:
        show buddy listen
        you "Look up someone named Gunnar too. I think they're famous. Possibly a writer?"
    show buddy question
    bud "Okay, yeah, I'll try."
    show buddy tricky
    bud "This is fucking crazy"
    show buddy talkhand
    bud "I'll come by later? Or call you if anything super interesting comes up."
    if corruption >= 10:
        show buddy sad
        bud "... be careful."
    hide buddy with moveoutleft
    "As Bud leaves, you start to think about your next move."
    "As you gaze around the room, two things catch your eye."
    jump day2_darkroom
#endregion

#region darkroom
label day2_darkroom:
    scene darkroom_workspace bright
    menu:
        set menuset
        "The desk":
            "Sitting nearly on the corner of the desk is a small package, with a note on it."
            "{font=NothingYouCouldDo-Regular.ttf}'Forgot to drop these off yesterday. Some addit'l of Erin's items, in case they're of interest'" #handwriting
            "Must be from the grant?"
            "You open the package and discover another small, hand-wrapped package of photo paper. The same paper you used last night."
            "And there's more of it this time - five whole sheets." #NOTE: this being hardcoded is a challenge if we change it.
            if photoFirst == True:
                jump day2_print
            else:
                $ paperFirst = True
                jump day2_darkroom
        "The photo on the wall":
            "In your dream you saw a photo hanging on the wall."
            show bg painting with Dissolve(1)
            "You hadn't really clocked it yesterday, but you see it today, just where it was in your dream."
            "You take it down and look at it for a little while. It is a print from one of Erin's last series - 'seen.'"
            show mask double exposure with Dissolve(1)
            "The whole series was like this - various masks, shown in a presentational style. You never liked this one. Something about it felt unsettling."
            hide mask double exposure with dissolve
            "You ponder the image for a minute before turning it over."
            show bg painting back with dissolve
            "On a hunch, you pull off the back of the frame. Tucked inside is a strip of photo negatives."
            "Most of the images appear to be the original negatives from 'seen' itself - four masks in all."
            "For a moment, you forget the strange circumstances you are in - it's a rush seeing an original negative from Erin"
            "Two of the images, however, appear not to be art at all."
            "Candid photographs of strange figures in robes."
            #"Most of the images are totally ruined, but it does look like there are a few near the end that are relatively untouched."
            if paperFirst == True:
                jump day2_print
            else:
                $ photoFirst = True
                jump day2_darkroom
#endregion

#region projector basics
label day2_print:
    $ begin_day(Days.DAY_TWO)
    $ onFirstBase = True #changes dialogue in select double
    scene darkroom_workspace bright
    "With these negatives, and more paper, you realize you have a chance to learn more about what is really going on."
    "You of course have some doubts - whatever forces you are playing with you don't understand."
    "And this paper being here is... suspicious..."
    show darkroom_workspace red
    if corruption >= 15:
        "But you find your heart quickening at the thought of seeing these photos come to life again"
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
    if onFirstBase == True:
        "You grab your tongs and pull out the photo."
        "Then, you make your way to the enlarger."
        "You're eager to see what you might be able to learn from these negatives you found."
        $ onFirstBase = False
    else:
        "You grab your tongs and pull out the photo."
        if corruption <= 15:
            "Then it's back to the enlarger, ready to see what the next negative might reveal..."
        else:
            "Then it's back to the enlarger. You're already thinking of the next negative, what kind of beautiful imagery it could create..."
            "No, wait, this is about learning, not creating... Right?"
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
    "'It' begins to happen again..."
    #NOTE: Add "if seen this photo already" code in once we standardize how it works.
    if donePhoto2:
        "You could watch it all play out once more, or you could just pull it out as soon as possible"
        menu:
            "Watch it all again":
                $ donePhoto2 = False
            "Pull it out":
                $ develop (30)
                "The same little pagent plays out, but your eyes are on the clock."
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
    unk "Peter knows far more than me, and whatever you think you may have picked up these last few days, more than you too."
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
    owl "So keep stringing things along, if you'd like. Delaying every decision"
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
    "The image is getting darker now, becoming overdeveloped"

label develop_sneaky_overexposed:
    $ renpy.block_rollback()
    $ develop_overexposed(5)
    $ corruption += 5
    show owl crossed at xflip, dcp, dc_overexpose
    owl "Soon we will transgress"
    owl "Soon, the bright will spill"
    $ develop_overexposed(10)
    show owl crossed at xflip, dcp, dc_overexpose
    owl "The guardian, the warden, the Porter will fall"
    $ develop_overexposed(15)
    show owl magic at xflip, dcp, dc_overexpose
    owl "BUT HE SHALL RETURN"
    $ develop_overexposed(20)
    show owl magic at xflip, dcp, dc_overexpose
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    jump complete_sneaky

label complete_sneaky:  
    $ finish_development()
    $ donePhoto2 = True
    "As you pull out the image, it ceases to move."
    "Your heart, however, continues to beat quickly."
    if corruption >= 15:
        "Should you be more careful with these forces?"
    jump post_image_completion_daytwo

#region sneaky siobhan/owl
label develop_sneaky_owl:
    $ start_double_exposing(OBJECT_IMAGE_OWL)
    "As your photo develops, you heart begins to quicken, almost uncontrollably."
    $ zoom_development = True
    pause 3
    show owl point at dcp, xflip, left with Dissolve(.4)
    show owl2 point at dcs, right with Dissolve(.8)
    "The two robed figures, each wearing the same mask begin to speak."
    $ develop_double(5)
    show owl point at dcp, xflip, left with Dissolve(.4)
    show owl2 point at dcs with Dissolve(.8)
    doubOwl "..."
    owl "Is this some kind of joke?"
    owl "Who are you?"
    owl "Why are you wearing my mask?"
    $ develop_double(10)
    show owl point at dcp, xflip, left with Dissolve(.4)
    show owl2 point at dcs with Dissolve(.8)
    doubOwl "..."
    doubOwl ".........."
    $ develop_double(15)
    show owl point at dcp, xflip, left with Dissolve(.4)
    show owl2 point at dcs with Dissolve(.8)
    owl "I'm not fucking around here, okay? Take off your mask! Who are you?"
    owl "Or is this another one of those nightmares??"
    show owl2 point:
        dcs
        WhiteNoise
    doubOwl "This corruption of the truth should not be possible."
    doubOwl "You have strayed beyond your limits, human."
    $ develop_double(20)
    show owl point at dcp, xflip, left with Dissolve(.4)
    show owl2 point at dcs, right with Dissolve(.8)
    doubOwl "Given a gift, you were unsatisfied."
    doubOwl "Your hunger is your unmaking"
    hide owl2 with Dissolve(.2)
    show porter temp:
        dcs
        yalign .01
        xalign .9
        xzoom -1
        WhiteNoise
    with Dissolve(.5)
    $ develop_double(25)
    porter "{sc=2}Your judgement was made long ago, transgressor.{/sc}"
    owl "This isn't... this isn't possible."
    $ develop_double(30)
    owl "When is this? When is this happening?"
    owl "{size=+4}We haven't even killed you yet! I have no hand to give you!!"
    $ reachedEnd = True

label develop_sneaky_owl_overexposed:
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out at the perfect time"
    else:
        "You know that if you keep this photo in any longer you will overexpose it"
    $ develop_overexposed(10)
    show owl2 at dcp, dc_overexpose
    show porter temp:
        dcs
        yalign .01
        xalign .9
        xzoom -1
        WhiteNoise
    $ corruption += 5
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    porter "{sc=2}This cannot be understood. And it will end.{/sc}"
    $ develop_overexposed(20)
    show owl2 at dcp, dc_overexpose
    porter "{sc=2}NOW{/sc}"
    $ develop_overexposed(30)
    show owl2 at dcp, dc_overexpose
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
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
    "You watch with curiosity as the photo begins to move, the masked figures begin their speech"
    $ zoom_development = True
    pause 3
    show owl point at dcp, xflip, left with Dissolve(.4)
    show flame argue at dcs, right with Dissolve(.8)
    "This time, the figure in the owl mask does not seem to want to talk."
    show owl point at dcp
    pause .1
    hide owl with moveoutleft
    "They hurry into the shadows, as if they do not want to be seen."
    $ develop_double(5)
    show flame argue at dcs
    flame "What are you doing sneaking around in the dark?"
    flame "I've already seen you, Siobhan." #this may be too much? But I think Peter would say it.
    show owl point at dcp, xflip, left with moveinleft
    with moveinright
    $ develop_double(10)
    show flame argue at dcs
    show owl point at xflip, dcp
    flame "Do you think I didn't notice someone has been going through my papers?"
    flame "I had very much hoped to catch you in the act."
    flame "But I didn't expect to catch you trying to sneak into the Bright House on your own."
    flame "Well? Speak."
    owl "I don't know what you think I'm doing, or what you think I've done."
    owl "But I do know you've been keeping a lot of secrets from us."
    $ develop_double(15)
    show flame argue at dcs
    show owl point at xflip, dcp
    flame "I've said many times that as we continue to explore together, I will share more of what I know."
    flame "That is entirely because I wanted to ensure I was working with people I could trust."
    flame "And here you are, living proof that I was right to be cautious."
    owl "I think you like holding all the power, stringing us along."
    owl "I think you want to keep the Bright House all to yourself."
    $ develop_double(20)
    show flame argue at dcs
    show owl point at xflip, dcp
    owl "You're only sharing it because of your own inability to understand it."
    flame "Don't be stupid! You had so much you could have gained from this!"
    flame "Your art, your insight, your abilities, in just a few days you have grown more than you might in months of toil!"
    flame "This is the light of creativity itself."
    flame "And now it will be shut to you forever."
    $ develop_double(25)
    show flame argue at dcs
    show owl point at xflip, dcp
    flame "I have summoned the Porter and told it that you summon it with stolen magic. That you intend to use to transgress its boundries"
    flame "It will open no more doors for you."
    $ develop_double(30)
    show flame argue at dcs
    show owl point at xflip, dcp
    flame "Now, get your things and leave my home."
    $ reachedEnd = True

label develop_sneaky_flame_overexposed:
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out at the perfect time"
    else:
        "You know that if you keep this photo in any longer you will overexpose it"
    $ develop_overexposed(10)
    show flame argue at dcs, dc_overexpose
    show owl point at xflip, dcp, dc_overexpose
    $ corruption += 5
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    flame "Your time here is done, Siobhan. In this house, and the Other."
    $ develop_overexposed(15)
    show flame argue at dcs, dc_overexpose
    show owl point at xflip, dcp, dc_overexpose
    owl "Blind in art, blind in all things but money."
    owl "BLIND TO THE DEPTHS OF MY TREACHERY"
    $ develop_overexposed(20)
    show flame argue at dcs
    show owl point at xflip, dcp, dc_overexpose
    owl "THE {sc=4}HAND{/sc} OF THE PORTER DRAWS THE DOORS"
    owl "THE DOORS ARE DRAWN BY THE {sc=4}HAND{/sc}."
    $ develop_overexposed(25)
    show flame argue at dcs
    show owl point at xflip, dcp, dc_overexpose
    owl "{sc=4}GIVE ME BACK MY HAND{/sc}!"
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    hide owl
    hide flame
    jump complete_sneaky_flame

label complete_sneaky_flame:  
    $ finish_development()
    $ donePhoto2 = True
    if photoRuined == True:
        "You pull out the wrecked photograph."
        "You suspect that you heard many useful things which were meant to be kept secret..."
    else:
        "You pull out the print, a bizarre image you suspect no one was meant to see."
        "A conversation which, certainly, no one was meant to hear."
    jump post_image_completion_daytwo
#endregion

#region sneaky erin/archer
label develop_sneaky_archer:
    #This scene needs more information
    $ start_double_exposing(OBJECT_IMAGE_ARCHER)
    "From the strange masked figures, you see faint movement and hear whispers, growing stronger, growing bolder."
    $ zoom_development = True
    pause 3
    $ develop_double(5)
    show owl point at dcp, xflip, left with Dissolve(.4)
    show sage base at dcs, right with Dissolve(.8)
    owl "Oh!"
    owl "It's... what are you doing here?"
    archer "I could ask you the same question."
    owl "I've been taking walks at night. Trying to, basically process everything we've seen in the Bright House."
    owl "I find wearing the costume helps me remember. Stupid as they are."
    owl "Because it's like, after that first day. When I came back through. It all made so much sense."
    owl "I could see the threads connecting {b}there{/b} to {b}here{/b}."
    owl "I felt like I'd just taken a tour backstage at a play I'd seen a thousand times."
    owl "But it fades so fast, doesn't it?"
    $ develop_double(10)
    show owl point at xflip, dcp
    show sage base at dcs
    archer "It does."
    archer "I think it's meant to. Or, I think we're not meant to understand."
    owl "Oh, that's definitely what {i}they{/i} think. Peter and his freaky little dog. Keeping tabs on us. Telling us where we can and can't go."
    archer "I don't know. I think there's a reason for that."
    archer "Although what do I know. I envy you. Your recent work has been... incredible. I don't know how to describe it."
    archer "But it feels like I can see a bit of that place when I look at it."
    owl "Who knows if anyone else will. Every piece I make just immediately feels like it's shit. Like it's so far from what I meant."
    $ develop_double(15)
    show owl point at xflip, dcp
    show sage base at dcs
    owl "But don't you think if you could just get a little further you could figure it out? If you feel stuck too, well, there's answers deeper for you, aren't there?"
    owl "Maybe not for poor Gunnar. I looked in his notebook. It's like the shining, writing the same sentence over and over again."
    owl "Not literally, like, he's not crazy. I don't think. But it's just first sentence, second sentence, cross it out."
    owl "I liked your kitchen thing. I think you're better at this than you think. The idea of using the masks is cool too. Not sure what Peter will think."
    archer "See? This is what I mean. I think my art sucks, you think your art sucks, but to the outside world it's good."
    owl "Maybe..."
    $ develop_double(20)
    show owl point at xflip, dcp
    show sage base at dcs
    owl "..."
    owl "Do you really trust Peter and that... creature?"
    archer "I don't know. I trust him not to get us killed or anything."
    archer "But I still don't feel like I understand what he's trying to do. Or why that spirit helps him."
    archer "I'm debating doing what you did..."
    archer "Trying to read some of Peter's notes and stuff."
    $ develop_double(25)
    show owl point at xflip, dcp
    show sage base at dcs
    owl "Yeah. Me too."
    owl "..."
    owl "I wonder where he keeps his... you know, his spells and stuff."
    owl "I wonder if we could find those too."
    archer "I think that's a bad idea."
    owl "Yeah, you're probably right."
    $ develop_double(30)
    $ reachedEnd = True

label develop_sneaky_archer_overexposed:
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out at the perfect time"
    else:
        "You know that if you keep this photo in any longer you will overexpose it"
    $ develop_overexposed(10)
    show owl point at xflip, left, dcp, dc_overexpose
    show sage base at dcs, right, dc_overexpose
    $ corruption += 5
    $ photo_ruined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    #This is crappy because it gives you no clues and maybe even throws you down an incorrect path.
    owl "... wait, you never answered me. What {i}are{/i} you doing out here? Dressed in your portal robes??"
    archer "Oh."
    archer "I... I don't know."
    archer "Wait, how could I possibly {i}not know{/i}?"
    $ develop_overexposed(15)
    show owl point at xflip, dcp, dc_overexpose
    show sage base at dcs, dc_overexpose
    archer "I was walking at night, but I don't remember putting on my mask. My robes."
    archer "{size=+2}Did I really do that{/size}?"
    $ develop_overexposed(20)
    show owl point at xflip, dcp, dc_overexpose
    show sage base at dcs, dc_overexpose
    archer "{size=+5}HOW MUCH OF THIS IS REAL{/size}?"
    $ develop_overexposed(25)
    show owl point at xflip, dcp, dc_overexpose
    show sage base at dcs, dc_overexpose
    archer "{size=+10}IS ANY OF THIS REAL{/size}??"
    jump complete_sneaky_archer

label complete_sneaky_archer:  
    $ finish_development()
    $ donePhoto2 = True
    if photoRuined == True:
        "You pull out the wrecked photograph."
        "You suspect that you heard many useful things which were meant to be kept secret..."
    else:
        "You pull out the print, a bizarre image you suspect no one was meant to see."
        "A conversation which, certainly, no one was meant to hear."
    jump post_image_completion_daytwo
#endregion

#region sneaky gunnar/frog
label develop_sneaky_frog: #This scene is hella long but needs to be...
    $ start_double_exposing(OBJECT_IMAGE_FROG)
    "While it's clear that this photo wasn't taken to be a piece of art, there's an incredible energy you feel watching the masked figures shiver to life."
    "Like you are stealing a glimpse at some great secret."
    $ zoom_development = True
    pause 3
    $ develop_double(5)
    show owl point at dcp, xflip, left with Dissolve(.4)
    show frog explain at dcs, right with Dissolve(.8)
    frog "You're still here. I wasn't expecting to see you. Didn't Peter tell you to clear out?"
    owl "I will. Tomorrow. Thought I'd come one last time to our usual 'meeting.'"
    frog "That's thoughtful of you, but you know that the Porter won't let you in anymore."
    frog "And if you can't get in, I can't get in, so I'm afraid our midnight jaunts have come to a close."
    owl "What makes you think the Poter will let you in? I'm sure Peter instructed it to prevent {i}any{/i} of us from getting in alone."
    frog "No harm in trying, is there?"
    frog "But not with you here. That definitely won't fly"
    $ develop_double(10)
    show owl point at xflip, dcp
    show frog explain at dcs
    owl "You know if you get the ritual wrong there can be consequences. If you attempt it without my help, it could go bad for you."
    owl "Are you really sure you've got it down?"
    frog "I'm a keen observer. I'll be alright."
    owl "So you know what to keep hidden in your left hand and what to trace on your right?"
    frog "..."
    frog "You're making things up."
    owl "I'm trying to help you."
    owl "Let me show you. And then I'll get out of your way."
    owl "Keep learning about this place. You and I have come to understand how {b}important{/b} it is. What's hidden within."
    "The figure in the owl mask presses something small and black into the other's left palm."
    "They then grab the other's right hand and gently uncurl their fingers before tracing a shape on the palm."
    frog "Good luck."
    hide owl with moveoutleft
    "The frog masked figure stands alone now. They raise their hands in purposeful, almost artful gestures."
    "They remain completely, eerily silent. The only sound is the swooshing of their robes and the creaking of old floorboards."
    "Then..."
    #NOTE: effects here!
    show porter talk at dcs, left, xflip, DramaticRevealPorter, dc_porter
    with flash
    pause 3.56
    porter "You."
    $ develop_double(15)
    show porter swear at dcs, xflip, EmergencyReset, dc_porter
    show frog explain at dcs, right
    porter "Peter has told me that you wander where you are not meant to wander"
    porter "Beyond the walls of the House and into the Gardens. That you have even gazed into the Well."
    porter "You will not ent-"
    show porter swear at dcs, xflip, Regicide, dc_porter
    porter "wh.."
    porter "what is that"
    show porter swear at dcs, xflip, DoubleRegicide, dc_porter
    frog "What is... what? This?"
    "They open their left palm and reveal the odd stone pressed within."
    porter "WHAT HAVE YOU DONE?"
    show porter swear at dcs, xflip, UltimateRegicide, dc_porter
    "The spirit's thin legs seem to collapse under it. It begins to shake."
    show porter swear at dcs, xflip, ArmGlow, dc_porter
    "Its arm begins to glow, consumed by a sickly yellow light."
    "The light travels through the air and into the darkness, travelling towards the hand of another."
    $ develop_double(20)
    show frog explain at dcs, right
    show porter swear at dcs, xflip, ArmGlow, dc_porter
    show owl point at dcs, center, ArmGlowOwlHand with moveinbottom
    owl "Apologizes to use you like that, but I wasn't going to let anyone freeze me out."
    owl "Not after all I've seen and learned."
    hide porter
    show porter dead at xflip, dcs, dc_porter with Fade(0.2, 0, 0.4, color="#e7e0ba")
    frog "What have you done?! What did you do to it?!"
    owl "Go. Your part is done here."
    frog "{size=+7}{sc=1}Aaaahh!"
    hide frog with moveoutright
    $ develop_double(25)
    show porter dead at xflip, dcs, dc_porter
    show owl point at center, dcs
    "Their hand now glowing with the same sickly light, the figure in the owl mask places their hand on the floor."
    "Slowly, they trace a circle around the writhing spirit."
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
    porter "{sc=3}{size=+10}GIVE IT BACK"
    hide porter with dissolve
    "Gasping for breath, you look around the room. It's just you."
    "You hear some kind of noise coming from the photo in the tray."
    "Full of dread, you turn back to the image, careful not to fully take your eye off the rest of the room."
    show owl point at dcs, dc_overexpose
    $ develop_overexposed(15)
    show owl point at dcs, dc_overexpose
    "They are weeping."
    $ develop_overexposed(20)
    show owl point at dcs, dc_overexpose
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    hide owl
    jump complete_sneaky_frog

label complete_sneaky_frog:
    $ finish_development()
    $ donePhoto2 = True
    if photoRuined == True:
        "You pull out the wrecked photograph."
        "You suspect that what you saw was meant to be kept secret.."
    else:
        "You pull out the print, a bizarre image you suspect no one was meant to see."
        "A conversation which, certainly, no one was meant to hear."
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
    if donePhoto3:
        "You could watch it all play out once more, or you could just pull it out as soon as possible"
        menu:
            "Watch it all again":
                $ donePhoto3 = False
            "Pull it out":
                $ develop (30)
                "The same little pagent plays out, but your eyes are on the clock."
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
    show porter talk at dcp, xflip, dc_porter with moveinleft
    porter "Or will you accompany them today?"
    $ develop(10)
    show porter listen at dcp, xflip, dc_porter
    show fire explain at dcp
    flame "You go. I'll wait here."
    show fire hips at dcp
    show porter talk at dcp, xflip, dc_porter
    porter "As you wish."
    $ develop(15)
    show porter listen at dcp, xflip, dc_porter
    show fire open at dcp
    flame "I think you can take them to the Vestibule today."
    show fire show at dcp
    flame "I wonder if they will find the statuary there as inspiring as I do." #deliberate reference to Piranisi here, hope it's not seen as copying.
    $ develop(20)
    show porter swear at dcp, xflip, dc_porter
    show fire hips at dcp
    porter "The Vestibule sits near the Windows of the Garden. I would not take them somewhere so bright."
    show porter sad at dcp, xflip, dc_porter
    porter "They have stepped through so many times so quickly already."
    $ develop(25)
    show fire crossed at dcp
    show porter swear at dcp, xflip, dc_porter
    porter "Even the service I owe to you to you cannot override my purpose."
    $ develop(30)
    show fire crossed at dcp
    show porter talk at dcp, xflip, dc_porter
    porter "They must rest soon or they will begin to overflow. You will see to it that it is so."
    if(development_end_signalled == False):
        "You eye the clock. Photo's half developed. If you pull it out now, you'll get more time to double expose before it overdevelops"
    $ develop(35)
    show fire hips at dcp
    show porter listen at dcp, xflip, dc_porter
    flame "Yes, of course, of course. They need to actually start producing some art at some point anyway."
    show fire open at dcp
    flame "Not that I blame them. What could be more dull than sitting around {i}working{/i} when you could be in another world."
    show fire hips at dcp
    porter "..."
    show fire show at dcp
    flame "Go. Take them to the Vestibule. Show them the Corridor of Statues."
    $ develop(40)
    show fire hips at dcp
    show porter listen at dcp, dc_porter, DoubleRegicide
    "The porter turns to face the strange glow at the end of the hallway. It steps into it and begins to disappear."
    show porter swear at dcp, dc_porter, UltimateRegicide
    "Then, the spirit raises a trembling, withered hand. It traces some kind of shape in the air."
    hide porter with dissolve
    "The portal disappears, along with the spirit."
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
    $ develop_overexposed(5)
    show fire crossed at right, dcp, dc_overexpose
    $ corruption += 5
    flame "Foolish little thing. {sc=1}Blind{/sc} little thing."
    $ develop_overexposed(10)
    show fire crossed at dcp, dc_overexpose
    flame "{sc=1}Mute{/sc} little thing. {sc=2}Bloodless{/sc} little thing."
    $ develop_overexposed(15)
    show fire crossed at dcp, dc_overexpose
    flame "{sc=2}TRAPPED{/sc} little thing. {sc=4}BETRAYED{/sc} little thing."
    $ develop_overexposed(20)
    show fire crossed at dcp, dc_overexpose
    flame "{sc=4}BUT IT WILL BE MADE WHOLE."
    flame "{sc=4}AND {sc=4}BRIGHT THINGS WILL BE CONTAINED{/sc}!"
    $ develop_overexposed(25)
    show fire crossed at dcp, dc_overexpose
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
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
    "As the owl mask begins to fade into view, you feel like the whole character of the light has shifted."
    $ develop_double(5)
    $ zoom_development = True
    pause 3
    show fire explain at dcp, right with Dissolve(.4)
    show owl hips at dcs, xflip, left with Dissolve(.8)
    flame "Wait. Something is wrong."
    "Shimmering into view on the other side of portal is the figure from your dreams" #the portal language is a hot mess, maybe needs a variable or hardcoded use of the term before optional scenes.
    show porter swear at dcp, dc_porter, center, DoubleRegicide with dissolve
    show fire crossed at dcp
    porter "I am sorry, but she carries too much brightness. This one remains today."
    show porter listen at dcp, dc_porter
    flame "I see. Of course."
    $ develop_double(10)
    show owl crossed at xflip, dcs
    show fire hips at dcp
    show porter swear at dcp, dc_porter
    "The lumbering thing moves its hand in a strange, purposeful motion."
    show porter listen at dcp, dc_porter
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
    flame "It made me think ponder how both worlds are really cousin worlds."
    show fire magic at dcp
    flame "Or, twins, in a way."
    show fire hips at dcp
    show owl scared at xflip, dcs
    owl "I don't think that deeply about it, to be honest. I just go with my gut."
    show owl crossed at xflip, dcs
    show fire show at dcp
    flame "Of course. That's what makes you a great artist."
    show fire hips at dcp
    flame "... maybe you can help Gunnar with that while you're at it."
    owl "'Too bright...'"
    show owl open at xflip, dcs
    owl "What does that {i}really{/i} mean?"
    $ develop_double(20)
    show owl crossed at xflip, dcs
    show fire argue at dcp
    flame "I imagine it's because you're simply more open to the truth of that place. Because of your artistic temperment."
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
    flame "Let's get some food. Maybe you can tell me more about your thoughts about the Orrery and it's Door?"
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
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the motion in the frame {b}jolt forwards{/b}, as if skipping time."
    "With the frame now empty, only the subtle shifting of the light tells you this photograph is still animate."
    $ develop_overexposed(15)
    "The colors burn into nothing, slowly making the photo unrecognizable."
    $ develop_overexposed(20)
    "Then, something strange starts to happen."
    "You start to percieve that in the brightness of the photograph there is a {size=+6}pattern"
    $ develop_overexposed(25)
    "That your {size=+2}{i}mistake{/i}{/size} has been not making your previous exposures {size=+8}BRIGHT{/size} enough."
    $ develop_overexposed(30)
    "You are struck with the urge to laugh and before you can exert any will in the matter an oddly flat chuckle escapes your lips"
    "The sound in the empty darkroom is jarring and jolts you back to your senses."
    "You pull out the photo, feeling suddenly uncomfortable."
    jump complete_portal_owl

label complete_portal_owl:  
    $ finish_development()
    $ donePhoto3 = True
    if photoRuined == True:
        "You pull out the wrecked photograph."
        "You suspect that you heard many useful things which were meant to be kept secret..."
    else:
        "You pull out the print, a bizarre image you suspect no one was meant to see."
        "A conversation which, certainly, no one was meant to hear."
    jump post_image_completion_daytwo
#endregion

#region photo3 peter/flame
label develop_portal_flame:
    $ start_double_exposing(OBJECT_IMAGE_FLAME)
    "As your photo develops, the light of the portal flickers and dims."
    "The two robed figures, each wearing the same mask, begin to come to life."
    $ develop_double(5)
    $ zoom_development = True
    pause 3
    show fire point at dcp, right with Dissolve(.4)
    show fire2 hips at dcs, xflip, left with Dissolve(.8)
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
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    doubFlame "Yes, but not for you."
    $ develop_overexposed(20)
    show fire scared at dcp, dc_overexpose
    show fire2 argue at xflip, dcs, WhiteNoise
    doubFlame "For the one who watches us."
    if corruption >= 15:
        doubFlame "The one who is {sc=3}bright"
    else:
        doubFlame "The one who is {sc=2}not yet too bright."
    #I want to put more of an ending clue here but need to write that first.
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
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
    $ zoom_development = True
    pause 3
    show flame argue at dcp, right with Dissolve(.4)
    show sage base at dcs, xflip, left with Dissolve(.8)
    flame "I'm glad you changed your mind."
    flame "I'd like to ask why, but I'm afraid it'll only make you run away again."
    archer "..."
    flame "Of course, you don't have to say anything."
    flame "I have to be honest."
    flame "When I pulled this little group together I had no idea what was going to happen."
    flame "Once it all started to go wrong, I felt like I had made a terrible mistake."
    $ develop_double(10)
    show sage base at xflip, dcs  
    show flame argue at dcp
    flame "Now I see that everything that happened was all in service of something greater."
    flame "So. Here is my guess. After all this time, you've come around to the same conclusion."
    archer "That's not it."
    show sage base at dcs  
    archer "I wanted nothing to do with what you two had done. Honestly, I still don't."
    archer "But I started having these... terrible, realistic nightmares. About the Porter."
    archer "Started seeing it in real life, started feeling this icy pain that would grip my heart at random times."
    $ develop_double(15)
    show sage base at xflip, dcs
    show flame argue at dcp
    archer "I spoke to Siobhan. Before she died. She wasn't easy to find, always with one foot in some other world."
    archer "I wanted her to undo what'd she'd done. She didn't listen. She wasn't afraid of the Porter."
    archer "I spoke to Gunnar. He was easy enough to find. He doesn't leave his apartment at all anymore, the nurse said."
    archer "The walls, the floors, every square inch covered in mad writings. I could read enough to know the dreams were coming for him too."
    $ develop_double(20)
    show sage base at xflip, dcs
    show flame argue at dcp
    archer "So if I'm going to be hounded by some nightmare thing for all the shit you lot got up to..."
    archer "...I'd like to at least get something out of it."
    flame "I understand that logic. I'm a bit disappointed that an artist such as yourself has such a... selfish perspective."
    flame "We all meet out end eventually. What matters is what we {b}create{/b} along the way."
    "The figure in the flame mask makes a gesture and something is drawn through the portal."
    show porter dead weyes at center, dcp, DoubleRegicide with Dissolve(1)
    flame "But, that doesn't matter. All that matters is that you are here now."
    flame "So, what will you take into yourself?"
    $ develop_double(25)
    show sage base at xflip, dcs
    show flame argue at dcp
    show porter dead weyes at center, dcp, dc_porter, DoubleRegicide
    archer "... I want its eyes."
    flame "..."
    "The flame-masked figure makes a gesture."
    "Yellow light begins to form around the Porter's eyes."
    show porter dead at center, dcp, dc_porter with Fade(0.5, 0.2, 0.3, color="#fddf37")
    flame "Done."
    $ develop_double(30)
    show sage base at xflip, dcs
    show flame argue at dcp
    show porter dead at center, dcp, dc_porter, DoubleRegicide
    "The eyes of the human mask, too, begin to glow."
    $ reachedEnd = True

label develop_portal_archer_overexposed:    
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out just in time - perfectly exposed."
    else:
        "If you don't pull the photo out now, it will be overexposed."
    $ develop_overexposed(10)
    show sage base at xflip, dcs, dc_overexpose
    show flame argue at dcp, dc_overexpose
    show porter dead at center, dcp, dc_porter, DoubleRegicide
    $ corruption += 5
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    flame "What do you see?"
    archer "bright."
    $ develop_overexposed(15)
    show sage base at xflip, dcs, dc_overexpose
    show flame argue at dcp, dc_overexpose
    show porter dead at center, dcp, dc_porter, DoubleRegicide
    archer "BRIGHT"
    archer "And I see..."
    $ develop_overexposed(20)
    show sage base at xflip, dcs, dc_overexpose
    show flame argue at dcp, dc_overexpose
    show porter dead at center, dcp, dc_porter, DoubleRegicide
    archer "I see a way out."
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    jump complete_portal_archer

label complete_portal_archer:  
    $ finish_development()
    $ donePhoto3 = True
    if photoRuined == True:
        "You pull out the wrecked photograph."
        "You suspect that you heard many useful things which were meant to be kept secret..."
    else:
        "You pull out the print, a bizarre image you suspect no one was meant to see."
        "A conversation which, certainly, no one was meant to hear."
    jump post_image_completion_daytwo
#endregion

#region photo3 gunnar/Frog
label develop_portal_frog:
    $ start_double_exposing(OBJECT_IMAGE_FROG)
    "You stare intently, aware of the eerie quiet of the darkroom. A quiet you know will soon be filled with voices."
    $ develop_double(5)
    $ zoom_development = True
    pause 3
    show flame argue at dcp, right with Dissolve(.4)
    show frog explain at dcs, xflip, left with Dissolve(.8)
    "As expected, the two robed figures begin to move and speak."
    "But there is another figure, visible faintly through the portal."
    show porter dead weyes at dcp, dc_porter, center, DoubleRegicide with Dissolve(1)
    frog "I can't believe that worked!"
    frog "That was incredible, Peter. You're a genius, a true genius!"
    "Peter, if that who it is, stares blankely at the Porter."
    $ develop_double(10)
    show porter dead weyes at dcp, dc_porter
    show frog explain at xflip, dcs
    show flame argue at dcp
    flame "Can you hear me?"
    porter "..."
    flame "What did she do to you?"
    frog "I told you, she took its power. I would have stopped her if I had known what she was doing."
    frog "I don't understand this stuff the way you do, or the way she did."
    flame "Quiet."
    frog "If we're going to do this, Peter..."
    flame "I wish we knew where she went."
    $ develop_double(15)
    show porter dead weyes at dcp, dc_porter
    show frog explain at xflip, dcs
    show flame argue at dcp
    frog "You think she's even in this world? Even in the Bright House? She could be anywhere."
    frog "A few simple gestures not just from the Bright House, but from the Garden, from..."
    frog "Hell, Peter, I wonder if you even know what else could be out there."
    flame "This feels wrong."
    frog "If you want to find her, you won't find her without {sc=2}power{/sc} of your own."
    frog "As for me, I just want to write."
    frog "I was so close to something great, Peter. Isn't that all you wanted to come out of this? Something truly great for humanity?"
    flame "..."
    $ develop_double(20)
    show porter dead weyes at dcp, dc_porter
    show frog explain at xflip, dcs
    show flame argue at dcp
    flame "Alright. Hand me the stone."
    "The frog passes a small, dark object to Peter, who grips it in his left palm."
    "He then traces some kind of design over his chest."
    "Holding out both hands, a yellow glow appears in the chest of the spirit."
    "The light forms a thin thread, connecting Peter's chest with the spirit's"
    $ develop_double(25)
    show porter dead weyes at dcp, dc_porter
    show frog explain at xflip, dcs
    show flame argue at dcp
    flame "Good god..."
    "The figure with the flame mask sits motionless."
    flame "It is done."
    flame "Your turn."
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
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    show porter dead weyes at center, dcp, dc_porter, dc_overexpose
    show frog explain at left, xflip, dcs, dc_overexpose
    show flame argue at right, dcp, dc_overexpose
    frog "How... how does it feel?"
    flame "I can feel its power."
    $ develop_overexposed(15)
    show porter dead weyes at dcp, dc_porter, dc_overexpose
    show frog explain at xflip, dcs, dc_overexpose
    show flame argue at dcp, dc_overexpose
    frog "What should it be?"
    $ develop_overexposed(20)
    show porter dead weyes at dcp, dc_porter, dc_overexpose
    show frog explain at xflip, dcs, dc_overexpose
    show flame argue at dcp, dc_overexpose
    frog "Do words live in the tongue? Or the mind? Do I want to see what is in that mind? Could I even comprehend it?"
    flame "{size=+10}FOOL{/size}."
    $ develop_overexposed(25)
    show porter dead weyes at dcp, dc_porter, dc_overexpose
    show frog explain at xflip, dcs, dc_overexpose
    show flame argue at dcp, dc_overexpose
    flame "{size=+7}IT MATTERS NOT{/size}."
    flame "{size=+7}ALL WILL BE RETURNED{/size}."
    $ develop_overexposed(30)
    show porter dead weyes at dcp, dc_porter, dc_overexpose
    show frog explain at xflip, dcs, dc_overexpose
    show flame argue at dcp, dc_overexpose
    flame "{size=+15}ALL MUST BE RETURNED{/size}"
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    jump complete_portal_frog

label complete_portal_frog:  
    $ finish_development()
    $ donePhoto3 = True
    if photoRuined == True:
        "You pull out the wrecked photograph."
        "You suspect that you heard many useful things which were meant to be kept secret..."
    else:
        "You pull out the print, a bizarre image you suspect no one was meant to see."
        "A conversation which, certainly, no one was meant to hear."
    jump post_image_completion_daytwo
#endregion
#endregion

#region end of day 2

label endOfDay2:
    "You wipe the sweat from your brow and sit in Erin's chair, thought swirling."
    "Trying to make sense of the events you've seen. To piece together the timeline."
    "You can't be sure that everything you've seen is real, or was real, but at the same time it almost adds up."
    "Your phone buzzes. It's Bud. They're outside."
    show buddy question with moveinleft
    bud "So I looked into Peter Carlson..."
    show buddy sad
    bud "Um, it got weird."
    show buddy question
    bud "So he's the guy who runs this foundation."
    show buddy sad
    bud "Also, there used to be a Siobhan Kent young artists grant. A lot of the recipients, uh, seem to have died."
    show buddy question
    bud "Same for the, uh Gunnar Olsen young poet award award winners."
    if porterKnown == True:
        show buddy talkhand
        bud "I didn't have a lot of luck looking up any kind of a spirit called the Porter."
        bud "That's probably just because like, where the hell do you even start with something like that."
        show buddy question
        bud "But it did come up in some of Gunnar's unfinished works. And the works of the poet award winners."
        show buddy talkhand
        bud "It's either some sort of like, vengeful killer or some sort of guardian angel."
        show buddy sad
        you "That's super helpful..."
        show buddy listen
        bud "Right?"
    you "Bud... did you have any nightmares last night?"
    show buddy question
    bud "Kinda, yeah, actually. I kept dreaming of these chopped up body parts and like, all these different creatures pecking at them."
    bud "This owl was eating someone's hand and then there was this moustached guy just like, watching it all from the woods." #NOTE: ARCHER REFERENCE
    show buddy talkhand
    bud "Oh god then he ate his heart!? Damn, I almost forgot how messed up it was."
    show buddy question
    bud "How did you know?"
    show buddy listen
    you "I had one too. About the porter."
    you "I don't know what Peter's game is here but I think we need to get out of all of this."
    show buddy question
    bud "So we just quit?"
    show buddy sad
    bud "..."
    show buddy talkhand
    bud "It's too late for that, isn't it?"
    show buddy listen
    "You fill Bud in on everything you've seen."
    show buddy sad
    "Bud sighs."
    bud "I feel crazy."
    show buddy question
    bud "Like, this is starting to make sense, but where the hell do we fit in?"
    show buddy sad
    you "I think the spirit wants something from us."
    show buddy listen
    you "In my dream, it showed me where to find some photos. Photos that Erin, or someone, had hidden."
    show buddy question
    bud "Yeah but like, it showed me all these random body parts getting ripped apart."
    show buddy listen
    you "It talked to me about body parts as well..."
    you "A heart, a hand, a tongue, and eyes."
    show buddy sad
    bud "..."
    show buddy question
    bud "Can I see that photo you found again?"
    show buddy talkhand
    bud "Look at the exposure. Erin's face over the porter's face."
    bud "Why would Erin do that?"
    show buddy listen
    "You look at the photo for a moment."
    you "Not her face over his face."
    you "Her eyes over its eyes."
    show buddy amused
    bud "Oh. Now {i}that{/i} is interesting."
    show buddy question
    bud "In the negative here, the spirit has no eyes..."
    bud "But in your dream, it did, right?"
    show buddy listen
    you "Yeah."
    bud "..."
    show buddy talkhand
    bud "I think we need to find the negative of this photograph."
    show buddy amused
    bud "Do you think it could be hidden somewhere here?"
    show buddy listen
    "Your search the other day was quick. As the photos hidden behind the picture frame made clear, you hadn't done a truly deep search."
    scene darkroom_workspace bright with Fade(.7, .5, .4)
    "The hours go by. The sun sets. There's so much stuff not just in the studio but the rest of the house that you realize this could take all night."
    show buddy question
    bud "Hey, I gotta get some sleep. I'm going to be totally dead tomorrow otherwise."
    show buddy amused
    bud "But I'll come by first thing in the morning?"
    show buddy listen
    "You nod and thank Bud for their help."
    hide buddy with dissolve
    "You're pretty tired as well."
    "Before you go, you grab all the prints you took today and shove them in your bag."
    jump night2
#endregion

#region night2
label night2:
    scene bg bedroom light with Dissolve(1)
    pause .3
    "The fear of the dreams keeps you up for a while..."
    $_window_show()
    show bg bedroom sleep with dissolve
    "But sometime around two in the morning sleep finds you."
    show bg nightmare:
        RaveLights
    with Dissolve(2.0)
    "And so do the dreams"
    show porter dead:
        yalign .03
        xalign .5
    with moveinbottom
    if corruption >= 25: #high
        porter "..."
        porter "I see now you are already {sc=4}BRIGHT{/sc}"
        porter "But that does not mean it is too late to RIGHT what is {sc=4}WRONG"
        porter "Like the {sc=4}SAGE DID{/sc}. She returned my eyes, and was so freed."
    elif corruption >=15:
        porter "You are {sc=4}SO BRIGHT{/sc} that I fear you are {sc=4}NEARLY LOST"
        porter "You have little time before it is too late."
        porter "Like the {sc=4}SAGE{/sc} was. She undid her wrong and returned my eyes, but it was too late for her."
    else:
        porter "You are not yet {sc=4}SO BRIGHT{/sc} as to be {sc=4}LOST{/sc}"
        porter "But if you are not quick, you will be soon."
        porter "Like the {sc=4}SAGE{/sc} was. She undid her wrong, but it was too late for her."
    porter "Now you know their {sc=4}TRANSGRESSION{/sc}"
    porter "Until it is {sc=2}UNDONE{/sc}..."
    porter "Undone in {sc=3}FULL{/sc}..."
    porter "You will not rest."
    $_window_hide()
    show porter dead at ZoomInto:
        WhiteNoise
    pause 1.1
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
    porter "{sc=4}HE{/sc} has the final piece."
    porter "{sc=4}HE{/sc} is there now"
    show bg nightmare
    porter "You must GO NOW."
    show bg nightmare:
        size(1920, 1080) crop (0, 0, 1920, 1080)
        linear .8 crop(1130, 310, 360, 240)
    porter "{size=+20}NOW!!{nw=.6}"
    scene bg bedroom light with flash
    "You wake up and your body is already halfway out of bed."
    "You throw on clothes, send a quick text to Bud, and rush out the door."
    jump day3Start
#endregion
