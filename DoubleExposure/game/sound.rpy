init python:
    #audio channels
    renpy.music.register_channel("clock_1", "sfx", synchro_start=True)
    renpy.music.register_channel("clock_2", "sfx", synchro_start=True)

    renpy.music.register_channel("ambiance_1", "sfx", synchro_start=True)
    renpy.music.register_channel("ambiance_2", "sfx", synchro_start=True)
    renpy.music.register_channel("ambiance_3", "sfx", synchro_start=True)

    renpy.music.register_channel("sfx_1", "sfx", loop=False)
    renpy.music.register_channel("sfx_2", "sfx", loop=False)
    renpy.music.register_channel("sfx_3", "sfx", loop=False)

    renpy.music.register_channel("photo_1", "music", synchro_start=True)
    renpy.music.register_channel("photo_2", "music", synchro_start=True)
    renpy.music.register_channel("photo_3", "music", synchro_start=True)
    
    renpy.music.register_channel("nightmare_1", "music")
    renpy.music.register_channel("nightmare_2", "music")
    renpy.music.register_channel("nightmare_3", "music")

    renpy.music.register_channel("drone_1", "music")
    renpy.music.register_channel("drone_2", "music")
    renpy.music.register_channel("drone_3", "music")

    renpy.music.register_channel("melody", "music", synchro_start=True)

    config.auto_voice = "voice/{id}.mp3"

    def play_darkroom_light_atl(trans, st, at):
        play_darkroom_light()

    def play_darkroom_light():
        renpy.sound.play("light-click.mp3", channel="sfx_1")
        renpy.music.play("ambient-darkroom-light.mp3", channel="ambiance_1", fadein=1.0, loop=True, relative_volume=0.8)

    def play_slide_place(trans, st, at):
        renpy.sound.play(renpy.random.choice(slide_place_fx), channel="sfx_1")

    def play_slide_move(trans, st, at):
        renpy.sound.play(renpy.random.choice(slide_move_fx), channel="sfx_2")
    
    def play_slide_remove(trans, st, at):
        renpy.sound.play(renpy.random.choice(slide_remove_fx), channel="sfx_2")

    def play_slide_ratchet(trans, st, at):
        renpy.sound.play(renpy.random.choice(slide_rachet_fx), channel="sfx_3", relative_volume=0.6)

    def play_slide_ratchet_short(trans, st, at):
        renpy.sound.play(renpy.random.choice(slide_rachet_short_fx), channel="sfx_3", relative_volume=0.6)

    def audio_overexpose_tick():
        renpy.sound.play("low-thud-single.mp3", channel="audio", relative_volume=0.8)

    def audio_start_clock():
        renpy.music.play("clock-fast.mp3", channel="clock_1", relative_volume=0.05, loop=True, fadein=2.0)
    
    def audio_warn_clock():
        renpy.music.play(["<sync clock_1>clock-both.mp3", "clock-both.mp3"], channel="clock_2", loop=True, relative_volume=0.2, fadein=1.0)
        renpy.music.stop(channel="clock_1", fadeout=2.0)

    def audio_start_kitchen():
        renpy.music.play("photo-underscore-1.mp3", channel="photo_1", loop=True, fadein=3.0)

    def audio_overexpose_kitchen():
        renpy.music.play(["<sync photo_1>photo-underscore-1_a.mp3", "photo-underscore-1_a.mp3"], channel="photo_2", loop=True, fadein=5.0)

    def audio_kitchen_melody(char):
        if (char == "siobhan"):
            renpy.music.play(["<sync photo_1>photo-underscore-1_melody-guitar.mp3", "photo-underscore-1_melody-guitar.mp3"], channel="melody", loop=True, relative_volume=0.3, fadein=5.0)
        elif (char == "peter"):
            renpy.music.play(["<sync photo_1>photo-underscore-1_melody-horns.mp3", "photo-underscore-1_melody-horns.mp3"], channel="melody", loop=True, relative_volume=0.5, fadein=5.0)
        elif (char == "gunnar"):
            renpy.music.play(["<sync photo_1>photo-underscore-1_melody-1.mp3", "photo-underscore-1_melody-2.mp3"], channel="melody", loop=True, relative_volume=0.6, fadein=5.0)

    def audio_escalate(step):
        if (step == 1):
            renpy.music.play("bass-drone-1.mp3", channel="drone_1", loop=True, fadein=3)
        elif (step == 2):
            renpy.music.play("guitar-Ab.mp3", channel="audio")
            renpy.music.play("gong-3.mp3", channel="audio", relative_volume=0.6)
        elif (step == 3):
            renpy.music.stop("photo_1", 3)
            renpy.music.stop("photo_2", 3)
            renpy.music.stop("photo_3", 3)
            renpy.music.play("bass-drone-2.mp3", channel="drone_2", loop=True, fadein=1)
        
    def audio_remove_photo():
        renpy.music.play("splash-small-1.mp3", channel="sfx_2", loop=False, relative_volume=0.5)
        renpy.music.stop("clock_1")
        renpy.music.stop("clock_2")
        renpy.music.stop("drone_1")
        renpy.music.stop("drone_2")
        renpy.music.stop("drone_3")
        renpy.music.stop("photo_1", 0.5)
        renpy.music.stop("photo_2", 0.5)
        renpy.music.stop("photo_3", 0.5)
        renpy.music.stop("music", 4.0)
        renpy.music.stop("melody", 3.0)
        renpy.music.play("ambient-darkroom-light.mp3", channel="ambiance_1", fadein=0.2, loop=True)

    def audio_hard_stop_all():
        renpy.music.stop("clock_1")
        renpy.music.stop("clock_2")
        renpy.music.stop("drone_1")
        renpy.music.stop("drone_2")
        renpy.music.stop("drone_3")
        renpy.music.stop("photo_1")
        renpy.music.stop("photo_2")
        renpy.music.stop("photo_3")
        renpy.music.stop("melody")
        renpy.music.stop("music")
        renpy.music.play("ambient-darkroom-light.mp3", channel="ambiance_1", fadein=0.2, loop=True)

    # DAY 2

    def audio_sneaky():
        renpy.music.play("strings-loop-phase-1.mp3", channel="photo_1", relative_volume=0.8, loop=True, fadein=8.0)

    def audio_sneaky_overexpose():
        renpy.music.play(["<sync photo_1>strings-loop-phase-2.mp3", "strings-loop-phase-2.mp3"], channel="photo_2", loop=True, fadein=3.0)
        renpy.music.play(["<sync photo_1>strings-loop-drums.mp3", "strings-loop-drums.mp3"], channel="photo_3", loop=True, fadein=3.0)

    def audio_sneaky_melody(char):
        if (char == "siobhan"):
            renpy.music.play(["<sync photo_1>strings-loop-guitar.mp3", "strings-loop-guitar.mp3"], channel="melody", loop=True, relative_volume=1, fadein=5.0)
        #elif (char == "peter"):
        #    renpy.music.play(["<sync photo_1>photo-underscore-1_melody-horns.mp3", "photo-underscore-1_melody-horns.mp3"], channel="melody", loop=True, relative_volume=0.5, fadein=5.0)
        #elif (char == "gunnar"):
        #    renpy.music.play(["<sync photo_1>photo-underscore-1_melody-1.mp3", "photo-underscore-1_melody-2.mp3"], channel="melody", loop=True, relative_volume=0.6, fadein=5.0)
        #elif (char == "erin"):

    def audio_portal():
        renpy.music.play("strings-loop-phase-1.mp3", channel="photo_1", relative_volume=0.8, loop=True, fadein=8.0)

    def audio_portal_overexpose():
        renpy.music.play(["<sync photo_1>strings-loop-phase-2.mp3", "strings-loop-phase-2.mp3"], channel="photo_2", loop=True, fadein=3.0)
        renpy.music.play(["<sync photo_1>strings-loop-drums.mp3", "strings-loop-drums.mp3"], channel="photo_3", loop=True, fadein=3.0)

    def audio_portal_melody(char):
        if (char == "siobhan"):
            renpy.music.play(["<sync photo_1>strings-loop-guitar.mp3", "strings-loop-guitar.mp3"], channel="melody", loop=True, relative_volume=1, fadein=5.0)
        #elif (char == "peter"):
        #    renpy.music.play(["<sync photo_1>photo-underscore-1_melody-horns.mp3", "photo-underscore-1_melody-horns.mp3"], channel="melody", loop=True, relative_volume=0.5, fadein=5.0)
        #elif (char == "gunnar"):
        #    renpy.music.play(["<sync photo_1>photo-underscore-1_melody-1.mp3", "photo-underscore-1_melody-2.mp3"], channel="melody", loop=True, relative_volume=0.6, fadein=5.0)
        #elif (char == "erin"):

label night_crickets:
    play ambiance_3 "crickets-1.mp3" volume 0.1 fadein 2 loop
    return

label night_crickets_stop:
    stop ambiance_3 fadeout 3
    return

label nightmare_start:
    play sfx_1 "gong-3.mp3"
    play drone_1 "eerie-1.mp3" volume 0.4 fadein 4 noloop
    play nightmare_1 "<loop 3>porter-drone.mp3" fadein 3 volume 0.4
    play sfx_2 "heavy-breathing.mp3" volume 0.1 loop fadein 4.0
    return

label nightmare_porter_appear:
    play drone_2 "bass-drone-1.mp3" volume 0.5 fadein 2
    play sound "gong-1.mp3"
    play sfx_3 ["<silence 2>", "guitar-Ab.mp3"] volume 0.5
    play audio "porter-wail.mp3" volume 1.0
    return

label nightmare_stop:
    stop ambiance_1 fadeout 1
    stop nightmare_1 fadeout 1
    stop nightmare_2 fadeout 1
    stop nightmare_3 fadeout 1
    stop drone_1
    stop drone_2
    stop drone_3
    show bg bedroom light with flash
    play audio "breath-2.mp3"
    return

define slide_place_fx = [
    "slides/place-1.mp3",
    "slides/place-2.mp3"
]

define slide_move_fx = [
    "slides/move-1.mp3",
    "slides/move-2.mp3",
    "slides/move-3.mp3",
    "slides/move-4.mp3",
    "slides/move-5.mp3"
]

define slide_remove_fx = [
    "slides/remove-1.mp3",
    "slides/remove-2.mp3"
]

define slide_rachet_fx = [
    "slides/ratchet-close-1.mp3",
    "slides/ratchet-close-2.mp3"
]

define slide_rachet_short_fx = [
    "slides/ratchet-close-short-1.mp3",
    "slides/ratchet-close-short-2.mp3",
    "slides/ratchet-close-short-3.mp3"
]