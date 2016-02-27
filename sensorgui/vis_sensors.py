import pyqtgraph as pg
from .array import Array


class VisSensors(pg.PlotWidget):
    def __init__(self):
        super().__init__()

        self.setRange(yRange=(-100, 100))
        self.x_angle = self.plot(pen='y')
        self.y_angle = self.plot(pen='r')
        self.z_angle = self.plot(pen='g')
        self.array = Array(4)

    def push_data(self, timestamp, angles):
        self.array.push_data([timestamp, angles[0], angles[1], angles[2]])

    def update_view(self):
        self.x_angle.setData(self.array.view[:, 1])
        self.y_angle.setData(self.array.view[:, 2])
        self.z_angle.setData(self.array.view[:, 3])
