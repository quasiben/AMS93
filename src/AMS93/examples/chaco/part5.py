import numpy as np
from numpy.random import lognormal, uniform

from chaco.api import (VPlotContainer, HPlotContainer,
                       Plot, ArrayPlotData, ScatterInspectorOverlay,
                       )
from chaco.tools.api import PanTool, ZoomTool, RangeSelection, RangeSelectionOverlay
from enable.api import ComponentEditor
from traits.api import HasTraits, Any, Instance
from traitsui.api import Item, View
from pyface.timer.api import Timer

def random_walk(numpoints, start=100.0, stddev=0.01):
    returns = np.exp(stddev * np.random.randn(numpoints))
    walk = start * np.cumprod(returns)
    return walk

class StreamPlot(HasTraits):
    plot = Instance(HPlotContainer)
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
        line1 = plot1.plot(("times", "price1"), type="line", color="blue")[0]
        scatter1 = plot1.plot(("times", "price1"), type="scatter", color="blue")[0]
        
        plot2 = Plot(plotdata)
        line2 = plot2.plot(("times", "price2"), type="line", color="green")[0]
        scatter2 = plot2.plot(("times", "price2"), type="scatter", color="green")[0]

        scatterplot = Plot(plotdata)
        scatterplot.plot(("price2", "price1"), type="scatter", color="green")

        #plot1.tools.append(PanTool(plot1))
        plot1.tools.append(ZoomTool(plot1))
        plot1.tools.append(RangeSelection(line1, auto_handle_event=False))
        plot1.overlays.append(RangeSelectionOverlay(line1, metadata_name="selections"))
        plot1.overlays.append(RangeSelectionOverlay(line1, metadata_name="selections"))        

        
        #plot2.tools.append(PanTool(plot2))
        plot2.tools.append(ZoomTool(plot2))
        plot2.tools.append(RangeSelection(line2, auto_handle_event=False))
        plot2.overlays.append(RangeSelectionOverlay(line2, metadata_name="selections"))
        
        #scatterplot.tools.append(PanTool(scatterplot))
        scatterplot.tools.append(ZoomTool(scatterplot))        
        
        plot1.index_range = plot2.index_range
        
        lineplots = VPlotContainer(plot1, plot2)
        container = HPlotContainer(lineplots, scatterplot)
        self.plot = container
        self.plotdata = plotdata


if __name__ == "__main__":
    streamplot = StreamPlot()
    streamplot.configure_traits()
