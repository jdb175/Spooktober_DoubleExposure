
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
    #100% breakpoint
    "Despite the insanity of what you're witnessing, old habits die hard and you find yourself checking the clock."
    "If your goal was to just print this photo you'd say it's time to pull it out of the bath, otherwise it will get ruined"
    "But does that even matter anymore? You already missed the window to do your original plan."
    # menu:
    #    "Finish the print":
    #     "Keep watching":
    return