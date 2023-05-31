import plotly.offline as pyo
import plotly.graph_objs as go

from app.utils.api_utils import apiNBP

def create_sample_graph() -> go.Figure:
    api = apiNBP()

    data = api.getGBP()

    fig = go.Figure(data=go.Scatter(x=data.exchange_rates, y=data.dates))


    return fig
