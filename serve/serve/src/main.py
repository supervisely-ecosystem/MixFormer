import os
import numpy as np
from dotenv import load_dotenv
from pathlib import Path
from typing import Any, Dict, Literal
from typing_extensions import Literal
from tqdm import tqdm

from lib.test.evaluation import create_default_local_file_ITP_test
from lib.train.admin import create_default_local_file_ITP_train

import sly_functions as F
import supervisely as sly
import supervisely.imaging.image as sly_image
from supervisely.nn.inference import BBoxTracking
from supervisely.nn.prediction_dto import PredictionBBox


NAME = os.environ.get("modal.state.modelName", "mixformer_vit_online")
os.environ["SMART_CACHE_TTL"] = str(5 * 60)
os.environ["SMART_CACHE_SIZE"] = str(512)

root = (Path(__file__).parent / ".." / ".." / "..").resolve().absolute()

load_dotenv(os.path.expanduser("~/supervisely.env"))


class MixFormer(BBoxTracking):
    def load_on_device(
        self,
        model_dir: str,
        device: Literal["cpu", "cuda", "cuda:0", "cuda:1", "cuda:2", "cuda:3"] = "cpu",
    ):
        name = F.SupportedModels.instance_by_name(NAME)
        self.model = F.Tracker(name)

    def initialize(self, init_rgb_image: np.ndarray, target_bbox: PredictionBBox) -> None:
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
        max_h, max_w, _ = rgb_image.shape
        tlbr = self._build_bbox_params(x, y, w, h, max_w, max_h)
        return PredictionBBox(class_name, tlbr, None)

    def _build_bbox_params(self, x: float, y: float, w: float, h: float, max_w: int, max_h: int):
        top = min(max(0, int(y)), max_h - 1)
        left = min(max(0, int(x)), max_w - 1)
        bottom = min(max(0, int(y + h)), max_h - 1)
        right = min(max(0, int(x + w)), max_w - 1)
        return [top, left, bottom, right]


if sly.is_debug_with_sly_net() or not sly.is_production():
    create_default_local_file_ITP_test(str(root), "", str(root / "save"))
    create_default_local_file_ITP_train(str(root), "")
else:
    create_default_local_file_ITP_test(str(root), "", "/weights")
    create_default_local_file_ITP_train(str(root), "")


mixformer = MixFormer()

if sly.is_production():
    mixformer.serve()
else:
    data_path = root / "data"
    img_path = data_path / "racing"
    out = img_path / "predicted"
    out.mkdir(exist_ok=True, parents=True)
    imgs_names = sorted(os.listdir(img_path))

    start, end = 80, 180
    imgs_pth = [img_path / name for name in imgs_names[start:end] if "jpg" in name]

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
