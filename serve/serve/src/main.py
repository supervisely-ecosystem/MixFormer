import os
import numpy as np
import cv2
from dotenv import load_dotenv
from pathlib import Path
from typing import Any, Dict, List, Literal
from typing_extensions import Literal
from tqdm import tqdm

import sly_functions as F
import supervisely as sly
import supervisely.imaging.image as sly_image
from supervisely.nn.inference import BBoxTracking
from supervisely.nn.prediction_dto import PredictionBBox


NAME = os.environ.get("modal.state.modelName", "mixformer_vit_online")
load_dotenv(os.path.expanduser("~/supervisely.env"))


class MixFormer(BBoxTracking):
    def load_on_device(
        self,
        model_dir: str,
        device: Literal["cpu", "cuda", "cuda:0", "cuda:1", "cuda:2", "cuda:3"] = "cpu",
    ):
        name = F.SupportedModels.instance_by_name(NAME)
        self.model = F.Tracker(name)

    def initialize(
        self, init_rgb_image: np.ndarray, target_bbox: PredictionBBox
    ) -> None:
        y1, x1, y2, x2 = target_bbox.bbox_tlbr
        w = abs(x2 - x1)
        h = abs(y2 - y1)
        self.model.initialize(init_rgb_image, x1, y1, w, h)

    def predict(
        self,
        rgb_image: np.ndarray,
        settings: Dict[str, Any],
        prev_rgb_image: np.ndarray,
        target_bbox: PredictionBBox,
    ) -> PredictionBBox:
        class_name = target_bbox.class_name
        x, y, w, h = self.model.track(rgb_image)
        tlbr = [int(y), int(x), int(y + h), int(x + w)]
        return PredictionBBox(class_name, tlbr, None)


# if sly.is_debug_with_sly_net() or not sly.is_production():
#     NAME = "mixformer_vit_online"
    # model_dir = root / "reference_model"
# else:
#     model_dir = Path("/weights")

mixformer = MixFormer()

if sly.is_production():
    mixformer.serve()
else:
    data_path = Path("/workspaces/MixFormer/data")
    img_path = data_path / "racing"
    out = img_path / "predicted"
    out.mkdir(exist_ok=True, parents=True)
    imgs_names = sorted(os.listdir(img_path))

    start, end = 80, 180
    imgs_pth = [img_path / name for name in imgs_names[start:end] if 'jpg' in name]

    # top left bottom right order
    start_object = PredictionBBox("", [187, 244, 236, 365], None)
    images = [sly_image.read(str(pth)) for pth in imgs_pth]

    preds = []
    mixformer.initialize(images[0], start_object)

    for image in tqdm(images[1:]):
        preds.append(mixformer.predict(image, {}, images[0], start_object))

    mixformer.visualize(
        preds,
        images[1:],
        out,
        thickness=5,
    )
