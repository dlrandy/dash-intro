# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.


from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

s = pd.Series([42,21,7,3.5])

sf = pd.DataFrame({
    'age':18,
    'name':['Alice','Bob','Carl'],
    'cardio':[34,56,89]})

# print(sf['age'])
# print(sf[1:2])
# print(sf.iloc[:,:1])

# print(sf.iloc[2,1])

# print(sf[sf['cardio']>50])

# print(sf.loc[:,'name'])

# print(sf.loc[:,['age','cardio']])

# sf['age'] = 16

# sf.loc[1:, 'age'] = 16

sf.loc[:,'friend'] = 'Alice'

print(sf)

if __name__ == '__main__':
    app.run(debug=True)













