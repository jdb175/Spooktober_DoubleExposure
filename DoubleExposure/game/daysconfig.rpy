#Importing libraries
python early:
    import math
    from enum import Enum

    DEVELOP_LABEL_PREFIX = "develop_"
    
    #region classes
    class EnlargerImage:
        def __init__(self, label, path, description, empty_path="", append_label=False):
            self.label = label
            self.path = path
            self.description = description
            self.empty_path = empty_path
            self.append_label = append_label

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

        
    def get_secondary_image_path(base_image : EnlargerImage, secondary_image : EnlargerImage):
        path = secondary_image.path
        if(base_image.append_label):
            path += " " + base_image.label
        return path + ".png"


    #endregion

    #region image configurations
    ### Base Images ###
    ##DAY ONE
    BASE_IMAGE_KITCHEN = EnlargerImage(
        label = "kitchen",
        path = "photos/kitchen erin.png",
        empty_path = "photos/kitchen.png",
        description = "The kitchen from 'night and day'")

    ##DAY TWO
    BASE_IMAGE_SNEAKY = EnlargerImage(
        label = "sneaky",
        path = "photos/night populated.png",
        empty_path = "photos/night empty.png",
        description = "A clandestine photo of people in robes",
        append_label = True)
    BASE_IMAGE_PORTAL = EnlargerImage(
        label = "portal",
        path = "photos/portal populated.png",
        empty_path = "photos/portal empty.png",
        description = "Robed people and a... portal??",
        append_label = True
    )

    ##DAY ONE
    OBJECT_IMAGE_SIOBHAN = EnlargerImage(
        label = "siobhan",
        path = "photos/kitchen siobhan",
        description = "A portrait of Siobhan Kent")
    OBJECT_IMAGE_PETER = EnlargerImage(
        label = "peter",
        path = "photos/kitchen peter",
        description = "Portrait, moustache man")
    OBJECT_IMAGE_GUNNAR = EnlargerImage(
        label = "gunnar",
        path = "photos/kitchen gunnar",
        description = "Portrait, man with book"
    )
    ##DAY TWO
    OBJECT_IMAGE_OWL = EnlargerImage(
        label = "owl",
        path = "masks/owl mask",
        description = "Owl mask"
    )
    OBJECT_IMAGE_FLAME = EnlargerImage(
        label = "flame",
        path = "masks/flame mask",
        description = "Flame mask"
    )
    OBJECT_IMAGE_ARCHER = EnlargerImage(
        label = "archer",
        path = "masks/sage mask",
        description = "'Sage' mask"
    )
    OBJECT_IMAGE_FROG = EnlargerImage(
        label = "frog",
        path = "masks/frog mask",
        description = "Frog mask"
    )


    ### Day Configurations

    DAY_CONFIGS = {
        Days.DAY_ONE: DayConfig(
            photo_paper = 3, #NOTE: SHOULD BE 2, but I increased for testing
            base_images = [
                BASE_IMAGE_KITCHEN
            ],
            object_images = [
                OBJECT_IMAGE_SIOBHAN,
                OBJECT_IMAGE_PETER,
                OBJECT_IMAGE_GUNNAR
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