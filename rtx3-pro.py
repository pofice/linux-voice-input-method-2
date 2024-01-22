import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pyperclip

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("RTX语音输入法", style={'color': 'gray'}),
    dcc.Input(id="input-box", type="text", placeholder="请在此输入", style={'width': '300px', 'height': '50px', 'color': 'black', 'border-color': 'gray'}), 
    html.Button('清除输入记录', id='clear-button', n_clicks=0, style={'width': '200px', 'height': '50px', 'color': 'black', 'background-color': 'gray'}),
    html.Div(id='copy-success', children='', style={'color': 'gray'})
], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'justify-content': 'center', 'background-color': 'black'}) 

@app.callback(
    Output('input-box', 'value'),
    Output('copy-success', 'children'),
    Input('input-box', 'value'),
    Input('clear-button', 'n_clicks'),
    State('input-box', 'value')
)
def update_output(input_value, n_clicks, state_value):
    ctx = dash.callback_context
    if not ctx.triggered:
        return "", ""
    else:
        button_id = ctx.triggered[0]['prop_id'].split('.')[0]
        if button_id == 'clear-button':
            return "", ""
        elif input_value:
            pyperclip.copy(input_value)
            return input_value, "文本已成功复制到剪贴板！"
        else:
            return state_value, ""

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0')