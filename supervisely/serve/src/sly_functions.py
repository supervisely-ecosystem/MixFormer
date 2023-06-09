import importlib
from typing import Tuple
from enum import Enum
from cv2 import Mat


class SupportedModels(Enum):
    VIT: str = 'mixformer_vit_online'
    CONVMAE: str = 'mixformer_convmae_online' 


class Tracker(object):
    def __init__(
        self, 
        name: SupportedModels,
        search_area_scale: float,
    ) -> None:
        self.parameter_name = 'baseline_large'
        if name is SupportedModels.VIT:
            self.model = 'mixformer_vit_large_online.pth.tar'
        else:
            self.model = 'mixformer_convmae_large_online.pth.tar'
        
        tracker_module = importlib.import_module('lib.test.tracker.{}'.format(name))
        tracker_class = tracker_module.get_tracker_class()
        param_module = importlib.import_module('lib.test.parameter.{}'.format(name))
        params = param_module.parameters(self.parameter_name, self.model, search_area_scale)
        self.tracker = tracker_class(params, "lasot")
    
    def initialize(self, rgb_image: Mat, x: int, y: int, h: int, w: int):
        init_info = {"init_bbox": [x, y, w, h]}
        self.tracker.initialize(rgb_image, init_info)
    
    def track(self, rgb_image: Mat) -> Tuple[int, int, int, int]:
        """Track object on given image.

        :param rgb_image: image in RGB format
        :type rgb_image: Mat
        :return: bbox parameters (x, y, w, h)
        :rtype: Tuple[int, int, int, int]
        """
        out = self.tracker.track(rgb_image, {})
        return out['target_bbox']