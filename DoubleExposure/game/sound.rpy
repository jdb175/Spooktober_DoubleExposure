init python:
    #audio channels
    renpy.music.register_channel("ambiance_1", "sfx", synchro_start=True)
    renpy.music.register_channel("ambiance_2", "sfx", synchro_start=True)
    renpy.music.register_channel("ambiance_3", "sfx", synchro_start=True)

    renpy.music.register_channel("sfx_1", "sfx", loop=False)
    renpy.music.register_channel("sfx_2", "sfx", loop=False)
    renpy.music.register_channel("sfx_3", "sfx", loop=False)

    renpy.music.register_channel("photo_1", "music")
    renpy.music.register_channel("photo_2", "music")
    renpy.music.register_channel("photo_3", "music")
    
    renpy.music.register_channel("nightmare_1", "music")
    renpy.music.register_channel("nightmare_2", "music")
    renpy.music.register_channel("nightmare_3", "music")

    renpy.music.register_channel("drone_1", "music")
    renpy.music.register_channel("drone_2", "music")
    renpy.music.register_channel("drone_3", "music")

    renpy.music.register_channel("melody", "music")

    config.auto_voice = "voice/{id}.mp3"

    def play_slide_place(trans, st, at):
        renpy.play(renpy.random.choice(slide_place_fx), channel="sfx_1")

    def play_slide_move(trans, st, at):
        renpy.play(renpy.random.choice(slide_move_fx), channel="sfx_2")
    
    def play_slide_remove(trans, st, at):
        renpy.play(renpy.random.choice(slide_remove_fx), channel="sfx_2")

    def play_slide_ratchet(trans, st, at):
        renpy.play(renpy.random.choice(slide_rachet_fx), channel="sfx_3", relative_volume=0.6)

    def play_slide_ratchet_short(trans, st, at):
        renpy.play(renpy.random.choice(slide_rachet_short_fx), channel="sfx_3", relative_volume=0.6)

    def start_clock():
        renpy.music.play("clock-fast.mp3", channel="ambiance_1", loop=True, relative_volume=0.1, fadein=2.0)
    
    def warn_clock():
        renpy.music.play(["<sync ambiance_1>clock-both.mp3", "clock-both.mp3"], channel="ambiance_2", loop=True, relative_volume=0.1, fadein=1.0)
        renpy.music.stop(channel="ambiance_1", fadeout=3.0)

define config.main_menu_music = "ambient-darkroom-light.mp3"

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