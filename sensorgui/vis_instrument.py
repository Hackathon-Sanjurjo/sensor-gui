import pyqtgraph as pg
import numpy as np

class VisInstrument(pg.PlotWidget):
	def __init__(self):
		super().__init__()
		self.setRange(yRange=(0,8000))
		self.setRange(xRange=(-0.4,0.8))
		x_ax = np.arange(1)


	def update_view(self, x, y, z):
		self.clear()
		x_ax = np.arange(1)
		bg1 = pg.BarGraphItem(x=x_ax, height=abs(x), width=0.3, brush='y')
		bg2 = pg.BarGraphItem(x=x_ax+0.33, height=abs(y), width=0.3, brush='r')
		#bg3 = pg.BarGraphItem(x=x_ax+0.66, height=abs(z), width=0.3, brush='g')
		self.addItem(bg1)
		self.addItem(bg2)
		#self.addItem(bg3)


