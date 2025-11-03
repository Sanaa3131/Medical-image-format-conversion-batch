import os
import glob
import SimpleITK as sitk
from utils.io import read_datalist
import numpy as np
import tqdm
from joblib import Parallel, delayed
from utils import mhd

# Paths
_root = 'path/to/dataset'
_tgt = 'path/to/dataset/converted'
os.makedirs(_tgt, exist_ok=True)

#_case_list = glob.glob(_root + '/*.nii.gz')
_case_list = glob.glob(_root + '/*.nii')

def process_case(_case):
    img_h = sitk.ReadImage(_case)
    # img_array = np.flip(np.flip(sitk.GetArrayFromImage(img_h),1),2)
    img_array = sitk.GetArrayFromImage(img_h)
    img_offset = img_h.GetOrigin()
    img_spacing = img_h.GetSpacing()
    header = {'ElementSpacing': img_spacing,
              'Offset':img_offset,
              'CompressedData': True }
    #mhd.write(os.path.join(_tgt, os.path.basename(_case).replace('.nii.gz', '.mhd')),
    mhd.write(os.path.join(_tgt, os.path.basename(_case).replace('.nii', '.mhd')),
              img_array,
              header=header)
Parallel(n_jobs=5)(delayed(process_case)(_CASE) for _CASE in tqdm.tqdm(_case_list))

