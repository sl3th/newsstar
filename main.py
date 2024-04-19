from flask import Flask, render_template, request
from post import data
import array as arr



app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def get_data():
    global current_data

    if request.method == "POST":
       s = request.form.get("searchbox")
    current_data = data(s)
    return render_template('index.html' , news=current_data)



@app.route('/search/post/<int:index>')
def show_post(index):
    post_data = current_data[index]
    return render_template("post.html", post=post_data)



if __name__ == '__main__':
    app.run(debug=True)
