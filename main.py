import sys
import pyqtgraph as pg
import pyqtgraph.opengl as gl
from PySide import QtCore
from PySide import QtGui


class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sensor GUI')
        self.resize(1000, 600)
        self.show()
        self.setCentralWidget(MainWidget())


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

        topleft = gl.GLViewWidget()
        topright = pg.PlotWidget()
        bottom = pg.PlotWidget()

        hbox = QtGui.QHBoxLayout(self)
        splitter1 = QtGui.QSplitter(QtCore.Qt.Horizontal)
        splitter1.addWidget(topleft)
        splitter1.addWidget(topright)
        splitter1.setSizes([80, 20])
        splitter2 = QtGui.QSplitter(QtCore.Qt.Vertical)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)
        splitter2.setSizes([80, 20])
        hbox.addWidget(splitter2)
        self.setLayout(hbox)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
