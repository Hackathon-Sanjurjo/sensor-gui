import sys
from PySide import QtCore
from PySide import QtGui
from sensorgui.vis_3d import Vis3D
from sensorgui.vis_sensors import VisSensors
from sensorgui.vis_instrument import VisInstrument


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sensor GUI')
        self.resize(1000, 600)
        self.show()
        self.main_widget = MainWidget()
        self.setCentralWidget(self.main_widget)

    def update_view(self):
        self.main_widget.update_view()


class MainWidget(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.splitter()

    def box(self):

        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        layout.addWidget(pw1)
        layout.addWidget(pw2)

    def splitter(self):

        self.vis_3d = Vis3D()
        self.vis_instrument = VisInstrument()
        self.vis_sensors = VisSensors()

        hbox = QtGui.QHBoxLayout(self)
        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(self.vis_3d)
        splitter1.addWidget(self.vis_instrument)
        splitter1.setSizes([80, 20])
        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(self.vis_sensors)
        splitter2.setSizes([80, 20])
        hbox.addWidget(splitter2)
        self.setLayout(hbox)

    def update_view(self):
        self.vis_3d.update_view()
        self.vis_sensors.update_view()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()

    timer = QtCore.QTimer()
    timer.timeout.connect(main_window.update_view)
    timer.start(30)

    sys.exit(app.exec_())
