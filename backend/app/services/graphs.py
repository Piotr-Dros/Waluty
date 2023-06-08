import plotly.offline as pyo
import plotly.graph_objs as go

from app.utils.nbp_api_utils import apiNBP

import app.utils.get_data_from_csv as currency

import plotly.graph_objects as go

def graph1() -> go.Figure:
    

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

 
    fig.update_layout(
        xaxis_title='Wartość',
        yaxis_title='Data',
        title='Wykres walut',
    )

    return fig

def graph2() -> go.Figure:
    


    data_rub = currency.readCurrency('rub')
    data_jep = currency.readCurrency('jpy')

    fig = go.Figure()
   

    fig.add_trace(go.Scatter(y=data_rub.values,x=data_rub.dates, name='RUB'))

    fig.add_trace(go.Scatter(y=data_jep.values,x=data_jep.dates, name='JPY'))

 
    fig.update_layout(
        xaxis_title='Wartość',
        yaxis_title='Data',
        title='Wykres RUB i JPY',
    )

    return fig

def graph3() -> go.Figure:
    
    data_pol=currency.readinflations('pol')
    data_usa=currency.readinflations('usa')
    data_deu=currency.readinflations('deu')
    data_gbr=currency.readinflations('gbr')
    data_jpn=currency.readinflations('jpn')
    data_rus=currency.readinflations('rus')

    fig = go.Figure()
   

    fig.add_trace(go.Scatter(y=data_pol.values,x=data_pol.dates, name='POL'))

    fig.add_trace(go.Scatter(y=data_usa.values,x=data_usa.dates, name='USA'))

    fig.add_trace(go.Scatter(y=data_deu.values,x=data_deu.dates, name='GER'))

    fig.add_trace(go.Scatter(y=data_gbr.values,x=data_gbr.dates, name='GBR'))

    fig.add_trace(go.Scatter(y=data_jpn.values,x=data_jpn.dates, name='JAP'))

    fig.add_trace(go.Scatter(y=data_rus.values,x=data_rus.dates, name='RUS'))

 
    fig.update_layout(
        xaxis_title='Wartość',
        yaxis_title='Data',
        title='Inflacja w krajach',
    )

    return fig



def graph4() -> go.Figure:
    
    data_pol=currency.readinflations('pol')
    data_usa=currency.readinflations('usa')
   

    fig = go.Figure()
   

    fig.add_trace(go.Scatter(y=data_pol.values,x=data_pol.dates, name='POL'))

    fig.add_trace(go.Scatter(y=data_usa.values,x=data_usa.dates, name='USA'))



 
    fig.update_layout(
        xaxis_title='Wartość',
        yaxis_title='Data',
        title='Inflacja w polsce i USA',
    )

    return fig


def graph5() -> go.Figure:
    
    data_pol=currency.readinflations('polfrom1990')
   
    fig = go.Figure()
   
    fig.add_trace(go.Scatter(y=data_pol.values,x=data_pol.dates, name='POL'))

 
    fig.update_layout(
        xaxis_title='Wartość',
        yaxis_title='Data',
        title='Inflacja w Polsce',
    )

    return fig