import numpy as np
from numpy.random import lognormal, uniform

from chaco.api import VPlotContainer, Plot, ArrayPlotData
from chaco.tools.api import PanTool, ZoomTool
from enable.api import ComponentEditor
from traits.api import HasTraits, Any, Instance
from traitsui.api import Item, View
from pyface.timer.api import Timer

def random_walk(numpoints, start=100.0, stddev=0.01):
    returns = np.exp(stddev * np.random.randn(numpoints))
    walk = start * np.cumprod(returns)
    return walk

class StreamPlot(HasTraits):
    plot = Instance(VPlotContainer)
    traits_view = View(Item('plot', editor=ComponentEditor(), show_label=False),
                       width=1000, height=600, resizable=True,
                       title="Linked Plots")

    plotdata = Instance(ArrayPlotData)

    def __init__(self):
        # Create the data and the PlotData object
        price1 = random_walk(100)
        price2 = random_walk(100, start=50)
        times = np.arange(100)
        plotdata = ArrayPlotData(times=times, price1=price1, price2=price2)
        
        # Create the scatter plot
        plot1 = Plot(plotdata)
        plot1.plot(("times", "price1"), type="line", color="blue")
        plot1.plot(("times", "price1"), type="scatter", color="blue")
        
        plot2 = Plot(plotdata)
        plot2.plot(("times", "price2"), type="line", color="green")
        plot2.plot(("times", "price2"), type="scatter", color="green")
        container = VPlotContainer(plot1, plot2)
        self.plot = container
        self.plotdata = plotdata


if __name__ == "__main__":
    streamplot = StreamPlot()
    streamplot.configure_traits()
