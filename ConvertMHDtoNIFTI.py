import os
import SimpleITK as sitk
from my_io import read_datalist
import tqdm
from joblib import Parallel, delayed

# Paths
_root = 'path/to/dataset'
_tgt = 'path/to/dataset/converted'
_case_list = 'path/to/caseid_list.txt'
_case_list = read_datalist(_case_list)

_image = 'image.mhd'
_muscles_label = 'label_lr.mhd'

# Create the required directories
os.makedirs(_tgt, exist_ok=True)
folders = ['images', 'labels']
for folder in folders:
    os.makedirs(os.path.join(_tgt, folder), exist_ok=True)

def process_case(_case):
    out_dir = _tgt

    # Process and rename the image
    original_image = sitk.ReadImage(os.path.join(_root, _case, _image))
    image_filename = _case + '_0000.nii.gz'
    sitk.WriteImage(original_image, os.path.join(out_dir, 'images', image_filename))
    

    # Process and keep the label name
    original_label = sitk.ReadImage(os.path.join(_root, _case, _muscles_label))
    label_filename = _case + '.nii.gz'
    sitk.WriteImage(original_label, os.path.join(out_dir, 'labels', label_filename))

Parallel(n_jobs=5)(delayed(process_case)(_CASE) for _CASE in tqdm.tqdm(_case_list))


