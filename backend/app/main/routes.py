from app.main import bp
from flask import render_template

import app.services.graphs as graph
@bp.route('/graph1')
def index():
    fig = graph.graph1()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph2')
def index2():
    fig = graph.graph2()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph3')
def index3():
    fig = graph.graph3()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph4')
def index4():
    fig = graph.graph4()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph5')
def index5():
    fig = graph.graph5()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph6')
def index6():
    fig = graph.graph6()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph7')
def index7():
    fig = graph.graph7()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph8')
def index8():
    fig = graph.graph8()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)
    
@bp.route('/graph9')
def index9():
    fig = graph.graph9()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)
@bp.route('/graph10')
def index10():
    fig = graph.graph10()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph11')
def index11():
    fig = graph.graph11()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph12')
def index12():
    fig = graph.graph12()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph13')
def index13():
    fig = graph.graph13()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph14')
def index14():
    fig = graph.graph14()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph15')
def index15():
    fig = graph.graph15()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph16')
def index16():
    fig = graph.graph16()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph17')
def index17():
    fig = graph.graph17()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph18')
def index18():
    fig = graph.graph18()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph19')
def index19():
    fig = graph.graph19()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph20')
def index20():
    fig = graph.graph20()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph21')
def index21():
    fig = graph.graph21()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)


@bp.route('/graph22')
def index22():
    fig = graph.graph22()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)


@bp.route('/graph23')
def index23():
    fig = graph.graph23()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)