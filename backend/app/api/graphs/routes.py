from app.api.graphs import bp
import app.services.graphs as graph

@bp.route('/1')
def index():
    fig = graph.graph1()
    
    fig_json = fig.to_json();

    return fig_json
@bp.route('/2')
def index1():
    fig = graph.graph2()
    
    fig_json = fig.to_json();

    return fig_json
@bp.route('/3')
def index2():
    fig = graph.graph3()
    
    fig_json = fig.to_json();

    return fig_json
@bp.route('/4')
def index3():
    fig = graph.graph4()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/5')
def index4():
    fig = graph.graph5()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/6')
def index5():
    fig = graph.graph6()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/7')
def index6():
    fig = graph.graph7()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/8')
def index7():
    fig = graph.graph8()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/9')
def index8():
    fig = graph.graph9()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/10')
def index9():
    fig = graph.graph10()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/11')
def index10():
    fig = graph.graph11()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/12')
def index11():
    fig = graph.graph12()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/13')
def index12():
    fig = graph.graph13()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/14')
def index13():
    fig = graph.graph14()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/15')
def index14():
    fig = graph.graph15()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/16')
def index15():
    fig = graph.graph16()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/17')
def index16():
    fig = graph.graph17()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/18')
def index17():
    fig = graph.graph18()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/19')
def index18():
    fig = graph.graph19()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/20')
def index19():
    fig = graph.graph20()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/21')
def index20():
    fig = graph.graph21()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/22')
def index21():
    fig = graph.graph22()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/23')
def index22():
    fig = graph.graph23()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/24')
def index23():
    fig = graph.graph24()
    fig_json = fig.to_json()
    return fig_json

@bp.route('/25')
def index24():
    fig = graph.graph25()
    fig_json = fig.to_json()
    return fig_json

