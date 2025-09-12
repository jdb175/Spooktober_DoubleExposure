
####OUT OF DATE STUFF – Being kept for posterity/potential future use####
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
    return


label photo1_firstDevOOD2:
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