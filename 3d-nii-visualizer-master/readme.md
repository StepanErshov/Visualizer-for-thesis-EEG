# A NIfTI (nii.gz) 3D Visualizer using VTK and Qt5

<img src="/3d-nii-visualizer-master/images/visualization.png" style="width: 1000px;"/>

### Run with Python

1.  Create a virtual environment. Mac can use virtualenv or conda. Windows must use conda.
2.  Install the dependencies (PyQt5, vtk, mne, zenodo_get and sip) `pip install PyQt5 vtk matplotlib mne zenodo_get`
3.  Start the program `python ./visualizer/brain_tumor_3d.py -i "./sample_data/10labels_example/T1CE.nii.gz" -m "./sample_data/10labels_example/mask.nii.gz"`

### Generate PyInstaller Binaries
**Note**: Must modify the paths in .spec file to match your project directory
* Mac: `pyinstaller Theia_Mac.spec`
* Windows: `pyinstaller Theia_Windows.spec`

### Test
* `python -m pytest`

### Acknowledgements

[1] S.Bakas et al, "Advancing The Cancer Genome Atlas glioma MRI collections with expert segmentation labels and radiomic features", Nature Scientific Data, 4:170117 (2017) DOI: 10.1038/sdata.2017.117

[2] B.Menze et al, "The Multimodal Brain Tumor Image Segmentation Benchmark (BRATS)", IEEE Transactions on Medical Imaging 34(10), 1993-2024 (2015) DOI: 10.1109/TMI.2014.2377694

[3] [My supervisor](https://github.com/TAUforPython/wavelets/blob/main/wavelets_cwt_dwt_example_EEG_ECG.ipynb)

[4] © 2024 The Author(s). Epilepsia published by Wiley Periodicals LLC on behalf of International League Against Epilepsy.

[5] [Data for EEG](https://openneuro.org/datasets/ds005602/versions/1.0.0)