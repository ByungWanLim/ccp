from mmseg.datasets.builder import DATASETS
from mmseg.datasets.custom import CustomDataset
import os.path as osp

classes = ('needleleaf', 'broadleaf', 'mixed', 'notree')
palette = [[255,0,0], [0,255,0], [0,0,255], [0,0,0]]

@DATASETS.registr_module()
class CCP(CustomDataset):
    CLASSES = classes
    PALETTE = palette
    def __init__(self, **kwargs):
        super().__init__(img_suffix='.tif', seg_map_suffix='.png', **kwargs)
        assert osp.exists(self.img_dir)