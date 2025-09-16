#Importing libraries
python early:
    import math
    from enum import Enum

    DEVELOP_LABEL_PREFIX = "develop_"
    
    #region classes
    class EnlargerImage:
        def __init__(self, label, path, description):
            self.label = label
            self.path = path
            self.description = description

        def __eq__(self, other): 
            if not isinstance(other, EnlargerImage):
                return False

            return self.label == other.label and self.path == other.path

    class DayConfig:
        def __init__(self, 
            photo_paper, 
            base_images,
            object_images
        ):
            self.photo_paper = photo_paper
            self.base_images = base_images
            self.object_images = object_images
    
    class Days(Enum):
        DAY_ONE="dayone"

    #endregion

    #region image configurations
    ### Base Images ###
    #TESTING
    BASE_IMAGE_HOUSE = EnlargerImage(
            label = "house", 
            path = "exposuretest/bakgroundimage.png",
            description = "An image of a house")

    BASE_IMAGE_FACE = EnlargerImage(
            label = "face", 
            path = "exposuretest/face_bg.png",
            description = "An image of a face")
    #DAY ONE
    BASE_IMAGE_KITCHEN = EnlargerImage(
        label = "kitchen",
        path = "placeholders/kitchen_temp.png",
        description = "The kitchen from 'night and day'")

    ### Object Images ###
    #TESTING
    OBJECT_IMAGE_MASK = EnlargerImage(
            label = "mask", 
            path = "exposuretest/pallid_mask_nobpg.png",
            description = "An image of a mask")

    OBJECT_IMAGE_GUY = EnlargerImage(
            label = "guy", 
            path = "exposuretest/guy.png",
            description = "It's a guy")
    #DAY ONE
    OBJECT_IMAGE_GUNNAR = EnlargerImage(
        label = "gunnar",
        path = "placeholders/gunnar_temp.png",
        description = "Portrait, pensive man")

    OBJECT_IMAGE_SIOBHAN = EnlargerImage(
        label = "siobhan",
        path = "placeholders/siobhan.png",
        description = "A portrait of Sioban Kent")
    
    OBJECT_IMAGE_PETER = EnlargerImage(
        label = "peter",
        path = "exposuretest/guy.png",
        description = "Portrait, moustache man")

    ### Day Configurations

    DAY_CONFIGS = {
        Days.DAY_ONE: DayConfig(
            photo_paper = 2,
            base_images = [
                BASE_IMAGE_KITCHEN
            ],
            object_images = [
                OBJECT_IMAGE_GUNNAR,
                OBJECT_IMAGE_SIOBHAN,
                OBJECT_IMAGE_PETER
            ])
    }

    #endregion