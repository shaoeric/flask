from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATE_AUTO_RELOAD'] = True

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/detail/')
def detail():
    return render_template('detail.html')

if __name__ == '__main__':
    app.run(debug=True)
