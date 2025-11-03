# import os
# from utils import mhd
# import SimpleITK as sitk
# from my_io import read_datalist

# import tqdm
# from joblib import Parallel, delayed

# #_root = '//Salmon/User/Chen/Vessel_data/Combined_dataset_Osaka36_Nara18'
# #_root = '//Salmon/User/mazen/Segmentation/Data/Shiga/GT/Phase9'
# _root = 'Y:/mazen/Segmentation/Data/Shiga/GT/Phase9'
# #_tgt = '//Scallop/User/mazen/Data/nnUNet/nnUNet_raw/vessels/all/nifti_onlyvessels/Labels'
# _tgt = 'Y:/mazen/Segmentation/Data/Shiga/GT/Phase9/nifti_for_nnunet'
# os.makedirs(_tgt, exist_ok=True)
# #_case_list ='//Salmon/User/mazen/Segmentation/Data/Shiga/GT/Phase9caseid_list.txt'
# _case_list ='Y:/mazen/Segmentation/Data/Shiga/GT/Phase9/caseid_list.txt'
# #_case_list ='//Salmon/User/Chen/Vessel_data/Combined_dataset_Osaka36_Nara18/caseid_list.txt'
# _case_list = read_datalist(_case_list)

# # _muscle_label = 'label.mhd'
# _image = 'image.mhd'
# # _vessels_label = 'vessels_label.mhd'
# # _vessels_nerves_label = 'vessels_nerves_label.mhd'
# #_vessels_nerve_bones_label = 'only_vessels_label.mhd'
# _muscles_label = 'label.mhd'
# # _case_list = [_case for _case in _case_list if not _case.startswith('N')]
# # _case_list = [_case for _case in _case_list if  _case.startswith('N')]
# print(_case_list)
# def process_case(_case):
#     # out_dir = os.path.join(_tgt, _case)
#     out_dir = _tgt
#     os.makedirs(out_dir, exist_ok=True)

#     # original_image = sitk.ReadImage(os.path.join(_root, _case_list[0], _muscle_label))
#     # sitk.WriteImage(original_image, os.path.join(out_dir, _muscle_label.replace('mhd', 'nii.gz')))
#     # plain_ct_image = 'crop_plain_ct_image.mhd'
#     # original_image = sitk.ReadImage(os.path.join(_root, _case, plain_ct_image))
#     # sitk.WriteImage(original_image, os.path.join(out_dir, _image.replace('mhd', 'nii.gz')))

#     # original_image = sitk.ReadImage(os.path.join(_root, _case_list[0], _vessels_nerves_label))
#     # sitk.WriteImage(original_image, os.path.join(out_dir, _vessels_nerves_label.replace('mhd', 'nii.gz')))

#     # original_image = sitk.ReadImage(os.path.join(_root, _case_list[0], _vessels_label))
#     # sitk.WriteImage(original_image, os.path.join(out_dir, _vessels_label.replace('mhd', 'nii.gz')))

#     original_image = sitk.ReadImage(os.path.join(_root, _case, _muscles_label))
#     #original_image = sitk.ReadImage(os.path.join(_root, _case, _vessels_nerve_bones_label))
#     # sitk.WriteImage(original_image, os.path.join(out_dir, _vessels_nerve_bones_label.replace('mhd', 'nii.gz')))
#     sitk.WriteImage(original_image, os.path.join(out_dir, _case+'.nii.gz'))

# Parallel(n_jobs=5)(delayed(process_case)(_CASE) for _CASE in tqdm.tqdm(_case_list))

##########################CONVERSION AND ORGANIZATION OF THE DATA################################################################
import os
import SimpleITK as sitk
from my_io import read_datalist
import tqdm
from joblib import Parallel, delayed

_root = 'Y:/mazen/Segmentation/Data/Shiga/GT/Phase10'
#_tgt = 'Z:/mazen/Data/nnUNet/nnUNet_raw/muscles/upper_muscles/Phase10/org'
_tgt = 'Z:/mazen/Data/nnUNet/nnUNet_raw/muscles/upper_muscles/Phase10/separated'
_case_list = 'Y:/mazen/Segmentation/Data/Shiga/GT/Phase10/caseid_list.txt'
_case_list = read_datalist(_case_list)
print(_case_list)


_image = 'image.mhd'
#Orginal_label
#_muscles_label = 'label.mhd'
#Separated label
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






