# A function that draws a line graph from a csv file.

#%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import os

def draw_line_graph_from_csv(file_name, x_axis, y_axes=None):
    df = pd.read_csv(file_name)
    filter = [x_axis] + y_axes

    title = os.path.basename(file_name)
    df[filter].plot(x=x_axis, title=title, grid=True, rot=10, figsize=(6, 4))