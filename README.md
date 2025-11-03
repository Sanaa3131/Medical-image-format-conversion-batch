# 🩻 Medical Image Format Conversion (Batch NIfTI ↔ MHD)

This repository provides Python scripts for **batch conversion** between NIfTI (`.nii`, `.nii.gz`) and MetaImage (`.mhd`, `.raw`) formats.  
It is designed for researchers working with **medical imaging datasets**, particularly when preparing or post-processing data for segmentation models such as **nnU-Net** or visualization tools like **3D Slicer**.

## 🚀 Features
- Batch conversion for multiple cases.
- Supports `.nii`, `.nii.gz`, and `.mhd` formats.
- Preserves voxel spacing and origin metadata.
- Parallelized processing using `joblib` for efficiency.

## ⚠️ Dependencies and Notes

This repository includes two Python scripts for converting between **NIfTI (.nii / .nii.gz)** and **MHD (.mhd)** medical image formats using [SimpleITK](https://simpleitk.org/).

Please note:
- The functions `read_datalist()` (from `my_io`) and `mhd.write()` / `mhd.read()` (from `utils.mhd`) were **developed internally by a member of my research laboratory** and therefore **cannot be shared publicly**.
- The `utils.mhd` module contains basic helper functions for reading and writing `.mhd` image volumes and their metadata (e.g., element spacing, origin, compression).
- These private modules can be replaced with equivalent SimpleITK functions or any open-source MHD I/O utilities if you wish to reproduce similar functionality.

Example SimpleITK replacement for MHD I/O:
```python
import SimpleITK as sitk
image = sitk.ReadImage("image.mhd")
sitk.WriteImage(image, "output.mhd")



