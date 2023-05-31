from app.api.graphs import bp

@bp.get('/')
def getGraphs():
    return {
        'graph': 'graph1'
    }