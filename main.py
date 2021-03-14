"""
*************************************************************************
*    Course: 100 Days of Code - Dra. Angela Yu                          *
*    Author: Jorge Chavarriaga                                          *
*    Day: 57- Jinja Donamic Html Pages - Project Blog                   *
*    Date: 2021-01-20                                                   *
*************************************************************************
"""


from flask import Flask, render_template
from datetime import date
import requests
from post import Post

actual_year = date.today().year
url = 'https://api.npoint.io/5abcca6f4e39b4955965'
posts = requests.get(url).json()
post_objects = []
for post in posts:
    post_obj = Post(post['id'], post['title'], post['subtitle'], post['body'])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", year=actual_year, all_posts=post_objects)

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post,  year=actual_year)


if __name__ == "__main__":
    app.run(debug=True)
