from flask import Flask, render_template
#from flask_bootstrap import Bootstrap
from plotting import Plotting
import io
import base64
import matplotlib.pyplot as plt
import pygal
from bokeh.resources import CDN
import json
from bokeh.embed import json_item
from bokeh.embed import components


app = Flask(__name__)
#bootstrap = Bootstrap(app)

@app.route('/plot')
def plot_matlib():
    grf=Plotting('oop.db')
    img = io.BytesIO()
    grf.temp_hum()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode()

    return '<img src="data:image/png;base64,{}">'.format(plot_url)


@app.route('/pygal_graph')
def graph():
    grf=Plotting('oop.db')
    ff = grf.pygal_graph()
    return ff.render_response()

@app.route('/')
def root():
    return render_template('home.html')


@app.route('/plt')
def b_graph():
    bkh = Plotting('oop.db')
    rend = bkh.bokeh_plot(1, 3)
    script, div = components(rend)

    return render_template("home.html", div=div, script=script)


@app.route('/pl')
def pl_bokeh_js():
    bkh = Plotting('oop.db')
    rend2 = bkh.bokeh_plot(1, 2)
    return json.dumps(json_item(rend2, "myplot"))

@app.route('/pl2')
def pl_bokeh_js2():
    bkh = Plotting('oop.db')
    rend2 = bkh.bokeh_plot(1, 3)
    return json.dumps(json_item(rend2, "myplot2"))

if __name__=='__main__':
    app.run(debug=True)
