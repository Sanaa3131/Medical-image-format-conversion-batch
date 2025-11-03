# 🩻 Medical Image Format Conversion (Batch NIfTI ↔ MHD)

This repository provides Python scripts for **batch conversion** between NIfTI (`.nii`, `.nii.gz`) and MetaImage (`.mhd`, `.raw`) formats.  
It is designed for researchers working with **medical imaging datasets**, particularly when preparing or post-processing data for segmentation models such as **nnU-Net** or visualization tools like **3D Slicer**.

## 🚀 Features
- Batch conversion for multiple cases.
- Supports `.nii`, `.nii.gz`, and `.mhd` formats.
- Preserves voxel spacing and origin metadata.
- Parallelized processing using `joblib` for efficiency.


