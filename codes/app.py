from flask import Flask, jsonify
from flask_socketio import SocketIO, emit
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import threading
import time
import serial

app = Flask(__name__)
socketio = SocketIO(app)

ser = serial.Serial('/dev/cu.usbmodem1201', 115200)

# Initialize variables for previous coordinates
prev_x, prev_y = 3, 3

# Hard-coded square coordinates
square_coords = [(3, 3), (3, 10), (10, 10), (10, 3), (3, 3)]

external_stylesheets = ['style.css']
dash_app = dash.Dash(__name__, server=app, external_stylesheets=external_stylesheets, url_base_pathname='/dash/')

dash_app.layout = html.Div(children=[
    html.H1(children='Real-Time Coordinates Plot'),
    
    dcc.Graph(
        id='live-update-graph',
        animate=True,
        style={
                'width': '50%',  # Set the width of the container
                'height': '100%'  # Set the height of the container
            }
    ),

    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    ),
    
    html.Button('Reset', id='reset-button', n_clicks=0)
])

data = []

@dash_app.callback(Output('live-update-graph', 'figure'),
                   [Input('interval-component', 'n_intervals'),
                    Input('reset-button', 'n_clicks')])
def update_graph_live(n, n_clicks):
    global data

    if n_clicks > 0:
        data = []  # Clear data on reset

    fig = go.Figure()

    # Add hard-coded square
    square_x, square_y = zip(*square_coords)
    fig.add_trace(go.Scatter(x=square_x, y=square_y, mode='lines', name='Hard-coded Square'))

    if data:
        # Add current position
        x, y = zip(*data)
        fig.add_trace(go.Scatter(x=x, y=y, mode='markers+lines', name='Position'))

        # Add arrows
        for i in range(1, len(data)):
            fig.add_annotation(
                dict(
                    x=x[i], 
                    y=y[i], 
                    ax=x[i-1], 
                    ay=y[i-1],
                    xref='x', 
                    yref='y', 
                    axref='x', 
                    ayref='y',
                    showarrow=True,
                    arrowhead=3,
                    arrowsize=1,
                    arrowwidth=2,
                    arrowcolor='black'
                ))

    fig.update_layout(title='Coordinates Graph with Arrows and Square',
                      xaxis_title='X',
                      yaxis_title='Y',
                      xaxis=dict(range=[-10, 20], scaleanchor="y", scaleratio=0.5),  # Set x-axis range and tick spacing
                      yaxis=dict(range=[-10, 20], scaleanchor="x", scaleratio=1))  # Set y-axis range and tick spacing

    return fig
def send_command(command, cali=False):
    command_str = f"{command}_cali" if cali else command
    try:
        with open('log.txt', 'a') as log_file:
            log_file.write(f"{command_str}\n")
        print(f"Sending command: {command_str}")
    except Exception as e:
        print(f"Failed to send command: {command_str}. Error: {e}")

def check_and_send_command(x, y):
    if y == 3 and (x >= 3 and x < 10):
        command = "EAST_TIP"
    elif x == 10 and (y >= 3 and y < 10):
        command = "NORTH_TIP"
    elif y == 10 and (x > 3 and x <= 10):
        command = "WEST_TIP"
    elif x == 3 and (y > 3 and y <= 10):
        command = "SOUTH_TIP"
    else:
        command = "UNKNOWN"

    try:
        with open('log.txt', 'a') as log_file:
            log_file.write(f"{command}\n")
    except Exception as e:
        print(f"Failed to send command: {command}. Error: {e}")
def calibrate():
    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            coords = line.split(',')
            if len(coords) == 3:
                y, x, _ = int(coords[0]), int(coords[1]), int(coords[2])  # Swap x and y for plotting
                print(f"Current coordinates during calibration: {x}, {y}")
                if x == 3 and y == 3:
                    print("Calibration complete. Reached (3, 3)")
                    break
                initial_x, initial_y = x, y
                if x > 3:
                    # command ='WEST_cali'
                    send_command("WEST", cali=True)
                elif x < 3:
                    # command ='EAST_cali'
                    send_command("EAST", cali=True)
                elif y > 3:
                    #  command ='SOUTH_cali'
                    send_command("SOUTH", cali=True)
                elif y < 3:
                    # command ='NORTH_cali'
                    send_command("NORTH", cali=True)


                line = ser.readline().decode('utf-8').strip()
                if line:
                    coords = line.split(',')
                    if len(coords) == 3:
                        y, x, _ = int(coords[0]), int(coords[1]), int(coords[2])
                        if x == initial_x and y == initial_y:
                            print("Movement not detected, repeating command")
                            continue

def read_serial():
    global prev_x, prev_y, data

    while True:
        line = ser.readline().decode('utf-8').strip()
        if line:
            coords = line.split(',')
            if len(coords) == 3:
                y, x , butt= int(coords[0]), int(coords[1]), int(coords[2])  # Swap x and y for plotting
                print(f"Current coordinates: {x}, {y}")
                if butt == 1:
                        calibrate()
                else:
                    check_and_send_command(x, y)
                    if x != 0 or y != 0:  # Skip (0, 0) coordinates
                        if prev_x is not None and prev_y is not None:
                            if x != prev_x or y != prev_y:
                                data.append((x, y))
                                prev_x, prev_y = x, y
                        else:
                            prev_x, prev_y = x, y
                        socketio.emit('update_plot', {'x': x, 'y': y})
                    time.sleep(0.1)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

if __name__ == '__main__':
    threading.Thread(target=read_serial).start()
    socketio.run(app, host='0.0.0.0', port=5002, debug=True)