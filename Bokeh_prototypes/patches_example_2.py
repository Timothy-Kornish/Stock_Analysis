import numpy as np

from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid
from bokeh.models.glyphs import Patch
from bokeh.io import curdoc, show

N = 30
x1 = np.linspace(-2, 2, N)
x2 = x1[::-1]
y1 = x1**2
y2 = x2**2 + (x2+2.2)
x = np.hstack((x1, x2))
y = np.hstack((y1, y2))
print(x)
print(x1)
print(x2)
print(type(x))
print(type(x1))
print(x[0])
print(x1[0])
print(y)
print(y1)
print(y2)
source = ColumnDataSource(dict(x=x, y=y))

plot = Plot(
    title=None, plot_width=300, plot_height=300,
    h_symmetry=False, v_symmetry=False, min_border=0, toolbar_location=None)

glyph = Patch(x="x", y="y", fill_color="#a6cee3")
plot.add_glyph(source, glyph)

xaxis = LinearAxis()
plot.add_layout(xaxis, 'below')

yaxis = LinearAxis()
plot.add_layout(yaxis, 'left')

plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

curdoc().add_root(plot)

show(plot)
