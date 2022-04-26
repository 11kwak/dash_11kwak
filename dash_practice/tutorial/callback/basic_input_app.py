#구성 요소의 속성이 변경될 때마다 Dash에서 자동으로 호출하는 함수인 콜백 함수 를 사용하여 대시 앱을 만드는 방법을 설명
# 대화형 대시 앱의 핵심

from dash import Dash, dcc, html, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


# 입력 속성이 변경될 때마다 콜백 데코레이터가 래핑하는 함수가 자동으로 호출됩니다. 
# Dash는 이 콜백 함수에 입력 속성의 새 값을 인수로 제공하고 Dash는 함수에서 반환된 값으로 출력 구성 요소의 속성을 업데이트합니다.
# 엑셀과 같은 반응 프로그래밍! 
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)