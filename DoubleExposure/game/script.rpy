#Importing libraries
init python:
    import math

#### Defining characters. Characters are global, so all files can see them ####
#Modern day
define you = Character("You") #You, the player!
define bud = Character("Bud", color="#0ea321") #Your present day friend, will rename this later?
define porter = Character("The Porter", color="#616161") #the Porter itself!
define spirit = Character("Spirit?", color="#616161") #The porter if we don't know its name

#Now, photo world/90s people
define Erin = Character("Erin", color="#ae4721ff") #Erin Darabondi
define Siob = Character("Siobhan", color="#0f675d") #Siobhan
define Peter = Character("Peter", color="#6b6a19") #Peter
define Gunnar = Character("Gunnar", color="#93b65a") #Gunnar

#Utility "characters"
define tutorial = Character("", color = "#c8580d")
define temp = Character("PLACEHOLDER", color = "#d92703", what_color = "#d92703") #to describe art or animations not yet in the game.
define unk = Character("???", color = "#707070") #unknown to the player
define unk2 = Character("???", color = "#b59cd8") #second unknown, in case two unknowns speak

### Defining Variables ###
default menuset = set() #we initialize this every time we have a menu set (see Ren'Py docs for more info)
default corruption = 0 #incremented as you overexpose photos. Checked whenever we feel like it.
default budLevel = 0 #friendship level with bud.
default zoom_development = False
default zoom_development_transitioned = False
default photoRuined = False
default reachedEnd = False

###Branching story related variables
default gunnarKnown = False #You know Gunnar's name
default peterKnown = False #You know Peter's name
default houseKnown = False #You've heard them talk about going 'through a gate'
default porterKnown = False #You've heard them talk about the Porter
default photoFound = False #You found the hidden photo in Erin's house.
default seenPhoto1 = False #Have you already watched the first scene?

### darkroom exploration vars
default lightOn = False
default papersGrabbed = False
default enlargeFirst = True
default traysFirst = True
default deskFirst = True
default onFirstBase = True

###images### 
#We may decide not to define these but just to use filenames later
#BGs
image parcel = "bg/bg parcel.png"
image darkroom_workspace bright = "bg/bg dark room day1.png"
image darkroom_workspace red = "bg/bg dark room day1 red.png"
image porterPhoto = "placeholders/porterPhoto_temp.png"
image nightAndDayPartial = "photos/kitchen erin.png"
image nightAndDay = "photos/erin original two.png"
image fakeClock = "clock/clock gold.png" #unlike many of these, actually needs to be defined.
image black_background = Solid("#000000") 
image white_background = Solid("#fff")  

image porter_eyes = "body parts nightmare/eyes.png"
image porter_hand = "body parts nightmare/hand.png"
image porter_heart = "body parts nightmare/heart.png"
image porter_tongue = "body parts nightmare/tongue.png"

#region effects
define flash = Fade(0.1, 0.0, 0.5, color="#fff")
transform ZoomInto:
    easein 20.0 zoom 10
transform smallNegativePerson:
    fit("scale-down")
    function play_slide_place
    matrixcolor SaturationMatrix(0) * InvertMatrix()
    zoom .54
    blur 15
    ypos .8
    alpha 0
    pause 0.05
    alpha 0.7
    pause 0.05    
    alpha 0.3
    pause 0.05    
    alpha 0.7
    pause 0.05 
    alpha 0.2
    pause 0.2
    linear 0.7 alpha 0.7
    function play_slide_ratchet
    linear 1.0  blur 5 zoom .5
    pause 0.2
    function play_slide_ratchet_short
    linear 0.2 blur 3 zoom .48
    pause 0.4
    function play_slide_ratchet_short
    linear 0.2 blur 0 zoom .45

    # xsize .6
    # ysize .6
    # ypos .8
    # matrixcolor InvertMatrix(1.0)
    # alpha .5

transform smallNegativeBase:
    function play_slide_place
    matrixcolor SaturationMatrix(0) * InvertMatrix()
    zoom .5
    blur 15
    yalign .75 xalign .54 rotate 0    
    alpha 0
    pause 0.05
    alpha 0.7
    pause 0.05    
    alpha 0.3
    pause 0.05    
    alpha 0.7
    pause 0.05 
    alpha 0.2
    pause 0.2
    linear 0.7 alpha 0.7
    function play_slide_ratchet
    linear 1.0 blur 5 zoom .48
    pause 0.2 
    function play_slide_ratchet_short
    linear 0.2 blur 3 zoom .45
    pause 0.4 
    function play_slide_ratchet_short
    linear 0.2 blur 0 zoom .4

transform offsetStoryEnlarger:
    zoom 1.15

transform zoomedEnlarger:
    zoom 1
    xalign 0.5
    yalign 0.5

transform dcp:
    ysize 1000
    fit "scale-down"
    alpha  .3 + min(base_development / MAX_DEVELOP_TIME, 1.0) *.7
        
transform dcs:
    ysize 1000
    fit "scale-down"
    alpha  .4 + min(secondary_development / SECONDARY_MAX_DEVELOP_TIME, 1.0) *.6

transform dc_overexpose:
    matrixcolor BrightnessMatrix(over_exposure/MAX_OVEREXPOSURE_TIME) * ContrastMatrix(1+over_exposure/MAX_OVEREXPOSURE_TIME)
    shader "MakeVisualNovels.PerlinWarp"
    # How many changes per second.
    # Higher is more energetic.
    u_fps (12.0*over_exposure/MAX_OVEREXPOSURE_TIME)
    # Body Warp Variables.
    # This provides smooth warps of the entire image.
    u_minSmooth (0.0) # Minimum of 0.0
    u_maxSmooth (2) # Maximum of 0.5
    u_warpIntensity (2.0*over_exposure/MAX_OVEREXPOSURE_TIME)
    u_speed (1.15)
    u_scale (10.0*over_exposure/MAX_OVEREXPOSURE_TIME)
    # Flipping Warp Variables.  
    # This produces more vividly bouncing deformations
    u_flipIntensity (30.0*over_exposure/MAX_OVEREXPOSURE_TIME)   
    u_flipSpeed (2.0)
    u_flipScale (80.0*over_exposure/MAX_OVEREXPOSURE_TIME)

transform porterBodyPart:
    xanchor 0.5
    yanchor 0.5
    ypos 400
    xpos 960
    shader "MakeVisualNovels.StillAberration"
    u_aberrationAmount(30.0)
    zoom 0
    parallel:
        easein 0.5 zoom 1
    parallel:
        xpos 957
        pause 0.1
        xpos 964
        pause 0.05
        xpos 954
        pause 0.08
        xpos 958
        pause 0.1     
        repeat
    parallel:
        ypos 408
        pause 0.1
        ypos 400
        pause 0.06
        ypos 405
        pause 0.1
        ypos 391
        pause 0.15
        ypos 395
        pause 0.06
        repeat
    parallel:
        linear 5 alpha 0

transform yflip:
    yzoom -1

transform xflip:
    xzoom -1

transform xhack: #no idea why I need this but we are like a day away from the end so
    xzoom 1

#transitions
#$ renpy.transition(Dissolve(1.0), layer="master")
#endregion

#region intro
#This will be replaced by something more official
label splashscreen:
    scene black
    with Pause(.4)
    #show text "Created for the Spooktober Visual Novel Jam 2025 (this will be an image later)"
    show spooktoberlogo at center:
        truecenter zoom .5
        alpha 0
        parallel:
            easein 2 zoom .8
        parallel:
            easein 2 alpha 1
    with Pause(3)
    hide spooktoberlogo with Dissolve(1)
    return

# The game always starts here. I like to put no story in this so it remains a pure starting point that jumps to whatever block we want
label start:
    stop music fadeout 1.0
    $ config.developer = True #disable for public builds! This is a Ren'Py variable
    $ corruption = 0
    $ budLevel = 0
    jump introScene
    return

label introScene:
    $_window_hide()
    #$ renpy.music.set_audio_filter("melody", my_reverb_filter)
    play sfx_1 "breath-1.mp3"
    play music 'piano-underscore.mp3'
    show nightAndDay with Dissolve(1.5):
        xalign .1
        yalign .19
        zoom 2
    pause 1.0
    #add a vignette effect?
    "{size=+10}Erin Darabondi."
    "Many artists have inspired you, but it was Erin who made you want to {i}be{/i} an artist."
    "Through her lens, strange and fantastic scenes became real."
    window hide
    show nightAndDay:
        easeout 2.5 zoom 1.0
    pause 2.7
    "The supposed 'truth' of photography used to present impossibilities."
    "A lot of your work ended up being different than hers. You wanted to carve your own path, of course."
    "You started getting a bit of attention as an artist. Showed at a few smaller galleries."
    "Some days it feels crazy, like you're on your way to becoming a 'real artist.'"
    "And some days feels like you've still got a million miles to go."
    "But Erin's love of double exposure, in particular, stuck with you."
    play photo_1 'piano-underscore-spook-1.mp3'
    hide nightAndDay
    show nightAndDayPartial with flash:
        alpha .7
    "Partially developing one photo..."
    "...and then exposing another over it, creating a new image."
    show nightAndDay with Dissolve(1)
    pause 1.0
    "When Erin was doing it in the early 90s, people couldn't yet just photoshop together any crazy idea."
    "Her imagery stood out."
    "You still do it the old fashioned way, too. Film. A darkroom."
    "It was your double exposure pieces that caught the eye of the Darabondi Foundation."
    #Stretch goal – show a drawing of a letter in hand, or SOMETHING
    play photo_2 'piano-underscore-spook-2.mp3'
    show darkroom_workspace red with Dissolve(.7)
    "You could hardly believe it when you found out that you'd be a recipient of their first ever Young Artist Grant."
    "A chance to work - to be {i}paid{/i} to work in Erin's old studio. With her old gear. To create works inspired by her."
    show bg machine with Dissolve(.7)
    "By her legacy."
    play drone_1 "eerie-1.mp3" volume 0.2 noloop fadein 2
    play drone_2 "bass-drone-2.mp3" volume 0.2 fadein 4
    show bg enlarger red with Dissolve(.7)
    "A legacy which, for better or for worse..."
    play sfx_1 "gong-1.mp3"
    play photo_3 'piano-underscore-spook-3.mp3'
    show porter photo:
        subpixel True
        zoom .9
        xalign 0.5
        yalign 0.5
        rotate 1.5
        xanchor 0.5
        yanchor 0.5
    with Fade(0.1, 0.2, 1.9, color="#ffffff")
    "...you are now a part of."
    show porter photo:
        parallel:
            easein 60 zoom 10
        parallel:
            easein 60 rotate 180
    pause 1
    show black_background with Fade(1.1, 0, 0)
    window hide
    play drone_3 'porter-drums-1.mp3' fadein 0.5
    #TRANSITION TIME!
    play sfx_2 'porter-wail.mp3'
    pause 1.1
    play audio ['ding-1.mp3'] noloop
    play audio ['low-thud-single.mp3'] noloop
    
    #pause 2.2

    stop music
    stop sfx_1
    stop photo_1
    stop photo_2
    stop photo_3
    stop drone_1
    stop drone_2
    stop drone_3
    show twodays with Dissolve(0)
    stop sfx_2 fadeout 1
    pause 10
    #show buddy. If this convo can happen outside of the darkroom (maybe a kitchen in the house?)
    scene darkroom_workspace bright
    play music "lil-guitar-loop.mp3" volume 0.2 fadein 1
    "It's your first day at Erin's studio. You're excited to poke around, maybe start to sketch out some ideas."
    "Although at the moment it's a bit hard to focus."
    show buddy smile with moveinleft
    bud "I don't think she's dead."
    show buddy amused
    bud "No way."
    show buddy talkhand
    bud "This 'Young Artist Foundation?' She runs it. She just got tired of the limelight."
    show buddy listen
    you "She wasn't {i}that{/i} big."
    you "And she had already started talking about her next series. Does that sound like someone ready to disappear?"
    show buddy amused
    bud "Ready or not, that's what happened."
    show buddy laughs
    bud "Without a trace..."
    show buddy smile
    "Bud is the {i}other{/i} grant winner. A collage artist, whose work, despite not being photography, much more closely mirrors Erin's."
    "Surreal themes and imagery, symbols dripping with meaning. Uncommon juxtapositions."
    "You thought it was a bit derivative at first. Now you're starting to think they're a bit obsessed."
    show buddy question
    bud "Don't tell me you've never wondered what happened to her!"
    menu:
        "I prefer to focus on the art, not the artist":
            #show bud dejected or pensive
            show buddy sad
            bud "Yeah, of course. Me too. That's why we're here."
        "Of course. I've read some pretty crazy theories":
            $ budLevel += 1
            show buddy tricky
            bud "I know, right? There was a group that tried to do a podcast about it. They didn't find much."
            #this would be a great place for a CLUE! Maybe corruption if we run such a mechanic.
        "Why would she need to fake her disappearence to run her own foundation? You have to admit that makes no sense.":
            #show bud dejected or pensive
            show buddy sad
            bud "Yeah, I know. I just prefer to imagine everything has a happy ending, you know?"
            #this would be a great place for a CLUE! Maybe corruption if we run such a mechanic.
    show buddy amused
    bud "I was just thinking about maybe doing some sort of piece around her. Like, Erin."
    show buddy question
    bud "What happened, or didn't happen. Putting her in places she isn't, but could have been."
    show buddy tricky
    bud "A lot of my work was already kind of inspired by her, so I feel like I have to really do something different, you know?"
    show buddy talkhand
    bud "Especially since I'm getting paid now."
    bud "This is my first grant, actually."
    show buddy question
    bud "What are you going to make? Do you know?"
    "Ah shit. To be honest, you've been struggling with that too."
    menu:
        "I'm actually really struggling with it.":
            $ budLevel += 1
            "I know the grant stipulates that we can make whatever we want, so long as it is 'in dialogue with Erin's work'"
            "Just specific enough to make things harder, but vague enough to get drowned in options"
            show buddy laughs
            bud "Dude, it's freaking HARD, right? It's like, suddenly there's all this pressure."
            show buddy amused
            bud "Well, you can always start with the basics. You do photography, have you done much double exposure."
            "Not really, actually"
            show buddy laughs
            bud "Hey, maybe start there!"
        "I've got some ideas.":
            show buddy sad
            bud "Okay, keep your secrets then."
    show buddy smile
    bud "Well, I should probably get to work. Got a long day of cutting stuff up, you know."
    hide buddy with moveoutleft
    stop music fadeout 4.0
    #play sfx_1 "step-and-door.mp3" fadein 1.0
    "You should probably get to work too."
    jump darkroomIntro

label darkroomIntro:
    show darkroom_workspace bright
    "You got a brief tour of the room yesterday, with someone from the foundation, but this is your chance to really settle in."
    "According to your grant representitive, the equipment has been mantained but otherwise things have been virtually untouched for the last 30 years."
    "They were hoping to turn the house into a museum but it never came through."
    "Which only makes it more exciting that you're suddenly allowed to poke around!"
    #temp "I like the idea of being able to click on objects in the room, and getting a brief rundown on them."
    #temp "Clickables are highlighted (no looking for secrets) and the scene would continue until you had clicked everything"

label darkroomIntro2:
    if lightOn:
        scene darkroom_workspace red
    else:
        scene darkroom_workspace bright
    menu:
        "Check out the enlarger":
            #First time here
            if lightOn:
                show bg enlarger red at zoomedEnlarger
            else:
                show bg enlarger at offsetStoryEnlarger
            if enlargeFirst == True:
                "The enlarger is an older model, old even for the 90s when Erin was working."
                "Oh wow, it looks like there are already some negatives in here!"
                play audio "slides/sweep-1.mp3"
                show siobhan one at center:
                    smallNegativePerson
                "Oh, I think I know this person! Siobhan Kent."
                "A contemporary of Erin. They had some sort of brief collaboration that never came to fruition."
                hide siobhan one
                play audio "slides/sweep-2.mp3"
                show gunnar points at center:
                    smallNegativePerson
                "No idea who this is."
                "This looks more like a personal shot than an art piece though."
                hide gunnar points
                play audio "slides/sweep-3.mp3"
                show peter one at center:
                    smallNegativePerson
                "Another mystery person"
                "A friend, maybe?"
                hide peter one
                play audio "slides/sweep-4.mp3"
                show kitchen erin:
                    smallNegativeBase
                "Oh, wow. Now {i}this{/i} is a find!"
                "This photo was used to make her famous piece 'night and day.' The final version had a this crazy blazing sun images exposed over it, in the doorway."
                "So this is like, the original negative from that work. That's crazy!"
                "Maybe this is my first project? Maybe I print this and expose something else over it!"
                "Put my own spin on the image..."
                "Create dialog with Erin through {i}fusing{/i} her art with mine."
                "Yeah, that sounds amazing!"
                hide kitchen erin
                $ enlargeFirst = False
            #Second time here
            else:
                "The negatives sit in the enlarger, ready to print"
            #Either way, we need to complete these steps first
            if lightOn == False:
                "I should flip on the safe light before working."
                jump darkroomIntro2
            elif papersGrabbed == False:
                "I should find some photo paper to print this on."
                jump darkroomIntro2
            elif enlargeFirst == True:
                "Looks like I have what I need to print this!"
                jump photo1_firstDev
            else:
                jump photo1_firstDev
        "Check out the safelight" if lightOn == False:
            "Erin's safelight is a classic red. Full spectrum light will ruin any photo paper."
            "May as well turn this on now."
            $ play_darkroom_light()
            scene darkroom_workspace red
            $ lightOn = True
            jump darkroomIntro2
        "Check out the trays" if papersGrabbed == False:
            if traysFirst == True:
                "These lovely baths of toxic chemicals are where your photos will develop."
                "You notice a hand-wrapped package sitting next to the baths labeled with scrawled ballpoint pen as 'photo paper exp. lot 4'"
                "You know she had experimented with printing on some unusual surfaces. Maybe that's what was going on here?"
                $ traysFirst = False
            if lightOn == False:
                if traysFirst == True:
                    "Either way, it can't be opened until the safe light is on."
                else:
                    "Once the safe light is on you can open the package of photo paper."
            else:
                play audio "slides/remove-2.mp3"
                "You carefully unwrap the parcel and discover two luxurious pieces of print paper."
                "It feels a bit wrong, but the grant was emphatic that you could use her original materials, so you grab the papers, eager to see what Erin had been tinkering with."
                $ papersGrabbed = True
            jump darkroomIntro2
#endregion

#region photo functions
label photo1_firstDev:
    "You slide one of the two pieces of photo paper under the enlarger."
    "It feels coarse to the touch. Strangely thick."
    $ begin_day(Days.DAY_ONE)
    jump projector_select_base_dayone

label projector_select_base_dayone:
    scene black_background with flash
    window hide
    $ start_enlarger()
    $ target_label = renpy.call_screen("enlarger_select_photo")
    show bg enlarger red bigger
    show photopaper enlarger
    with flash
    "You expose the paper, starting a print of 'day and night'"
    scene
    show bg tray red
    "Next comes the developing liquid."
    "You judge that your photo will be fully exposed after {b}{size=+5}60 seconds{/b}{/size}."
    "That means that if you want to maximize the quality of your double exposure, you should pull it out at {b}{size=+5}30 seconds{/b}{/size}."
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
    "You make sure your watch is in easy view as you submerge the photos."
    hide fakeClock
    hide clock pointer aligned
    show photopaper tray at developingImageWave with Dissolve(0.5):
        matrixcolor TintMatrix("#975555") 
    "You drop the print in the bath and wait."
    jump expression target_label

#jumps here afer you're done with the base image
label projector_select_double_dayone:
    scene darkroom_workspace red
    stop ambiance_1 fadeout 1.0
    stop ambiance_2 fadeout 1.0
    stop photo_1 fadeout 1.0
    stop photo_2 fadeout 1.0
    stop photo_3 fadeout 1.0
    play sfx_1 "splash-small-1.mp3" noloop volume 0.2
    "You grab your tongs and pull out the photo"  
    $ complete_label = get_tag_if_finished()
    if onFirstBase == False:
        if(complete_label):
            jump expression complete_label
        "It's ready for a second exposure."
    else:
        if(complete_label):
            jump expression complete_label
        "Immediately, whatever it was you were watching stops completely."
        play sfx_2 "heartbeat.mp3" volume 0.6 fadein 2.0 loop
        "The room is quiet, except for the sound of your heart pounding in your chest."
        "You don't know what you just saw but you're absolutely certain you saw it."
        "Right?"     
        "The only way to be sure would be to finish the print..."
        $ onFirstBase = False
    stop sfx_2 fadeout 2.0  
    window hide
    $ start_enlarger()
    $ target_label = renpy.call_screen("enlarger_select_photo")        
    jump expression target_label

label post_image_completion_dayone:
    scene darkroom_workspace red
    $ seenPhoto1 = True
    stop sfx_2 fadeout 2.0
    stop melody fadeout 0.5
    stop photo_1 fadeout 0.5
    stop photo_2 fadeout 0.5
    play sfx_1 "breath-2.mp3" noloop
    play ambiance_1 "ambient-darkroom-light.mp3" fadein 1.0 # make sure light buzz is playing
    play ambiance_2 "ambient-darkroom-rumble.mp3" fadein 0.5
    $ photoRuined = False
    $ reachedEnd = False
    if(current_photo_paper > 0):
        if(current_photo_paper == 1):
            "You have a single piece of photo paper left."
            "You could do this again... maybe see something different this time?"
            "For now, the only proper image you have to work with is the negative of 'night and day.'"
            "But as it's what you've got, you hurry back to the enlarger to start another print."
        else:
            "You have [current_photo_paper] pieces of photo paper left."
        jump projector_select_base_dayone
    jump endOfDayOneChoices
#endregion
# this system works by jumping to known labels
# == Projector ==~
# projector_select_double_<DAY>

# === Base image development ==
# develop_<BASETAG>
# develop_<BASETAG>_overexposed

# === For every object image + base image combo
# develop_<BASETAG>_<OBJECTTAG>
# develop_<BASETAG>_<OBJECTTAG>_overexposed
# complete_<BASETAG>_<OBJECTTAG>

# The first call to develop_overexposed() will check if there is a pending exit, so you can put
# any message related to "watch out you're about to overexpose" there

# image definitions are in daysconfig, you can expand by following the pattern in the current ones. Any amount of dialogue should work
# you can develop at any increments, but 60 is currently the max value beyond which you overexpose.

# TODO: easier display of the completed image


#region day one - kitchen base
label develop_kitchen:
    scene black_background with fade
    $ start_developing(BASE_IMAGE_KITCHEN)
    play photo_1 "photo-underscore-1.mp3" fadein 5.0
    if seenPhoto1 == True:
        "As you develop the scene from 'night and day' for a second time, the same thing happens."
        "Erin begins to move and speak, the same motions and words as she did before."
        "You could watch it all play out again, or you could just wait to pull it out as soon as possible"
        menu:
            "Watch it all again":
                $ seenPhoto1 = False
            "Pull it out":
                $ develop (30)
                "You keep your eye on the clock and pull the photo out as soon as possible."
                $ stop_developing_instant()
    "The image begins to emerge, slowly at first."
    $ develop(5)
    "Then, something else starts to happen."
    $ develop(10)
    "In the photo, the figure by the window starts to move."
    $ zoom_development = True
    pause 3
    show erin smile at dcp, left with Dissolve(1)
    "Erin."
    "Her lips part. Subtly, but unmistakably"
    play sfx_1 "breath-1.mp3" volume 0.8
    "She turns towards the camera and begins to mutter to herself"
    $ develop(15)
    show erin ponder at dcp
    Erin "Something like that..."
    hide erin with moveoutleft
    "She walks towards the camera, disappearing out of frame."
    Erin "Well shit, I do believe that's going to do it."
    $ develop(20)
    Erin "And you put something in the door and {i}bada bing bada boom{/i} you've got yourself some art."
    show erin smile at dcp, left with moveinleft
    Erin "I should probably shoot a few takes. Different expressions."
    $ develop(25)
    show erin ponder at dcp
    Erin "Since I have no idea how I'm going to be feeling after all of this."
    Erin "That's assuming, of course, you even come back at all..."
    $ develop(30)
    "You pull your gaze away for a moment to check the clock. It's almost {b}{size=+2}30 seconds{/b}{/size}."
    if(not development_end_signalled):
        $ audio_warn_clock()        
        "Technically you should be pulling the photo out just about now. The longer you leave it, the closer to overexposure it gets."
        "But does that matter when {i}{b}this{/i}{/b} is happening?"
        "You could choose to push it just a {i}little{/i} longer..."
    $ develop(35)
    $ audio_overexpose_kitchen()
    Erin "Shit. Erin, you're shaking."
    Erin "Well, if this is going to be my last photograph, it may as well be a good one."
    show erin think at dcp
    "She turns and looks at the doorway."
    show erin ponder at dcp
    Erin "Maybe Peter is completely full of shit."
    $ develop(40)
    show erin think at dcp
    Erin "..."
    show erin ponder at dcp
    Erin "I don't think he is though."
    $ develop(45)
    Erin "And you've come too far to back out now. Whatever happens..."
    show erin think at dcp
    "Erin sighs."
    $ develop(50)
    show erin think at dcp
    "Despite the insanity of what you're witnessing, old habits die hard and you find yourself checking the clock."
    if(not development_end_signalled):
        "There's still a chance to expose something over the image, although aleady it'll likely be a bit overdeveloped."
        "But does that even matter anymore?"
    $ develop(55)
    show erin ponder at dcp
    Erin "There's something I like about working this way. Not having anything planned. Not knowing what I'll choose to share the frame with me."
    $ develop(60)
    "The image is getting darker now. You're about to ruin it."

label develop_kitchen_overexposed:    
    $ renpy.block_rollback()
    $ audio_escalate(1)
    $ develop_overexposed(5)
    $ corruption += 5
    show erin ponder at dcp, dc_overexpose
    Erin "But maybe it's not about who 'shares the frame with me...'"
    Erin "But who is {sc=4}outside{/sc} the frame. Watching?"
    Erin "You don't seem to care much about your images, do you?"
    $ develop_overexposed(10)
    show erin ponder at dcp, dc_overexpose
    Erin "{sc=4}Ruining{/sc} the things you create."
    Erin "I wouldn't make that mistake."
    show erin smile at dcp, dc_overexpose
    "This is getting weird..."
    show erin ponder at dcp, dc_overexpose
    $ develop_overexposed(15)
    show erin ponder at dcp, dc_overexpose
    Erin "It's not your fault... but you should know..."
    $ audio_escalate(2)
    Erin "that there is {sc=4}ONLY SO MUCH SKIN{/sc}"
    $ develop_overexposed(20)
    show erin ponder at dcp, dc_overexpose
    Erin "ONLY SO MANY {sc=4}EYES{/sc}"
    Erin "AND THE THINGS TAKEN WILL BE RETURNED"
    $ develop_overexposed(25)
    $ audio_escalate(3)
    show erin smile at dcp, dc_overexpose
    "An icy chill grips your heart and you feel the room start to spin."
    "You feel like SOMETHING TERRIBLE has happened."
    "Almost without thinking, you grab the tongs and pull out the image."
    jump complete_kitchen

label complete_kitchen:
    $ finish_development()
    "Immediately, whatever it was you were watching stops completely."
    play sfx_2 "heartbeat.mp3" volume 0.6 fadein 3.0 loop
    if onFirstBase == True:
        "The room is quiet, except for the sound of your heart pounding in your chest."
        "You don't know what you just saw but you're absolutely certain you saw it."
        "Right?"        
        $ onFirstBase = False
    jump post_image_completion_dayone

#region Siobhan
label develop_kitchen_siobhan:
    "You lower the print into the developing fluid, filled with a nervous anticipation."
    "Will it happen again?"
    $ start_double_exposing(OBJECT_IMAGE_SIOBHAN)
    "For a moment, Siobhan looks awkward, overlayed crudely over the doorway."
    $ audio_start_kitchen()
    "Then, she starts to move. Her feet, partially suspended, touch the ground."
    $ audio_kitchen_melody("siobhan")
    $ zoom_development = True
    pause 3
    $ develop_double(5)
    show erin think at dcp, left with dissolve
    "Like she's there." #this timing needs to improve
    show siobhan talk at dcs, right with Dissolve(1)
    Siob "I hear you... but I trust Peter. Something about his energy."
    show erin ponder at dcp, left with dissolve
    Erin "Normally, sure, but liking someone's 'energy' doesn't feel like enough to go on when it comes to life and death."
    show erin think at dcp
    Siob "Well, I'll go first and if I die or... come back weird, then you don't have to go."
    Siob "But if I do... well, I just want to say, I love your work."
    $ develop_double(10)
    show siobhan talk at dcs
    show erin smile at dcp
    Erin "Admit it, you'd never heard of me."
    Siob "Of course not. But Peter showed me some stuff. Showed me Gunnar's stuff too."
    Siob "I guess he's like, famous famous. Did you know?"
    show erin ponder at dcp
    Erin "Yeah."
    Erin "You seem excited for tomorrow."
    show erin smile at dcp
    Siob "Fuck yeah man. You aren't? You can be afraid and excited, you know that right?"
    $ develop_double(15)    
    show erin ponder at dcp
    show siobhan talk at dcs
    Erin "I just feel like we're trusting Peter quite a bit here and he's not telling us much."
    show erin ponder at dcp
    Siob "Like, what should he be telling us?"
    show erin ponder at dcp
    Erin "Well, so, what {i}is{/i} the Porter? Like how did he find it? Why should he trust it?"
    $ porterKnown = True
    Erin "He calls it a spirit but couldn't it be a demon or something?"
    show erin smile at dcp
    show siobhan talk at dcs
    Siob "Oh, yeah, I was worried about that too."
    $ develop_double(20)
    show erin smile at dcp
    show siobhan talk at dcs
    Siob "But I did some um, some digging. While you guys were doing that bonefire thing last night."
    Siob "I figured a guy like Peter writes absolutely everything down."
    Siob "To be fair, I also thought he'd like, lock all that shit up in a secret library or something."
    Siob "But it was all just out in his office."
    $ develop_double(25)
    show erin ponder at dcp
    show siobhan talk at dcs
    Erin "You read his stuff??"
    show erin smile at dcp
    Siob "SHHH!"
    Siob "But, yeah."
    Siob "You want me to tell you or what?"
    show erin ponder at dcp
    Erin "... yeah, I do."
    $ develop_double(30)
    show erin smile at dcp
    show siobhan talk at dcs
    Siob "He says it's an 'old spirit.' It's not from 'there,' it's from 'here.' That it came with this place."
    Siob "Or the woods nearby, he's not sure. But he's not the first to write about it."
    $ reachedEnd = True

label develop_kitchen_siobhan_overexposed:
    $ renpy.block_rollback()
    $ audio_warn_clock()
    if development_end_signalled:
        "You pull the photo out at the perfect time."
    else:
        "You know that if you keep this photo in any longer you will overexpose it."
    $ develop_overexposed(10)
    show erin ponder at left, dcp, dc_overexpose
    show siobhan talk at right, dcs, dc_overexpose
    $ photoRuined = True
    $ audio_overexpose_kitchen()
    $ corruption += 5
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    Erin "'The Porter.' Did Peter come up with that name?"
    Siob "No. It is his {b}Name{/b}."
    Siob "It is his {b}Function{/b}."
    $ develop_overexposed(20)
    show erin ponder at dcp, dc_overexpose
    show siobhan talk at dcs, dc_overexpose
    Siob "It was {b}TAKEN{/b} from him."
    $ audio_escalate(1)
    Siob "{sc=5}BUT HE WILL NOT BE CONTAINED{/sc}"
    $ audio_escalate(2)
    Erin "{sc=5}HE WILL HAVE WHAT IS HIS{/sc}!"
    $ develop_overexposed(30)
    show erin ponder at dcp, dc_overexpose
    show siobhan talk at dcs, dc_overexpose
    $ audio_escalate(3)
    "An icy chill grips your heart and you feel the room start to spin." #copypasted for now
    $ audio_remove_photo()
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    jump complete_kitchen_siobhan

label complete_kitchen_siobhan:  
    $ finish_development()
    if photoRuined == True:
        "You pull out the wrecked photograph. Now useless as a piece of art, it hopefully served you well as a source of information."
    else:
        "You pull out the print, a perfectly unremarkable of two people having a conversation in a kitchen."
        "A conversation that you, and possibly you alone, have heard."
    jump post_image_completion_dayone
#endregion

#region gunnar
label develop_kitchen_gunnar:
    $ start_double_exposing(OBJECT_IMAGE_GUNNAR)
    $ audio_start_kitchen()
    "As the man begins to fade into the doorway, his mouth immediately begins to move"
    $ audio_kitchen_melody("gunnar")
    $ develop_double(5)
    $ zoom_development = True
    pause 3
    show erin think at dcp, left with dissolve
    show gunnar points at dcs, right
    unk "I'm sure you've heard this before, but I will say it again."
    unk "Fame is the {i}worst{/i} thing that could happen to you."
    show erin ponder at dcp
    Erin "You're right. I {i}have{/i} heard that before."
    show erin think at dcp
    unk "Oh don't get me wrong, I understand you."
    $ develop_double(10)
    show gunnar points at dcs
    show erin ponder at dcp
    Erin "Do you?"
    show erin think at dcp
    unk "The fire to prove yourself. To do something great. It's pointless to ignore it."
    unk "I'm not saying you should stop chasing fame. May as well tell a moth to steer clear of candles."
    unk "I'm just telling you that you won't like it." #Note, I think Erin actually kinda thinks this is funny now. It was annoying at first.
    show erin ponder at dcp
    Erin "So what, embrace the flame?"
    show erin think at dcp
    unk "Isn't that what we're doing here?"
    unk "Chasing somthing that could very well destroy us?"
    $ develop_double(15)
    show erin ponder at dcp
    show gunnar points at dcs
    Erin "I'm not going to get destroyed. That's why I'm not going first."
    Erin "Is that what you're doing?"
    show erin think at dcp
    unk "Hah!"
    unk "Well..."
    unk "If Peter is right and this... place... really exists, then someone should to write about it."
    $ houseKnown = True
    $ develop_double(20)
    show erin think at dcp
    show gunnar points at dcs
    unk "And I suppose I can't stand the thought of it being anyone other than me."
    show erin ponder at dcp
    Erin "I think you might be vain, Gunnar. Has anyone ever told you that?"
    $ gunnarKnown = True
    show erin think at dcp
    Gunnar "I've seen your work. Very psychological, very personal. You must think your head is a very interesting place to be."
    Gunnar "My books have multiple points of view. And I try {i}{b}very{/i}{/b} hard to make sure none of them are my own."
    show erin ponder at dcp
    Erin "So you're saying I'm going to be in your book?"
    show erin think at dcp
    Gunnar "Who knows what's going to come out of this. Book. Poem. Alien scribblings. The Truth about the Creation of Time."
    Gunnar "But if you end up being interesting enough... sure, I might put you in."
    $ develop_double(25)
    show erin think at dcp
    show gunnar points at dcs
    Gunnar "But enough ramblings of a vain man. What drive Erin Darabondi to step through the threshold of the so-called Bright House?"
    show erin ponder at dcp
    Erin "..."
    Erin "I have no idea."
    show erin think at dcp
    Gunnar "Bullshit."
    show erin ponder at dcp
    Erin "Do you really trust Peter?"
    show erin think at dcp
    Gunnar "If he tells us this Bright House is safe, well, I trust he believes that."
    Gunnar "I know you - both of you - have just met him, but I've known him a long time. He knows what he's doing."
    Gunnar "Not in all things. I pray to God you never have to see his personal attempts at art."
    $ develop_double(30)
    show erin think at dcp
    show gunnar points at dcs
    Gunnar "He's got no talent of his own, but damned if he can't see it in others."
    $ reachedEnd = True

label develop_kitchen_gunnar_overexposed:    
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out at the perfect time."
    else:
        $ audio_warn_clock()
        "You know that if you keep this photo in any longer you will overexpose it."
    $ develop_overexposed(10)
    $ audio_overexpose_kitchen()
    show erin think at left, dcp, dc_overexpose
    show gunnar points at right, dcs, dc_overexpose
    $ photoRuined = True
    $ corruption += 5
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    Gunnar "There's a lot that he sees, Erin."
    Gunnar "But he can't see enough. Not what he needs to."
    $ audio_escalate(1)
    Gunnar "He is BLIND, just as I AM BLIND."
    $ develop_overexposed(20)
    $ audio_escalate(2)
    show erin think at dcp, dc_overexpose
    show gunnar points at dcs, dc_overexpose
    Gunnar "WHERE ARE MY {sc=2}EYES{/sc}, ERIN?"
    $ audio_escalate(3)
    Gunnar "{sc=3}WHERE ARE MY EYES, INTERLOPER{/sc}?"
    $ develop_overexposed(30)
    show erin think at dcp, dc_overexpose
    show gunnar points at dcs, dc_overexpose
    "An icy chill grips your heart and you feel the room start to spin." #copypasted for now
    "You feel like SOMETHING TERRIBLE has happened."
    jump complete_kitchen_gunnar

label complete_kitchen_gunnar: 
    $ finish_development()
    if photoRuined == True:
        "You pull out the wrecked photograph. Now useless as a piece of art, it hopefully served you well as a source of information."
    else:
        "You pull out the print, a perfectly unremarkable of two people having a conversation in a kitchen."
        "A conversation that you, and possibly you alone, have heard."
    jump post_image_completion_dayone
#endregion

#region peter
label develop_kitchen_peter:
    $ start_double_exposing(OBJECT_IMAGE_PETER)
    $ audio_start_kitchen()
    "The man from the negative begins to appear, fitting almost naturally into the scene."
    $ zoom_development = True
    pause 3
    $ develop_double(5)
    show erin think at dcp, left with dissolve
    show peter explain at dcs, right with dissolve
    $ audio_kitchen_melody("peter")
    unk "I've spoken with Siobhan. She'll be going through tonight. Gunnar is happy to go tomorrow, unless you'd prefer his spot."
    show peter listen at dcs
    show erin ponder at dcp
    Erin "That's fine with me."
    show erin think at dcp
    show peter playful at dcs
    unk "I'm pleased to see you're already working. And I'm honored that my kitchen is going to be a part of some great work of art."
    unk "This is what impresses me the most about you creative types. I'd assume a kitchen is just... boring, I don't know."
    unk "But I guess you see something in it."
    $ develop_double(10)
    show erin ponder at dcp
    show peter judges at dcs
    Erin "Maybe it'll make more sense when you see the piece."
    show peter listen at dcs
    Erin "Honestly, I don't even know what this piece is going to be either. Usually I've got something more like a plan."
    show peter judges at dcs
    Erin "But I think it'll be interesting to capture these images of {b}before{/b}. And then, once we go through... to the ..."
    show erin think at dcp
    show peter playful at dcs
    unk "Bright House, yes."
    show erin ponder at dcp
    show peter listen at dcs
    Erin "To the Bright House. To show how we see things after."
    Erin "If I go. You know I still - "
    show erin think at dcp
    show peter explain at dcs
    unk "It's okay. You don't have to be here if you don't want to. And you don't have to decide anything now."
    show erin smile at dcp
    show peter judges at dcs
    Erin "Thank you, Mr. Carlson"
    $ peterKnown = True
    $ develop_double(15)
    show peter explain at dcs
    show erin think at dcp
    Peter "Please, just Peter is fine."
    Peter "Anyway, I'll leave you to your work."
    show peter remark at dcs
    Peter "Dinner's at 5 if you want it and then Siobhan's going through at 7:00PM sharp. In the Grand hall."
    show peter judges at xflip, dcs
    hide peter with moveoutright
    show erin ponder at dcp
    Erin "Peter, wait!"
    show peter listen at dcs, right with moveinright
    Erin "I have a question."
    show erin think at dcp
    show peter remark at dcs
    Peter "I hope I have an answer."
    $ develop_double(20)
    show peter listen at dcs
    show erin ponder at dcp
    Erin "What is the Porter? I know you said a 'helper spirit' but I mean, how do you know that?"
    show erin think at dcp
    $ porterKnown = True
    Peter "Incredible amounts of research. And a good deal of personal experience."
    Peter "You will see it yourself, you know. Tonight. 7:00PM sharp, in fact."
    Peter "..."
    Peter "I know that is not adequate. But the truth is I don't think anything I say could be enough. You either believe me or don't."
    Peter "Or do several years of your own painstaking research."
    $ develop_double(25)
    show erin ponder at dcp
    show peter explain at dcs
    Erin "Fine. But I still don't fully understand why you need us here."
    Erin "I mean, I guess I can understand. You find something incredible, you want to share it."
    Erin "But is that really it?"
    show erin think at dcp
    Peter "This place is not just incredible. It would be incredible no matter what it looked like, of course. Another world, apart from our own..."
    $ houseKnown = True
    Peter "But I promise you, Erin, it is so much more. And that's the problem."
    Peter "If I had Gunnar's way with words, I could describe it to you so you'd understand."
    Peter "Or if I had your grasp of the symbolic image, or Siobhan's power to capture emotion..."
    $ develop_double(30)
    show peter explain at dcs
    show erin think at dcp
    Peter "I found the Bright House through nothing more than pure, stupid curiosity."
    $ reachedEnd = True

label develop_kitchen_peter_overexposed:
    $ audio_warn_clock()
    $ renpy.block_rollback()
    if development_end_signalled:
        "You pull the photo out at the perfect time."
    else:
        "You know that if you keep this photo in any longer you will overexpose it."
    $ develop_overexposed(10)
    $ audio_overexpose_kitchen()
    $ corruption += 5
    $ photoRuined = True
    if reachedEnd == False:
        "As the photo begins to become overexposed, you see the figures in the frame {b}jolt forwards{/b}, as if skipping time."
    show peter explain at right, dcs, dc_overexpose
    show erin think at left, dcp, dc_overexpose
    Peter "But now that I've found it, I find myself feeling so... inadequate before it."
    $ audio_escalate(1)
    Peter "Inadequate like the foolish, weak thing that I am."
    $ develop_overexposed(20)
    $ audio_escalate(2)
    show peter playful at dcs, dc_overexpose
    show erin think at dcp, dc_overexpose
    Peter "I am a {sc=4}Worm{/sc}, a {sc=4}Thief{/sc}!"
    $ develop_overexposed(30)
    $ audio_escalate(3)
    show peter explain at dcs, dc_overexpose
    show erin think at dcp, dc_overexpose
    Peter "He will Find me. He will find You too."
    Peter "{sc=4}THIS ALL MUST BE UNDONE{/sc}."
    jump complete_kitchen_peter

label complete_kitchen_peter: 
    $ finish_development()
    if photoRuined == True:
        "You pull out the wrecked photograph. Now useless as a piece of art, it hopefully served you well as a source of information."
    else:
        "You pull out the print, a perfectly unremarkable of two people having a conversation in a kitchen."
        "A conversation that you, and possibly you alone, have heard."
    jump post_image_completion_dayone
#endregion
#endregion

#region endofday1
label endOfDayOneChoices:
    stop photo_1
    stop photo_2
    stop photo_3
    scene darkroom_workspace red
    "You stand in the darkroom for a minute, dumbfounded, still processing what just happened."
    if corruption > 10:
        "You look at the photos you just printed. Out the corner of your eye you feel like you can see them moving still. But they aren't."
    else:
        "You look at the photos you just printed. No sign of anything out of the ordinary."
    "If you can trust what you've just seen, it seems like Erin was a part of something strange. Magical."
    "And you have no choice to believe that understanding what she was up to could explain what you've just seen."
    "On the other hand, Erin disappeared without a trace. Knowing more might be a very bad idea."
    if corruption > 10:
        play sfx_1 "eerie-1.mp3" volume 0.1
        play sfx_2 ["<silence 2>", "low-thud-single.mp3"] volume 0.2
        "You start to feel the hairs on the back of your neck raise. Like something is watching you."
        "Like something is in the darkroom with you."
    jump findPhoto

label findPhoto:
    hide nightAndDayPartial with Dissolve(.75)
    menu:
        set menuset
        "Search the room for further clues":
            "You spend hours searching the room. Supposedly her effects were left undisturbed, so it stands to reason you might find something that helps explain this."
            if corruption >= 10:
                play sfx_1 "eerie-1.mp3" volume 0.6
                play sfx_2 ["<silence 2>", "low-thud-single.mp3"] volume 0.2
                "The whole time, you feel that presense over your shoulder, watching you."
                "It's not a good feeling."
            elif corruption >= 5:
                play sfx_1 "eerie-1.mp3" volume 0.1
                "You start to feel the hairs on the back of your neck raise. Like something is watching you."
                "Like something is in the darkroom with you."
            "You find notes on projects, decades-old receipts for photography equipment, and other glimpses into her life that normally you'd find fascinating."
            "And then, tucked away in the back of a file nestled among old tax documents, you find something."
            play sfx_2 "low-thud-single.mp3" volume 0.5            
            show porter photo erin:
                zoom .9
                xalign 0.0
                yalign 0.5
                rotate 1.5
            #CANNONICALLY, THIS MEANS THAT ITS EYES HAVE BEEN RETURNED.
            "Something unsettling indeed."
            "The photo is printed on similar paper to the photos you found."
            "Scribbled hastily on the back in ballpoint pen, a title."
            "{font=ReenieBeanie-Regular.ttf}{size=+26}'restitution. atonement?'"
            play sfx_1 "slides/remove-2.mp3" volume 0.3
            "You slip it into your bag."
            hide porter photo erin
            jump findPhoto
        "Try printing another photograph":
            "The photo paper you found is gone, but you of course had brought some of your own."
            "You pull it out of your bag and attempt another exposure."
            show nightAndDayPartial with flash:
                zoom .9
                xalign 0.0
                yalign 0.5
                rotate 1.5
            "Nothing special happens."
            "It's just an ordinary photo."
            hide nightAndDayPartial
            jump findPhoto
    jump night1

label night1:
    stop ambiance_1 fadeout 2
    stop ambiance_2 fadeout 2
    scene bg bedroom light with dissolve
    "With your head swirling with questions, you head home to try and get some sleep."
    call night_crickets
    show bg bedroom sleep with Dissolve(1)
    "It comes slowly, but sleep does come."
    call nightmare_start
    scene bg nightmare:
        RaveLights
    with Dissolve(2.0)
    "..."    
    call nightmare_porter_appear
    show porter talk:
        subpixel True
        yalign .5
        xalign .5
        xanchor 0.5
        yanchor 0.25
        zoom 200
        alpha 0
        parallel:
            ease 2 alpha 1         
        parallel:
            ease 2 zoom 2
        linear 250 zoom 6
    play photo_1 "porter-single-voice.mp3" volume 0.2 noloop
    stop ambiance_3 fadeout 4.0
    unk "{sc=2}i see you{/sc}"
    unk "return what is {sc=1}mine{/sc}."
    unk "you {sc=2}WILL{/sc} return what is mine."
    play nightmare_2 ["porter-drums-1.mp3"] fadein 10 volume 1
    play sfx_1 "low-thud-single.mp3"
    show black_background:
        alpha 1.0
        pause 0.5
        linear 2.5 alpha 0
    show porter_eyes at porterBodyPart
    show porter dead with dissolve
    unk "{sc=4}my eyes{/sc}... kept in anothers head"
    play sfx_1 "low-thud-single.mp3"
    hide porter_eyes
    show black_background:
        alpha 1.0
        pause 0.5
        linear 2.5 alpha 0
    show porter_heart at porterBodyPart
    unk "{sc=4}my blood{/sc} thick in anothers veins"
    play nightmare_3 ["<sync nightmare_2>porter-drums-2.mp3", "porter-drums-2.mp3"] fadein 6 volume 0.8
    hide porter_heart
    show black_background:
        alpha 1.0
        pause 0.5
        linear 2.5 alpha 0
    show porter_hand at porterBodyPart
    unk "{sc=4}my hand{/sc} joined to another's arm"
    hide porter_hand
    show black_background:
        alpha 1.0
        pause 0.5
        linear 2.5 alpha 0
    show porter_tongue at porterBodyPart
    unk "{sc=4}my tongue{/sc} curled in anothers mouth"
    play sound "porter-single-voice-higher.mp3" volume 0.2
    play ambiance_1 "heartbeat.mp3" volume 1 fadein 2
    play drone_3 "bass-drone-2.mp3" volume 1 fadein 6
    unk "they could not run. and neither can you."
    unk "not from me"
    unk "and not from the {sc=4}bright"
    if corruption >= 15: #Calibrated currently for 3 papers, which means max corruption 15
        unk "i see it has already started to consume you"
        unk "you are {sc=4}careless{/sc}, like them"
        unk "it will be your end if you are not more careful"
    if corruption >= 5:
        unk "..."
        unk "you are already tainted"
        unk "do not be {sc=4}careless{/sc} as they were"
        unk "corruption may yet be avoided"
    else:
        unk "you have been careful..."
        unk "you have not pushed your luck as they did."
        unk "corrpution may yet be avoided"
    $_window_hide
    play sfx_1 "guitar-Ab.mp3"
    show porter dead at ZoomInto:
        WhiteNoise
    pause 1.1
    play sfx_3 "duet-Bb.mp3"
    scene darkroom_workspace red: #subpixel True? Use nightmare version?
        WhiteNoise
        size(1920, 1080) crop (0, 0, 1920, 1080)
        pause 1 #should be dissolve length
        easein 3 crop(770, 150, 360, 240)
    with Dissolve(1)
    play sfx_2 "gong-1.mp3"
    play sound "porter-wail.mp3"
    play ambiance_3 "crickets-1.mp3" volume 0.05 fadein 2 loop
    pause 2
    call nightmare_stop
    "You awake in a cold sweat. You try to sleep, but all you can see is that... face."
    "The face from the photo you found."
    "Like it is burned into your vision."
    "Was it trying to show you something?"
    stop music fadeout 2.0
    jump day2Start
    return
#endregion