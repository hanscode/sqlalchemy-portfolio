from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/new', methods=['GET', 'POST'])
def add_project():
    print(request.form)
    return render_template('new.html')


@app.route('/projects')
def project():
    return render_template('detail.html')


@app.route('/about')
def about():
    return render_template('about.html')



if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.1')