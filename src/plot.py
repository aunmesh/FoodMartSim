import numpy as np
import pandas as pd
from bokeh.plotting import figure, curdoc, show
from bokeh.models.sources import ColumnDataSource
from bokeh.client import push_session
from bokeh.driving import linear
from bokeh.models import Range1d

# ["Market_Profit", "Qty_Traded"]
#

def smoothen(a, b, n=100):
    y_smoothed = np.convolve(b, np.ones(n) / n)[n - 1:1 - n]
    a = a[0: y_smoothed.shape[0]]
    return a, y_smoothed

Log_File = 'MarketProfit'
data = pd.read_csv(Log_File)

'''
Field1_name = 'Market_Profit_per_trade'
Field2_name = 'Difference_in_mean_types'

Field1 = np.asarray(data[Field1_name])
Field2 = np.asarray(data[Field2_name])

# OPTIONAL
#x, Field1 = smoothen(x, Field1)

popFig = figure(plot_width=800,
                plot_height=400,
                title =  Field1_name +" vs " + Field2_name,
                x_axis_label= Field1_name,
                y_axis_label= Field2_name)

datacoords = ColumnDataSource(data = dict( F1 = Field2[0:-1], y=Field1[0:-1]) )

linea = popFig.line("x", "y", source=datacoords)
show(popFig)

@linear(m=0.05, b=0)
'''

################################################
################################################


Field1_name = 'Market_Profit_per_trade'
#Field2_name = 'Qty_Traded'

Field1 = np.asarray(data[Field1_name])
x = np.linspace(0, Field1.shape[0] - 1, Field1.shape[0])

# OPTIONAL
#x, Field1 = smoothen(x, Field1)

popFig = figure(plot_width=800,
                plot_height=400,
                title =  Field1_name +" plot",
                x_axis_label='Time',
                y_axis_label='Population')
datacoords = ColumnDataSource(data=dict(x=x[0:-1], y=Field1[0:-1]))
linea = popFig.line("x", "y", source=datacoords)
show(popFig)
'''
Field2 = np.asarray(data[Field2_name])

# OPTIONAL
#x, Field2 = smoothen(x, Field2)

HapFig = figure(plot_width=800,
                plot_height=400,
                title= Field2_name + " plot",
                x_axis_label='Time',
                y_axis_label=Field2_name
                y_range = (0, 0.5)
                )

datacoords = ColumnDataSource(data=dict(x=x[100:-1], y=happy[100:-1]))
lineb = HapFig.line("x", "y", source=datacoords)
show(HapFig)
'''

def update(step):
    data = pd.read_csv(Log_File)

    popul = np.asarray(data[Field1_name])
    happy = np.asarray(data[Field2_name])

    x = np.linspace(0 , popul.shape[0] - 1, happy.shape[0] - 1)

    linea.data_source.data["x"] = x
    linea.data_source.data["y"] = popul[0:-1]
    lineb.data_source.data["x"] = x
    lineb.data_source.data["y"] = happy[0:-1]

# open a session to keep our local document in sync with server

session = push_session(curdoc())
curdoc().add_periodic_callback(update, 0.01)  # period in ms
session.show()
session.loop_until_closed()
