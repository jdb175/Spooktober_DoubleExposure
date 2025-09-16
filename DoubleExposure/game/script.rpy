#### Defining characters. Characters are global, so all files can see them ####
#Modern day
define you = Character("You") #You, the player!
define bud = Character("Buddy") #Your present day friend, will rename this later
define porter = Character("The Porter") #the Porter itself!
define spirit = Character("Spirit?") #The porter if we don't know its name

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
default corruption = 0 #incremented as you overexpose photos. Checked whenever we feel like it.
default curDevLevel = 0 #used as a placeholder for how developed your current photo is. Will be replaced when the real photo system is added.
default budLevel = 0 #friendship level with bud.

#Branching story related variables
default gunnarKnown = False #You know Gunnar's name
default peterKnown = False #You know Peter's name
default houseKnown = False #You've heard them talk about going 'through a gate'
default porterKnown = False #You've heard them talk about the Porter
default photoFound = False #You found the hidden photo in Erin's house.

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
    $ budLevel = 0
    jump introScene
    return

label day_one:
    $ begin_day(Days.DAY_ONE)
    "Start exposing an image"
    jump projector_select_base_dayone

label projector_select_base_dayone:
    scene black_background
    $ start_enlarger()
    $ target_label = renpy.call_screen("enlarger_select_photo")   
    "You expose the paper, starting a print of 'day and night'"
    "Next comes the developing liquid. You drop the print in the bath and wait."
    "If you're going to expose another photo, you'll want to pull this one out when it is half-developed."
    jump expression target_label

#jumps here afer you're done with the base image
label projector_select_double_dayone:
    scene black_background #or something else
    if onFirstBase == True:
        "You grab your tongs and pull out the photo."
        "Immediately, whatever it was you were watching stops completely."
        "The photo looks as it should - a half-developed print of the negative you saw earlier."
        "The room is quiet, except for the sound of your heart pounding in your chest."
        "You don't know what you just saw but you're absolutely certain you saw it."
        "Right?"
        $ onFirstBase = False
    else:
        "You grab your tongs and pull out the photo."
    scene black_background
    "You make your way back to the enlarger. There were several negatives that you could overlay over this photo pretty easily."
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


#region day one - kitchen base
label develop_kitchen:
    scene black_background with fade
    $ start_developing(BASE_IMAGE_KITCHEN)
    $ develop(5)
    "The image begins to emerge, slowly at first."
    "Then, something else starts to happen."
    $ develop(10)
    "In the photo, the figure by the window starts to move."
    temp "ZOOM INTO PHOTO BACKGROUND"
    show Erin_headshot
    "Erin."
    "She turns towards the camera and somehow, you hear her muttering to herself"
    $ develop(15)
    Erin "Something like that..."
    "She walks towards the camera, disappearing out of frame."
    hide Erin_headshot
    Erin "Well shit, I do believe that's going to do it."
    $ develop(20)
    Erin "And you put something in the door and *bada bing bada boom* you got yourself a photo."
    show Erin_headshot
    Erin "I should probably shoot a few takes. Different expressions."
    $ develop(25)
    Erin "Since I have no idea how I'm going to be feeling after all of this."
    Erin "That's assuming, of course, you even come back at all..."
    if(persistent.development_end_signalled == False):
        "You pull your gaze away for a moment to check the clock. It's halfway done."
        "Technically you should be pulling the photo out now. The longer you leave it, the closer to overexposure it gets."
        "But... what if it stops?"
        "Or what if it doesn't stop?"
        "What is even happening here?!"
    $ develop(30)
    Erin "Shit. Erin, you're shaking."
    Erin "Well, if this is going to be my last photograph, it may as well be a good one."
    $ develop(35)
    "She turns and looks at the doorway."
    Erin "Maybe Peter is completely full of shit."
    $ develop(40)
    Erin "..."
    Erin "I don't think he is though."
    $ develop(45)
    Erin "And you've come too far to back out now. Whatever happens..."
    "Erin sighs."
    $ develop(50)
    if(persistent.development_end_signalled == False):
        "Despite the insanity of what you're witnessing, old habits die hard and you find yourself checking the clock."
        "There's still a chance to expose something over the image, although aleady it'll likely be a bit overdeveloped."
        "But does that even matter anymore?"
    $ develop(55)
    Erin "There's something I like about working this way. Not having anything planned. Not knowing what I'll choose to share the frame with me."
    $ develop(60)
    "The image is getting darker now. You're about to ruin it."

label develop_kitchen_overexposed:
    $ develop_overexposed(5)
    temp "As this scene continues - as in any 'overexposed scene' - glitches start to appear. Music warps. Her smile changes."
    $ corruption += 5
    Erin "You don't seem to care much about your images, do you?"
    Erin "Ruining a good print opportunity like this."
    $ develop_overexposed(10)
    Erin "I wouldn't make that mistake."
    "This is getting weird..."
    $ develop_overexposed(15)
    Erin "It's not your fault... but you should know..."
    Erin "that there is ONLY SO MUCH SKIN"
    $ develop_overexposed(20)
    Erin "ONLY SO MANY EYES"
    Erin "AND THE THINGS TAKEN WILL BE RETURNED"
    $ develop_overexposed(25)
    "An icy chill grips your heart and you feel the room start to spin."
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    jump complete_kitchen

#region Siobhan
label develop_kitchen_siobhan:
    "You lower the print into the developing fluid, filled with a nervous anticipation."
    "Will it happen again?"
    $ start_double_exposing(OBJECT_IMAGE_SIOBHAN)
    "For a moment, Siobhan looks awkward, overlayed crudely over the doorway."
    "Then, she starts to move. Her feet, partially suspended, touch the ground."
    "Like she's there."
    $ develop_double(5)
    show Siob_headshot at right
    Siob "*I* don't know. I trust Peter. Something about his energy."
    show Erin_headshot at left
    Erin "Normally, sure, but liking someone's 'energy' doesn't feel like enough to go on when it comes to life and death."
    Siob "Well, I'll go first and if I die or... come back weird, then you don't have to go."
    Siob "But if I do... well, I just want to say, I love your work."
    $ develop_double(10)
    Erin "Admit it, you'd never heard of me."
    Siob "Of course not. But Peter showed me some stuff. Showed me Gunnar's stuff too."
    Siob "I guess he's like, famous famous. Did you know?"
    Erin "Yeah."
    Erin "You seem excited for tomorrow."
    Siob "Fuck yeah man. You aren't? You can be afraid and excited, you know that right?"
    $ develop_double(15)
    Erin "I just feel like we're trusting Peter quite a bit here and he's not telling us much."
    Siob "Like, what should he be telling us?"
    Erin "Well, so, what *is* the Porter? Like how did he find it? Why should he trust it?"
    $ porterKnown = True
    Erin "He calls it a spirit but couldn't it be a demon or something?"
    Siob "Oh, yeah, I was worried about that too."
    $ develop_double(20)
    Siob "But I did some um, some digging. While you guys were doing that bonefire thing last night."
    Siob "I figured a guy like Peter writes absolutely everything down."
    Siob "To be fair, I also thought he'd like, lock all that shit up in a secret library or something."
    Siob "But it was all just out in his office."
    $ develop_double(25)
    Erin "You read his stuff??"
    Siob "SHHH!"
    Siob "But, yeah."
    Siob "You want me to tell you or what?"
    Eirn "... yeah, I do."
    $ develop_double(30)
    Siob "He says it's an 'old spirit.' It's not from 'there,' it's from 'here.' That it came with this place."
    Siob "Or the woods nearby, he's not sure. But he's not the first to write about it."
    jump complete_kitchen_siobhan

label develop_kitchen_siobhan_overexposed:
    "You know that if you keep this photo in any longer you will overexpose it"
    $ develop_overexposed(10)
    $ corruption += 5
    Erin "'The Porter.' Did Peter come up with that name?"
    Siob "No. It is His Name."
    Siob "It is His Function."
    $ develop_overexposed(20)
    Siob "It was taken From Him"
    Siob "BUT HE WILL NOT BE CONTAINED"
    Erin "HE WILL HAVE WHAT IS HIS"
    $ develop_overexposed(30)
    "An icy chill grips your heart and you feel the room start to spin." #copypasted for now
    hide Siob_headshot
    hide Erin_headshot
    hide photo1
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    jump complete_kitchen_siobhan

label complete_kitchen:  
    $ finish_development()
    show BG1 at truecenter:
        matrixcolor None
    "You grab your tongs and pull out the photo."
    "Immediately, whatever it was you were watching stops completely."
    "The photo looks as it should - a half-developed print of the negative you saw earlier."
    "The room is quiet, except for the sound of your heart pounding in your chest."
    "You don't know what you just saw but you're absolutely certain you saw it."
    "Right?"
    jump post_image_completion_dayone

label complete_kitchen_siobhan:  
    $ finish_development()
    show BG1 at truecenter:
        matrixcolor None
    show Mask at truecenter:
        matrixcolor None
    "As you pull out the image, it ceases to move."
    jump post_image_completion_dayone
#endregion

#region gunnar
label develop_kitchen_gunnar:
    $ start_double_exposing(OBJECT_IMAGE_GUNNAR)
    "As the man begins to fade into the doorway, his mouth immediately begins to move"
    $ develop_double(5)
    show Gunnar_headshot at right
    unk "I'm sure you've heard this before, but I will say it again."
    unk "Fame is the *worst* thing that could happen to you."
    show Erin_headshot at left
    Erin "You're right. I *have* heard that before."
    unk "Oh don't get me wrong, I understand you."
    $ develop_double(10)
    Erin "Do you?"
    unk "The fire to prove yourself. To do something great. It's pointless to ignore it."
    unk "I'm not saying you should stop chasing fame. May as well tell a moth to steer clear of candles."
    unk "I'm just telling you that you won't like it." #Note, I think Erin actually kinda thinks this is funny now. It was annoying at first.
    Erin "So what, embrace the flame"
    unk "Isn't that what we're doing here?"
    unk "Chasing somthing that could very well destroy us?"
    $ develop_double(15)
    Erin "I'm not going to get destroyed. That's why I'm not going first."
    Erin "Is that what you're doing?"
    unk "Hah!"
    unk "Well..."
    unk "If Peter is right and this... place... really exists, then someone should to write about it."
    $ houseKnown = True
    $ develop_double(20)
    unk "And I suppose I can't stand the thought of it being anyone other than me."
    Erin "I think you might be vain, Gunnar. Has anyone ever told you that?"
    $ gunnarKnown = True
    Gunnar "I've seen your work. Very psychological, very personal. You must think your head is a very interesting place to be."
    Gunnar "My books have multiple points of view. And I try *very* hard to make sure none of them are my own."
    Erin "So you're saying I'm going to be in your book?"
    Gunnar "Who knows what's going to come out of this. Book. Poem. Alien scribblings. The Truth about the Creation of Time."
    Gunnar "But if you end up being interesting enough... sure, I might put you in."
    $ develop_double(25)
    Gunnar "But enough ramblings of a vain man. What drive Erin Darabondi to step through the threshold of the so-called Bright House?"
    Erin "..."
    Erin "I have no idea."
    Gunnar "Bullshit."
    Erin "Do you really trust Peter?"
    Gunnar "If he tells us this Bright House is safe, well, I trust he believes that."
    Gunnar "I know you - both of you - have just met him, but I've known him a long time. He knows what he's doing."
    Gunnar "Not in all things. I pray to God you never have to see his personal attempts at art."
    $ develop_double(30)
    Gunnar "He's got no talent of his own, but damned if he can't see it in others."

label develop_kitchen_gunnar_overexposed:
    "You know that if you keep this photo in any longer you will overexpose it"
    $ develop_overexposed(10)
    $ corruption += 5
    Gunnar "There's a lot that he sees, Erin."
    Gunnar "But he can't see enough. Not what he needs to."
    Gunnar "He is BLIND, just as I AM BLIND."
    $ develop_overexposed(20)
    Gunnar "WHERE ARE MY EYES, ERIN?"
    Gunnar "WHERE ARE MY EYES, INTERLOPER?"
    $ develop_overexposed(30)
    "An icy chill grips your heart and you feel the room start to spin." #copypasted for now
    hide Gunnar_headshot
    hide Erin_headshot
    jump complete_kitchen_gunnar

label complete_kitchen_gunnar: 
    $ finish_development()
    "Almost without thinking, you grab the tongs and pull out the image."
    "You feel like SOMETHING TERRIBLE has happened."
    jump post_image_completion_dayone
#endregion

#region peter
label develop_kitchen_peter:
    $ start_double_exposing(OBJECT_IMAGE_PETER)
    $ develop_double(10)
    "(guy) one"
    $ develop_double(20)
    "(guy) two"
    $ develop_double(30)
    "(guy) three"

label develop_kitchen_peter_overexposed:
    "(guy) You know that if you keep this photo in any longer you will overexpose it"
    $ develop_overexposed(10)
    "(guy) 60+10 double"
    $ develop_overexposed(20)
    "(guy) 60+20 double"
    $ develop_overexposed(30)
    "(guy) 60+30 double"
    jump complete_kitchen_peter

label complete_kitchen_peter: 
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
    "Started getting a bit of attention as an artist. Showed at a few smaller galleries"
    "Which some days feels crazy, like you're a *real artist*"
    "And some days feels like you're so far from real success."
    "Erin's love of double exposure, in particular, stuck with you."
    temp "SHOW: Something new exposed over the current art piece" #Show something exposed over the piece.
    "Partially developing one photo, and then"
    "When Erin was doing it in the 90s, digital wasn't a thing. Her imagery stood out."
    "You still do it the old fashioned way, too. Film. A darkroom."
    "It was your double exposure pieces that caught the eye of the Darabondi Foundation."
    #Stretch goal – show a drawing of a letter in hand, or SOMETHING
    #Non-stretch goal, would be just to switch to the darkroom here, or back to the picture of Erin.
    "You could hardly believe it when you found out."
    "You were chosen as a recipient of their first ever Young Artist Grant"
    temp "SHOW: The darkroom photo exposing view. A photo is developing." #show the darkroom.
    "A chance to work - to be *paid* to work in Erin's old studio. With her old gear. To create works inspired by her."
    "By her legacy."
    temp "SHOW: as the photo develops, a terrifying face comes into view, one we will soon learn to be that of the Porter" #show the Porter appearing in the photo
    "A legacy which, for better or for worse, you are now a part of..."
    #TRANSITION TIME!
    temp "THREE DAYS EARLIER..."
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
            $ budLevel += 1
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
            $ budLevel += 1
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

default onFirstBase = True

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
    "You slide one of the two pieces of photo paper under the enlarger."
    "It feels coarse to the touch. Strangely thick."
    $ begin_day(Days.DAY_ONE)
    jump projector_select_base_dayone
    #"You expose the paper, starting a print of 'day and night'"
    #"Next comes the developing liquid. You drop the print in the bath and wait."
    #"If you're going to expose another photo, you'll want to pull this one out when it is half-developed."
    #"The image begins to emerge, slowly at first."
    #"Then, something else starts to happen."
    #"In the photo, the figure by the window starts to move."
    #show Erin_headshot
    #"Erin."
    #"She turns towards the camera and somehow, you hear her muttering to herself."
    #Erin "Something like that..."
    #"She walks towards the camera, disappearing out of frame."
    #hide Erin_headshot with fade
    #Erin "Well shit, I do believe that's going to do it."
    #Erin "And you put something in the door and *bada bing bada boom* you got yourself a photo."
    #show Erin_headshot
    #Erin "I should probably shoot a few takes. Different expressions."
    #Erin "Since I have no idea how I'm going to be feeling after all of this."
    #Erin "That's assuming, of course, you even come back at all..."
    #"You pull your gaze away for a moment to check the clock. It's halfway done."
    #"Technically you should be pulling the photo out now. The longer you leave it, the closer to overexposure it gets."
    #"But... what if it stops?"
    #"Or what if it doesn't stop?"
    #"What is even happening here?!"
    #50% breakpoint!
    #menu:
    #    "Pull out the photo":
    #        hide photo1
    #        "You grab your tongs and pull out the photo."
    #        "Immediately, whatever it was you were watching stops completely."
    #        "The photo looks as it should - a half-developed print of the negative you saw earlier."
    #        "The room is quiet, except for the sound of your heart pounding in your chest."
    #        jump photo1_firstDouble
    #    "Keep watching":
    #        "Your heart pounding, you try to focus back on what you are seeing and hearing."
    #        "You can always decide to pull it out later, even if it ruins the image a bit."
    #Erin "Shit. Erin, you're shaking."
    #Erin "Well, if this is going to be my last photograph, it may as well be a good one."
    #"She turns and looks at the doorway."
    #Erin "Maybe Peter is completely full of shit."
    #Erin "..."
    #Erin "I don't think he is though."
    #Erin "And you've come too far to back out now. Whatever happens..."
    #Erin "..."
    #Erin "There's something I like about working this way. Not having anything planned. Not knowing what I'll choose to share the frame with me."
    #80% breakpoint
    #"Despite the insanity of what you're witnessing, old habits die hard and you find yourself checking the clock."
    #"You'd guess it is 80 percent of the way to fully developed - 30 percent more than you'd hoped for your double-exposure plan."
    #"But does that even matter anymore? You already missed the window to do your original plan."
    #menu:
    #    "Pull it out and salvage the print":
    #        hide photo1
    #        hide Erin_headshot
    #        $ curDevLevel = 80
    #        jump photo1_firstDouble
    #    "Keep watching":
    #        "You know that this will ruin the image... but to hell with the image!"
    #temp "As this scene continues - as in any 'overexposed scene' - glitches start to appear. Music warps. Her smile changes."
    #$ corruption += 5
    #Erin "... I know I shouldn't be using the paper."
    #Erin "I know I shouldn't be making it."
    #Erin "And you shouldn't be using it..."
    #"This is getting weird..."
    #menu:
    #    "Pull out the print":
    #        hide photo1
    #        hide Erin_headshot
    #        jump photo1_ruined
    #    "Keep watching":
    #        "... its almost like she's talking to you now..."
    #Erin "It's not your fault... but you should know..."
    #Erin "that there is ONLY SO MUCH SKIN"
    #Erin "ONLY SO MANY EYES"
    #Erin "AND THE THINGS TAKEN WILL BE RETURNED"
    #$ corruption += 10
    #"An icy chill grips your heart and you feel the room start to spin."
    #"Almost without thinking, you grab the tongs and pull out the image."
    #"You feel like SOMETHING TERRIBLE has happened."
    #jump photo1_ruined
    #return
    
#label photo1_ruined:
#    #FIX ME!!!
#    "Well, you've ruined this photo, but that hardly matters."
#    jump photo1_secondBase

#label photo1_firstDouble:
#    "You grab your tongs and pull out the photo."
#    "Immediately, whatever it was you were watching stops completely."
#    "The photo looks as it should - a half-developed print of the negative you saw earlier."
#    "The room is quiet, except for the sound of your heart pounding in your chest."
#    "You don't know what you just saw but you're absolutely certain you saw it."
#    "Right?"
#    menu:
#        "Finish the print":
#            "Either way, it's clear - you have to learn more. And the best way to do that is to continue with your plan"
#            "If Erin was doing... whatever this is... and she made double exposures... well, it's that all the more reason to make one too?"
#    jump photo1_doubleMenu


#label photo1_doubleMenu:
#    "You make your way back to the enlarger. There were several negatives that you could overlay over this photograph pretty easily."
#    "The question is, which one?"
#    menu:
#        "The image of Siobhan":
#            jump photo1_addSiob
#        "The image of the scruffy man":
#            jump photo1_addGunnar
#        "The image of the younger man":
#            jump photo1_addPeter

#label firstDoubleText:
#    scene darkroom_trays with flash
#    "You lower the print into the developing fluid, filled with a nervous anticipation."
#    "Will it happen again?"
#    return

label photo1_addSiob:
    #call firstDoubleText
    #show photo1
    #show Erin_headshot at left
    #show Siob_headshot at right
    #"For a moment, Siobhan looks awkward, overlayed crudely over the doorway."
    #"Then, she starts to move. Her feet, partially suspended, touch the ground."
    #"Like she's there."
    #Siob "*I* don't know. I trust Peter. Something about his energy."
    #Erin "Normally, sure, but liking someone's 'energy' doesn't feel like enough to go on when it comes to life and death."
    #Siob "Well, I'll go first and if I die or... come back weird, then you don't have to go."
    #Siob "But if I do... well, I just want to say, I love your work."
    #Erin "Admit it, you'd never heard of me."
    #Siob "Of course not. But Peter showed me some stuff. Showed me Gunnar's stuff too."
    #Siob "I guess he's like, famous famous. Did you know?"
    Erin "Yeah."
    Erin "You seem excited for tomorrow."
    Siob "Fuck yeah man. You aren't? You can be afraid and excited, you know that right?"
    Erin "I just feel like we're trusting Peter quite a bit here and he's not telling us much."
    Siob "Like, what should he be telling us?"
    if curDevLevel >= 80: # won't be hardcoded in real system, this is to cut you off if you took the other scene too far
        "The photo is starting to get overexposed. You ought to pull it out. If you think that matters anymore."
        menu:
            "Pull it out":
                hide Siob_headshot
                jump photo1_secondBase
            "Keep watching":
                jump photo1_addSiob_past100
    #if we're here, we weren't at 80.
    Erin "Well, so, what *is* the Porter? Like how did he find it? Why should he trust it?"
    $ porterKnown = True
    Erin "He calls it a spirit but couldn't it be a demon or something?"
    Siob "Oh, yeah, I was worried about that too."
    Siob "But I did some um, some digging. While you guys were doing that bonefire thing last night."
    Siob "I figured a guy like Peter writes absolutely everything down."
    Siob "To be fair, I also thought he'd like, lock all that shit up in a secret library or something."
    Siob "But it was all just out in his office."
    Erin "You read his stuff??"
    Siob "SHHH!"
    Siob "But, yeah."
    Siob "You want me to tell you or what?"
    Eirn "... yeah, I do."
    Siob "He says it's an 'old spirit.' It's not from 'there,' it's from 'here.' That it came with this place."
    Siob "Or the woods nearby, he's not sure. But he's not the first to write about it."
    #Now we hit 100%
    "You look at the clock. The photo is fully developed. Leaving it in any further will ruin it."
    menu:
        "Pull it out":
            hide Siob_headshot
            jump photo1_secondBase
        "Keep watching":
            jump photo1_addSiob_past100

label photo1_addSiob_past100:
    $ corruption += 5
    Erin "'The Porter.' Did Peter come up with that name?"
    Siob "No. It is His Name."
    Siob "It is His Function."
    Siob "It was taken From Him"
    Siob "BUT HE WILL NOT BE CONTAINED"
    Erin "HE WILL HAVE WHAT IS HIS"
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
    Erin "You're right. I *have* heard that before."
    unk "Oh don't get me wrong, I understand you."
    Erin "Do you?"
    unk "The fire to prove yourself. To do something great. It's pointless to ignore it."
    unk "I'm not saying you should stop chasing fame. May as well tell a moth to steer clear of candles."
    unk "I'm just telling you that you won't like it." #Note, I think Erin actually kinda thinks this is funny now. It was annoying at first.
    Erin "So what, embrace the flame"
    unk "Isn't that what we're doing here?"
    unk "Chasing somthing that could very well destroy us?"
    Erin "I'm not going to get destroyed. That's why I'm not going first."
    Erin "Is that what you're doing?"
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
    $ houseKnown = True
    unk "And I suppose I can't stand the thought of it being anyone other than me."
    Erin "I think you might be vain, Gunnar. Has anyone ever told you that?"
    $ gunnarKnown = True
    Gunnar "I've seen your work. Very psychological, very personal. You must think your head is a very interesting place to be."
    Gunnar "My books have multiple points of view. And I try *very* hard to make sure none of them are my own."
    Erin "So you're saying I'm going to be in your book?"
    Gunnar "Who knows what's going to come out of this. Book. Poem. Alien scribblings. The Truth about the Creation of Time."
    Gunnar "But if you end up being interesting enough... sure, I might put you in."
    Gunnar "But enough ramblings of a vain man. What drive Erin Darabondi to step through the threshold of the so-called Bright House?"
    Erin "..."
    Erin "I have no idea."
    Gunnar "Bullshit."
    Erin "Do you really trust Peter?"
    Gunnar "If he tells us this Bright House is safe, well, I trust he believes that."
    Gunnar "I know you - both of you - have just met him, but I've known him a long time. He knows what he's doing."
    Gunnar "Not in all things. I pray to God you never have to see his personal attempts at art."
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
    unk "I'm pleased to see you're already working. And I'm honored that my kitchen is going to be a part of some great work of art."
    unk "This is what impresses me the most about you creative types. I'd assume a kitchen is just... boring, I don't know."
    unk "But I guess you see something in it."
    Erin "Maybe it'll make more sense when you see the piece."
    Erin "Honestly, I don't even know what this piece is going to be either. Usually I've got something more like a plan."
    Erin "But I think it'll be interesting to capture these images of *before*. And then, once we go through... to the ..."
    unk "Bright House, yes."
    Erin "To the Bright House. To show how we see things after."
    Erin "If I go. You know I still - "
    unk "It's okay. You don't have to be here if you don't want to. And you don't have to decide anything now."
    Erin "Thank you, Mr. Carlson"
    $ peterKnown = True
    Peter "Please, just Peter is fine."
    Peter "Anyway, I'll leave you to your work. Dinner's at 5 if you want it and then Siobhan's going through at 7:00PM sharp. In the Grand hall."
    hide Peter_headshot
    Erin "Peter, wait!"
    if curDevLevel >= 80: # won't be hardcoded in real system, this is to cut you off if you took the other scene too far
        "The photo is starting to get overexposed. You ought to pull it out. If you think that matters anymore."
        menu:
            "Pull it out":
                hide Peter_headshot
                jump photo1_secondBase
            "Keep watching":
                jump photo1_addPeter_past100
    #If we're here, we weren't at 80
    show Peter_headshot
    Erin "I have a question."
    Peter "I hope I have an answer."
    Erin "What is the Porter? I know you said a 'helper spirit' but I mean, how do you know that?"
    $ porterKnown = True
    Peter "Incredible amounts of research. And a good deal of personal experience."
    Peter "You will see it yourself, you know. Tonight. 7:00PM sharp, in fact."
    Peter "..."
    Peter "I know that is not adequate. But the truth is I don't think anything I say could be enough. You either believe me or don't."
    Peter "Or do several years of your own painstaking research."
    Erin "Fine. But I still don't fully understand why you need us here."
    Erin "I mean, I guess I can understand. You find something incredible, you want to share it."
    Erin "But is that really it?"
    Peter "This place is not just incredible. It would be incredible no matter what it looked like, of course. Another world, apart from our own..."
    $ houseKnown = True
    Peter "But I promise you, Erin, it is so much more. And that's the problem."
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
    #We finish up our second development and move on to the first night.
    else:
        "You stand in the darkroom for a minute, dumbfounded, still processing what just happened."
        if corruption > 5:
            "You look at the photos you just printed. Out the corner of your eye you feel like you can see them moving still. But they aren't."
        else:
            "You look at the photos you just printed. No sign of anything out of the ordinary."
        "If you can trust what you've just seen, it seems like Erin was a part of something strange. Magical."
        "And you have no choice to believe that understanding what she was up to could explain what you've just seen."
        "On the other hand, Erin disappeared without a trace. Knowing more might be a very bad idea."
        if corruption > 10:
            "You start to feel the hairs on the back of your neck raise. Like something is watching you."
            "Like something is in the darkroom with you."
    jump endOfDayOneChoices

label endOfDayOneChoices:
        menu:
            set menuset
            "Search the room for further clues":
                "You spend hours searching the room. Supposedly her effects were left undisturbed, so it stands to reason you might find something that helps explain this."
                if corruption >= 10:
                    "The whole time, you feel that presense over your shoulder, watching you."
                    "It's not a good feeling."
                elif corruption >= 5:
                    "You start to feel the hairs on the back of your neck raise. Like something is watching you."
                    "Like something is in the darkroom with you."
                "You find notes on projects, decades-old receipts for photography equipment, and other glimpses into her life that normally you'd find fascinating."
                "And then, tucked away in the back of a file nestled among old tax documents, you find something."
                temp "SHOW: a photo of a hideous, thin spirit, staring out of the darkness."
                temp "Double exposed over it are the faces that you've come to know from the negatives. They are overlayed strangely over the creature"
                $ photoFound = True
                "Something unsettling indeed."
                "The photo is printed on similar paper to the photos you found."
                "There is no note, no explanation."
                "You slip it into your bag."
                jump night1_intro
            "Try printing another photograph":
                "The photo paper you found is gone, but you of course had brought some of your own."
                "You pull it out of your back and attempt another exposure."
                "Nothing. Just a photo."
                jump endOfDayOneChoices
            "Go home. Make sense of this tomorrow":
                "It's late. You're alone in a creepy darkroom. You don't know what's happening. And frankly, none of this technically concerns you."
                jump night1_intro

label night1_intro:
    hide darkroom_trays with dissolve
    "Your head swirling with questions, you head home to try and get some sleep."
    "It comes slowly, but sleep does come."
    "..."
    temp "we show a face appearing here. A terrible face, one we may recognize. We hear heavy breathing"
    unk "..."
    unk "i see you" #Could we do a cool text effect here?
    unk "return what is mine"
    unk "you WILL return what is mine"
    if corruption >= 5:
        unk "..."
        unk "you are already tainted"
    if corruption >= 10:
        unk "you are already TOO BRIGHT"
    else:
        unk "before you are tainted"
    temp "we SHOW the eyes"
    unk "my eyes... kept in anothers head"
    temp "SHOW heart"
    unk "my blood thick in anothers veins"
    temp "SHOW hand"
    unk "my hand joined to another's arm"
    temp "SHOW tongue"
    unk "my tongue curled in anothers mouth"
    unk "they could not run. and neither can you."
    temp "SHOW Porter."
    temp "ZOOM forwards through its mouth, into the darkroom scene."
    #I want these to be burned somewhere, which would require art of a trash bin or oven or something, but we can just hide them in the enlarger for now.
    temp "ZOOM into a detail in the scene - a specific photo on the wall."
    temp "FLASH out of the scene"
    "You awake in a cold sweat. You try to sleep, but all you can see is that... face."
    if photoFound == True:
        "The face from the photo you found."
    "Like it is burned into your vision."
    "Was it trying to show you something?"
    jump day2Start
    return