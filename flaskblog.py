from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        'title': 'Jaime daniels',
        'date_posted': 'August 21, 2021',
        'content': 'some information'
    },
    {
        'title': 'Jaime daniels',
        'date_posted': 'August 21, 2021',
        'content': 'some information'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='about')


if __name__ == '__main__':
    app.run(debug=True)