from app.main import bp
from flask import render_template

from app.services.graphs import create_sample_graph

@bp.route('/')
def index():
    fig = create_sample_graph()
    
    plot_div = fig.to_html(full_html=False)

    return render_template('index.html', plot_div=plot_div)