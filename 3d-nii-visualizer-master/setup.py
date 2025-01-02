from cx_Freeze import setup, Executable
import os

# Укажите дополнительные файлы, которые нужно включить
include_files = [
    ("./sample_data/10labels_example/T1CE.nii.gz", "sample_data/10labels_example"),
    ("./sample_data/10labels_example/mask.nii.gz", "sample_data/10labels_example"),
    ("./visualizer/MainWindow.py", "visualizer"),
]

setup(
    name="Brain Tumor Visualizer",
    version="1.0",
    description="A 3D EEG visualizer application",
    options={
        "build_exe": {
            "include_files": include_files,
        }
    },
    executables=[Executable("visualizer/brain_tumor_3d.py", base="Win32GUI")]
)