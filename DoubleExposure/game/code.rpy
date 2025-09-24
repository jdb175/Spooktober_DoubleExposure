init python:   
    import random
    MIN_DEVELOP_TIME = 30
    MAX_OVEREXPOSURE_TIME = 30
    MAX_DEVELOP_TIME = 60
    SECONDARY_MAX_DEVELOP_TIME = 30
    ENLARGER_LABEL_BASE = "projector_select_base"
    ENLARGER_LABEL_DOUBLE = "projector_select_double"

    def begin_day(day : Days):
        print("Beginning Day")
        # These are fake persistents, to avoid that renpy seems to rollback variable states on backtrack which we don't want
        # The only downside seems to be dev reloading is broken...

        # general control flow variables
        persistent.current_day = day.value
        persistent.current_photo_paper = DAY_CONFIGS[Days(day)].photo_paper        
        persistent.current_base_image = None
        persistent.current_secondary_image = None

        # development state
        persistent.base_development = 0 # Current level of base photo development, when it exceeds MAX_DEVELOP_TIME we jump to overexposure
        persistent.last_base_development = 0 # Previous level of base development, used for visual effects
        persistent.secondary_development = 0 # Current level of secondary photo development, used for visual effects
        persistent.over_exposure = 0 # Current level of overexposure for visual effects
        persistent.can_stop_developing = False # Whether the "stop developing" button should be active
        persistent.development_end_signalled = False # Whether there is a pening request to stop development. Used because hitting the button doesn't jump out of in-process dialogue
        persistent.is_double_exposing = False # Whether we are developing a double exposure
        persistent.development_end_target = "DEFAULT_DEVELOPMENT_END_LABEL" # The label that will be jumped to when current development is ended
        persistent.development_double_end_target = "DEFAULT_DEVELOPMENT_END_LABEL" # The label that will be jumped to when current development is ended
        persistent.development_overexpose_target = "DEFAULT_OVEREXPOSE_LABEL" # The label that will be jumped to when current development overexposes

        # enlarger state
        persistent.projected_image = None # The image that is currently selected in the enlarger
        persistent.enlarger_image_index = 0 # The image of the current selection in the enlarger
        persistent.enlarger_jump_label = "DEFAULT_ENLARGER_JUMP_LABEL" # The label to jump to after completing the current enlarger session
        persistent.enable_cycling = False # should cycling be enabled


#region development
    def start_developing(image : EnlargerImage):
        audio_start_clock()
        print("starting development for ", image.label)
        renpy.scene()
        renpy.show("black")
        renpy.block_rollback()
        store.zoom_development = False
        store.zoom_development_transitioned = False
        persistent.current_base_image = image
        persistent.current_secondary_image = None
        persistent.base_development = 0
        persistent.last_base_development = 0
        persistent.secondary_development = 0
        persistent.over_exposure = 0.0
        persistent.can_stop_developing = False
        persistent.development_end_signalled = False
        persistent.development_end_target = ENLARGER_LABEL_DOUBLE + "_" + persistent.current_day
        persistent.development_overexpose_target = "develop_" + image.label + "_overexposed"
        persistent.is_double_exposing = False
        renpy.show_screen("clock")
        renpy.show_screen("develop_photo", _layer="master")

    def stop_developing():
        print("Flagging to end development after the next line")
        persistent.development_end_signalled = True
        persistent.can_stop_developing = False

    def stop_developing_instant():
        if(persistent.base_development < MIN_DEVELOP_TIME):
            persistent.last_base_development = MIN_DEVELOP_TIME
            persistent.base_development = MIN_DEVELOP_TIME
        
        persistent.development_end_signalled = True
        persistent.can_stop_developing = False
        _checkPendingJump()


    def start_double_exposing(image : EnlargerImage):
        audio_start_clock()
        print("starting double exposure for ", image.label, ", base image is ", persistent.current_base_image.label)
        renpy.scene()
        renpy.show("black")
        renpy.show_screen("clock")
        renpy.show_screen("develop_photo", _layer="master")
        renpy.block_rollback()
        store.zoom_development = False
        store.zoom_development_transitioned = False
        persistent.current_secondary_image = image
        persistent.development_overexpose_target = "develop_" + persistent.current_base_image.label + "_" + image.label + "_overexposed"
        persistent.development_end_target =  "complete_" + persistent.current_base_image.label
        persistent.development_double_end_target = "complete_" + persistent.current_base_image.label + "_" + image.label
        persistent.is_double_exposing = True

    def _checkPendingJump(checkExposure = True):
        print("checking if there is a jump pending, ", persistent.development_end_signalled, ", checKExposure is ", checkExposure)

        if(persistent.development_end_signalled):
            persistent.development_end_signalled = False
            persistent.can_stop_developing = True
            renpy.hide_screen("clock")
            renpy.hide_screen("develop_photo")      
            renpy.scene()
            renpy.show("black")
            renpy.block_rollback()  
            renpy.jump(persistent.development_end_target)
    
        if(persistent.base_development >= MAX_DEVELOP_TIME and checkExposure):
            persistent.development_end_signalled = False
            renpy.scene()
            renpy.show("black")
            renpy.show_screen("clock")
            renpy.show_screen("develop_photo")
            renpy.block_rollback()  
            renpy.jump(persistent.development_overexpose_target)

    def _develop(base_development: int = -1, secondary_development: int = -1):
        print("developing base:", base_development, ", secondary", secondary_development)
        _checkPendingJump()

        increment : int = 0

        if(base_development < 0):
            increment = secondary_development - persistent.secondary_development
        else:
            increment = base_development - persistent.base_development

        if(increment < 0):
            persistent.can_stop_developing = False
        else:
            if(increment > 0):
                persistent.last_base_development = persistent.base_development
                persistent.base_development += increment

                if(persistent.is_double_exposing):
                    persistent.secondary_development += increment
                    persistent.development_end_target = persistent.development_double_end_target
                
                persistent.can_stop_developing = persistent.base_development >= MIN_DEVELOP_TIME
    
    def develop_overexposed(overexposure: int):
        print("overexposing:", overexposure)
        audio_overexpose_tick()
        _checkPendingJump(False)
        persistent.can_stop_developing = False
        persistent.over_exposure = overexposure #/ MAX_DEVELOP_TIME

    def develop_double(development: int):
        _develop(secondary_development = development)

    def develop(development: int):
        _develop(base_development = development)

    def finish_development():
        audio_remove_photo()
        print("Finishing Development")
        renpy.scene()
        renpy.show("black")
        renpy.hide_screen("clock")
        renpy.hide_screen("develop_photo")
        renpy.show_screen("final_photo", 
            base_image=persistent.current_base_image, 
            secondary_image=persistent.current_secondary_image, 
            base_development=persistent.base_development, 
            secondary_development=persistent.secondary_development, 
            overexposure=persistent.over_exposure,
            _layer="master")
        renpy.block_rollback()
        persistent.current_base_image = None
        persistent.current_secondary_image = None

#endregion

#region enlarger
    def populate_enlarger_data():
        print("Populating enlarger data")
        images_len = 0
        if(persistent.current_base_image):
            object_images = DAY_CONFIGS[Days(persistent.current_day)].object_images
            images_len = len(object_images)
            persistent.projected_image = object_images[persistent.enlarger_image_index]
            persistent.enlarger_jump_label = DEVELOP_LABEL_PREFIX + persistent.current_base_image.label + "_" + object_images[persistent.enlarger_image_index].label
        else:
            base_images = DAY_CONFIGS[Days(persistent.current_day)].base_images
            images_len = len(base_images)
            persistent.projected_image = base_images[persistent.enlarger_image_index]
            persistent.enlarger_jump_label = DEVELOP_LABEL_PREFIX + base_images[persistent.enlarger_image_index].label

        persistent.enable_cycling = (images_len > 1)

    def start_enlarger():
        print("Starting enlarger")
        renpy.block_rollback()
        if not (persistent.current_base_image):
            persistent.current_photo_paper-= 1

        persistent.enlarger_image_index = 0
        populate_enlarger_data()
    
    def stop_enlarger():
        print("Stopping enlarger")
        renpy.block_rollback()

    def cycle_enlarger(sign: int):   
        print("Cycling enlarger")
        images = []
        if(persistent.current_base_image):
            images = DAY_CONFIGS[Days(persistent.current_day)].object_images
        else:
            images = DAY_CONFIGS[Days(persistent.current_day)].base_images

        if(len(images) == 1):
            return

        persistent.enlarger_image_index += sign
        persistent.enlarger_image_index = persistent.enlarger_image_index % len(images)

        populate_enlarger_data()

        print("Cycling ", sign, ": ", persistent.enlarger_image_index, "/ ", len(images))
        renpy.hide_screen("enlarger_select_photo")
        renpy.show_screen("enlarger_select_photo")
#endregion