# general control flow variables
default current_day = Days.DAY_ONE
default current_photo_paper = DAY_CONFIGS[Days(Days.DAY_ONE)].photo_paper        
default current_base_image = None
default current_secondary_image = None
# development state
default base_development = 0 # Current level of base photo development, when it exceeds MAX_DEVELOP_TIME we jump to overexposure
default last_base_development = 0 # Previous level of base development, used for visual effects
default secondary_development = 0 # Current level of secondary photo development, used for visual effects
default over_exposure = 0 # Current level of overexposure for visual effects
default can_stop_developing = False # Whether the "stop developing" button should be active
default development_end_signalled = False # Whether there is a pending request to stop development. Used because hitting the button doesn't jump out of in-process dialogue
default is_double_exposing = False # Whether we are developing a double exposure
default development_end_target = "DEFAULT_DEVELOPMENT_END_LABEL" # The label that will be jumped to when current development is ended
default development_double_end_target = "DEFAULT_DEVELOPMENT_END_LABEL" # The label that will be jumped to when current development is ended
default development_overexpose_target = "DEFAULT_OVEREXPOSE_LABEL" # The label that will be jumped to when current development overexposes
# enlarger state
default projected_image = None # The image that is currently selected in the enlarger
default enlarger_image_index = 0 # The image of the current selection in the enlarger
default enlarger_jump_label = "DEFAULT_ENLARGER_JUMP_LABEL" # The label to jump to after completing the current enlarger session
default enable_cycling = False # should cycling be enabled

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
        store.current_day = day.value
        store.current_photo_paper = DAY_CONFIGS[Days(day)].photo_paper        
        store.current_base_image = None
        store.current_secondary_image = None

        # development state
        store.base_development = 0 # Current level of base photo development, when it exceeds MAX_DEVELOP_TIME we jump to overexposure
        store.last_base_development = 0 # Previous level of base development, used for visual effects
        store.secondary_development = 0 # Current level of secondary photo development, used for visual effects
        store.over_exposure = 0 # Current level of overexposure for visual effects
        store.can_stop_developing = False # Whether the "stop developing" button should be active
        store.development_end_signalled = False # Whether there is a pening request to stop development. Used because hitting the button doesn't jump out of in-process dialogue
        store.is_double_exposing = False # Whether we are developing a double exposure
        store.development_end_target = "DEFAULT_DEVELOPMENT_END_LABEL" # The label that will be jumped to when current development is ended
        store.development_double_end_target = "DEFAULT_DEVELOPMENT_END_LABEL" # The label that will be jumped to when current development is ended
        store.development_overexpose_target = "DEFAULT_OVEREXPOSE_LABEL" # The label that will be jumped to when current development overexposes

        # enlarger state
        store.projected_image = None # The image that is currently selected in the enlarger
        store.enlarger_image_index = 0 # The image of the current selection in the enlarger
        store.enlarger_jump_label = "DEFAULT_ENLARGER_JUMP_LABEL" # The label to jump to after completing the current enlarger session
        store.enable_cycling = False # should cycling be enabled


#region development
    def start_developing(image : EnlargerImage):
        print("starting development for ", image.label)
        renpy.scene()
        renpy.show("black")
        renpy.block_rollback()
        store.zoom_development = False
        store.zoom_development_transitioned = False
        store.current_base_image = image
        store.current_secondary_image = None
        store.base_development = 0
        store.last_base_development = 0
        store.secondary_development = 0
        store.over_exposure = 0.0
        store.can_stop_developing = False
        store.development_end_signalled = False
        store.development_end_target = ENLARGER_LABEL_DOUBLE + "_" + store.current_day
        store.development_overexpose_target = "develop_" + image.label + "_overexposed"
        store.is_double_exposing = False
        renpy.show_screen("clock")
        renpy.show_screen("develop_photo", _layer="master")

    def stop_developing():
        print("Flagging to end development after the next line")
        store.development_end_signalled = True
        store.can_stop_developing = False

    def stop_developing_instant():
        if(store.base_development < MIN_DEVELOP_TIME):
            store.last_base_development = MIN_DEVELOP_TIME
            store.base_development = MIN_DEVELOP_TIME
        
        store.development_end_signalled = True
        store.can_stop_developing = False
        _checkPendingJump()


    def start_double_exposing(image : EnlargerImage):
        print("starting double exposure for ", image.label, ", base image is ", store.current_base_image.label)
        renpy.scene()
        renpy.show("black")
        renpy.show_screen("clock")
        renpy.show_screen("develop_photo", _layer="master")
        renpy.block_rollback()
        store.zoom_development = False
        store.zoom_development_transitioned = False
        store.current_secondary_image = image
        store.development_overexpose_target = "develop_" + store.current_base_image.label + "_" + image.label + "_overexposed"
        store.development_end_target =  "complete_" + store.current_base_image.label
        store.development_double_end_target = "complete_" + store.current_base_image.label + "_" + image.label
        store.is_double_exposing = True

    def _checkPendingJump(checkExposure = True):
        print("checking if there is a jump pending, ", store.development_end_signalled, ", checKExposure is ", checkExposure)

        if(store.development_end_signalled):
            store.development_end_signalled = False
            store.can_stop_developing = False
            renpy.hide_screen("clock")
            renpy.hide_screen("develop_photo")      
            renpy.scene()
            renpy.show("black")
            renpy.block_rollback()  
            renpy.jump(store.development_end_target)
    
        if(store.base_development >= MAX_DEVELOP_TIME and checkExposure):
            store.development_end_signalled = False
            #renpy.scene()
            #renpy.show("white")
            #renpy.show_screen("clock")
            #renpy.show_screen("develop_photo", _layer="master")
            renpy.block_rollback()  
            renpy.jump(store.development_overexpose_target)

    def _develop(base_development: int = -1, secondary_development: int = -1):
        print("developing base:", base_development, ", secondary", secondary_development)
        _checkPendingJump()
        renpy.block_rollback()

        increment : int = 0

        if(base_development < 0):
            increment = secondary_development - store.secondary_development
        else:
            increment = base_development - store.base_development

        if(increment < 0):
            store.can_stop_developing = False
        else:
            if(increment > 0):
                store.last_base_development = store.base_development
                store.base_development += increment

                if(store.is_double_exposing):
                    store.secondary_development += increment
                    store.development_end_target = store.development_double_end_target
                
                store.can_stop_developing = store.base_development >= MIN_DEVELOP_TIME and (store.base_development >= 60 or not store.is_double_exposing)
    
    def develop_overexposed(overexposure: int):
        print("overexposing:", overexposure)
        _checkPendingJump(False)
        store.can_stop_developing = False
        store.over_exposure = overexposure #/ MAX_DEVELOP_TIME

    def develop_double(development: int):
        _develop(secondary_development = development)

    def develop(development: int):
        _develop(base_development = development)

    def finish_development():
        print("Finishing Development")
        renpy.scene()
        renpy.hide_screen("clock")
        renpy.show("black")
        renpy.hide_screen("develop_photo")
        renpy.show_screen("final_photo", 
            base_image=store.current_base_image, 
            secondary_image=store.current_secondary_image, 
            base_development=store.base_development, 
            secondary_development=store.secondary_development, 
            overexposure=store.over_exposure,
            _layer="master")
        renpy.block_rollback()
        store.current_base_image = None
        store.current_secondary_image = None

#endregion

#region enlarger
    def populate_enlarger_data():
        print("Populating enlarger data")
        images_len = 0
        if(store.current_base_image):
            object_images = DAY_CONFIGS[Days(store.current_day)].object_images
            images_len = len(object_images)
            store.projected_image = object_images[store.enlarger_image_index]
            store.enlarger_jump_label = DEVELOP_LABEL_PREFIX + store.current_base_image.label + "_" + object_images[store.enlarger_image_index].label
        else:
            base_images = DAY_CONFIGS[Days(store.current_day)].base_images
            images_len = len(base_images)
            store.projected_image = base_images[store.enlarger_image_index]
            store.enlarger_jump_label = DEVELOP_LABEL_PREFIX + base_images[store.enlarger_image_index].label

        store.enable_cycling = (images_len > 1)

    def start_enlarger():
        print("Starting enlarger")
        renpy.block_rollback()
        if not (store.current_base_image):
            store.current_photo_paper-= 1

        store.enlarger_image_index = 0
        populate_enlarger_data()
    
    def stop_enlarger():
        print("Stopping enlarger")
        renpy.block_rollback()

    def cycle_enlarger(sign: int):   
        print("Cycling enlarger")
        images = []
        if(store.current_base_image):
            images = DAY_CONFIGS[Days(store.current_day)].object_images
        else:
            images = DAY_CONFIGS[Days(store.current_day)].base_images

        if(len(images) == 1):
            return

        store.enlarger_image_index += sign
        store.enlarger_image_index = store.enlarger_image_index % len(images)

        populate_enlarger_data()

        print("Cycling ", sign, ": ", store.enlarger_image_index, "/ ", len(images))
        renpy.hide_screen("enlarger_select_photo")
        renpy.show_screen("enlarger_select_photo")
#endregion