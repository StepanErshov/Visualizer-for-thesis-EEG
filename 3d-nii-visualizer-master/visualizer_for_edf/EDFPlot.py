import zenodo_get
import mne
import matplotlib.pyplot as plt 

# ссылка на базу данных ЭЭГ
#https://zenodo.org/records/2547147#.Y7eU5uxBwlI

data_from_raw_edf = mne.io.read_raw_edf('C:\\projects\\python\\3d-nii-visualizer-master\\3d-nii-visualizer-master\\visualizer_for_edf\\eeg17.edf', preload=True)

# EDF - файл содержит многоканальную запись ЭЭГ
# ECG - файл содержит запись электрокардиограммы
data_from_raw_edf.plot(scalings = 'auto', show = False)
# список каналов из файла EDF
print(data_from_raw_edf.ch_names)
plt.show()