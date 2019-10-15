from flask import Flask, Response, render_template
# from flask_bootstrap import Bootstrap
from plotting import Plotting
import io
# import base64
# import matplotlib.pyplot as plt
# import pygal
from bokeh.resources import CDN
import json
from bokeh.embed import json_item
from bokeh.embed import components
from dotenv import load_dotenv
import os
import gevent
from gevent import sleep



load_dotenv()
server_id = os.getenv("SERVER_ID")
port_no = int(os.getenv("PORT_NO"))
server_user = os.getenv("SERVER_USER")
server_key = os.getenv("SERVER_KEY")

print(server_id, int(port_no), server_user, server_key)

app = Flask(__name__)
#bootstrap = Bootstrap(app)

# @app.route('/plot')
# def plot_matlib():
#     grf=Plotting('oop.db')
#     img = io.BytesIO()
#     grf.temp_hum()
#     plt.savefig(img, format='png')
#     img.seek(0)
#     plot_url = base64.b64encode(img.getvalue()).decode()
#
#     return '<img src="data:image/png;base64,{}">'.format(plot_url)


# @app.route('/pygal_graph')
# def graph():
#     grf=Plotting('oop.db')
#     ff = grf.pygal_graph()
#     return ff.render_response()

@app.route('/')
def root():
    return render_template('home.html')


@app.route('/stream')
def temp_read_stream():
    def push_temp_read():
        import mqtt_connection
        while True:
            y = str(mqtt_connection.temp_call())
            print(y)
            json_data = json.dumps({'value': str(y)})
            yield "data:{}\n\n".format(json_data)
            #yield f"data:{json_data}\n\n"
            sleep(3)

    return Response(push_temp_read(), mimetype='text/event-stream')


@app.route('/temp_out')
def temp_outside():

    from mqtt_connection import ConnToSensors
    tmp_out = ConnToSensors(server_id, port_no, "newdb.db", server_user, server_key)
    msg_loop = tmp_out.run_sub("sensors/#")

    return json.dumps(msg_loop)
    sleep(1)


job1 = gevent.spawn(temp_outside)
job2 = gevent.spawn(temp_read_stream)
gevent.wait([job1, job2])

# @app.route('/plt')
# def b_graph():
#     bkh = Plotting('oop.db')
#     rend = bkh.bokeh_plot(1, 3)
#     script, div = components(rend)
#
#     return render_template("home.html", div=div, script=script)

@app.route('/pl')
def pl_bokeh_js():
    bkh = Plotting('oop.db')
    rend1 = bkh.bokeh_plot(1, 2)
    return json.dumps(json_item(rend1))

@app.route('/pl2')
def pl_bokeh_js2():
    bkh = Plotting('oop.db')
    rend2 = bkh.bokeh_plot(1, 3)
    return json.dumps(json_item(rend2))

if __name__=='__main__':
    app.run(debug=True)
