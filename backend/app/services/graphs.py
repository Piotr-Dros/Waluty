import plotly.offline as pyo
import plotly.graph_objs as go

from app.utils.nbp_api_utils import apiNBP

import app.utils.get_data_from_csv as currency

import plotly.graph_objects as go

def create_sample_graph() -> go.Figure:
    

    data_gbp = currency.readCurrency('gbp')
    data_usd = currency.readCurrency('usd')
    data_rub = currency.readCurrency('rub')
    data_chf = currency.readCurrency('chf')
    data_eur = currency.readCurrency('eur')
    data_jep = currency.readCurrency('jpy')

    fig = go.Figure()
    print(data_chf)

    fig.add_trace(go.Scatter(y=data_gbp.values,x=data_gbp.dates, name='GBP'))

    fig.add_trace(go.Scatter(y=data_usd.values,x=data_usd.dates, name='USD'))

    fig.add_trace(go.Scatter(y=data_rub.values,x=data_rub.dates, name='RUB'))

    fig.add_trace(go.Scatter(y=data_rub.values,x=data_rub.dates, name='CHF'))

    fig.add_trace(go.Scatter(y=data_eur.values,x=data_eur.dates, name='EUR'))

    fig.add_trace(go.Scatter(y=data_jep.values,x=data_jep.dates, name='JPY'))

    # Dostosowanie osi i etykiet
    fig.update_layout(
        xaxis_title='Wartość',
        yaxis_title='Data',
        title='Wykres GBP i USD',
    )

    return fig
