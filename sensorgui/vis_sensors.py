import numpy
import pyqtgraph as pg


class VisSensors(pg.PlotWidget):
    def __init__(self):
        super().__init__()

        self.curve = self.plot(pen='y')
        self.data = numpy.random.normal(size=(10,1000))
        self.ptr = 0
        self.update_view()

    def update_view(self):
        self.curve.setData(self.data[self.ptr%10])
        if self.ptr == 0:
            self.enableAutoRange('xy', False)
        self.ptr += 1
