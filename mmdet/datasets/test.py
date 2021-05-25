import mmcv
import numpy as np

from .builder import DATASETS
from .custom import CustomDataset
from .coco import CocoDataset


@DATASETS.register_module()
class TestDataset(CocoDataset):

    CLASSES = ('leg',)