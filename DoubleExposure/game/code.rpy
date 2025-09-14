# general control flow variables
default persistent.current_day = Days.DAY_ONE
default persistent.current_photo_paper = 0
default persistent.current_base_image = None
default persistent.current_secondary_image = None

# development state
default persistent.base_development = 0 # Current level of base photo development, when it exceeds MAX_DEVELOP_TIME we jump to overexposure
default persistent.secondary_development = 0 # Current level of secondary photo development, used for visual effects
default persistent.over_exposure = 0 # Current level of overexposure for visual effects
default persistent.can_stop_developing = False # Whether the "stop developing" button should be active
default persistent.development_end_signalled = False # Whether there is a pening request to stop development. Used because hitting the button doesn't jump out of in-process dialogue
default persistent.is_double_exposing = False # Whether we are developing a double exposure
default persistent.development_end_target = "DEFAULT_DEVELOPMENT_END_LABEL" # The label that will be jumped to when current development is ended
default persistent.development_overexpose_target = "DEFAULT_OVEREXPOSE_LABEL" # The label that will be jumped to when current development overexposes

# enlarger state
default persistent.projected_image = None # The image that is currently selected in the enlarger
default persistent.enlarger_image_index = 0 # The image of the current selection in the enlarger
default persistent.enlarger_jump_label = "DEFAULT_ENLARGER_JUMP_LABEL" # The label to jump to after completing the current enlarger session

init python:
    MIN_DEVELOP_TIME = 30
    MAX_DEVELOP_TIME = 60
    ENLARGER_LABEL_BASE = "projector_select_base"
    ENLARGER_LABEL_DOUBLE = "projector_select_double"

    def begin_day(day : Days):
        persistent.current_day = day.value
        persistent.current_photo_paper = PHOTO_PAPER[day]

#region development
    def start_developing(image : EnlargerImage):
        persistent.current_base_image = image
        persistent.current_secondary_image = None
        persistent.base_development = 0
        persistent.secondary_development = 0
        persistent.over_exposure = 0.0
        persistent.can_stop_developing = False
        persistent.development_end_signalled = False
        persistent.development_end_target = ENLARGER_LABEL_DOUBLE + "_" + persistent.current_day
        persistent.development_overexpose_target = "develop_" + image.label + "_overexposed"
        persistent.is_double_exposing = False
        renpy.show_screen("develop_photo")

    def stop_developing():
        print("Flagging to end development after the next line")
        persistent.development_end_signalled = True
        persistent.can_stop_developing = False

    def start_double_exposing(image : EnlargerImage):
        renpy.show_screen("develop_photo")
        persistent.current_secondary_image = image
        persistent.development_overexpose_target = "develop_" + persistent.current_base_image.label + "_" + image.label + "_overexposed"
        persistent.development_end_target = "complete_" + persistent.current_base_image.label + "_" + image.label
        persistent.is_double_exposing = True

    def _checkPendingJump(checkExposure = True):
        print("checking if there is a jump pending, ", persistent.development_end_signalled)

        if(persistent.development_end_signalled):
            persistent.development_end_signalled = False
            persistent.can_stop_developing = True
            renpy.hide_screen("develop_photo")
            renpy.block_rollback()
            renpy.jump(persistent.development_end_target)
    
        if(persistent.base_development == MAX_DEVELOP_TIME and checkExposure):
            persistent.development_end_signalled = False
            renpy.jump(persistent.development_overexpose_target)

    def _develop(base_development: int = -1, secondary_development: int = -1):
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
                persistent.base_development += increment

                if(persistent.is_double_exposing):
                    persistent.secondary_development += increment
                
                persistent.can_stop_developing = persistent.base_development >= MIN_DEVELOP_TIME

    def develop_overexposed(overexposure: int):
        _checkPendingJump(False)
        persistent.can_stop_developing = False
        persistent.over_exposure = overexposure #/ MAX_DEVELOP_TIME

    def develop_double(development: int):
        _develop(secondary_development = development)

    def develop(development: int):
        _develop(base_development = development)
#endregion

#region enlarger
    def populate_enlarger_data():
        if(persistent.current_base_image):
            objectImages = OBJECT_IMAGES[Days(persistent.current_day)]
            persistent.projected_image = objectImages[persistent.enlarger_image_index]
            persistent.enlarger_jump_label = DEVELOP_LABEL_PREFIX + persistent.current_base_image.label + "_" + objectImages[persistent.enlarger_image_index].label
        else:
            base_images = BASE_IMAGES[Days(persistent.current_day)]
            persistent.projected_image = base_images[persistent.enlarger_image_index]
            persistent.enlarger_jump_label = DEVELOP_LABEL_PREFIX + base_images[persistent.enlarger_image_index].label

    def start_enlarger():
        renpy.block_rollback()
        if not (persistent.is_double_exposing):
            persistent.current_photo_paper-= 1

        persistent.enlarger_image_index = 0
        populate_enlarger_data()
    
    def stop_enlarger():
        renpy.block_rollback()

    def cycle_enlarger(sign: int):
        base_images = BASE_IMAGES[Days(persistent.current_day)]

        persistent.enlarger_image_index += sign
        persistent.enlarger_image_index = persistent.enlarger_image_index % len(base_images)

        populate_enlarger_data()

        print("Cycling ", sign, ": ", persistent.enlarger_image_index, "/ ", len(base_images))
        renpy.hide_screen("enlarger_select_photo")
        renpy.show_screen("enlarger_select_photo")
#endregion