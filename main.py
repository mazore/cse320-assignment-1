import numpy as np
import nibabel as nib
from nilearn import datasets, plotting

# read .mnc format data
img = nib.load('data/t1_clean.mnc')
data = img.get_fdata() # get_data() is deprecated in favor of get_fdata()
affine = img.affine
print(affine)

# directly save image
nib.save(img, 'img.nii')

plotting.plot_img(img)
