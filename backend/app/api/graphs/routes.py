from app.api.graphs import bp
from app.services.graphs import graph1,graph2,graph3,graph4,graph5

@bp.route('/1')
def index():
    fig = graph1()
    
    fig_json = fig.to_json();

    return fig_json

@bp.route('/2')
def index2():
    fig = graph2()
    
    fig_json = fig.to_json();

    return fig_json

@bp.route('/3')
def index3():
    fig = graph3()
    
    fig_json = fig.to_json();

    return fig_json

@bp.route('/4')
def index4():
    fig = graph4()
    
    fig_json = fig.to_json();

    return fig_json

@bp.route('/5')
def index5():
    fig = graph5()
    
    fig_json = fig.to_json();

    return fig_json