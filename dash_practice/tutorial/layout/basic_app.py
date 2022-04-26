# import 
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# dash 선언
app = Dash(__name__)


# df 만들고 plotly 로 그래프 객체 만들었어 
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")



# app layout 만들면서 그래프 변수에 fig 넣어줬어
app.layout = html.Div(children=[
    html.H1(children='안녕 DASH야'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

# 파이썬 실행시 서버 실행
if __name__ == '__main__':
    app.run_server(debug=True)  #dash는 기본적으로 핫 리로딩(코드 변경되면 자동 변경) 싫으면 dev_tools_hot_reload=False