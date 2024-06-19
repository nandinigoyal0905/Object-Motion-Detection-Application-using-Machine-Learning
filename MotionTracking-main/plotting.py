from project import df
from bokeh.io import curdoc
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource

df["Start_string"] = df["Start"].dt.strftime("%Y-%m-%d %H:%M:%S")
df["End_string"] = df["End"].dt.strftime("%Y-%m-%d %H:%M:%S")

cds = ColumnDataSource(df)
curdoc().theme = "dark_minimal"

p = figure(x_axis_type='datetime', height=100, width=500, sizing_mode="scale_width", Title="MOTION GRAPH")
p.yaxis.minor_tick_line_color = None
p.ygrid[0].ticker.desired_num_ticks = 1

hover = HoverTool(tooltip=[("Start", "@Start_string"), ("End", "@End_string")])
p.add_tools(hover)

q = p.quad(left="Start", right="End", bottom=0, top=1, Color="green", source=cds)

output_file("motion.html")
show(p)
