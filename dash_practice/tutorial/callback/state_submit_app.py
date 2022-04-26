# -*- coding: utf-8 -*-
# 상태 비저장 프레임워크는 상태 저장 프레임워크보다 확장 가능하고 강력합니다. 방문하는 대부분의 웹 사이트는 상태 비저장 서버에서 실행됩니다.
# 그만큼 부작용도 있음. 데이터 사용자 하나하나가 따로 저장하고싶으면? dcc store사용 

from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
    html.Div(id='output-state')
])

# input으로 submit id를 넣고 나머지 input을 state로 변경
@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'))
def update_output(n_clicks, input1, input2):
    return u'''
        The Button has been pressed {} times,
        Input 1 is "{}",
        and Input 2 is "{}"
    '''.format(n_clicks, input1, input2)


if __name__ == '__main__':
    app.run_server(debug=True)