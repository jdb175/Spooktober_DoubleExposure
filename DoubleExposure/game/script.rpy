#### Defining characters. Characters are global, so all files can see them ####
#Modern day
define you = Character("You") #You, the player!
define bud = Character("Buddy") #Your present day friend, will rename this later

#Now, photo world/90s people
define Erin = Character("Erin") #Erin Darabondi
define Siob = Character("Siobhan") #Siobhan
define Peter = Character("Peter") #Peter

#Utility "characters"
define tutorial = Character("", color = "#c8580d")
define temp = Character("PLACEHOLDER", color = "#d92703", what_color = "#d92703") #to describe art or animations not yet in the game.
define unk = Character("???", color = "#707070") #unknown to the player
define unk2 = Character("???", color = "#b59cd8") #second unknown, in case two unknowns speak

### Defining Variables ###
default menuset = set() #we initialize this every time we have a menu set (see Ren'Py docs for more info)
default corruption = 0
default curDevLevel = 0

default budLevel = 0 #friendship level with bud.

###images### 
#We may decide not to define these but just to use filenames later
#BGs
image darkroom_workspace = "placeholders/darkroom_temp1@2.jpg"
image darkroom_trays = "placeholders/darkroom_temp2.png"
#image photo1 = "placeholders/photo1_temp"


image background_negative = "placeholders/darkroom_temp2.png"

#characters
#image Siob_headshot = "placeholders/Siob_temp1.jpg"
#image Peter_headshot = "placeholders/Peter_temp1.png"
#image Gunnar_headshot = "placeholders/Gunnar_temp1.png"

#exposure
image BG1 = "exposuretest/bakgroundimage.png"
image Mask = "exposuretest/pallid_mask_nobpg.png" 
image BG1_WithMask = Composite(
    (1191,647),
    (0,0), "exposuretest/bakgroundimage.png",
    (0,0), "exposuretest/pallid_mask_nobpg.png" 
)
image black_background = Solid("#000000") 
image white_background = Solid("#fff")  

#effects
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

# The game always starts here. I like to put no story in this so it remains a pure starting point that jumps to whatever block we want
label start:
    $ config.developer = True #disable for public builds! This is a Ren'Py variable
    $ corruption = 0
    jump day_one
    return

label day_one:
    $ begin_day(Days.DAY_ONE)
    "Start exposing an image"
    jump projector_select_base_dayone

label projector_select_base_dayone:
    scene black_background
    $ start_enlarger()
    $ target_label = renpy.call_screen("enlarger_select_photo")        
    jump expression target_label

label projector_select_double_dayone:
    scene black_background
    "Now project the double exposure, it is day one"
    $ start_enlarger()
    $ target_label = renpy.call_screen("enlarger_select_photo")        
    jump expression target_label

label post_image_completion_dayone:
    scene black_background
    if(persistent.current_photo_paper > 0):
        if(persistent.current_photo_paper == 1):
            "You have just 1 piece of photo paper left"
        else:
            "You have [persistent.current_photo_paper] pieces of photo paper left"
        jump projector_select_base_dayone
    "You're out of paper"
    jump introScene

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

# image definitions are in daysconfig, you can expand by following the pattern in the current ones. Any amount of dialogue should work
# you can develop at any increments, but 60 is currently the max value beyond which you overexpose.

# TODO: easier display of the completed image


#region day one - house base
label develop_house:
    scene black_background with fade
    $ start_developing(BASE_IMAGE_HOUSE)
    $ develop(10)
    "One line"
    "two lines"
    $ develop(20)
    "One line"
    "two lines"
    $ develop(30)
    "One line"
    "two lines"
    if(persistent.development_end_signalled == False):
        "You know that this is when you are meant to take the photo out, if you want enough time to expose the negative"
    $ develop(40)
    "One line"
    "two lines"
    $ develop(50)
    "One line"
    "two lines"
    $ develop(60)
    "One line"
    "two lines"
    if(persistent.development_end_signalled == False):
        "If you keep this in any longer, you'll overexpose it"

label develop_house_overexposed:
    $ develop_overexposed(10)
    "One line"
    "two lines"
    $ develop_overexposed(20)
    "One line"
    "two lines"
    $ develop_overexposed(30)
    "One line"
    "two lines"
    jump complete_house

#region mask
label develop_house_mask:
    $ start_double_exposing(OBJECT_IMAGE_MASK)
    $ develop_double(10)
    "one"
    $ develop_double(20)
    "two"
    $ develop_double(30)
    "three"
    jump complete_house_mask

label develop_house_mask_overexposed:
    "You know that if you keep this photo in any longer you will overexpose it"
    $ develop_overexposed(10)
    "60+10 double"
    $ develop_overexposed(20)
    "60+20 double"
    $ develop_overexposed(30)
    "60+30 double"
    jump complete_house_mask

label complete_house:  
    $ finish_development()
    show BG1 at truecenter:
        matrixcolor None
    "Here is the completed image"    
    jump post_image_completion_dayone

label complete_house_mask:  
    $ finish_development()
    show BG1 at truecenter:
        matrixcolor None
    show Mask at truecenter:
        matrixcolor None
    "Here is the completed image"
    jump post_image_completion_dayone
#endregion

#region guy
label develop_house_guy:
    $ start_double_exposing(OBJECT_IMAGE_GUY)
    $ develop_double(10)
    "(guy) one"
    $ develop_double(20)
    "(guy) two"
    $ develop_double(30)
    "(guy) three"

label develop_house_guy_overexposed:
    "(guy) You know that if you keep this photo in any longer you will overexpose it"
    $ develop_overexposed(10)
    "(guy) 60+10 double"
    $ develop_overexposed(20)
    "(guy) 60+20 double"
    $ develop_overexposed(30)
    "(guy) 60+30 double"
    jump complete_house_guy

label complete_house_guy: 
    $ finish_development() 
    "(guy) Here is the completed image"
    jump post_image_completion_dayone
#endregion
#endregion

label introScene:
    scene black
    #Open on black?
    "Erin Darabondi."
    show Erin_headshot
    temp "SHOW: headshot of Erin" #Show a headshot photo of Erin
    "Many artists have inspired you, but it was Erin who made you want to *be* an artist."
    "Through her lens, strange and fantastic scenes became real."
    "The 'truth' of photography used to present impossibilities."
    hide Erin_headshot
    temp "SHOW: one of Erin's works, if we have the art budget" #Show a piece here, if we can.
    "A lot of your work ended up being different than hers. You wanted to carve your own path, of course."
    "But Erin's love of double exposure, in particular, stuck with you."
    temp "SHOW: Something new exposed over the current art piece" #Show something exposed over the piece.
    "Taking two images and making them one."
    "Maybe that's what caught the eye of the Darabondi Foundation."
    #Stretch goal – show a drawing of a letter in hand, or SOMETHING
    #Non-stretch goal, would be just to switch to the darkroom here, or back to the picture of Erin.
    "You could hardly believe it when you found out that you'd be a recipient of their first ever Young Artist Grant"
    temp "SHOW: The darkroom photo exposing view. A photo is developing." #show the darkroom.
    "A chance to work - to be *paid* to work - in Erin's old studio. To create works inspired by her."
    "By her legacy."
    temp "SHOW: as the photo develops, a terrifying face comes into view, one we will soon learn to be that of the Porter" #show the Porter appearing in the photo
    "A legacy which, for better or for worse, you are now a part of..."
    #TRANSITION TIME!
    "THREE DAYS EARLIER..."
    #show buddy. If this convo can happen outside of the darkroom (maybe a kitchen in the house?)
    temp "SHOW: Bud. If we can create a background elsewhere in Erin's house, this is happening there. Otherwise, it is happening in the wide of the darkroom."
    bud "I don't think she's dead."
    bud "No way."
    bud "This 'Young Artist Foundation?' She runs it. She just got tired of the limelight."
    you "She wasn't *that* big."
    you "And she had already started talking about her next series. Does that sound like someone ready to disappear?"
    bud "Ready or not, that's what happened."
    bud "Without a trace..."
    "Bud is the *other* grant winner. A collage artist, whose work, despite not being photography, much more closely mirrors Erin's."
    "Surreal themes and imagery, symbols dripping with meaning. Uncommon juxtapositions."
    "You thought it was a bit derivative at first. Now you're starting to think they're a bit obsessed."
    bud "Don't tell me you've never wondered what happened to her!"
    menu:
        "I prefer to focus on the art, not the artist":
            #show bud dejected or pensive
            bud "Yeah, of course. Me too. That's why we're here."
        "Of course. I've read some pretty crazy theories":
            bud "I know, right? There was a group that tried to do a podcast about it. They didn't find much."
            #this would be a great place for a CLUE! Maybe corruption if we run such a mechanic.
        "Why would she need to fake her disappearence to run her own foundation? You have to admit that makes no sense.":
            #show bud dejected or pensive
            bud "Yeah, I know. I just prefer to imagine everything has a happy ending, you know?"
            #this would be a great place for a CLUE! Maybe corruption if we run such a mechanic.
    bud "I was just thinking about maybe doing some sort of piece around her. Like, Erin."
    bud "What happened, or didn't happen. Putting her in places she isn't, but could have been."
    bud "A lot of my work was already kind of inspired by her, so I feel like I have to really do something different, you know?"
    bud "Especially since I'm getting paid now."
    bud "This is my first grant, actually."
    bud "What are you going to make? Do you know?"
    "Ah shit. To be honest, you've been struggling with that too."
    menu:
        "I'm actually really struggling with it.":
            "I know the grant stipulates that we can make whatever we want, so long as it is *in dialogue with Erin's work*"
            "Just specific enough to make things harder, but vague enough to get drowned in options"
            bud "Dude, it's freaking HARD, right? It's like, suddenly there's all this pressure."
            bud "Well, you can always start with the basics. You do photography, have you done much double exposure."
            "Not really, actually"
            bud "Hey, maybe start there!"
            temp "I'd like friendship with Bud to get you some clues or something... Maybe they stick with you during day 1 if you're nice, or you get their phone number..."
        "I've got some ideas.":
            bud "Okay, keep your secrets then."
            bud "Well, I should probably get to work. Got a long day of cutting stuff up, you know."
    "You should probably get to work too."
    jump darkroomIntro

### darkroom exploration vars
default lightOn = False
default papersGrabbed = False
default papersRemaining = 0 
default enlargeFirst = True
default traysFirst = True
default deskFirst = True

label darkroomIntro:
    show darkroom_workspace
    "You got a brief tour of the room yesterday, with someone from the foundation, but this is your chance to really settle in."
    "According to your grant representitive, the equipment has been mantained but otherwise things have been virtually untouched for the last 30 years."
    "They were hoping to turn the house into a museum but it never came through."
    "Which only makes it more exciting that you're suddenly allowed to poke around!"
    #temp "I like the idea of being able to click on objects in the room, and getting a brief rundown on them."
    #temp "Clickables are highlighted (no looking for secrets) and the scene would continue until you had clicked everything"

label darkroomIntro2:
    menu:
        "Check out the enlarger":
            #First time here
            if enlargeFirst == True:
                "The enlarger is an older model, old even for the 90s when Erin was working."
                "Oh wow, it looks like there are already some negatives in here!"
                tutorial "Use the arrow keys to change the active negative"
                temp "once this is working, you'll be able to see the following negatives:"
                show Siob_headshot at center:
                    matrixcolor InvertMatrix(1.0)
                "Oh, I think I know this person! Siobhan Kent. A contemporary of Erin. They had some sort of brief collaboration that never came to fruition."
                hide Siob_headshot
                show Gunnar_headshot at center:
                    matrixcolor InvertMatrix(1.0)
                "No idea who this is. This looks more like a personal shot than an art piece though."
                hide Gunnar_headshot
                show Peter_headshot at center:
                    matrixcolor InvertMatrix(1.0)
                "Same with this one."
                hide Peter_headshot
                show photo1
                temp "SHOW: A dramantically lit and composed photograph of a kitchen, with Erin looking out the window"
                "Oh, wow. Now *this* is a find!"
                "This photo was used to make her famous piece 'night and day.' The final version had a this crazy blazing sun images exposed over it, in the doorway."
                "So this is like, the original negative from that work. That's crazy!"
                "Maybe this is my first project? Maybe I print this and expose something else over it!"
                "Put my own spin on the image..."
                "Create dialog *with* Erin through fusing her art with mine."
                "Yeah, that sounds amazing!"
                hide photo1
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
            else:
                "Looks like I have what I need to print this!"
                jump photo1_firstDev
        "Check out the safelight" if lightOn == False:
            "Erin's safelight is a classic red. Full spectrum light will ruin any photo paper."
            "May as well turn this on now."
            temp "We'd switch from the full-light version of the scene to the red light version here."
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
                "You carefully unwrap the parcel and discover two luxurious pieces of print paper."
                "It feels a bit wrong, but the grant was emphatic that you could use her original materials, so you grab the papers, eager to see what Erin had been tinkering with."
                $ papersGrabbed = True
                $ papersRemaining = 2
            jump darkroomIntro2


label photo1_firstDev:
    "You slide one of the two pieces of photo paper under the enlarger and start a print of 'day and night'"
    scene darkroom_trays with flash
    "Next comes the developing liquid. You drop the print in the bath and wait."
    "If you're going to expose another photo, you'll want to pull this one out when it is half-developed."
    #Beginning default scene
    show photo1
    "The image begins to emerge, slowly at first."
    "Then, something else starts to happen."
    "Erin's lips part. Subtly, but unmistakably"
    "You hear her voice. Whether it's from the photo or in your head you can't quite tell."
    show Erin_headshot
    Erin "Everything we did was wrong. From the start."
    Erin "The Bright House. The Porter. I see that now."
    Erin "But there is a part of me that can hardly stop myself."
    Erin "When I picture that glorious light leaking into our world, I almost shudder with the rapture of the thought."
    Erin "I see our world for the dark place it is. Even in the bright of day it is filled with shadows."
    Erin "I would see it filled with light."
    #50% exposed
    "You pull your gaze away for a moment to check the clock. It's halfway done."
    "Technically you should be pulling the photo out now. The longer you leave it, the closer to overexposure it gets."
    "But... what if it stops?"
    "Or what if it doesn't stop?"
    "What is even happening here?!"
    menu:
        "Pull out the photo":
            hide photo1
            hide Erin_headshot
            $ curDevLevel = 50
            jump photo1_firstDouble
        "Keep watching":
            "Your heart pounding, you try to focus back on what you are seeing and hearing."
            "You can always decide to pull it out later, even if it ruins the image a bit."
    Erin "But it scares me."
    Erin "Because I am supposed to love this world. The world. My world."
    Erin "And with every day that passes I find it harder to see it for anything other than a shadow."
    Erin "The light within me makes all else dark."
    Erin "That is what I will show with this piece."
    #80% breakpoint
    "Despite the insanity of what you're witnessing, old habits die hard and you find yourself checking the clock."
    "You'd guess it is 80 percent of the way to fully developed - 30 percent more than you'd hoped for your double-exposure plan."
    "But does that even matter anymore? You already missed the window to do your original plan."
    menu:
        "Pull it out and salvage the print":
            hide photo1
            hide Erin_headshot
            $ curDevLevel = 80
            jump photo1_firstDouble
        "Keep watching":
            "You know that this will ruin the image... but to hell with the image!"
    temp "As this scene continues - as in any 'overexposed scene' - glitches start to appear. Music warps. Her smile changes."
    $ corruption += 5
    Erin "... I know I shouldn't be using the paper."
    Erin "I know I shouldn't be making it."
    Erin "And you shouldn't be using it..."
    "This is getting weird..."
    menu:
        "Pull out the print":
            hide photo1
            hide Erin_headshot
            jump photo1_ruined
        "Keep watching":
            "... its almost like she's talking to you now..."
    Erin "It's not your fault... but you should know..."
    Erin "that there is ONLY SO MUCH SKIN"
    Erin "ONLY SO MANY EYES"
    Erin "AND THE THINGS TAKEN WILL BE RETURNED"
    $ corruption += 10
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    jump photo1_ruined
    
label photo1_ruined:
    "Well, you've ruined this photo, but that hardly matters."
    jump photo1_secondBase

label photo1_firstDouble:
    "You grab your tongs and pull out the photo."
    "Immediately, whatever it was you were watching stops completely."
    "The photo looks as it should - a half-developed print of the negative you saw earlier."
    "The room is quiet, except for the sound of your heart pounding in your chest."
    "You don't know what you just saw but you're absolutely certain you saw it."
    "Right?"
    menu:
        "Finish the print":
            "Either way, it's clear - you have to learn more. And the best way to do that is to continue with your plan"
            "If Erin was doing... whatever this is... and she made double exposures... well, it's that all the more reason to make one too?"
    jump photo1_doubleMenu


label photo1_doubleMenu:
    "You make your way back to the enlarger. There were several negatives that you could overlay over this photograph pretty easily."
    "The question is, which one?"
    menu:
        "The image of Siobhan":
            jump photo1_addSiob
        "The image of the scruffy man":
            jump photo1_addGunnar
        "The image of the younger man":
            jump photo1_addPeter

label firstDoubleText:
    scene darkroom_trays with flash
    "You lower the print into the developing fluid, filled with a nervous anticipation."
    "Will it happen again?"
    return

label photo1_addSiob:
    call firstDoubleText
    show photo1
    show Erin_headshot at left
    show Siob_headshot at right
    "As Siobhan's head beings to appear, her lips begin to move, just as Erin's did."
    Siob "*I* don't know. I trust Peter. Something about his energy."
    Erin "Normally, sure, but liking someone's 'energy' doesn't feel like enough to go on when it comes to life and death."
    Siob "Well, I'll go first and if I die or... come back weird, then you don't have to go."
    Siob "But if I do... well, I just want to say, I love your work."
    if curDevLevel >= 80: # won't be hardcoded in real system, this is to cut you off if you took the other scene too far
        "The photo is starting to get overexposed. You ought to pull it out. If you think that matters anymore."
        menu:
            "Pull it out":
                hide Siob_headshot
                jump photo1_secondBase
            "Keep watching":
                jump photo1_addSiob_past100
    #if we're here, we weren't at 80.
    Erin "You're better."
    Siob "That's not true."
    Siob "Gunnar is the real big fish here anyway. Actually famous and all."
    Siob "No idea how Peter found us. Or why he chose us, you know?"
    Erin "I think he saw my series. 'Otherworld.' A title like that *had* to grab his attention."
    Siob "See, what's funny is that you seem to really believe in this stuff."
    Erin "You don't?"
    #Now we hit 100%
    "You look at the clock. The photo is fully developed. Leaving it in any further will ruin it."
    menu:
        "pull it out":
            hide Siob_headshot
            jump photo1_secondBase
        "Keep watching":
            jump photo1_addSiob_past100

label photo1_addSiob_past100:
    $ corruption += 5
    Siob "When I see it, I will, yeah."
    Siob "'The Porter.' Did Peter come up with that name?"
    Erin "No. It is His Name."
    Siob "It is His Function."
    Erin "It was taken From Him"
    Siob "BUT HE WILL NOT BE CONTAINED"
    "An icy chill grips your heart and you feel the room start to spin." #copypasted for now
    hide Siob_headshot
    hide Erin_headshot
    hide photo1
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    jump photo1_secondBase
    
    
label photo1_addGunnar:
    call firstDoubleText
    show photo1
    show Gunnar_headshot at right
    show Erin_headshot at left
    "As the man's head begins to appear, his mouth begins to move"
    unk "I'm sure you've heard this before, but I will say it again."
    unk "Fame is the *worst* thing that could happen to you."
    Erin "You're right. I have heard that before."
    unk "I'm serious! I've almost stopped writing entirely, in fact."
    Erin "So like, why are you here then?"
    if curDevLevel >= 80: # won't be hardcoded in real system, this is to cut you off if you took the other scene too far
        "The photo is starting to get overexposed. You ought to pull it out. If you think that matters anymore."
        menu:
            "Pull it out":
                hide Gunnar_headshot
                jump photo1_secondBase
            "Keep watching":
                jump photo1_addGunnar_past100
    #if we're here, we weren't at 80.
    unk "Hah!"
    unk "Well..."
    unk "If Peter is right and this... place... really exists, then someone should to write about it."
    unk "And I suppose I can't stand the thought of it being anyone other than me."
    Erin "Has anyone ever told you you've vain, Gunnar?"
    Gunnar "You are too, Erin, or you wouldn't be here."
    Erin "I have no idea why I'm here, if I'm being honest."
    Gunnar "I know you've both just met him, but I've known Peter a long time. He knows what he's doing."
    Gunnar "He's got no talent of his own, but damned if he can't see it in others."
    #Now we hit 100%
    "You look at the clock. The photo is fully developed. Leaving it in any further will ruin it."
    menu:
        "pull it out":
            hide Gunnar_headshot
            jump photo1_secondBase
        "Keep watching":
            jump photo1_addGunnar_past100


label photo1_addGunnar_past100:
    $ corruption += 5
    Gunnar "There's a lot that he sees, Erin."
    Gunnar "But he can't see enough. Not what he needs to."
    Gunnar "He is BLIND, just as I AM BLIND."
    Gunnar "WHERE ARE MY EYES, ERIN?"
    Gunnar "WHERE ARE MY EYES, INTERLOPER?"
    "An icy chill grips your heart and you feel the room start to spin." #copypasted for now
    hide Gunnar_headshot
    hide Erin_headshot
    hide photo1
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    jump photo1_secondBase

label photo1_addPeter:
    call firstDoubleText
    show photo1
    show Peter_headshot at right
    show Erin_headshot at left
    unk "I've spoken with Siobhan. She'll be going through tonight. Gunnar is happy to go tomorrow, unless you'd prefer his spot."
    Erin "That's fine with me."
    unk "Can I sit with you a moment? I'm usually pretty good at reading people and I really can't tell how you're doing."
    unk "you don't have to be here if you don't want to."
    Erin "Thank you, Mr. Carlson"
    Peter "Please, just Peter is fine."
    if curDevLevel >= 80: # won't be hardcoded in real system, this is to cut you off if you took the other scene too far
        "The photo is starting to get overexposed. You ought to pull it out. If you think that matters anymore."
        menu:
            "Pull it out":
                hide Peter_headshot
                jump photo1_secondBase
            "Keep watching":
                jump photo1_addPeter_past100
    #If we're here, we weren't at 80
    Peter "Enjoy your breakfast, and see you this evening, 5pm in the workroom."
    Erin "Wait, I have a question."
    Peter "I hope I have an answer"
    Erin "I still don't fully understand why you need us in the first place."
    Erin "I mean, I guess I can understand. You find something incredible, you want to share it."
    Peter "It's not just incredible. It is so much more. And that's the problem."
    Peter "If I had Gunnar's way with words, I could describe it to you so you'd understand."
    Peter "Or if I had your grasp of the symbolic image, or Siobhan's power to capture emotion..."
    Peter "I found the Bright House through nothing more than pure, stupid curiosity."
    #Now we hit 100%
    "You look at the clock. The photo is fully developed. Leaving it in any further will ruin it."
    menu:
        "pull it out":
            hide Peter_headshot
            jump photo1_secondBase
        "Keep watching":
            jump photo1_addPeter_past100

label photo1_addPeter_past100:
    Peter "But now that I've found it, I find myself feeling so... inadequate before it."
    Peter "Inadequate like the foolish, weak thing that I am."
    Peter "The Worm, the Thief, a Thief among Theives"
    Peter "He will Find me. He will find You too."
    Peter "THIS ALL MUST BE UNDONE."
    hide Peter_headshot
    hide photo1
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    jump photo1_secondBase


label photo1_secondBase:
    hide Erin_headshot
    hide photo1
    $ papersRemaining -= 1 #not the best place for this, but again, this is a hack
    "You pull out the photo. As before, it immediately stops moving and you are left with the quiet of the studio at night."
    if papersRemaining >= 1:
        "You have a single piece of photo paper left."
        "You could do this again... maybe see something different this time?"
        "For now, the only proper image you have to work with is the negative of 'night and day.' Maybe tomorrow you can try something else"
        "But as it's what you've got, you hurry back to the enlarger and start another print of 'night and day'"
        "As before, Erin's lips start to move and she begins to speak. She appears to be saying the same thing as the first time you developed the image"
        menu:
            "Watch it again":
                "You decide to watch it all again."
                jump photo1_firstDev
            "Wait until it is ready for a second exposure":
                "You watch the clock, only half-listening to Erin's speech, pulling out the photo as soon as possible to create a new exposure."
                jump photo1_doubleMenu
    else:
        "With that, you've used the last of the photo paper you found among Erin's things."
        "You run home, bringing some of your own back to the darkroom, but it's no use."
        "You just get a normal image."
        "Your head swirling with thoughts and questions, you feel like the best thing to do is head to bed."
        jump night1_intro

label night1_intro:
    temp "YOU HAVE A SPOOKY DREAM HERE AND DAY 1 ENDS!"
    return




################################################################ END OF SCRIPT (EVERYTHING AFTER THIS IS OLD, KEPT FOR POSTERITY/REVISING)

####OUT OF DATE####
label photo1_firstDevOOD1:
    "You slide one of the two pieces of photo paper under the enlarger and start a print of 'day and night'"
    scene darkroom_trays with flash
    "Next comes the developing liquid. You drop the print in the bath and wait."
    "If you're going to expose another photo, you'll want to pull this one out when it is half-developed."
    #Beginning default scene
    show photo1
    "The image begins to emerge, slowly at first."
    "Then, something else starts to happen."
    "In the photo, the figure by the window starts to move."
    show Erin_headshot
    "Erin."
    "She turns towards the camera and somehow, you hear her muttering to herself."
    Erin "Something like that..."
    "She walks towards the camera, disappearing out of frame."
    hide Erin_headshot
    temp "NOTE: No animation expected in the photo, but it would be great to fade Erin out of it at this moment."
    Erin "They need to really SEE it."
    Erin "Brighter, maybe. We'll try another."
    show Erin_headshot
    temp "SHOW: She reappears in frame, returning to her pose at the window"
    Erin "Everything is about to change, huh?"
    Erin "Let's see if that is true."
    hide Erin_headshot
    "You pull your gaze away for a moment to check the clock. It's halfway done."
    "Technically you should be pulling the photo out now. The longer you leave it, the closer to overexposure it gets."
    "But... what if it stops?"
    "Or what if it doesn't stop?"
    "What is even happening here?!"
    #50% breakpoint!
    menu:
        "Pull out the photo":
            hide photo1
            "You grab your tongs and pull out the photo."
            "Immediately, whatever it was you were watching stops completely."
            "The photo looks as it should - a half-developed print of the negative you saw earlier."
            "The room is quiet, except for the sound of your heart pounding in your chest."
            jump photo1_firstDouble
        "Keep watching":
            "Your heart pounding, you try to focus back on what you are seeing and hearing."
            "You can always decide to pull it out later, even if it ruins the image a bit."
    show Erin_headshot
    Erin "Shit. Erin, you're shaking."
    Erin "Well, if this is going to be my last photograph, it may as well be a good one."
    "She turns and looks at the doorway."
    Erin "Who is going to step through that door tonight?"
    Erin "And who is going to come back out?"
    Erin "..."
    Erin "There's something I like about working this way. Not having anything planned. Not knowing what I'll choose to share the frame with me."
    #100% breakpoint
    "Despite the insanity of what you're witnessing, old habits die hard and you find yourself checking the clock."
    "If your goal was to just print this photo you'd say it's time to pull it out of the bath, otherwise it will get ruined"
    "But does that even matter anymore? You already missed the window to do your original plan."
    # menu:
    #    "Finish the print":
    #     "Keep watching":
    return