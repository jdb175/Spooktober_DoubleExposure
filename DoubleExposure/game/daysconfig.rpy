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
    
    class Days(Enum):
        DAY_ONE=0

    #endregion

    #region image configurations
    ### Base Images ###

    BASE_IMAGE_HOUSE = EnlargerImage(
            "house", 
            "exposuretest/bakgroundimage.png",
            "An image of a house")

    BASE_IMAGE_FACE = EnlargerImage(
            "face", 
            "exposuretest/face_bg.png",
            "An image of a face")

    ### Object Images ###

    OBJECT_IMAGE_MASK = EnlargerImage(
            "mask", 
            "exposuretest/pallid_mask_nobpg.png",
            "An image of a mask")

    OBJECT_IMAGE_GUY = EnlargerImage("guy", 
            "exposuretest/guy.png",
            "It's a guy")

    ### Day Configurations

    PHOTO_PAPER = {
        Days.DAY_ONE: 3
    }

    BASE_IMAGES = {
        Days.DAY_ONE: [
            BASE_IMAGE_HOUSE,
            BASE_IMAGE_FACE
        ]
    }   

    OBJECT_IMAGES = {
        Days.DAY_ONE: [
            OBJECT_IMAGE_MASK,
            OBJECT_IMAGE_GUY
        ]
    }

    #endregion