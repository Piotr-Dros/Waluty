from app.api.graphs import bp
from app.services.graphs import create_sample_graph

@bp.get('/')
def getGraphs():
    fig = create_sample_graph()

    fig_json = fig.to_json();

    return fig_json