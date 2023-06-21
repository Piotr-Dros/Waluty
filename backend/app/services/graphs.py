import plotly.offline as pyo
import plotly.graph_objs as go

from app.utils.nbp_api_utils import apiNBP

import app.utils.get_data_from_csv as currency

import plotly.graph_objects as go

import plotly.express as px

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

def graph6() -> go.Figure:#minimalna pensja
    
    data=currency.readCurrency('minimalPension')
    

    
    fig = px.pie(values=data.values, names=data.dates)



 
    fig.update_layout(
        xaxis_title='Wartość',
        yaxis_title='Kraj',
        title='Minimalna pensja w krajach',
    )

    return fig

def graph7() -> go.Figure:#Słupkowy usd 2022
    data=currency.readCurrency2022('usd')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='USD 2022',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph8() -> go.Figure:#Słupkowy rub 2022
    data=currency.readCurrency2022('rub')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='RUB 2022',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph9() -> go.Figure:#Słupkowy jpy 2022
    data=currency.readCurrency2022('jpy')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='JPY 2022',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph10() -> go.Figure:#Słupkowy GBP 2022
    data=currency.readCurrency2022('gbp')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='GBP 2022',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph11() -> go.Figure:#Słupkowy EUR 2022
    data=currency.readCurrency2022('eur')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='EUR 2022',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph12() -> go.Figure:#Słupkowy CHF 2022
    data=currency.readCurrency2022('chf')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='CHF 2022',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig


def graph13() -> go.Figure:#Słupkowy usd 2014
    data=currency.readCurrency2014('usd')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='USD 2014-2015',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph14() -> go.Figure:#Słupkowy rub 2014
    data=currency.readCurrency2014('rub')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='RUB 2014-2015',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph15() -> go.Figure:#Słupkowy jpy 2014
    data=currency.readCurrency2014('jpy')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='JPY 2014-2015',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph16() -> go.Figure:#Słupkowy GBP 2014
    data=currency.readCurrency2014('gbp')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='GBP 2014-2015',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph17() -> go.Figure:#Słupkowy EUR 2014
    data=currency.readCurrency2014('eur')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='EUR 2014-2015',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig
 


def graph18() -> go.Figure:#Słupkowy CHF 2004
    data=currency.readCurrency2004('chf')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='CHF 2004-2007',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig


def graph19() -> go.Figure:#Słupkowy usd 2004
    data=currency.readCurrency2004('usd')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='USD 2004-2007',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph20() -> go.Figure:#Słupkowy rub 2004
    data=currency.readCurrency2014('rub')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='RUB 2004-2007',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph21() -> go.Figure:#Słupkowy jpy 2004
    data=currency.readCurrency2004('jpy')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='JPY 2004-2007',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph22() -> go.Figure:#Słupkowy GBP 2004
    data=currency.readCurrency2004('gbp')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='GBP 2004-2007',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph23() -> go.Figure:#Słupkowy EUR 2004
    data=currency.readCurrency2004('eur')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='EUR 2004-2007',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph24() -> go.Figure:#pl/usd 2016
    data=currency.readCurrency2016_18('usd201617')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='2016-2017 500+',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

def graph25() -> go.Figure:#18/19 usd/pol
    data=currency.readCurrency2016_18('usd201819')
    print(data.dates)
    fig = go.Figure(data=go.Bar(x=data.dates, y=data.values))


    fig.update_layout(
        title='2018-2019',
        xaxis_title='Data',
        yaxis_title='Kurs',
        xaxis=dict(
        tickmode='array',
        tickvals=data.dates,
        ticktext=data.dates,
        )
    )

    return fig

 
 