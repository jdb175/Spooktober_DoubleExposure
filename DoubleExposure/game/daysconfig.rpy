#Importing libraries
python early:
    import math
    from enum import Enum

    DEVELOP_LABEL_PREFIX = "develop_"
    
    #region classes
    class EnlargerImage:
        def __init__(self, label, path, description, empty_path=""):
            self.label = label
            self.path = path
            self.description = description
            self.empty_path = empty_path

        def __eq__(self, other): 
            if not isinstance(other, EnlargerImage):
                return False

            return self.label == other.label

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
        DAY_TWO="daytwo"

    #endregion

    #region image configurations
    ### Base Images ###
    ##TESTING
    BASE_IMAGE_HOUSE = EnlargerImage(
            label = "house", 
            path = "exposuretest/bakgroundimage.png",
            description = "An image of a house")

    BASE_IMAGE_FACE = EnlargerImage(
            label = "face", 
            path = "exposuretest/face_bg.png",
            description = "An image of a face")
    ##DAY ONE
    BASE_IMAGE_KITCHEN = EnlargerImage(
        label = "kitchen",
        path = "photos/kitchen erin.png",
        empty_path = "photos/kitchen.png",
        description = "The kitchen from 'night and day'")
    ##DAY TWO
    BASE_IMAGE_SNEAKY = EnlargerImage(
        label = "sneaky",
        path = "exposuretest/bakgroundimage.png",
        empty_path = "exposuretest/bakgroundimage.png",
        description = "A clandestine photo of people in robes")
    BASE_IMAGE_PORTAL = EnlargerImage(
        label = "portal",
        path = "exposuretest/face_bg.png",
        empty_path = "exposuretest/face_bg.png",
        description = "Robed people and a... portal??"
    )

    ### Object Images ###
    ##TESTING
    OBJECT_IMAGE_MASK = EnlargerImage(
            label = "mask", 
            path = "exposuretest/pallid_mask_nobpg.png",
            description = "An image of a mask")

    OBJECT_IMAGE_GUY = EnlargerImage(
            label = "guy", 
            path = "exposuretest/guy.png",
            description = "It's a guy")
    ##DAY ONE
    OBJECT_IMAGE_SIOBHAN = EnlargerImage(
        label = "siobhan",
        path = "photos/kitchen siobhan.png",
        description = "A portrait of Sioban Kent")
    
    OBJECT_IMAGE_PETER = EnlargerImage(
        label = "peter",
        path = "photos/kitchen peter.png",
        description = "Portrait, moustache man")
    ##DAY TWO
    OBJECT_IMAGE_OWL = EnlargerImage(
        label = "owl",
        path = "masks/owl mask.png",
        description = "Owl mask"
    )
    OBJECT_IMAGE_FLAME = EnlargerImage(
        label = "flame",
        path = "masks/flame mask.png",
        description = "Flame mask"
    )
    OBJECT_IMAGE_ARCHER = EnlargerImage(
        label = "archer",
        path = "placeholders/archer temp.png",
        description = "Archer mask"
    )
    OBJECT_IMAGE_FROG = EnlargerImage(
        label = "frog",
        path = "masks/frog mask.png",
        description = "Frog mask"
    )


    ### Day Configurations

    DAY_CONFIGS = {
        Days.DAY_ONE: DayConfig(
            photo_paper = 2,
            base_images = [
                BASE_IMAGE_KITCHEN
            ],
            object_images = [
                OBJECT_IMAGE_SIOBHAN,
                OBJECT_IMAGE_PETER
            ]),
        Days.DAY_TWO: DayConfig(
            photo_paper = 5,
            base_images = [
                BASE_IMAGE_SNEAKY,
                BASE_IMAGE_PORTAL
            ],
            object_images = [
                OBJECT_IMAGE_OWL,
                OBJECT_IMAGE_FLAME,
                OBJECT_IMAGE_ARCHER,
                OBJECT_IMAGE_FROG
            ])
    }

    #endregion