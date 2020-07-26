
class ExperimentConfig():
    """This class is to be used in conjunction with the `sacred` logging tool
    to add options as properties to the cfg object."""
    def __init__(self, cfg):
        for key, val in cfg.items():
            setattr(self, key, val)

