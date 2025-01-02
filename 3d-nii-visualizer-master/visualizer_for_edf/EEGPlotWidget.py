import math
import time
import os

import PyQt5.QtWidgets as QtWidgets
import PyQt5.QtCore as Qt
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from vtkUtils import *
from config import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import mne

class EEGPlotWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.canvas)

        # ComboBox для выбора канала
        self.channel_selector = QtWidgets.QComboBox()
        self.layout.addWidget(self.channel_selector)
        self.setLayout(self.layout)

        # Загрузка данных
        self.load_data()

        # Подключение сигнала изменения выбора канала
        self.channel_selector.currentIndexChanged.connect(self.update_plot)

    def load_data(self):
        # Чтение данных из файла EDF
        self.data_from_raw_edf = mne.io.read_raw_edf(
            "C:\\projects\\python\\3d-nii-visualizer-master\\3d-nii-visualizer-master\\visualizer_for_edf\\EDF_example_FS_healthy.edf",
            preload=True,
        )

        # Получение данных ЭЭГ и временных меток
        self.eeg_data, self.eeg_times = self.data_from_raw_edf.get_data(return_times=True)

        # Заполнение ComboBox названиями каналов
        self.channel_selector.addItems(self.data_from_raw_edf.ch_names)

        # Устанавливаем диапазон для обработки данных
        self.t_index_begin = 0  # Начало диапазона
        self.t_index_end = len(self.eeg_times)  # Конец диапазона
        self.t = self.eeg_times[self.t_index_begin:self.t_index_end]

        # Изначально отображаем первый канал
        self.update_plot()

    def update_plot(self):
        # Получаем индекс выбранного канала
        channel_index = self.channel_selector.currentIndex()
        selected_channel_data = self.eeg_data[channel_index, self.t_index_begin:self.t_index_end]

        # Визуализация данных выбранного канала
        self.ax.clear()
        self.ax.plot(self.t, selected_channel_data, label=f"Канал: {self.data_from_raw_edf.ch_names[channel_index]}")
        self.ax.set_title(f"Данные ЭЭГ для канала: {self.data_from_raw_edf.ch_names[channel_index]}")
        self.ax.set_xlabel("Время (с)")
        self.ax.set_ylabel("Амплитуда")
        self.ax.legend()
        self.ax.grid()
        self.canvas.draw()

class MainWindow(QtWidgets.QMainWindow, QtWidgets.QApplication):
    def __init__(self, app):
        self.app = app
        QtWidgets.QMainWindow.__init__(self, None)

        # base setup
        (
            self.renderer,
            self.frame,
            self.vtk_widget,
            self.interactor,
            self.render_window,
        ) = self.setup()
        self.brain, self.mask = setup_brain(
            self.renderer, self.app.BRAIN_FILE
        ), setup_mask(self.renderer, self.app.MASK_FILE)

        # Create an instance of the EEG plot widget
        self.eeg_plot_widget = EEGPlotWidget()

        # Create grid for all widgets
        self.grid = QtWidgets.QGridLayout()

        # Add each widget
        self.add_vtk_window_widget()
        self.add_brain_settings_widget()
        self.add_mask_settings_widget()
        self.add_views_widget()

        # Add the EEG plot widget to the grid layout
        self.grid.addWidget(self.eeg_plot_widget, 0, 3, 5, 2)  # Adjust position as needed

        # Set layout and show
        self.render_window.Render()
        self.setWindowTitle(APPLICATION_TITLE)
        self.frame.setLayout(self.grid)
        self.setCentralWidget(self.frame)
        self.set_axial_view()
        self.interactor.Initialize()
        self.show()

    @staticmethod
    def setup():
        renderer = vtk.vtkRenderer()
        frame = QtWidgets.QFrame()
        vtk_widget = QVTKRenderWindowInteractor()
        interactor = vtk_widget.GetRenderWindow().GetInteractor()
        render_window = vtk_widget.GetRenderWindow()

        frame.setAutoFillBackground(True)
        vtk_widget.GetRenderWindow().AddRenderer(renderer)
        render_window.AddRenderer(renderer)
        interactor.SetRenderWindow(render_window)
        interactor.SetInteractorStyle(vtk.vtkInteractorStyleTrackballCamera())

        return renderer, frame, vtk_widget, interactor, render_window

# Запуск приложения
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow(app)
    sys.exit(app.exec_())