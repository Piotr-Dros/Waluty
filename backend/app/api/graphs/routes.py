from app.api.graphs import bp
from app.services.graphs import graph1

@bp.get('/')
def getGraphs():
    fig = graph1()

    fig_json = fig.to_json();

    return fig_json

