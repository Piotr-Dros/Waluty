from app.main import bp
from flask import render_template

from app.services.graphs import graph1,graph2,graph3,graph4,graph5

@bp.route('/graph1')
def index():
    fig = graph1()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph2')
def index2():
    fig = graph2()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph3')
def index3():
    fig = graph3()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph4')
def index4():
    fig = graph4()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)

@bp.route('/graph5')
def index5():
    fig = graph5()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)
