
init python:
    MIN_DEVELOP_TIME = 30
    MAX_DEVELOP_TIME = 60

    def beginDay(day : Days):
        persistent.currentDay = day.value
        persistent.photoPaper = PHOTO_PAPER[day]

    def startDeveloping(enlargerTarget, overExposureTarget):
        persistent.baseDeveloped = 0
        persistent.secondaryDeveloped = 0
        persistent.overExposure = 0.0
        persistent.canStopDeveloping = False
        persistent.baseAlpha = 0.0
        persistent.secondaryAlpha = 0.0
        persistent.overExposureBrightness = 0.0
        persistent.endingDevelopment = False
        persistent.endTarget = enlargerTarget
        persistent.overExposeTarget = overExposureTarget
        persistent.doubleExposing = False

    def stopDeveloping():
        print("Flagging to end development after the next line")
        persistent.endingDevelopment = True
        persistent.canStopDeveloping = False

    def startDoubleExposing(endTarget, overExposureTarget):
        persistent.overExposeTarget = overExposureTarget
        persistent.endTarget = endTarget
        persistent.doubleExposing = True

    def _checkPendingJump(checkExposure = True):
        print("checking if there is a jump pending, ", persistent.endingDevelopment)

        if(persistent.endingDevelopment):
            persistent.endingDevelopment = False
            persistent.canStopDeveloping = True
            renpy.jump(persistent.endTarget)
    
        if(persistent.baseDeveloped == MAX_DEVELOP_TIME and checkExposure):
            persistent.endingDevelopment = False
            renpy.jump(persistent.overExposeTarget)

    def _develop(baseDevelopment: int = -1, secondaryDevelopment: int = -1):
        _checkPendingJump()

        increment : int = 0

        if(baseDevelopment < 0):
            increment = secondaryDevelopment - persistent.secondaryDeveloped
        else:
            increment = baseDevelopment - persistent.baseDeveloped

        if(increment < 0):
            persistent.canStopDeveloping = False
        else:
            if(increment > 0):
                persistent.baseDeveloped += increment
                persistent.baseAlpha = min(persistent.baseDeveloped/MAX_DEVELOP_TIME, 1.0)

                if(persistent.doubleExposing):
                    persistent.secondaryDeveloped += increment
                    persistent.secondaryAlpha = min(persistent.secondaryDeveloped/MAX_DEVELOP_TIME, 1.0)
                
                persistent.canStopDeveloping = persistent.baseDeveloped >= MIN_DEVELOP_TIME


    def develop_overexposed(overexposure: int):
        _checkPendingJump(False)
        persistent.canStopDeveloping = False
        persistent.overExposureBrightness = overexposure / MAX_DEVELOP_TIME

    def develop_double(development: int):
        _develop(secondaryDevelopment=development)

    def develop(development: int):
        _develop(baseDevelopment=development)


    def stop_enlarger():
        if(persistent.exposedBaseImage):
            persistent.exposedBaseImage = None
        else:
            baseImages = BASE_IMAGES[Days(persistent.currentDay)]
            persistent.exposedBaseImage = baseImages[persistent.imageIndex]

    def populate_enlarger_data():
        if(persistent.exposedBaseImage):
            objectImages = OBJECT_IMAGES[Days(persistent.currentDay)]
            persistent.exposingImage = objectImages[persistent.imageIndex]
            persistent.enlargerJumpLabel = DEVELOP_LABEL_PREFIX + persistent.exposedBaseImage.label + "_" + objectImages[persistent.imageIndex].label
        else:
            baseImages = BASE_IMAGES[Days(persistent.currentDay)]
            persistent.exposingImage = baseImages[persistent.imageIndex]
            persistent.enlargerJumpLabel = DEVELOP_LABEL_PREFIX + baseImages[persistent.imageIndex].label

    def start_enlarger():
        if not (persistent.doubleExposing):
            persistent.photoPaper-= 1

        persistent.imageIndex = 0
        populate_enlarger_data()

    def cycle_enlarger(sign: int):
        baseImages = BASE_IMAGES[Days(persistent.currentDay)]

        persistent.imageIndex += sign
        persistent.imageIndex = persistent.imageIndex % len(baseImages)

        populate_enlarger_data()

        print("Cycling ", sign, ": ", persistent.imageIndex, "/ ", len(baseImages))
        renpy.hide_screen("enlarger_select_photo")
        renpy.show_screen("enlarger_select_photo")