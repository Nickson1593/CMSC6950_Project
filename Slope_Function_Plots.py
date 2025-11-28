#Load Slope Function
%load Slope_Function.py

import plotly.graph_objects as go
from plotly.subplots import make_subplots

#Define Variables Using Slope Function
X,Y,Z,Slope = surface_slope('Crustal_Thickness_With_Boundary_XYZ.txt')

#Make Subplots
fig = make_subplots(rows=2, cols=1,specs=[[{'type':'surface'}],[{'type':'surface'}]], subplot_titles=[('Aspect Ratio 2:2:0.75'),('Aspect Ratio 2:2:0.001')], horizontal_spacing=0.01, vertical_spacing=0.05)
