import plotly.offline as pyo
import plotly.graph_objs as go

def create_sample_graph() -> go.Figure:
    x = [1, 2, 3, 4, 5]
    y = [1, 4, 9, 16, 25]
    
    fig = go.Figure(data=go.Scatter(x=x, y=y))

    return fig