# -*- coding: utf-8 -*
import cv2
from imagepy.core.engine import Filter

class Plugin(Filter):
    """Bilateral: derived from imagepy.core.engine.Filter """
    title = 'Bilateral'
    note = ['all', 'auto_msk', 'auto_snap','preview']
    para = {'size':2, 'sigma1':2.0, 'sigma2':2.0}
    view = [(int, (0,30), 0, 'size', 'size', 'pix'),
            (float, (0,30), 1,  'sigma1', 'sigma1', 'pix'),
            (float, (0,30), 1,  'sigma2', 'sigma2', 'pix')]
    
    def run(self, ips, snap, img, para = None):
        cv2.bilateralFilter(snap, para['size'], para['sigma1'], para['sigma2'], dst = img)
